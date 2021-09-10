import $ from 'jquery';
import { previewTemplate } from 'components/templates';

/**
 * @class PreviewGenerator
 * @public
 */
export default class PreviewGenerator {
    /**
     * @method constructor
     */
    constructor(options) {
        this.options = options;
        this.options.template = previewTemplate;
        this.container = $(this.options.container);
        this.elements = {
            text: this.container.find('#id_name'), // text value
            type: this.container.find('#id_link_type_0, #id_link_type_1'), // link or button
            context: this.container.find('#id_link_context'), // color class
            size: this.container.find('#id_link_size'), // size class
            outline: this.container.find('#id_link_outline'), // outline class
            block: this.container.find('#id_link_block'), // block class
            icons: this.container.find('.djangocms-icon .js-icon'), // left and right icon
        };
        this.spacer = '---';
        this.markup = (text = this.spacer) => `
            <span class="js-button"><span class="js-icon-left"></span><span class="js-button-text">${text}</span><span class="js-icon-right"></span></span>
        `;
        this.template = $(this.options.template(
            'bootstrap5-button-group', this.options.title
        ));
        this.preview = this.template.find('.js-preview');
        this.preview.append(this.markup());
        this.button = this.preview.find('.js-button');
        this.buttonText = this.preview.find('.js-button-text');
        this.closed = false;

        this.events();
        this.initialize();

        // wait till icon pickers are initialized
        setTimeout(() => this.update());
    }

    initialize() {
        this.container.append(this.template);
    }

    events() {
        // close event
        this.template.find('.js-close').on('click', (e) => {
            e.preventDefault();
            (this.closed) ? this.open() : this.close();
        });

        // prevent action on the previews
        this.button.on('click', (e) => {
            e.preventDefault();
        });

        // changing the text
        this.elements.text.on('keyup change', (e) => {
            let text = $(e.currentTarget).val() || this.spacer;
            this.buttonText.text(text);
        });

        // have to do a timeout here because
        // when used in ckeditor it takes a tick to update
        // the display name value with selected text
        setTimeout(() => this.elements.text.trigger('change'));

        // changing the type
        this.elements.type.on('change', () => {
            this.update();
        });

        // changing the context
        this.elements.context.on('change', () => {
            this.update();
        }).trigger('change');

        // add outline
        this.elements.outline.on('change', () => {
            this.elements.context.trigger('change');
        });

        // change the size
        this.elements.size.on('change', () => {
            this.update();
        });

        // change the size
        this.elements.block.on('change', () => {
            this.update();
        });

        this.elements.icons.on('change', 'select, input', () => {
            this.update();
        });

        if (window.djangoCMSIcon) {
            window.djangoCMSIcon.$('button.iconpicker').on('change', () => {
                this.update();
            });
        }
    }

    update() {
        const context = this.elements.context.val() || '';

        // reset
        this.button.attr('class', '');

        // handle type, context and outline
        if (this.elements.type.eq(0).is(':checked')) {
            this.button.addClass('text-' + context);
        } else {
            if (this.elements.outline.is(':checked')) {
                this.button.addClass('btn btn-outline-' + context);
            } else {
                this.button.addClass('btn btn-' + context);
            }
        }

        // handle size class
        this.button.addClass(this.elements.size.val());

        const resetIcon = (left) => {
            $(`.js-icon-${left ? 'left' : 'right'}`).html('');
        };

        this.elements.icons.each((i, el) => {
            const element = $(el);
            const left = element.is('.js-icon-icon_left');

            if (!element.find(':checkbox').is(':checked')) {
                resetIcon(left);
                return;
            }

            const icon = element.find('input[type=hidden]').val();

            if (!icon) {
                resetIcon(left);
                return;
            }

            const iconSetValue = element.find('select').val();
            let iconSet = iconSetValue;

            try {
                iconSet = JSON.parse(iconSetValue);
            } catch (e) {} // eslint-disable-line

            const iconSetPrefix = element.find('select option:selected').data('iconset-prefix');

            if (typeof iconSet === 'string') {
                $(`.js-icon-${left ? 'left' : 'right'}`).html(`
                    <span class="${iconSetPrefix} ${icon}"></span>
                `);
            } else {
                const staticPath = this.container.data('static');
                const {
                    spritePath,
                    iconClass,
                } = iconSet;

                if (iconSet.svg) {
                    $(`.js-icon-${left ? 'left' : 'right'}`).html(`
                        <span class="${iconClass} ${icon}">
                            <svg role="presentation">
                                <use xlink:href="${staticPath}${spritePath}#${icon}"></use>
                            </svg>
                        </span>
                    `);
                } else {
                    $(`.js-icon-${left ? 'left' : 'right'}`).html(`
                        <span class="${iconClass} ${icon}"></span>
                    `);
                }
            }
        });

        // handle block class
        if (this.elements.block.is(':checked')) {
            this.button.addClass('btn-block');
        }
    }

    close() {
        this.template.find('.js-preview, h2').hide();
        this.template.find('.js-close').text('...');
        this.closed = true;
    }

    open () {
        this.template.find('.js-preview, h2').show();
        this.template.find('.js-close').html('&times;');
        this.closed = false;
    }

}
