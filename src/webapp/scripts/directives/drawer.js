var svgApp = angular.module('wafermapApp');


svgApp.directive("drawer", function($parse,$window) {
  return{
    restrict: "A",
    transclude: true,
    template:
    `
       <div  class="drawer" ng-class="{'close':isClose, 'open':!isClose}" >
            <div  ng-click="isClose = !isClose" style="height:100%;width:20px;background-color:orange;float:left"></div>
            <div ng-transclude style="display:{{(isClose)? 'none':'inline';}}"/>
        </div>

        <style>
            .drawer {
                -webkit-transition: height 100ms linear;
                -moz-transition: height 100ms linear;
                -o-transition: height 100ms linear;
                -ms-transition: height 100ms linear;
                transition: width 0.5S linear,opacity 0.5S linear;

                background-color: gray;
                opacity : 0.99;
                position:absolute;
                height: 250px;
                width : 100%;
                left:0px;
                top : 50px;
                border : solid 1px black;

            }
            .close {
                width:20px;
                opacity:0.3;
                border:none;
            }
            .open {
                width:100%;
            }
    </style>


    `
  };
});