from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import ListPost, DetailedPost, UserList, UserDetail
from .views import PostViewSet, UserViewSet

# urlpatterns = [
#     path('<int:pk>/', DetailedPost.as_view()),
#     path('', ListPost.as_view()),
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view())
   
# ]

router = SimpleRouter()
router.register('users', UserViewSet, basename = 'users')
router.register('', PostViewSet, basename = 'posts')

urlpatterns = router.urls