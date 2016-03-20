'use strict';

 angular.module('wafermapApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ui.router'
]).config(['$routeProvider', '$stateProvider', '$urlRouterProvider',
    function ($routeProvider, $stateProvider, $urlRouterProvider) {
        $stateProvider.state('home', {
            url: '/',
            templateUrl: 'views/main.html',
            controller: 'MainCtrl'
        })
        .state('wafermapviewer', {
            url: '/wafermapviewer',
            templateUrl: 'views/wafermapviewer.html',
            controller: 'WafermapController'
        })
        .state('wafermapeditor', {
            url: '/wafermapeditor',
            templateUrl: 'views/wafermapeditor.html',
            controller: 'WafermapEditorController'
        })
        ;

        $urlRouterProvider.otherwise("/");
    }
])
;