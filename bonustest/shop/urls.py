from django.conf.urls import url

from .views import (
     CategoryListView, CategoryView, ProductsListView, ProductView,
     IndexView
)
from .api import urls as api_urls
from rest_framework.urlpatterns import format_suffix_patterns

"""
urlpatterns = [
    url(r'login', login_view, {"template_name": "login.html"}, name="login"),
    url(r'logout', logout_view, {"next_page": "/"}, name="logout"),
    url(r'^$', CategoryListView.as_view(), name="categories_list"),
    url(r'category/(?P<cat_id>\d+)', CategoryView.as_view(), name="category"),
    url(r'products/$', ProductsListView.as_view(),
        name="products_list"),
    url(r'products/(?P<pk>\d+)/$', ProductView.as_view(), name="product"),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
"""

urlpatterns = [
    url(r'', IndexView.as_view(), name="index"),
]
