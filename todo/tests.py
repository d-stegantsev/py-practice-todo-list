from django.test import TestCase
from django.urls import reverse
from todo.models import Task, Tag


class TaskTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="test")
        self.task = Task.objects.create(
            content="Test task", is_done=False
        )
        self.task.tags.add(self.tag)

    def test_task_list_view(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test task")

    def test_task_create(self):
        response = self.client.post(reverse("todo:task-create"), {
            "content": "New task",
            "deadline": "",
            "tags": [self.tag.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)

    def test_task_update(self):
        response = self.client.post(reverse(
            "todo:task-update",
            args=[self.task.pk]
        ), {
            "content": "Updated task",
            "deadline": "",
            "tags": [self.tag.id]
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated task")

    def test_task_delete(self):
        response = self.client.post(
            reverse("todo:task-delete", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_task_toggle_status(self):
        self.assertFalse(self.task.is_done)
        response = self.client.get(
            reverse("todo:task-toggle", args=[self.task.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
