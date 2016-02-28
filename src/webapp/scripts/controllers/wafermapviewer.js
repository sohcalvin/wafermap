'use strict';
angular.module('wafermapApp')
.controller('WafermapController', ['$scope', '$state','$http',
    function ($scope, $state, $http) {
        $scope.mapData = {};
        $scope.getMapData = function(id){
                    $http.get("../map/1").then(function(data) {
                    $scope.mapData["wafer1"] = data.data;
            });
        };
        $scope.getMapData(1);
    }
]);