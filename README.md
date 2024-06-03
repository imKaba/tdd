# TDD

We are just having fun around here.. join us

## 1. To run your tests.

> make sure you are on your project root folder

```bash
python manage.py test

```

## 2. How to write tests using [django](https://docs.djangoproject.com/en/5.0/topics/testing/overview/).

```python
# file: task/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    # # uncomment below after running test_model_has_string_representation

    # def __str__(self):
    #     return self.title



class Project(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    status = models.CharField(max_length=200, choices=[('ongoing', 'ON GOING'), ('paused', 'PAUSED'), ('over', 'OVER')], default='ongoing')

    def check_status(self):
        return self.status    

```



- Accounts
[K.a.b.a](https://github.com/ikeecode) and [imKaba](https://github.com/imKaba)

