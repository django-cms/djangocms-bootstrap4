from django.forms import BooleanField, IntegerField, models
from django.utils.translation import gettext_lazy as _

from djangocms_bootstrap4.constants import DEVICE_SIZES

from .constants import GRID_SIZE
from .models import Bootstrap4GridColumn, Bootstrap4GridRow


class Bootstrap4GridRowForm(models.ModelForm):
    create = IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create when saving.'),
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )

    class Meta:
        model = Bootstrap4GridRow
        fields = '__all__'


class Bootstrap4GridColumnBaseForm(models.ModelForm):
    class Meta:
        model = Bootstrap4GridColumn
        fields = '__all__'


# convert regular text type fields to number
extra_fields_column = {}
for size in DEVICE_SIZES:
    extra_fields_column[f'{size}_col'] = IntegerField(
        label='col' if size == 'xs' else f'col-{size}',
        required=False,
        min_value=1,
        max_value=GRID_SIZE,
    )
    extra_fields_column[f'{size}_order'] = IntegerField(
        label='order' if size == 'xs' else f'order-{size}',
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )
    extra_fields_column[f'{size}_offset'] = IntegerField(
        label='offset' if size == 'xs' else f'offset-{size}',
        required=False,
        min_value=0,
        max_value=GRID_SIZE,
    )
    extra_fields_column[f'{size}_ml'] = BooleanField(
        label='ml-auto' if size == 'xs' else f'ml-{size}-auto',
        required=False,
    )
    extra_fields_column[f'{size}_mr'] = BooleanField(
        label='mr-auto' if size == 'xs' else f'mr-{size}-auto',
        required=False,
    )

Bootstrap4GridColumnForm = type(
    'Bootstrap4GridColumnBaseForm',
    (Bootstrap4GridColumnBaseForm,),
    extra_fields_column,
)
