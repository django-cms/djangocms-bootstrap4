export const iconTemplate = (icon, staticPath = '/static/', title = '') => `
    <span class="icon icon-${icon}" title="${title}"></span>`

export const previewTemplate = (classes = '', title = 'Preview') => `
    <div class="djangocms-bootstrap5-preview ${classes}">
        <h2>${title}</h2>
        <div class="b4-preview js-preview"></div>
        <a href="#close" class="b4-close js-close">&times;</a>
    </div>
`;
