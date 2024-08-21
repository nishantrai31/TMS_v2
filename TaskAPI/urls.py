


# # Create a nested router for tasks related to users

# # Add the nested routes to the main router



from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TaskAPI.views import CommentViewSet, ProjectViewSet, TaskAssignmentViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'task_assignments', TaskAssignmentViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
