var editor = {}
var $ = django.jQuery
var enable_json_editor = function(element){
  var id = element.id
  if (id.indexOf('__prefix__') === -1) { // activate editor only if it is not an inline template row
    var textarea_id = "id_"+element.id.replace('_editor', '')
    var schema = JSON.parse(element.getAttribute('data-schema'))
    var data = JSON.parse(element.getAttribute('data-data'))
    var options = {
        theme: "bootstrap3",
        iconlib: "fontawesome4",
        schema: schema,
    };
    editor[id] = new JSONEditor(element, options);
    JSONEditor.plugins.sceditor.emoticonsEnabled = element.getAttribute("data-sceditor");
    editor[id].on('change', function () {
        var errors = editor[id].validate();
        if (errors.length) {
            console.log(errors);
        }
        else {
            var json = editor[id].getValue();
            $('#'+textarea_id)[0].value = JSON.stringify(json);
        }
    });
    if (data != null) {
      editor[id].setValue(data);
    }
    
  }
}

$(document).ready(function() {
  $(document).find("[id$=_editor]").each(function(){
    enable_json_editor(this);      
  });  
});

$(document).on('formset:added', function(event, $row, formsetName) {
  $row.find("[id$=_editor]").each(function(){
    enable_json_editor(this);      
  });  
    
});