from django.db import models

# Create your models here.


class StidentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    is_deleted = models.BooleanField(default=False)
    student_birthday = models.DateField(null=True, blank=True)
    student_info = models.TextField()

    # change the model manager
    objects = StidentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name
