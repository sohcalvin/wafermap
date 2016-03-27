'use strict';
angular.module('wafermapApp')
.controller('WafermapEditorController', ['$scope', '$http',
    function($scope, $http) {
        $scope.mapData;
        $scope.patternName;
        $scope.result;
        $scope.savePattern = function(){
            var req = {
                method: 'POST',
                url: 'http://localhost:5000/wafer_pattern_manager',
                headers: {
                    'Content-Type': undefined
                },
                data: {
                    "mapData": $scope.mapData,
                    "patternName" : $scope.patternName
                }
            };
            $http(req).then(
                function(response){
                    console.log(response);

                },
                function(response){
                    console.log("Error:" + response.data);
                });


        };
        $scope.classify = function(){
            $scope.result = "..."
            $scope.result_detail =[]
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

                    var arrOfObj = new Array();
                    for(var i in proba){
                        arrOfObj.push({"pattern" : i, "proba" : proba[i]})
                    }
                    arrOfObj.sort(function(a,b){return b.proba - a.proba;})
                    $scope.result_detail = arrOfObj;


                },
                function(response){
                    console.log("Error:" + response.data);
                });


        };

    }
]);