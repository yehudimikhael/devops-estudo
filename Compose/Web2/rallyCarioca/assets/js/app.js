var codeapp = angular.module('codeapp', ['nya.bootstrap.select']);

codeapp.run(function($http){
    $http.defaults.headers.common.Authorization = 'Basic YmVlcDpib29w'
  });


codeapp.controller('homeController', function($scope, $http){

  $scope.popup = 0;
  $scope.email = null;
  $scope.pass = null;

  //Poppup
  $scope.change= function(){
    if($scope.popup == 0){
      $scope.popup = 1;
      console.log($scope.popup)
    }
    else{
      $scope.popup = 0;
      console.log($scope.popup)
    }

  }
  $http({
    method: 'GET',
    url:'http://docker-back:5000/competidor'
  }).then(function(response){
    $scope.competidor = response.data
  })
 
 

});