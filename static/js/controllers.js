'use strict';

/* Controllers */

function TopCtrl($scope, $rootScope, $location) {
	$scope.searchEvents = function() {
		if ($location.$$path !== '') {
				location = '#';
		}

		setTimeout(function() {
			var eventNameFilters = $('.eventName');
			if (eventNameFilters.length == 0) {
				$('.addFilter').click();
			}
			
			eventNameFilters.val($scope.keywords).trigger("input");
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

	var clone = function(o) {
		return jQuery.extend(true, {}, o);
	};

	// var Slider = (function() {
	// 	var id = 0;
	// 	var prefix = "slider";

	// 	var transform = function(o) {
	// 		o = setId(o);

	// 		var sliderId = prefix + o.id;
	// 		$('#' + prefix + 'Init')[0].setAttribute('id', sliderId);
	// 		$('#' + sliderId).slider().on('slideStop', onChange).data("slider");
	// 	};

	// 	var onChange = function(ev) {
	// 		$scope.fillFilters();
	// 		dirtyChecking();
	// 	};

	// 	var setId = function(o) {
	// 		id += 1;
	// 		o['id'] = id;
	// 		return o;
	// 	};

	// 	return {
	// 		transform: transform
	// 	};
	// })();
	// $scope.Slider = Slider;

	var F = (function(F) {
		F.textfield = {
			text: 'value',
			type: 'textfield'
		};

		F.numericfield = {
			text: 'value',
			type: 'numericfield'
		};

		F.eventName = clone(F.textfield);
		F.eventName['class'] = 'eventName';

		// F.deviance = {
		// 	text: 'deviance',
		// 	type: 'slider'
		// };

		// F.percentage = {
		// 	text: 'percentage',
		// 	type: 'slider'
		// };

		F.percentage = {
			text: 'value',
			type: 'percentage'
		};

		F.type = {
			text: 'by',
			type: 'selectfield',
			values: [
				{name: 'number', next: [last(F.numericfield)]}
			]
		};

		F.type2 = clone(F.type);
		F.type2['values'].push({
			name: 'percentage',
			next: [last(F.percentage)]
		});

		F.gender = {
			text: 'gender',
			type: 'selectfield',
			values: [
				{name: 'both',		next: [F.type]},
				{name: 'males',		next: [F.type2]},
				{name: 'females',	next: [F.type2]}
			]
		};

		F.fields = {
			text: 'field',
			type: 'selectfield',
			values: [
				{name: 'name',			next: [last(F.eventName)]},
				{name: 'all_members',	next: [F.gender]},
				{name: 'attending',		next: [F.gender]},
				{name: 'unsure',		next: [F.gender]},
				{name: 'declined',		next: [F.gender]},
				{name: 'not_replied',	next: [F.gender]}
			]
		};

		var fields_idx = 0;
		F.get = function() {
			var fields = clone(F.fields);
			fields["idx"] = fields_idx;
			fields_idx += 1;
			return fields;
		};

		return F;
	})({});

	$scope.removeFilter = function(index) {
		$scope.filters.splice(index, 1);
		filledFilters.splice(index, 1);
	};

	$scope.addFilter = function() {
		$scope.filters.push(F.get());
	}

	$scope.filters = [];
	var filledFilters = [];

	$scope.fillFilters = function() {
		var input = this.value;
		var params = [];
		var filterIdx;

		var me = this.$parent;
		while(me.$parent) {
			if (me.c_values) {
				params.splice(0, 0, {value: me.c_values.name});
			}
			else if (me.choice && !me.choice.last) {
				params[0]["key"] = me.choice.text;
			}

			me = me.$parent;
			if (me.$parent.$parent === me.$root) {
				filterIdx = me.choice.idx;
				break;
			}
		}

		filledFilters[filterIdx] = {
			input: input,
			params: params
		};
	};

	$scope.processFilters = function(item) {
		for (var i=0; i<filledFilters.length; i++) {
			var F = filledFilters[i];
			if (!F) { continue; }
			for (var j=0, bundle; j<F.params.length; j++) {
				var param = F.params[j];
				var key = param['key'];
				var value = param['value'];

				if (key === "field") {
					if (value === 'name') {
						if (item.name.toUpperCase().indexOf(
								F.input.toUpperCase()) === -1) {
							return false;
						}
					}
					else  if (['all_members', 'attending', 'unsure',
							'declined', 'not_replied'].indexOf(value) >= 0) {

						bundle = {
							'both': item[value],
							'males': item.males[value],
							'females': item.females[value]
						};
					}
				}
				else if (key === 'gender' && bundle &&
						bundle.hasOwnProperty('both') &&
						bundle.hasOwnProperty('males') &&
						bundle.hasOwnProperty('females') &&
						(value === 'both' ||
						value === 'males' ||
						value === 'females')) {

					bundle["active"] = value;
				}
				else if (key === 'by' && bundle['active'] &&
						typeof F.input === 'number') {

					if (value === 'number') {
						// deviance hardcoded 25%

						var tmp = bundle[bundle["active"]];
						if (F.input > tmp * 1.25 ||
								F.input < tmp * 0.75) {
							return false;
						}
					}
					else if (value === 'percentage' &&
							bundle["active"] !== 'both') {
						// deviance hardcoded 25%

						var percentage = (bundle[bundle['active']] /
							bundle['both']) * 100;
						if (F.input > percentage * 1.25 ||
								F.input < percentage * 0.75) {
							return false;
						}
					}
				}
			}
		}

		return true;
    };
}

function EventDetailsCtrl($scope, $routeParams, FbEventDetails) {
	$scope.event = FbEventDetails.query({
		eid: $routeParams.eid
	}, fill_charts);


	function fill_charts(event) {
		$scope.data1 = [{
			label: 'Males',
			value: event.males.attending,
			color: '#39E639'
		}, {
			label: 'Females',
			value: event.females.attending,
			color: '#FFA640'
		}];

		$scope.data2 = [{
			label: 'Males',
			value: event.males.all_members,
			color: '#39E639'
		}, {
			label: 'Females',
			value: event.females.all_members,
			color: '#FFA640'
		}];

		$scope.data3 = [{
			label: 'Males',
			value: event.males.unsure,
			color: '#39E639'
		}, {
			label: 'Females',
			value: event.females.unsure,
			color: '#FFA640'
		}];

		$scope.data4 = [{
			label: 'Males',
			value: event.males.not_replied,
			color: '#39E639'
		}, {
			label: 'Females',
			value: event.females.not_replied,
			color: '#FFA640'
		}];
	}
}