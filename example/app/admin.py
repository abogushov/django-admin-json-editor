from django.contrib import admin
from django import forms

from app.models import ArrayJSONModel
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
        }


@admin.register(JSONModel)
class JSONModelAdmin(admin.ModelAdmin):
    form = JSONModelAdminForm


@admin.register(ArrayJSONModel)
class ArrayJSONModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        widgets = {'roles': JSONEditorWidget(HOST_ROLES_SCHEMA, False)}
        form = super().get_form(request, obj, widgets=widgets, **kwargs)
        return form
