from django.template import TemplateDoesNotExist
from django.template.loader import select_template
from django.utils.functional import lazy
from django.utils.safestring import mark_safe


def concat_classes(classes):
    """
    merges a list of classes and return concatinated string
    """
    return ' '.join(_class for _class in classes if _class)


def get_template_path(prefix, template, name):
    return 'djangocms_bootstrap4/{}/{}/{}.html'.format(prefix, template, name)


def get_plugin_template(instance, prefix, name, templates):
    template = getattr(instance, 'template', templates[0][0])
    template_path = get_template_path(prefix, template, name)

    try:
        select_template([template_path])
    except TemplateDoesNotExist:
        # TODO render a warning inside the template
        template_path = get_template_path(prefix, 'default', name)

    return template_path


# use mark_safe_lazy to delay the translation when using mark_safe
# otherwise they will not be added to /locale/
# https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#other-uses-of-lazy-in-delayed-translations
mark_safe_lazy = lazy(mark_safe, str)
