'use strict';
angular.module('wafermapApp')
.controller('WafermapController', ['$scope', '$state','$http','$compile',
    function ($scope, $state, $http,$compile) {
        $scope.mapData = [];
        $scope.mapList;

        $scope.getMapList = function(max){
            $http.get("../map").then(function(response){
                    $scope.mapList = response.data;
                    $scope.getMapDataFromMapList();
                }
            );
        }
        $scope.getMapDataFromMapList = function(){
            for(var i in $scope.mapList){
                $scope.getMapData($scope.mapList[i]);
                if(i >16) break;
            }
        }
        $scope.getMapData = function(mapListItem){
                    var mapName = mapListItem.name;
                    var mapUrl = mapListItem.url;
                    $http.get(".." + mapUrl).then(function(response) {
                       $scope.mapData[mapName] = response.data;
                       var patternName = $scope.mapData[mapName].title;
                       $scope.addWaferMap(mapName, patternName);
            });
        };

        $scope.addWaferMap = function(mapName, patternName){
            console.log("Adding " + mapName + " for " + patternName );
            var mapgrid = $("#mapgrid1");
            if(patternName == "Pattern2"){
                mapgrid = $("#mapgrid2");
            }
            if(patternName == "Pattern3"){
                mapgrid = $("#mapgrid3");
            }
            mapgrid.append($compile("<wafermap map-data='mapData."+mapName+"'></wafermap>")($scope));
        };


        $scope.getMapList(5);


    }
]);