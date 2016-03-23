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
                    var classifiedPattern = response.data.pattern;
                    var proba = response.data.class_to_proba;
                    $scope.result = classifiedPattern + " - Prob("+proba[classifiedPattern] +")";
                    $scope.result_detail = "";
                    for(var i in proba){
                        $scope.result_detail += i + " : " + proba[i] + "\n";
                    }
                    console.log($scope.result_detail);


                },
                function(response){
                    console.log("Error:" + response.data);
                });


        };

    }
]);