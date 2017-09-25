export function selectToButtons(options) {
    const templates = {
        wrapper: '<div class="bootstrap4-button-group">' +
                 '  <div class="btn-group" role="group" aria-label="">' +
                 '    {buttons}' +
                 '  </div>' +
                 '</div>',
        button: '<button type="button" class="btn">{icon}<span class="sr-only">{text}</span></button>',
        icon: '<span class="icon icon-{icon}">' +
              '  <svg role="presentation">' +
              '      <use xlink:href="' + options.static + 'djangocms_bootstrap4/sprites/icons.svg#{icon}"></use>' +
              '  </svg>' +
              '</span>'
    };
    const select = $(options.select);
    const selectOptions = select.find('option');

    // template manipulation
    let buttons = '';
    let icon = '';
    selectOptions.each(function (index, selectOption) {
        // prepare icon
        icon = templates.icon.slice(0).replace(new RegExp('{icon}', 'g'), options.icons[index]);
        // add button
        buttons += templates.button.slice(0).replace(
            '{text}', $(selectOption).text()
        ).replace('{icon}', icon);
    });
    let group = templates.wrapper.slice(0).replace('{buttons}', buttons);

    if (options.icons.length !== selectOptions.length) {
        throw new Error('Provided icons do not match options.');
    }

    select.after(group);
}
