from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_grid.models import (
    Bootstrap4GridColumn, Bootstrap4GridContainer, Bootstrap4GridRow,
)


class B4GridModelTestCase(TestCase):

    def test_grid_instance(self):
        instance = Bootstrap4GridContainer.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(Container)")

    def test_row_instance(self):
        instance = Bootstrap4GridRow.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(0 columns)")

    def test_column_instance(self):
        instance = Bootstrap4GridColumn.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(auto) ")
        instance.xs_col = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .col-12",
        )
        instance.column_type = "column"
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column .col-12",
        )
        instance.md_col = 12
        instance.md_offset = 12
        instance.xs_offset = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column .col-12 .offset-12 .col-md-12 .offset-md-12",
        )
        instance.xs_ml = 12
        instance.md_ml = 12
        self.assertEqual(
            instance.get_short_description(),
            "(col-12) .column .col-12 .offset-12 .ml-auto .col-md-12 .offset-md-12 .ml-md-auto",
        )
