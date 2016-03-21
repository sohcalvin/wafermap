'use strict';
angular.module('wafermapApp')
.controller('WafermapEditorController', ['$scope', '$http',
    function($scope, $http) {
        $scope.mapData;

        $scope.classify = function(){
            console.log($scope.mapData);
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

                },
                function(response){
                    console.log("Error:" + response.data);
                });


        }

    }
]);