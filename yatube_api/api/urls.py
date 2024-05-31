from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from .constants import API_VERSION

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet),
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{API_VERSION}/', include('djoser.urls')),
    path(f'{API_VERSION}/', include('djoser.urls.jwt')),
    path(f'{API_VERSION}/', include(router_v1.urls)),
]
