/*
 * Copyright https://github.com/divio/django-cms
 */

// #############################################################################
// ALDRYN-BOOTSTRAP3
(function ($) {
    'use strict';

    // shorthand for jQuery(document).ready();
    $(function () {
        /**
         * Handles all reauired JavaScript for the aldryn-bootstrap3 addon.
         *
         * @class bootstrap3
         */
        var bootstrap3 = {

            /**
             * Widget used in aldryn_bootstrap3/widgets/context.html.
             * Provides a button group list and enables the user
             * to select one of the choices.
             *
             * @method contextWidget
             * @param {jQuery} element context element to render
             */
            contextWidget: function contextWidget(element) {
                var data = element.data();
                var fieldName = data.context;
                var contextInputs = element.find('.js-btn-group-context-' + fieldName + ' label');
                var selectedContextInput;

                contextInputs.find('input').each(function (index, item) {
                    var input = $(item);
                    var label = input.parent();
                    var element = contextInputs.find('input[value="default"]');

                    // initial active state
                    if (input.prop('checked')) {
                        selectedContextInput = input;
                        label.addClass('active');
                    }

                    if (!selectedContextInput) {
                        selectedContextInput = element;
                    }

                    // set color context
                    if (item.value && item.value !== 'muted') {
                        label.addClass('btn btn-' + item.value);
                    } else {
                        label.addClass('btn btn-default');
                    }

                    // set active states
                    label.on('click', function () {
                        var input = $(this).find('input');

                        selectedContextInput.prop('checked', false);
                        input.prop('checked', true);

                        selectedContextInput = input;
                    });

                });
            },

            /**
             * Widget used in aldryn_bootstrap3/widgets/icon.html.
             * Renders a selectable icon dropdown where you can choose
             * from font-awesome or glyphicons depending on your settings.
             *
             * @method iconWidget
             * @param {jQuery} element context element to render
             */
            iconWidget: function iconWidget(element) {
                var data = element.data();
                var name = data.name;
                var iconPicker = element.find('.js-icon-' + name + ' .js-icon-picker');
                var iconSet = element.find('.js-icon-' + name + ' .js-iconset');
                var enableIconCheckbox = element.find('.js-icon-' + name + ' .js-icon-enable');
                var widgets = element.find('.js-icon-' + name + ' .js-icon-widgets');
                var iconPickerButton = iconPicker.find('button');
                var initialValue = iconPickerButton.data('icon');
                var initialIconset = iconSet.find('option[data-prefix=' + data.iconset + ']').attr('value');

                // initialize bootstrap iconpicker functionality
                iconPickerButton.iconpicker({
                    arrowClass: 'btn-default',
                    icon: initialValue,
                    iconset: initialIconset
                });

                // show label instead of dropdown if there is only one choice available
                if (iconSet.find('option').length === 1) {
                    iconSet.hide();
                    iconSet.parent().prepend('' +
                        '<label class="form-control-static">' +
                            iconSet.find('option').text() +
                        '</label>');
                }

                // set correct iconset when switching the font via dropdown
                iconSet.on('change', function () {
                    iconPickerButton.iconpicker('setIconset', $(this).val());
                });

                // checkbox is shown if field is not required, switches visibility
                // of icon selection to on/off
                enableIconCheckbox.on('change', function () {
                    if ($(this).prop('checked')) {
                        widgets.removeClass('hidden');
                        iconPicker.trigger('change');
                    } else {
                        widgets.addClass('hidden');
                        iconPickerButton.find('input').val('');
                    }
                }).trigger('change');
            },

            /**
             * Renders the preview on top of the button/ling widget page.
             * Only one button widget allowed per page.
             *
             * @method buttonPreviewPreview
             */
            buttonPreviewPreview: function buttonPreviewPreview() {
                var container = $('.aldryn-bootstrap3-button');
                var previewBtn = container.find('.js-preview-btn span');
                var defaultBtnText = previewBtn.text();
                var typeState = '';
                var blockClass = '';
                var timer = function () {};
                var timeout = 50;

                // helper references
                var sizeContext = $('.field-btn_size');
                var btnContext = $('.field-btn_context');
                var colorContext = $('.field-txt_context');
                var blockContext = $('.field-btn_block');

                // attach event to the label
                $('#id_label').on('keydown', function () {
                    clearTimeout(timer);
                    var el = $(this);
                    timer = setTimeout(function () {
                        updatePreview({
                            type: 'text',
                            text: el.val()
                        });
                    }, timeout);
                }).trigger('keydown');

                // attach event to the link/button switch
                $('#id_type_0, #id_type_1').on('change', function () {
                    updatePreview({
                        type: 'markup',
                        context: $(this).val()
                    });
                }).filter(':checked').trigger('change');

                // handle button context selection
                // autotrigger will be handled by link/button switcher
                btnContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'context',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // handle text color button context selection
                colorContext.find('label').on('click', function () {
                    updatePreview({
                        type: 'context',
                        cls: cleanClass($(this).attr('class'))
                    });
                });

                // handle block checkbox
                $('#id_btn_block').on('change', function () {
                    updatePreview({
                        type: 'block',
                        state: $(this).prop('checked')
                    });
                }).trigger('change');

                // every event fires updatePreview passing in arguments what
                // has to be done
                function updatePreview(obj) {
                    // handle "label" inputs
                    if (obj.type === 'text' && obj.text !== '') {
                        previewBtn.text(obj.text);
                    } else if (obj.type === 'text') {
                        previewBtn.text(defaultBtnText);
                    }

                    // handle link/button selection which hides/shows text context
                    if (obj.type === 'markup' && obj.context === 'lnk') {
                        typeState = obj.context;
                        sizeContext.hide();
                        blockContext.hide();
                        btnContext.hide();
                        colorContext.show();
                        colorContext.find('label.active').trigger('click');
                    }
                    if (obj.type === 'markup' && obj.context === 'btn') {
                        typeState = obj.context;
                        sizeContext.show();
                        blockContext.show();
                        colorContext.hide();
                        btnContext.show();
                        btnContext.find('label.active').trigger('click');
                    }

                    // update context
                    if (obj.type === 'context') {
                        if (typeState === 'lnk') {
                            previewBtn.attr('class', 'text text-' + obj.cls + blockClass);
                        } else {
                            previewBtn.attr('class', 'btn btn-' + obj.cls + blockClass);
                        }
                    }

                    // change block type
                    if (obj.type === 'block' && obj.state) {
                        blockClass = ' btn-block';
                        previewBtn.addClass(blockClass);
                    } else if (obj.type === 'block') {
                        blockClass = '';
                        previewBtn.removeClass('btn-block');
                    }
                }

                // make sure we only pass the required class argument
                function cleanClass(cls) {
                    cls = cls
                        .replace('btn btn-', '')
                        .replace('active', '');
                    return cls;
                }



                /*
                var buttonContextTriggers = $('.js-btn-group-context-btn_context .btn');
                var textLinkContextTriggers = $('.js-btn-group-context-txt_context .btn');
                var sizesTriggers = $('.js-btn-group-sizes .btn');

                var previewButton = $('.js-btn-preview a');
                var previewButtonText = previewButton.text();

                // Init defaults
                var currentButtonContextTriggerValue;
                var currentTextLinkContextTriggerValue;
                var currentSizesTriggerValue;
                var currentBlockTriggerValue;
                var currentTypeSwitch ;

                // Init text/button switch
                var typeSwitch = $('#id_type_0, #id_type_1');
                var buttonElements = $('.field-btn_context, .field-btn_size, .field-btn_block');
                var textElements = $('.field-txt_context');

                // Set btn-block
                var btnBlock = $('#id_btn_block');

                var setBtnBlock = function () {
                    if ($('#id_btn_block:checkbox:checked').length == 1) {
                        previewButton.addClass('btn-block');
                        currentBlockTriggerValue = 'btn-block';
                    } else {
                        previewButton.removeClass('btn-block');
                        currentBlockTriggerValue = '';
                    }
                };

                setBtnBlock();

                btnBlock.on('click', function () {
                    setBtnBlock();
                });

                // Set button context
                buttonContextTriggers.each(function (index, item) {
                    if ($(item).find('input').attr('checked') == 'checked') {
                        var context = $(item).find('input[checked="checked"]').val();
                        currentButtonContextTriggerValue = context;
                        if (typeSwitch.val() == 'btn') {
                            $('.js-btn-preview a').addClass('btn-' + context);
                        }
                    }
                });

                // Set textlink context
                textLinkContextTriggers.each(function (index, item) {
                    if ($(item).find('input').attr('checked') == 'checked') {
                        var context = $(item).find('input[checked="checked"]').val();
                        currentTextLinkContextTriggerValue = context;
                        if (typeSwitch.val() == 'lnk') {
                            $('.js-btn-preview .btn').addClass('text-' + context);
                        }
                    }
                });


                // Set sizes
                sizesTriggers.each(function (index, item) {
                    if ($(item).find('input').attr('checked') == 'checked') {
                        var size = $(item).find('input[checked="checked"]').val();
                        $('.js-btn-preview .btn').addClass('btn-' + size);
                        currentSizesTriggerValue = size;
                    }
                });

                // Set button context of elements for preview
                buttonContextTriggers.on('click', function (e) {
                    var context = $(this).find('input').val();

                    previewButton.removeClass('btn-' + currentButtonContextTriggerValue);
                    previewButton.addClass('btn-' + context);

                    currentButtonContextTriggerValue = context;
                });

                // Set text link context of elements for preview
                textLinkContextTriggers.on('click', function (e) {
                    var context = $(this).find('input').val();

                    previewButton.removeClass('text-' + currentTextLinkContextTriggerValue);
                    previewButton.addClass('text-' + context);

                    currentTextLinkContextTriggerValue = context;
                });

                // Set sizes of elements for preview
                sizesTriggers.on('click', function (e) {
                    var size = $(this).find('input').val();

                    previewButton.removeClass('btn-' + currentSizesTriggerValue);
                    previewButton.addClass('btn-' + size);

                    currentSizesTriggerValue = size;
                });

                // Update text in button for preview
                previewButton.text($("#id_label").val());

                $("#id_label").on('input', function () {
                    if ($(this).val()) {
                        $('.js-btn-preview a').text($(this).val());
                    } else {
                        $('.js-btn-preview a').text(previewButtonText);
                    }
                    refreshIcons();
                });

                // Set Icon of button
                $.each(['icon_left', 'icon_right'], function (index, name) {
                    var enableIconCheckbox = $('#id_' + name);
                    console.log('enableIconCheckbox: ', enableIconCheckbox);
                    var iconPicker = enableIconCheckbox.parent().find('button');

                    // update code
                    var updateIconPreview = function () {
                        var iconSelectedCss = iconPicker.find('i').attr('class');
                        console.log('iconSelectedCss: ', iconSelectedCss);
                        previewButton.find('.js-icon-position-' + name).remove();
                        var iconHtml = '<i class="js-icon-position-' + name + ' ' + iconSelectedCss + '"></i> '
                        if (name === 'icon_left') {
                            previewButton.prepend(iconHtml);
                        }
                        if (name === 'icon_right') {
                            previewButton.append(iconHtml);
                        }
                    };

                    // on change
                    iconPicker.on('change', updateIconPreview);
                    enableIconCheckbox.on('change', updateIconPreview);

                    // initial
                    enableIconCheckbox.trigger('change');
                });

                var refreshIcons = function () {
                    $.each(['icon_left', 'icon_right'], function (index, name) {
                        var enableIconCheckbox = $('.js-icon-' + name + ' .js-icon-enable');
                        console.log('enableIconCheckbox: ', enableIconCheckbox);
                        enableIconCheckbox.trigger('change');
                    });
                };

                // Update class of preview button based on classes
                var extraClasses = $("#id_classes");
                previewButton.addClass(extraClasses.val());

                extraClasses.on('input', function () {
                    if (currentTypeSwitch == 'btn') {
                        previewButton.attr('class', 'btn ' + currentBlockTriggerValue + ' btn-' + currentButtonContextTriggerValue + ' btn-' + currentSizesTriggerValue + ' ' + $(this).val());
                    }
                    if (currentTypeSwitch == 'lnk') {
                        previewButton.attr('class', 'text-' + currentTextLinkContextTriggerValue + ' ' + $(this).val());
                    }
                });

                // Init current type
                var setCurrentType = function () {
                    typeSwitch.each(function (index, name) {
                        if ($(this).is(':checked')) {
                            currentTypeSwitch = $(this).val();
                        }
                    });

                    if (currentTypeSwitch == 'btn') {
                        previewButton.addClass('btn');
                        previewButton.addClass('btn-' + currentButtonContextTriggerValue);
                        previewButton.addClass('btn-' + currentSizesTriggerValue);
                        previewButton.removeClass('text-' + currentTextLinkContextTriggerValue);
                        textElements.hide();
                        buttonElements.show();
                    }

                    if (currentTypeSwitch == 'lnk') {
                        previewButton.removeClass('btn');
                        previewButton.removeClass('btn-' + currentButtonContextTriggerValue);
                        previewButton.removeClass('btn-' + currentSizesTriggerValue);
                        previewButton.removeClass('btn-block');
                        previewButton.addClass('text-' + currentTextLinkContextTriggerValue);
                        textElements.show();
                        buttonElements.hide();
                    }

                };

                setCurrentType();

                typeSwitch.on('change', function () {
                    setCurrentType();
                });
                */
            }

        };

        // auto initialization
        if ($('.aldryn-bootstrap3-context').length) {
            $('.aldryn-bootstrap3-context').each(function () {
                bootstrap3.contextWidget($(this));
            });
        }
        if ($('.aldryn-bootstrap3-icon').length) {
            $('.aldryn-bootstrap3-icon').each(function () {
                bootstrap3.iconWidget($(this));
            });
        }
        if ($('.aldryn-bootstrap3-button').length) {
            bootstrap3.buttonPreviewPreview();
        }
    });
})(window.jQuery || django.jQuery);
