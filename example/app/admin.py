from django.contrib import admin
from django import forms

from django_admin_json_editor import JSONEditorWidget

from .models import JSONModel


DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'text': {
            'title': 'Some text',
            'type': 'string',
            'format': 'textarea',
        },
        'status': {
            'title': 'Status',
            'type': 'boolean',
        },
        'html': {
            'title': 'HTML',
            'type': 'string',
            'format': 'html',
            'options': {
                'wysiwyg': 1,
            }
        },
    },
}


class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = '__all__'
        widgets = {
            'data': JSONEditorWidget(DATA_SCHEMA, collapsed=False, sceditor=True),
        }


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    form = JSONModelAdminForm
