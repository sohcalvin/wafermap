'use strict';
angular.module('wafermapApp')
.controller('WafermapEditorController', ['$scope', '$http',
    function($scope, $http) {
        $scope.mapData;
        $scope.result;

        $scope.classify = function(){
            console.log($scope.mapData);
            $scope.result = "..."
            var req = {
                method: 'POST',
                url: 'http://localhost:5000/wafer_predictor',
                headers: {
                    'Content-Type': undefined
                },
                data: { "mapData": $scope.mapData }
            };
            $http(req).then(
                function(response){
                    console.log(response.data);
                    $scope.result = response.data;

                },
                function(response){
                    console.log("Error:" + response.data);
                });


        };

    }
]);