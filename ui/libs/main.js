var cardTemplate = '<div class="col-md-4">' + 
'    <!--Card-->' + 
'    <div class="card">' + 

'        <!--Card image-->' + 
'        <div class="view overlay hm-white-slight">' + 
'            <img src="" class="img-fluid tw-imageUrl" alt="">' + 
'            <a href="#!">' + 
'                <div class="mask"></div>' + 
'            </a>' + 
'        </div>' + 
'        <!--/.Card image-->' + 

'        <!--Card content-->' + 
'        <div class="card-block">' + 
'            <!--Title-->' + 
'            <h4 class="card-title tw-restaurant-name"></h4>' + 
'            <!--Text-->' + 
'            <p class="card-text tw-restaurant-details">Some quick example text to build on the card title and make up the bulk of the cards content.</p>' + 
'            <div class="read-more">' + 
'             <a href="#!" class="btn btn-primary">Visit</a>' + '</div>' + 
'        </div>' + 
'        <!--/.Card content-->' + 

'    </div>' + 
'    <!--/.Card-->    ' + 
'</div>';

$.ajax({
  url: 'http://10.20.55.17:5002/getEntity',
  contentType: 'application/json',
  dataType: 'json',
  type: 'GET',
  success: function(resp) {
    var $cardMarkup,
      restaurantObject;

    for (var i = 0; i < resp.length; i++) {
      $cardMarkup = $(cardTemplate);
      $cardMarkup
        .find('tw-imageUrl').attr('src', )

    }
  }
})