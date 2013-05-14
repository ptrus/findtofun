'use strict';

/* Directives */

myApp.directive('ngOnkeyup', function(){
  return {
    restrict: 'A',
    link: function(scope, elem, attr, ctrl) {
      elem.bind('keyup', function(){
        scope.$apply(function(s) {
          s.$eval(attr.ngOnkeyup);
        });
      });
    }
  };
});