from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from judge.views import ProblemViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
# router.register(r'problems', ProblemViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('', problem_list, name='problem_list'),
# ]

urlpatterns = [
    path('', views.problem_list, name='problem_list'),
    path('create/', views.problem_create, name='problem_create'),
    path('update/<int:pk>/', views.problem_update, name='problem_update'),
    path('delete/<int:pk>/', views.problem_delete, name='problem_delete'),
]

