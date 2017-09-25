/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/divio/djangocms-boilerplate-webpack
 */

// import 'bootstrap/js/dist/alert'
import { selectToButtons } from 'components/selectToButtons';


$(() => {
    selectToButtons({
        select: '#id_vertical_alignment',
        help: true,
        // length needs to match with select options
        icons: ['align-reset', 'flex-align-start', 'flex-align-center', 'flex-align-end'],
        static: $('.djangocms-bootstrap4-row').data('static'),
    });
});
