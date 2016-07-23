var TW = TW || {};
var menuItemTemplate = '<div class="media">' + 
'    <a class="media-left waves-light">' + 
'        <img class="img-circle tw-imageUrl menu-item-image" alt="Generic placeholder image">' + 
'    </a>' + 
'    <div class="media-body">' + 
'        <a href="#!" class="btn right btn-primary tw-menu-item-button">Select</a>' +  
'        <span class="tw-item-price"></span>' +  
'        <h4 class="media-heading tw-item-name"></h4>' + 
'        <ul class="rating inline-ul tw-star-container"></ul>' + 
'        <p class="tw-item-description"></p>' +
'    </div>' + 
'</div>';

var queryParams = window.location.search.split('&');
var id = queryParams[0].split('=')[1];
var name = decodeURIComponent(queryParams[1].split('=')[1]);

console.log('id:', id, ' name:', name);

$('.tw-restaurant-name').html(name);

$.ajax({
  url: 'http://10.20.55.17:5002/getCatalog?entity_id=' + id,
  contentType: 'application/json',
  dataType: 'json',
  type: 'GET',
  success: function(resp) {
    var menuItem,
      $card;

    TW.items = resp;

    for (var i = 0; i < resp.length; i++) {
      menuItem = resp[i];
      $item = $(menuItemTemplate);

      $item.find('.tw-imageUrl').attr('src', menuItem.imageUrl);
      $item.find('.tw-item-name').html(menuItem.name);
      $item.find('.tw-item-price').html('Price: Rs' + menuItem.price);
      $item.find('.tw-menu-item-button').attr('data-id', menuItem.id); 
      $item.find('.tw-item-description').html(menuItem.description || 'description');

      addStars($item.find('.tw-star-container'), menuItem.stars || 1);
      
      $item.appendTo('.tw-menu');
    }

    addListeners();
  }
});

function addStars($container, numStars) {
  for (var i = 0; i < Math.min(numStars, 5); i++) {
    $('<li><i class="fa fa-star amber-text"></i></li>').appendTo($container)  
  }

  for (var i = numStars; i < 5; i++) {
    $('<li><i class="fa fa-star"></i></li>').appendTo($container)  
  }
}

function addListeners() {
  $('.tw-menu-item-button').click(function(event) {
    if ($(this).hasClass('btn-primary')) {
      $(this).removeClass('btn-primary').addClass('btn-success');
      $(this).html('Selected');

      return;
    } else if ($(this).hasClass('btn-success')) {
      $(this).removeClass('btn-success').addClass('btn-primary');
      $(this).html('Select');
    }
  });
}

$('.tw-checkout-button').click(function() {
  // Check number of selected items
  var selectedItems = $('.tw-menu-item-button.btn-success');

  if (selectedItems.length === 0) {
    alert('Please select atleast 1 item');
    return;
  }

  var items = [];

  selectedItems.each(function(index, item) {
    items.push({ 
      id: Number($(item).attr('data-id')),
      quantity: 1 
    })
  });

  $.ajax({
    url: 'http://10.20.55.17:5002/blockCatalog?transaction=' + JSON.stringify(items),
    contentType: 'application/json',
    dataType: 'json',
    type: 'GET',
    success: function(resp) {
      if (resp.status === 1) {
        alert('Your order has been placed successfully!!');
        return;
      }

      for (var i = 0; i < resp.items.length; i++) {
        if (resp.items[i].quantityRemaining < 0) {
          alert('Sorry! Demand is high and in meanwhile some items have gone out of stock');
          
          $('.btn[data-id="' + resp.items[i].id + '"]')
            .removeClass('tw-menu-item-button')
            .addClass('btn-danger')
            .html('Out of Stock');
        }
      }
    }
  });
});