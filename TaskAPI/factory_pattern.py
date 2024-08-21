from .models import PRIORITY_CHOICES, STATUS_CHOICES, Task, Project, TaskAssignment, Comment
import attr
class TaskFactory:
    @classmethod
    def create_task(cls, title, description=None, status=STATUS_CHOICES.TO_DO, priority=PRIORITY_CHOICES.LOW, due_date=None):
        """
        Creates a new Task instance using the provided parameters.

        :param title: The title of the task.
        :param description: The description of the task (default is None).
        :param status: The status of the task (default is STATUS_CHOICES.TO_DO).
        :param priority: The priority of the task (default is PRIORITY_CHOICES.LOW).
        :param due_date: The due date of the task (default is None).
        :return: A new Task instance.
        """
        return Task(title=title, description=description, status=status, priority=priority, due_date=due_date)



class ProjectFactory:
    @classmethod
    def create_project(cls, name, description=None, start_date=None, end_date=None):
        return Project(name=name, description=description, start_date=start_date, end_date=end_date)


class TaskAssignmentFactory:
    @classmethod
    def create_task_assignment(cls, task, user):
        return TaskAssignment(task=task, user=user)



class CommentFactory:
    @classmethod
    def create_comment(cls, task, user, text):
        return Comment(task=task, user=user, text=text)



@attr.s(frozen=True)
class FactoryType:
    Task = attr.ib(default="Task")
    Comment = attr.ib(default="Comment")
    Project = attr.ib(default="Project")
    TaskAssignment = attr.ib(default="TaskAssignment")
factory_type = FactoryType()
class Task_Factory:
    @staticmethod
    def create(type, data):
        obj = None
        if type == factory_type.Task:
            obj = TaskFactory().create_task(**data)
        elif type == factory_type.Comment:
            obj = CommentFactory().create_comment(**data)
        elif type == factory_type.Project:
            obj = ProjectFactory().create_project(**data)
        elif type == factory_type.TaskAssignment:
            obj = TaskAssignmentFactory().create_task_assignment(**data)
        return obj