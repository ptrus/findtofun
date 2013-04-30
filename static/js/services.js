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
    return $resource('/api/v1/singevent', {}, {
        query: {
            method: 'GET',
            isArray: false
        }
    });
});