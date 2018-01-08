export const iconTemplate = (icon, staticPath = '/static/', title = '') => `
    <span class="icon icon-${icon}" title="${title}">
        <svg role="presentation">
            <use xlink:href="${staticPath}djangocms_bootstrap4/sprites/icons.svg#${icon}"></use>
        </svg>
    </span>`;

export const previewTemplate = (classes = '', title = 'Preview') => `
    <div class="djangocms-bootstrap4-preview ${classes}">
        <h2>${title}</h2>
        <div class="b4-preview js-preview"></div>
        <a href="#close" class="b4-close js-close">x</a>
    </div>
`;
