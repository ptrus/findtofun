'use strict';

/* Controllers */

myApp.controller('EventListCtrl', function($scope) {
  $scope.toptenEnabled = true;
  $scope.googlemaspEnabled = false;
  $scope.calendarEnabled = false;
  $scope.dateEnabled = true;
  $scope.locationEnabled = true;
  $scope.radioModel = 'Left';
  $scope.toptenClicked = function() {
    $scope.toptenEnabled = true;
    $scope.googlemaspEnabled = false;
    $scope.calendarEnabled = false;
    $scope.dateEnabled = true;
    $scope.locationEnabled = true;
  };
  $scope.googlemapsClicked = function() {
    $scope.toptenEnabled = false;
    $scope.googlemaspEnabled = true;
    $scope.calendarEnabled = false;
    $scope.dateEnabled = true;
    $scope.locationEnabled = false;
  };
  $scope.calendarClicked = function() {
    $scope.toptenEnabled = false;
    $scope.googlemaspEnabled = false;
    $scope.calendarEnabled = true;
    $scope.dateEnabled = false;
    $scope.locationEnabled = true;
  };
  angular.extend($scope, {
        center: {
            lat: 46.34, // initial map center latitude
            lng: 15.456 // initial map center longitude
        },
        markers: [], // an array of markers,
        zoom: 12 // the zoom level
  });

});

myApp.controller('CarouselDemoCtrl', function($scope) {
  $scope.myInterval = 5000;
  $scope.slides = [
    {image: 'http://placekitten.com/200/200',text: 'Kitten.'},
    {image: 'http://placekitten.com/225/200',text: 'Kitty!'},
    {image: 'http://placekitten.com/250/200',text: 'Cat.'},
    {image: 'http://placekitten.com/275/200',text: 'Feline!'}
  ];
});

myApp.controller('MapCtrl', function($scope) {
    var ll = new google.maps.LatLng(13.0810, 80.2740);
    $scope.mapOptions = {
        center: ll,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    //Markers should be added after map is loaded
    $scope.onMapIdle = function() {
        var marker = new google.maps.Marker({
            map: $scope.myMap,
            position: ll
        });
        $scope.myMarkers = [marker];
    };

    $scope.markerClicked = function(m) {
        window.alert("clicked");
    };

});

myApp.controller('EventButtonsCtrl', function($scope) {
        $scope.eventsList = [
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"},
            {title: "Dynamic Group Header - 1"}
        ];
        var visible = [];

        $scope.toggleShow = function(index){
            var position = visible.indexOf(index);
            if(position===-1) {
                visible.push(index);
                return;
            }
            visible.splice(position, 1);
        };

        $scope.shouldShow = function(index){
            return visible.indexOf(index) != -1;
        };


});

function FtfCtrl($scope) {

}

function ContactCtrl($scope) {

}

function EventsListCtrl($scope, Events) {
    $scope.events = Events.query();
}

function EventDetailsCtrl($scope, SingleEvent) {
    $scope.singleEvent = SingleEvent.query();
}