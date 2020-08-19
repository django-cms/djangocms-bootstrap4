from django.test import TestCase

from djangocms_bootstrap4.fields import (
    AttributesField, IntegerRangeField, TagTypeField,
)


class B4FieldsTestCase(TestCase):

    def test_attributes_field(self):
        field = AttributesField()
        self.assertEqual(field.verbose_name, "Attributes")
        self.assertEqual(field.blank, True)

    def test_tag_type_field(self):
        field = TagTypeField()
        self.assertEqual(field.verbose_name, "Tag type")
        self.assertEqual(field.choices, (
            ('div', 'div'),
            ('section', 'section'),
            ('article', 'article'),
            ('header', 'header'),
            ('footer', 'footer'),
            ('aside', 'aside')
        ))
        self.assertEqual(field.default, "div")
        self.assertEqual(field.max_length, 255)
        self.assertEqual(
            field.help_text,
            "Select the HTML tag to be used.",
        )

    def test_integer_range_field(self):
        field = IntegerRangeField()
        self.assertEqual(field.min_value, None)
        self.assertEqual(field.max_value, None)
        field.min_value = 255
        field.max_value = 255
        field = field.formfield()
        self.assertEqual(field.min_value, 255)
        self.assertEqual(field.max_value, 255)
