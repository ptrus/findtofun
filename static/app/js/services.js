'use strict';

/* Services */

angular.module('ftfServices', ['ngResource'])
    .factory('Events', function($resource) {
    return $resource('/api/v1/event', {}, {
        query: {
            method: 'GET',
            isArray: false
        }
    });
})
    .factory('SingleEvent', function($resource) {
    return $resource('/api/v1/event/12', {}, {
        query: {
            method: 'GET',
            isArray: false
        }
    });
});