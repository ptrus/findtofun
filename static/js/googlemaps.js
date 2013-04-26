'use strict';

/* Google Maps */

var map;
function initialize() {
	var mapOptions = {
		zoom: 16,
		center: new google.maps.LatLng(46.05223, 14.50567),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}