'use strict';

/* Services */

angular.module('ftfServices', ['ngResource'])
    .factory('FbEvents', function($resource) {
        return $resource('/api/v1/fbevents/', {}, {
            query: {
                method: 'GET',
                isArray: false
            }
        })
    })
    .factory('FbEventDetails', function($resource) {
        return $resource('/api/v1/fbevents/:eid', {eid: '@eid'}, {
            query: {
                method: 'GET',
                isArray: false
            }
        });
    });
