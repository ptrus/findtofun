'use strict';

/* Application */

/* Maybe to add: ui.keypress */
var myApp = angular.module('ftf', ['ftfServices', 'AwesomeChartJS']);

myApp.config(['$routeProvider', function($routeProvider) {
	$routeProvider.when('', {
		templateUrl: '/s/partials/events_list.html',
		controller: EventsListCtrl
	})
		.when('/event/:eid', {
		templateUrl: '/s/partials/event_details.html',
		controller: EventDetailsCtrl
	})
		.when('/contact', {
		templateUrl: '/s/partials/contact.html',
	})
		.otherwise({
		redirectTo: ''
	});
}]);