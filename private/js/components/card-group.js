import $ from 'jquery';
import ButtonGroup from 'components/button-group';

/**
 * @class CardGroup
 * @public
 */
export default class CardGroup extends ButtonGroup {
    /**
     * @method constructor
     * @param {Object} options (inherited from ButtonGroup)
     * @param {Array} classes
     */
    constructor(options) {
        super(options);
    }

    /**
     * @method setEvents
     * @param {jQuery} template
     * @return {jQuery} template
     */
    getTemplate() {
        this.templates = {
            wrapper: (cls = '', blueprints = '', buttons = '') => `
                <div class="bootstrap5-blueprint${cls}">
                    ${blueprints}
                    <div class="bootstrap5-button-group bootstrap5-button-group-blueprint">
                        <div class="btn-group" role="group" aria-label="">
                            ${buttons}
                        </div>
                    </div>
                </div>`,
            blueprints: (lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.') => `
                <div class="card-deck">
                    <div class="card">
                        <div class="card-img-top">
                            <img src="https://dummyimage.com/600x250/777777/dcdcdc" class="img-fluid">
                        </div>
                        <div class="card-body">
                            <div class="card-text">${lorem}</div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-header">
                            <div class="card-text">Card header</div>
                        </div>
                        <div class="card-body">
                            <div class="card-text">${lorem}</div>
                        </div>
                        <div class="card-footer">
                            <div class="card-text">Card footer</div>
                        </div>
                    </div>
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Card title</h4>
                            <p class="card-text">${lorem}</p>
                            <span class="btn-primary">Go somewhere</span>
                        </div>
                    </div>
                </div>`,
            button: (text = '') => `
                <span type="button" class="btn btn-default" title="${text}">
                    ${text}
                </span>`,
        };

        let cls = '';
        let buttons = this.selectOptions.toArray().reduce((btns, selectOption) => {
            let text = $(selectOption).text();
            // add button
            btns += this.templates.button(text);
            return btns;
        }, '');
        let template = this.templates.wrapper(
            cls,
            this.templates.blueprints(),
            buttons,
        );

        this.select.addClass('hidden');

        return template;
    }

}
