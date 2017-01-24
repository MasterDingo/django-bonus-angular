from django.conf.urls import url

from .views import (
    CategoriesList, CategoryDetail, ProductsList, ProductDetail,
    UserView, login, logout
)

urlpatterns = [
    url(r'login$', login),
    url(r'logout$', logout),
    url(r'categories/$', CategoriesList.as_view()),
    url(r'categories/(?P<pk>\d+)/$', CategoryDetail.as_view()),
    url(r'products/$', ProductsList.as_view()),
    url(r'products/(?P<pk>\d+)/$', ProductDetail.as_view()),
    url(r'user/$', UserView.as_view()),
]
