from django.urls import include, path
from rest_framework import routers
from portcoreapi import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'description', views.DescriptionViewSet)
router.register(r'buttons', views.ButtonsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("port_api/", include('portcoreapi.urls'), name='portapi'),
]

