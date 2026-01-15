from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.subject})"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(
        Teacher,
        related_name='students',
        verbose_name="Учителя"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
