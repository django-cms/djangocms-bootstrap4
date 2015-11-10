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
         * @class Bootstrap3
         * @namespace CMS
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
                var data = $('script[data-bootstrap3]').data();
                var fieldName = data.bootstrap3;
                var contextInputs = $('.js-btn-group-context-' + fieldName + ' label input');
                var selectedContextInput;

                contextInputs.each(function (index, item) {
                    var label = $(item).parent();
                    var input = $(item);
                    var element = $('.js-btn-group-context-' + fieldName + ' label input[value="default"]');

                    // Initial active state
                    if (input.prop('checked')) {
                        selectedContextInput = input;
                        label.addClass('active');
                    }

                    if (selectedContextInput == undefined) {
                        selectedContextInput = element;
                    }

                    // Set context
                    if (item.value && item.value !== 'muted') {
                        label.addClass('btn btn-' + item.value);
                    } else {
                        label.addClass('btn btn-default');
                    }


                     // Set active states
                    label.on('click', function () {
                        var input = $(this).find('input');

                        selectedContextInput.attr('checked', false);
                        input.attr('checked', true);

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
