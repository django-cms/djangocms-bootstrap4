/**
 * Templates
 */
export const iconTemplate = (icon, staticPath = '/static/', title = '') => `
    <span class="icon icon-${icon}" title="${title}">
        <svg role="presentation">
            <use xlink:href="${staticPath}djangocms_bootstrap4/sprites/icons.svg#${icon}"></use>
        </svg>
    </span>`;
