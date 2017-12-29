import ButtonGroup from 'components/button-group';

/**
 * @class ContextGroup
 * @public
 */
export default class ContextGroup extends ButtonGroup {
    /**
     * @method constructor
     * @param {Object} options (inherited from ButtonGroup)
     * @param {Array} classes
     */
    constructor(options) {
        super(options);

        this.options = options;
        this.setClasses();
    }

    /**
     * @method setClasses
     */
    setClasses() {
        // adds classes to the buttons
        const buttons = this.element.find('.btn');
        buttons.toArray().forEach(function (item, index) {
            buttons.eq(index).removeClass('btn-default');
            buttons.eq(index).addClass(this.options.classes[index])
        }, this);

        // remove group class
        this.element.find('.btn-group').removeClass('btn-group');

        // add class to the wrapper
        this.element.addClass('bootstrap4-button-group-context');

        if (this.options.extraClass) {
            this.element.addClass(this.options.extraClass);
        }
    }

}
