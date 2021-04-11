from django.urls import include, path
from rest_framework import routers
from accounts import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('registration', views.RegisterView.as_view(), name='registration'),
    path('auth/', include('djoser.urls.authtoken')),
]