var map, min, max;
function initialize() {
	var mapOptions = {
		zoom: 16,
		center: new google.maps.LatLng(46.05223, 14.50567),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	var bounds = map.getBounds();
	min = bounds.getSouthWest();
	max = bounds.getNorthEast();
	$("#timeFrom").text("Lat: "+ min + " Lng: " + max);
}

var addressField = document.getElementById('search_address');
var geocoder = new google.maps.Geocoder();

function search() {
    geocoder.geocode(
        {'address': addressField.value}, 
        function(results, status) { 
            if (status == google.maps.GeocoderStatus.OK) { 
                var loc = results[0].geometry.location;
                // use loc.lat(), loc.lng()
				$("#loc").text("Lat: "+loc.lat() + " Lng: " + loc.lng());
				
            } 
            else {
                alert("Not found: " + status); 
            } 
        }
    );
};