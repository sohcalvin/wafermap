'use strict';
angular.module('wafermapApp')
.controller('WafermapEditorController', ['$scope',
    function($scope) {
        $scope.mapData;

        $scope.classify = function(){
            console.log($scope.mapData);
        }

    }
]);