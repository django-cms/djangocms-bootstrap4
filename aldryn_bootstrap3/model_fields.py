# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from six import with_metaclass
import django.core.exceptions
import django.db.models
from django.utils.encoding import smart_text
from . import fields


class Breakpoint(with_metaclass(
                    django.db.models.SubfieldBase,
                    django.db.models.CharField)):
    default_form_class = fields.Breakpoint

    def __init__(self, *args, **kwargs):
        if 'max_length' not in kwargs:
            kwargs['max_length'] = 255
        if 'blank' not in kwargs:
            kwargs['blank'] = True
        super(Breakpoint, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {
            'form_class': self.default_form_class,
        }
        defaults.update(kwargs)
        return super(Breakpoint, self).formfield(**defaults)

    def to_python(self, value):
        if not value:
            return []
        elif isinstance(value, (list, tuple)):
            return [smart_text(val) for val in value]
        elif isinstance(value, basestring):
            return self.to_python([v.strip() for v in value.split(',')])
        else:
            raise django.core.exceptions.ValidationError(
                self.error_messages['invalid_list'], code='invalid_list')

    def get_prep_value(self, value):
        value.sort()
        return ','.join([v.strip() for v in value])

    def south_field_triple(self):
        """Returns a suitable description of this field for South."""
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.CharField"
        args, kwargs = introspector(self)
        # That's our definition!
        return (field_class, args, kwargs)
