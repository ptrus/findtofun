'use strict';

/* Controllers */

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