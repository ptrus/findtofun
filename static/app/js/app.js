'use strict';

/* Application */

angular.module('ftf', ['ftfServices']).
config(['$routeProvider', function($routeProvider) {
	$routeProvider.when('/', {
		templateUrl: '/s/partials/index.html',
		controller: FtfCtrl
	})
		.when('/events', {
		templateUrl: '/s/partials/events_list.html',
		controller: EventsListCtrl
	})
		.when('/details', {
		templateUrl: '/s/partials/event_details.html',
		controller: EventDetailsCtrl
	})
		.otherwise({
		redirectTo: '/'
	});
}]);
