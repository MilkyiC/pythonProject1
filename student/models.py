from django.db import models

class Student(models.Model):
    full_name=models.CharField(verbose_name="ФИО",max_length=255)
    date_of_birth=models.DateField(verbose_name="Дата рождения")
    curator=models.ForeignKey(
        'Curator',
        verbose_name="ФИО",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    class Mets:
        verbose_name="Студент",
        verbose_name_plural="Студенты"
        ordering=['full_name']

    def __str__(self):
        return self.full_name

class Book(models.Model):
    author=models.CharField(verbose_name="ФИО",max_length=255)
    title = models.CharField(verbose_name="Название", max_length=255)
    start_date=models.DateField(verbose_name="Дата начала",null=True)
    end_date=models.DateField(verbose_name="Дата конца", auto_now=True)
    full_name=models.ForeignKey(
        Student,
        verbose_name="ФИО",
        max_length=255,
        on_delete=models.CASCADE
    )
    class Mets:
        verbose_name="Книга",
        verbose_name_plural="Книги"
        ordering=['title']

    def __str__(self):
        return self.title

    def tm(self):
        return self.end_date-self.start_date

class Passport(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=255)
    series_number=models.CharField(verbose_name="Серия и номер",max_length=10,unique=True)
    full_name=models.OneToOneField(
        Student,
        verbose_name="ФИО",
        max_length=255,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    class Mets:
        verbose_name="Паспортные данные",
        verbose_name_plural="Паспортные данные"
        ordering=['full_name']
    def __str__(self):
        return f"{self.full_name} - {self.series_number}"

class Course(models.Model):

    class Study_cources(models.TextChoices):
        chemistry = "Хим",("Химия")
        russian = "Рус", ("Русский язык")
        math = "Мат", ("Математика")

    hours=models.IntegerField(verbose_name="Количество часов", default=144)
    title = models.CharField(verbose_name="Название", max_length=3, choices=Study_cources.choices, default=Study_cources.math)
    class Mets:
        verbose_name="Курс",
        verbose_name_plural="Курсы"
        ordering=['title']

    def __str__(self):
        return f"{self.title} - {self.hours}"

class Curator(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=255)
    department = models.CharField(verbose_name="Кафедра", max_length=255)
    class Mets:
        verbose_name="Куратор",
        verbose_name_plural="Кураторы"
        ordering=['full_name']
    def __str__(self):
        return f"{self.full_name} - {self.department}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

