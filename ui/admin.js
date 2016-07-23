var TW = TW || {};

$('.tw-rule-add-button').click(function() {
  var res = $('#form1').val()
  var quantity = $('#formquantity').val()
  var operator = $('#formoperator').val()
  var itemid = $('#formItemId ').val()

  $.ajax({
    url: 'http://10.20.55.17:5002/addRule?entity_id=' + res + '&quantity=' + quantity + '&operator=' + operator + '&item_id=' + itemid,
    type: 'GET',
    success: function(resp) {
      alert('Rule added successfully!')
    }
  });

});