var app = angular.module('app', ['ngRoute', 'ngResource'])

app.config(function ($routeProvider,
                     $locationProvider,
                     $resourceProvider,
                     $httpProvider) {
    $locationProvider.hashPrefix('');
    $routeProvider
        .when('/', {
            templateUrl: "/static/html/partials/_categories-list.html",
            controller: "CategoryCtrl"
        })
        .when('/category/:id', {
            templateUrl: "/static/html/partials/_products-list.html",
            controller: "CategoryCtrl"
        })
        .when('/products', {
            templateUrl: "/static/html/partials/_products-list.html",
            controller: "ProductCtrl"
        })
        .when('/product/:id', {
            templateUrl: "/static/html/partials/_product.html",
            controller: "ProductCtrl"
        })
        .otherwise({redirectTo:'/'});


    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.factory('Category', ['$resource', function($resource){
  return $resource('/api/categories/:id/');
}]);

app.factory('Product', ['$resource', function($resource){
  return $resource('/api/products/:id/');
}]);

app.factory('User', ['$resource', function($resource) {
  return $resource('/api/user/');
}]);

app.controller('UserCtrl', ['$scope', 'User', '$http', '$route',
               function($scope, User, $http, $route) {
  $scope.user = User.get();
  $scope.loginInfo = {
    "username": "",
    "password": ""
  }

  $scope.loginFormShown = false;
  $scope.showLoginForm = function() {
    $scope.loginFormShown = !$scope.loginFormShown;
  }

  $scope.hideLoginForm = function() {
    $scope.loginFormShown = false;
  }

  var loginError = function(obj) {
    $scope.errorMessage = obj.message
  }

  $scope.login = function($event) {
    console.log($scope)
    $http.post('/api/login',
              {
                'username': $scope.loginInfo.username,
                'password': $scope.loginInfo.password
              }
    ).then(function(answer) {
      if(answer.data.success) {
        $scope.user = answer.data.user
        $scope.loginInfo.username = "";
        $scope.loginInfo.password = "";
        $scope.hideLoginForm();
        $route.reload();
      } else {
        loginError(answer.data)
      }
    }, loginError)

    $event.preventDefault();
    return false;
  }

  $scope.logout = function() {
    $http.get('/api/logout').then(function() {
      $scope.user = null;
      $route.reload();
    })
  }
}])

app.controller('CategoryCtrl', ['$scope', 'Category', '$routeParams',
                                function($scope, Category, $routeParams) {
  var cat_id = $routeParams.id;
  if(cat_id) {
    var category = Category.get({
      id: cat_id
    })
    category.$promise.then(function() {
      $scope.category_id = category.id;
      $scope.category_name = category.name;
      $scope.products = category.products;
    });
  } else {
    $scope.categories = Category.query();
  }
}])

app.controller('ProductCtrl', ['$scope', 'Product', '$routeParams',
                               function($scope, Product, $routeParams) {
  var prod_id = $routeParams.id;
  if(prod_id) {
    $scope.product = Product.get({
      id: prod_id
    })
  } else {
    $scope.products = Product.query();
  }
}])
