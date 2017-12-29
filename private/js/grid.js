/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/divio/djangocms-boilerplate-webpack
 */

import ButtonGroup from 'components/button-group';
import GridLayout from 'components/grid-layout'
import { iconTemplate } from 'components/templates'


$(() => {
    // Row plugin
    if ($('.djangocms-bootstrap4-row').length) {
        const static_url = $('.djangocms-bootstrap4-row').data().static;

        // Bootstrap 4 Grid Row - Vertical Alignment
        new ButtonGroup({
            static: static_url,
            select: '#id_vertical_alignment',
            icons: ['align-reset', 'flex-align-start', 'flex-align-center', 'flex-align-end'],
        });
        // Bootstrap 4 Grid Row - Horizontal Alignment
        new ButtonGroup({
            static: static_url,
            select: '#id_horizontal_alignment',
            icons: ['align-reset', 'flex-content-start', 'flex-content-center', 'flex-content-end',
                'flex-content-around', 'flex-content-between'],
        });

        $('.form-row.field-create > div').before(
            iconTemplate('columns', static_url)
        );
    }

    // Column plugin
    const column = $('.djangocms-bootstrap4-column');
    if (column.length) {
        const static_url = $('.djangocms-bootstrap4-column').data().static;

        // Bootstrap 4 Grid Column - Alignment
        new ButtonGroup({
            select: '#id_column_alignment',
            icons: ['align-reset', 'flex-self-start', 'flex-self-center', 'flex-self-end'],
            static: static_url,
        });
        // Bootstrap 4 Grid Column - Reponsive Settings
        new GridLayout({
            sizes: column.data().sizes,
            rows: column.data().rows,
            reset: column.data().reset,
            static: static_url,
        });
    }
});
