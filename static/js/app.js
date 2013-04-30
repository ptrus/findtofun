'use strict';

/* Application */

if (window.location.hash == '#_=_') {
	window.location.hash = '';
}

var myApp = angular.module('ftf', ['ftfServices','ui.bootstrap', 'google-maps', 'ui']);

myApp.config(['$routeProvider', function($routeProvider) {
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
		.when('/contact', {
		templateUrl: '/s/partials/contact.html',
		controller: ContactCtrl
	})
		.when('/done', {
		templateUrl: '/s/partials/done.html',
		controller: FtfCtrl
	})
		.when('/error', {
		templateUrl: '/s/partials/error.html',
		controller: FtfCtrl
	})
		.when('/logout', {
		templateUrl: '/s/partials/logout.html',
		controller: FtfCtrl
	})
		.otherwise({
		redirectTo: '/'
	});
}]);