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
    });
})(window.jQuery || django.jQuery);
