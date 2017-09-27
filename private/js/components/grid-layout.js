/**
 * @class GridLayout
 * @public
 */
export default class GridLayout {
    /**
     * @method constructor
     * @param {Object} options
     */
    constructor(options) {
        this.options = options;

        this.setHeader();
        this.setColumn();
        this.setInputType();
    }

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

    setColumn() {
        let container = $(`
            .form-row.field-xs_col,
            .form-row.field-xs_auto,
            .form-row.field-xs_order,
            .form-row.field-xs_ml,
            .form-row.field-xs_mr
        `);
        let template = (text) => `
            <div class="field-box field-box-label">
                <span class="d-inline-block text-right">${text}</span>
            </div>
        `;

        container.toArray().forEach(function (item, index) {
            $(item).prepend(template(this.options.rows[index]));
        }, this);
        container.prepend('');
    }

    setInputType() {
        let container = $('.form-row.field-xs_col, .form-row.field-xs_order');

        container.find('input').prop({
            'type': 'number',
            // TODO this should come from the backend
            'max': 12,
            'min': 1,
        });
    }

}
