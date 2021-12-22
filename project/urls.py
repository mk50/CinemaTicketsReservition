"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('guest',views.viewsets_guest)
router.register('movie',views.viewsets_movie)
router.register('reversation',views.viewsets_reversation)


urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('django/jsonresponsenomodel/',views.no_rest_model),
    path('django/jsonresponsefrommodel/',views.no_rest_from_model),
    # GET POST
    path('rest/fbv/',views.FBV_list),
    # GET PUT DELETE
    path('rest/fbv/<int:pk>',views.FBV_pk),
    #GET POST
    path('rest/cbv/',views.CBV_list.as_view()),
    #GET POST PUT
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    #GET POST
    path('rest/mixin_list/',views.mixin_list.as_view()),
    #GET POST PUT
    path('rest/mixin_list/<int:pk>',views.mixin_pk.as_view()),
    #GET POST
    path('rest/generic_list/',views.generic_list.as_view()),
    #GET POST PUT
    path('rest/generic_list/<int:pk>',views.generic_pk.as_view()),
    path('rest/viewset/',include(router.urls)),
    #find movie make search
    path('fbv/findmovie',views.find_movie),
    path('fbv/newreversation',views.new_reversation),
    path('api_auth',include('rest_framework.urls')),
    #Token authentication
    path('api_auth_token',obtain_auth_token),
    path('post/generics/<int:pk>',views.Post_pk.as_view())
]
