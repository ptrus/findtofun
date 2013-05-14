'use strict';

/* Controllers */

function TopCtrl($scope, $rootScope, $location) {
	$scope.searchEvents = function() {
		if ($location.$$path !== '') {
				$location.path('#');
		}
		
		setTimeout(function() {
			$('#f-name').val($scope.keywords).trigger("input");
		}, 10);
	};
}

function EventsListCtrl($scope, $routeParams, FbEvents) {
	$scope.fbevents = FbEvents.query(function() {
		makeSortableTable();
	});

	var makeSortableTable = function () {
		sorttable.makeSortable($("#event-list")[0]);
	};

   var dirtyChecking = function() {
		$scope.$digest();
    };

	var last = function(o) {
		o["last"] = true;
		return o;
	};

	$scope.clone = function(o) {
		return jQuery.extend(true, {}, o);
	}

	var Slider = (function() {
		var i = 0;
		var prefix = "slider"

		var transform = function(o) {
			$('.slider').slider();
			var sl = $('#' + prefix + o.id).slider()
			.on('slideStop', function(ev){
				console.log(sl.getValue());
			})
	  		.data("slider");
		};

		var setId = function(o) {
			o["id"] = prefix + i;
			console.log(i);
			i += 1;
			return o;
		}

		var initHelper = function(o) {
			return setId($scope.clone(o));
		}

		return {
			transform: transform,
			setId: setId,
			init: initHelper
		}
	})();
	$scope.Slider = Slider;

	$scope.textfield = {
		text: 'value',
		type: 'textfield'
	};

	$scope.numericfield = {
		text: 'value',
		type: 'numericfield'
	};

	$scope.deviance = {
		text: 'deviance',
		type: 'slider'
	};

	$scope.percentage = {
		text: 'percentage',
		type: 'slider'
	};

	$scope.type = {
		text: 'by',
		type: 'selectfield',
		values: [
			{
				name: 'number',
				next: [
					last($scope.numericfield),
					last(Slider.init($scope.deviance)),
				]
			},
			{
				name: 'percentage',
				next: [
					last($scope.percentage),
					last($scope.deviance)
				]
			}
		]
	};

	$scope.gender = {
		text: 'gender',
		type: 'selectfield',
		values: [
			{name: 'both',		next: [$scope.type]},
			{name: 'male',		next: [$scope.type]},
			{name: 'female',	next: [$scope.type]}
		]
	};

	$scope.fields = {
		text: 'field',
		type: 'selectfield',
		values: [
			{name: 'tomi',			next: [last($scope.deviance)]},
		    {name: 'name', 			next: [last($scope.textfield)]},
		    {name: 'all_members',	next: [$scope.gender]},
		    {name: 'attending',		next: [$scope.gender]},
		    {name: 'unsure', 		next: [$scope.gender]},
		    {name: 'declined', 		next: [$scope.gender]},
		    {name: 'not_replied', 	next: [$scope.gender]}
	   	]
  	};

	$scope.filters = [];

	$scope.debug = function() {
		debugger;
	};

	$scope.fireBigFilter = function() {
		console.log(this.value);
	};

	// Set up slider for deviance and gender
	$('.slider').slider();
	var sl_deviance = $('#sl-deviance').slider()
        .on('slideStop', dirtyChecking).data('slider');

	$scope.bigFilter = function(item) {
    	return (item.name.indexOf($scope.f_name) !== -1) || !$scope.f_name;
		var l1 = [
			$scope.f_all_members,
			$scope.f_attending,
			$scope.f_unsure,
			$scope.f_declined,
			$scope.f_not_replied];

		var o;
		if (gender_deviance === 'Both') {
			o = item;
		}
		else if (gender_deviance == 'Males') {
			o = item.males;
		}
		else if (gender_deviance == 'Females') {
			o = item.females;
		}

		var l2 = [
			o.all_members,
			o.attending,
			o.unsure,
			o.declined,
			o.not_replied];

		for (var i=0; i<l1.length; i++) {
			if (l1[i] && 
				(
					l1[i] + l1[i] * sl_deviance.getValue() / 100 < l2[i] ||
					l1[i] - l1[i] * sl_deviance.getValue() / 100 > l2[i]
				)) {
				return false;
			}
		}
		return true;
    };

    function compare_integers_prefix(v1, v2) {
    	v1 = v1.toString();
    	v2 = v2.toString();

    	return v1 === v2.substring(0, v1.length);
    }
}

function EventDetailsCtrl($scope, $routeParams, FbEventDetails) {
	$scope.event = FbEventDetails.query({
		eid: $routeParams.eid
	}, fill_charts);


	function fill_charts(event) {
		$scope.data1 = [{
			label: 'Females',
			value: event.males.attending,
			color: '#39E639'
		}, {
			label: 'Males',
			value: event.females.attending,
			color: '#FFA640'
		}];

		$scope.data2 = [{
			label: 'Females',
			value: event.males.all,
			color: '#39E639'
		}, {
			label: 'Males',
			value: event.females.all,
			color: '#FFA640'
		}];

		$scope.data3 = [{
			label: 'Females',
			value: event.males.unsure,
			color: '#39E639'
		}, {
			label: 'Males',
			value: event.females.unsure,
			color: '#FFA640'
		}];

		$scope.data4 = [{
			label: 'Females',
			value: event.males.not_replied,
			color: '#39E639'
		}, {
			label: 'Males',
			value: event.females.not_replied,
			color: '#FFA640'
		}];
	}
}