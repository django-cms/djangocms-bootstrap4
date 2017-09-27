/**
 * @class GridLayout
 * @public
 */
export default class GridLayout {
    /**
     * @method constructor
     * @param {Object} options
     * @param {Array} options.sizes
     * @param {Array} options.row
     * @param {String} options.static
     */
    constructor(options) {
        this.options = options;

        this.setHeader();
        this.setColumn();
        this.setInputType();
        this.setAutoInput();
    }

    /**
     * @method setHeader
     */
    setHeader() {
        let container = $('.form-row.field-xs_auto .field-box');
        let sizes = ['size-xs', 'size-sm', 'size-md', 'size-lg', 'size-xl'];
        let wrapper = (wrapper) => `<div class="icon-thead">${wrapper}</div>`;
        let icons = (icon, title = '', staticPath = this.options.static) => `
            <span class="icon icon-${icon}" title="${title}">
                <svg role="presentation">
                    <use xlink:href="${staticPath}djangocms_bootstrap4/sprites/icons.svg#${icon}"></use>
                </svg>
            </span>
            <span class="icon-title">${title}</span>`;
        let tmp = '';

        sizes.forEach(function (item, index) {
            tmp = icons(item, this.options.sizes[index]);

            container.eq(index).prepend(
                wrapper(tmp)
            );
        }, this);
    }

    /**
     * @method setColumn
     */
    setColumn() {
        const container = $(`
            .form-row.field-xs_col,
            .form-row.field-xs_auto,
            .form-row.field-xs_order,
            .form-row.field-xs_ml,
            .form-row.field-xs_mr
        `);
        const template = (text = '', link = '#', staticPath = this.options.static) => `
            <div class="field-box field-box-label">
                <a href="${link}" target="_blank" class="d-inline-block text-right">
                    ${text}
                    <span class="icon icon-info icon-primary">
                        <svg role="presentation">
                            <use xlink:href="${staticPath}djangocms_bootstrap4/sprites/icons.svg#info"></use>
                        </svg>
                    </span>
                </a>
            </div>
        `;
        const links = [
            'https://getbootstrap.com/docs/4.0/layout/grid/#variable-width-content',
            'https://getbootstrap.com/docs/4.0/layout/grid/#grid-options',
            'https://getbootstrap.com/docs/4.0/layout/grid/#reordering',
            'https://getbootstrap.com/docs/4.0/layout/grid/#offsetting-columns',
            'https://getbootstrap.com/docs/4.0/layout/grid/#offsetting-columns',
        ];

        container.toArray().forEach(function (item, index) {
            $(item).prepend(template(this.options.rows[index], links[index]));
        }, this);
    }

    /**
     * @method setInputType
     */
    setInputType() {
        const container = $('.form-row.field-xs_col, .form-row.field-xs_order');

        container.find('input').prop({
            'type': 'number',
            // TODO this should come from the backend
            'max': 12,
            'min': 1,
        });
    }

    /**
     * @method setAutoInput
     */
    setAutoInput() {
        const checks = $(
            '#id_xs_auto, #id_sm_auto, #id_md_auto, #id_lg_auto, #id_xl_auto'
        );

        checks.on('change', function () {
            let check = $(this);
            let cls = '#' + check.attr('id').replace('auto', '') + 'col';
            let input = check.closest('.module').find(cls);

            if (check.is(':checked')) {
                input.attr('disabled', true).addClass('disabled');
            } else {
                input.attr('disabled', false).removeClass('disabled');
            }
        });
    }

}
