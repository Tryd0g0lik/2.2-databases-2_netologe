from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', null=True)

    group = models.IntegerField(max_length=2, verbose_name='Класс')
    teachers = models.ManyToManyField(Teacher, through='School',
                                      related_name='groups')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
class School(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schools')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='schools')
    lesson = models.CharField(max_length=20, null=True, verbose_name='Лекция')
