from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns) 
