from django.urls import path
from rest_framework.authtoken import views as authtoken

from . import views

urlpatterns = [
    path('api/v1/api-token-auth/', authtoken.obtain_auth_token),
    path('api/v1/posts/', views.api_posts),
    path('api/v1/posts/<int:pk>/', views.api_posts_detail),
    path('api/v1/groups/', views.api_groups),
    path('api/v1/groups/<int:pk>/', views.api_groups_detail),
    path('api/v1/posts/<int:pk>/comments/', views.api_posts_detail_comments),
    path(
        'api/v1/posts/<int:post_pk>/comments/<int:comment_pk>/',
        views.api_posts_detail_comments_detail
    ),
]
