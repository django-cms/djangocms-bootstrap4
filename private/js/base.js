/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/divio/djangocms-boilerplate-webpack
 */

// import 'bootstrap/js/dist/alert'
import { selectToButtons } from 'components/selectToButtons';


$(() => {
    if ($('.djangocms-bootstrap4-row').length) {
        let static_url = $('.djangocms-bootstrap4-row').data('static');

        // Bootstrap 4 Grid Row - Vertical Alignment
        new selectToButtons({
            select: '#id_vertical_alignment',
            icons: ['align-reset', 'flex-align-start', 'flex-align-center', 'flex-align-end'],
            static: static_url,
        });
        // Bootstrap 4 Grid Row - Horizontal Alignment
        new selectToButtons({
            select: '#id_horizontal_alignment',
            icons: ['align-reset', 'flex-content-start', 'flex-content-center', 'flex-content-end',
                'flex-content-around', 'flex-content-between'],
            static: static_url,
        });
    }
});
