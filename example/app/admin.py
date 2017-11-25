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
    'required': ['text']
}

HOST_ROLES_SCHEMA = {
    'type': 'array',
    'title': 'roles',
    'items': {
        'type': 'object',
        'required': [
            'name',
            'tag',
        ],
        'properties': {
            'name': {
                'title': 'Name',
                'type': 'string',
                'format': 'text',
                'minLength': 1,
            },
            'tag': {
                'title': 'Tag',
                'type': 'string',
                'format': 'text',
                'minLength': 1,
            }
         }
    }
}


class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = '__all__'
        widgets = {
            'data': JSONEditorWidget(DATA_SCHEMA, collapsed=False, sceditor=True),
            'roles': JSONEditorWidget(HOST_ROLES_SCHEMA, collapsed=False),
        }


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    form = JSONModelAdminForm
