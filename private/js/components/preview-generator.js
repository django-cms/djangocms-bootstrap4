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
        };
        this.spacer = '---';
        this.markup = (text = this.spacer) => `
            <span class="js-button">${text}</span>
        `;
        this.template = $(this.options.template(
            'bootstrap4-button-group', this.options.title
        ));
        this.preview = this.template.find('.js-preview');
        this.preview.append(this.markup());
        this.button = this.preview.find('.js-button');
        this.closed = false;

        this.events();
        this.initialize();
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
        this.elements.text.on('keyup', (e) => {
            let text = $(e.currentTarget).val() || this.spacer;
            this.button.text(text);
        }).trigger('keyup');

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
    }

    update() {
        let context = this.elements.context.val() || '';

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

        // handle block class
        if (this.elements.block.is(':checked')) {
            this.button.addClass('btn-block');
        }
    }

    close() {
        this.template.find('.js-preview, h2').hide();
        this.template.find('.js-close').text('O');
        this.closed = true;
    }

    open () {
        this.template.find('.js-preview, h2').show();
        this.template.find('.js-close').text('X');
        this.closed = false;
    }

}
