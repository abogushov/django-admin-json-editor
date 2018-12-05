from django.contrib import admin
from django import forms

from django_admin_json_editor import JSONEditorWidget

from .models import JSONModel, ArrayJSONModel, Tag, OtherJSONModel, RelatedJSONModel


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

OTHER_DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'other_text': {
            'title': 'Some other text',
            'type': 'string',
            'format': 'textarea',
        },
        'status': {
            'title': 'Status',
            'type': 'boolean',
        },
    },
    'required': ['other_text']
}

RELATED_DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'related_info': {
            'title': 'Some related info',
            'type': 'string',
            'format': 'textarea',
        },
        'relevant': {
            'title': 'Relevant',
            'type': 'boolean',
        },
    },
    'required': ['related_info']
}


def dynamic_schema(widget):
    return {
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
                    'enum': [i for i in Tag.objects.values_list('name', flat=True)],
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
        widget = JSONEditorWidget(dynamic_schema, False)
        form = super().get_form(request, obj, widgets={'roles': widget}, **kwargs)
        return form


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
    
    
class RelatedJSONModelStackedInline(admin.StackedInline):
    model = RelatedJSONModel
    extra = 0
    def get_formset(self, request, obj=None, **kwargs):
        widgets = {
            'related_data': JSONEditorWidget(RELATED_DATA_SCHEMA, False),
        }
        return super().get_formset(request, obj, widgets=widgets, **kwargs)
        
@admin.register(OtherJSONModel)
class OtherJSONModelAdmin(admin.ModelAdmin):
    inlines = [ RelatedJSONModelStackedInline, ]
    def get_form(self, request, obj=None, **kwargs):
        widgets = {
            'data': JSONEditorWidget(OTHER_DATA_SCHEMA, collapsed=False),
        }
        return super().get_form(request, obj, widgets=widgets, **kwargs)

    