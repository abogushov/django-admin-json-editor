from django_admin_json_editor.admin import JSONEditorWidget


def test_empty_schema_widget():
    widget = JSONEditorWidget(schema={})
    assert widget.render('name', 'value')
