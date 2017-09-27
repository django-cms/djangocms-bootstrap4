/**
 * @class selectToButtons
 * @public
 */
export default class SelectToButtons {
    /**
     * @method constructor
     * @param {Object} options
     * @param {String} options.select
     * @param {String} options.static
     * @param {String[]} [options.icons]
     */
    constructor(options) {
        this.options = options;
        this.templates = {
            wrapper: (cls = '', buttons = '') => `
                <div class="bootstrap4-button-group${cls}">
                    <div class="btn-group" role="group" aria-label="">
                        ${buttons}
                    </div>
                </div>`,
            button: (icon = '', text = '') => `
                <button type="button" class="btn" title="${text}">
                    ${icon}<span class="sr-only">${text}</span>
                </button>`,
            icon: (icon, staticPath = this.options.static) => `
                <span class="icon icon-${icon}">
                    <svg role="presentation">
                        <use xlink:href="${staticPath}djangocms_bootstrap4/sprites/icons.svg#${icon}"></use>
                    </svg>
                </span>`,
        };
        this.select = $(this.options.select);
        this.selectOptions = this.select.find('option');

        // initialize
        this.select.after(
            this.setEvents($(this.getTemplate()))
        );
    }

    /**
     * @method setEvents
     * @param {jQuery} template
     * @return {jQuery} template
     */
    setEvents(template) {
        let buttons = template.find('button');
        let select = this.select;
        let options = this.select.find('option');
        let index = options.index(options.filter(':selected'));

        buttons.on('click', function (e) {
            e.preventDefault();
            // set the value on the select
            select.find('option')
                .prop('selected', false)
                .eq(buttons.index(this))
                .prop('selected', true);
            // set icon color
            buttons.find('.icon').removeClass('icon-white');
            $(this).find('.icon').addClass('icon-white');
            // set active state of the button
            buttons.removeClass('btn-primary');
            $(this).addClass('btn-primary');
        }).bind(this);

        // set initial active item
        buttons.eq(index).trigger('click');

        return template;
    }

    /**
     * @method getTemplate
     * @return {String} template
     */
    getTemplate() {
        let cls = '';

        this.select.addClass('sr-only');

        if (this.options.icons &&
            this.options.icons.length !== this.selectOptions.length) {
            throw new Error('Provided icons do not match options.');
        } else if (this.options.icons) {
            cls = ' bootstrap4-button-group-icons';
        }

        const buttons = this.selectOptions.toArray().reduce((btns, selectOption, index) => {
            let text = $(selectOption).text();
            let icon;

            // prepare icon
            if (this.options.icons) {
                icon = this.templates.icon(this.options.icons[index]);
            } else {
                icon = text;
            }
            // add button
            btns += this.templates.button(icon, text);

            return btns;
        }, '');

        return this.templates.wrapper(cls, buttons);
    }

}
