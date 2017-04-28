
/* global angular */


	// Your JavaScript Code here
var app = angular.module("myApp", []);

// Manage app data
app.controller('myCtrl', ['$scope','thumbnails', function($scope, thumbnails) {
    // Use thumbnails service to fetch data asynchronously from API
    thumbnails.then(function(data) {
        
        // Store thumbnail data for use in view
        $scope.thumbnailsObj = data;
    });
 
}]);