
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import publist, create_auth
from .views import shelist
#from .views import usrlist
from .views import UsersViewSet
from api_basics import views

router = routers.DefaultRouter()
router.register(r'userss', views.UsersViewSet,  basename="users")
router.register(r'publication', views.PublicationsViewSet,  basename="publication")
# router.register(r'shelves', shelist())
# router.register(r'publications', publist())

urlpatterns = [
    path('publications/', publist),
    path('shelves/', shelist),
    path('auth/', create_auth),
 #   path('users/', usrlist),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]