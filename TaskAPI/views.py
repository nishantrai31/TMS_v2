"""Views for tasks"""

from datetime import datetime
from rest_framework import viewsets,authentication,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from TaskAPI.factory_pattern import factory_type, Task_Factory
from .models import STATUS_CHOICES, Task, Project, TaskAssignment, Comment
from .serializers import TaskSerializer, ProjectSerializer, TaskAssignmentSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'priority']
    ordering_fields = ['due_date']
    serializer_class = TaskSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = Task_Factory.create(factory_type.Task,serializer.validated_data)
        task.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], serializer_class=None)
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status != STATUS_CHOICES.IN_PROGRESS:
            return Response({'error': 'Task must be in progress to complete.'}, status=status.HTTP_400_BAD_REQUEST)
        task.status = STATUS_CHOICES.COMPLETED
        task.save()
        return Response({'message': 'Task marked as completed.'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        overdue_tasks = Task.objects.filter(due_date__lt=datetime.date.today())
        for task in overdue_tasks:
            for user in task.assigned_users.all():

                send_mail(
                    subject='Overdue Task: ' + task.title,
                    message='You have an overdue task: ' + str(task),
                    from_email='your_email@example.com',
                    recipient_list=[user.email],
                )
        serializer = TaskSerializer(overdue_tasks, many=True)
        return Response(serializer.data)



class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def create(self, request, *args, **kwargs):
        '''
        Create a new project using the provided data in the request.
        Parameters:
        - request: Request data containing project details.
        Returns:
        - Response with the serialized project data and a status of 'CREATED'.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project = Task_Factory.create(factory_type.Project,serializer.validated_data)
        project.save()
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        project = self.get_object()
        completed_tasks = project.tasks.filter(status=STATUS_CHOICES.COMPLETED).count()
        total_tasks = project.tasks.count()
        progress = (completed_tasks / total_tasks) * 100

        # Consider weighting tasks based on priority
        weighted_progress = 0
        for task in project.tasks.all():
            if task.status == STATUS_CHOICES.COMPLETED:
                weighted_progress += task.priority_weight  # Assuming a priority_weight attribute
        total_priority_weights = sum(task.priority_weight for task in project.tasks.all())
        weighted_progress = (weighted_progress / total_priority_weights) * 100

        return Response({'progress': progress, 'weighted_progress': weighted_progress})

class TaskAssignmentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        assignment = Task_Factory.create(factory_type.TaskAssignment,serializer.validated_data)
        assignment.save()
        return Response(TaskAssignmentSerializer(assignment).data, status=status.HTTP_201_CREATED)

class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = Task_Factory.create(factory_type.Comment,serializer.validated_data)
        comment.save()
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)




    