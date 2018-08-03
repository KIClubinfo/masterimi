from django.urls import path, include
from rest_framework.routers import SimpleRouter

from parcours_imi import views

router = SimpleRouter(trailing_slash=False)
router.register(r'courses', views.CourseViewSet)
router.register(r'masters', views.MasterViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]