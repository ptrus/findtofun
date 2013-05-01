'use strict';

/* Controllers */

function TopCtrl($scope) {}

function EventsListCtrl($scope, FbEvents) {
	$scope.fbevents = FbEvents.query();
}

function EventDetailsCtrl($scope, $routeParams, FbEventDetails) {
	$scope.event = FbEventDetails.query({
		eid: $routeParams.eid
	}, fill_chart);


	function fill_chart(event) {
		$scope.data = [{
			label: 'Females',
			value: event.females,
			color: '#39E639'
		}, {
			label: 'Males',
			value: event.males,
			color: '#FFA640'
		}];
	}
}