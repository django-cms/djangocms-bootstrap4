/**
 * @class selectToButtons
 * @public
 */
export class selectToButtons {
    /**
     * @method constructor
     * @param {Object} options
     */
    constructor(options) {
        this.options = options;
        this.templates = {
            wrapper: '<div class="bootstrap4-button-group{class}">' +
                     '  <div class="btn-group" role="group" aria-label="">' +
                     '    {buttons}' +
                     '  </div>' +
                     '</div>',
            button: '<button type="button" class="btn">' +
                    '  {icon}<span class="sr-only">{text}</span>' +
                    '</button>',
            icon: '<span class="icon icon-{icon}">' +
                  '  <svg role="presentation">' +
                  '    <use xlink:href="' + this.options.static + 'djangocms_bootstrap4/sprites/icons.svg#{icon}"></use>' +
                  '  </svg>' +
                  '</span>',
        };
        this.select = $(this.options.select);
        this.selectOptions = this.select.find('option');

        // initialize
        this.select.after(
            this.setEvents($(this.getTemplate()))
        );
    }

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

    getTemplate() {
        let buttons = '';
        let icon = '';
        let wrapper = this.templates.wrapper.slice(0);

        this.select.addClass('sr-only');

        if (this.options.icons &&
            this.options.icons.length !== this.selectOptions.length) {
            throw new Error('Provided icons do not match options.');
        } else if (this.options.icons) {
            wrapper = wrapper.replace('{class}', ' bootstrap4-button-group-icons');
        } else {
            wrapper = wrapper.replace('{class}', '');
        }

        this.selectOptions.toArray().forEach(function (selectOption, index) {
            // prepare icon
            if (this.options.icons) {
                icon = this.templates.icon.slice(0).replace(
                    new RegExp('{icon}', 'g'), this.options.icons[index]
                );
            } else {
                icon = $(selectOption).text();
            }
            // add button
            buttons += this.templates.button.slice(0).replace(
                '{text}', $(selectOption).text()
            ).replace('{icon}', icon);
        }, this);

        return wrapper.replace('{buttons}', buttons);
    }

}
