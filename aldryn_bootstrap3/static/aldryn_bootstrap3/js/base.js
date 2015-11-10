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
             */
            contextWidget: function contextWidget() {
                var data = $('.aldryn-bootstrap3-context').data();
                var fieldName = data.context;
                var contextInputs = $('.js-btn-group-context-' + fieldName + ' label input');
                var selectedContextInput;

                contextInputs.each(function (index, item) {
                    var input = $(item);
                    var label = input.parent();
                    var element = $('.js-btn-group-context-' + fieldName + ' label input[value="default"]');

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
            }

        };

        // auto initialization
        if ($('.aldryn-bootstrap3-context').length) {
            bootstrap3.contextWidget();
        }
    });
})(window.jQuery || django.jQuery);
