/*
 * Copyright (c) 2013, Divio AG
 * Licensed under BSD
 * http://github.com/divio/djangocms-boilerplate-webpack
 */

// import 'bootstrap/js/dist/alert'
import ContextGroup from 'components/context-group';
import PreviewGenerator from 'components/preview-generator';
import ButtonGroup from 'components/button-group';


$(() => {
    const { static_url } = $('.djangocms-bootstrap4').data().static;

    // general color context without auto alignment
    // ALERT, BADGE,
    new ContextGroup({
        select: '#id_alert_context, #id_badge_context',
        classes: [
            'btn-primary', 'btn-secondary',
            'btn-success', 'btn-danger', 'btn-warning',
            'btn-info', 'btn-light', 'btn-dark',
        ],
    });
    // general color context with auto alignment
    // CARD
    new ContextGroup({
        select: '#id_card_context',
        classes: [
            '', 'btn-primary', 'btn-secondary',
            'btn-success', 'btn-danger', 'btn-warning',
            'btn-info', 'btn-light', 'btn-dark',
        ],
        extraClass: 'bootstrap4-button-group-context-colors',
    });
    new ContextGroup({
        select: '#id_card_text_color',
        classes: [
            '', 'btn-primary', 'btn-secondary',
            'btn-success', 'btn-danger', 'btn-warning',
            'btn-info', 'btn-light', 'btn-dark',
        ],
        extraClass: 'bootstrap4-button-group-context-colors',
    });
    // simple buttons
    // CARD
    new ContextGroup({
        select: '#id_inner_type',
        classes: [
            'btn-secondary', 'btn-secondary', 'btn-secondary',
        ],
    });
    // LIST
    new ContextGroup({
        select: '#id_list_context',
        classes: [
            '', 'btn-primary', 'btn-secondary',
            'btn-success', 'btn-danger', 'btn-warning',
            'btn-info', 'btn-light', 'btn-dark',
        ],
    });
    // LINK
    new ContextGroup({
        select: '#id_link_context',
        classes: [
            '', 'btn-link', 'btn-primary', 'btn-secondary',
            'btn-success', 'btn-danger', 'btn-warning',
            'btn-info', 'btn-light', 'btn-dark',
        ],
        extraClass: 'bootstrap4-button-group-context-colors',
    });
    new ContextGroup({
        select: '#id_link_size',
        classes: [
            'btn-sm btn-secondary', 'btn-secondary', 'btn-secondary btn-lg',
        ],
        extraClass: 'bootstrap4-button-group-context-size',
    });

    // IMAGE PREVIEW
    if ($('.djangocms-bootstrap4-link').length) {
        new PreviewGenerator({
            container: '.djangocms-bootstrap4-link',
            title: $('.djangocms-bootstrap4-link').data().preview,
        });
    }

    // adds alignment button
    // BLOCKQUOTE, CARD, FIGURE
    if (
        $('#id_quote_alignment').length ||
        $('#id_card_alignment').length ||
        $('#id_figure_alignment').length
    ) {
        // alignment
        new ButtonGroup({
            static_url,
            select: '#id_quote_alignment, #id_card_alignment, #id_figure_alignment',
            icons: ['align-reset', 'flex-content-start', 'flex-content-center', 'flex-content-end'],
        });
    }
});
