from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
from .constants import API_VERSION

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet)
router_v1.register(r'groups', GroupViewSet),
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comment')
router_v1.register(r'follow', FollowViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_VERSION}/', include(router_v1.urls)),
]
