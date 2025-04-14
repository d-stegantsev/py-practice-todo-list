from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_status,
    TagUpdateView,
    TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/toggle/", toggle_task_status, name="task-toggle"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
app_name = "todo"
