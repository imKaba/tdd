from django.test import TestCase
# 0536236296 : Delight Momo account

from .models import Task, Project

# Create your tests here.


class TaskModelTest(TestCase):
    def test_task_model_exists(self):
        task = Task.objects.count()

        self.assertEqual(task, 0)


    def test_model_has_string_representation(self):
        task = Task.objects.create(title="Give the book to ben")
    
        self.assertEqual(str(task), task.title)

    
    def test_get_home_page(self):
        response = self.client.get("/", {"title" : "I dont know what i am doing "})
        self.assertTrue(response.status_code == 200)





class ProjectModelTest(TestCase):
    def setUp(self):
        Project.objects.create(name='Save ben')
        Project.objects.create(name='Build Dooria', status='paused')


    def test_project_status(self):
        save_ben = Project.objects.get(name='Save ben')
        dooria = Project.objects.get(name='Build Dooria')

        self.assertEqual(save_ben.check_status(), 'ongoing')
        self.assertEqual(dooria.check_status(), 'over', 'custom message')
        
