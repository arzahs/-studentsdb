function initJournal() {
  var indicator = $('#ajax-progress-indicator');

  $('.day-box input[type="checkbox"]').click(function(event){
    var box = $(this);
    $.ajax(box.data('url'), {
      type: 'POST',
      async: true,
      dataType: 'json',
      data: {
        'pk': box.data('student-id'),
        'date': box.data('date'),
        'present': box.is(':checked') ? '1': '0',
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      'beforeSend': function(xhr, settings){
        indicator.show();
      },
      'error': function(xhr, status, error){
        alert(error);
        indicator.hide();
      },
      'success': function(data, status, xhr){
        indicator.hide();
      }
    });
  });
}


function initGroupSelector() {
// look up select element with groups and attach our even handler
// on field "change" event
$('#group-selector select').change(function(event){
// get value of currently selected group option
var group = $(this).val();

if (group) {

  $.cookie('current_group', group, {'path': '/', 'expires': 365});
  console.log('add group');
} 
else {
  $.removeCookie('current_group', {'path': '/'});
  console.log('remove group');
}
  location.reload(true);
  console.log('reload');
  return true;
});

}

function initDateFields() {
$('input.dateinput').datetimepicker({
'format': 'YYYY-MM-DD'
}).on('dp.hide', function(event){
  $(this).blur();
});
}

$(document).ready(function(){
  initJournal();
  initGroupSelector();
  initDateFields();
});
