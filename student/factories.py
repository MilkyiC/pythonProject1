import factory

from student import models

class StudentFactory(factory.django.DjangoModelFactory):
    full_name=factory.Faker('full_name')
    date_of_birth=factory.Faker('date_of_birth',min_age=10,max_age=21)
    curator = factory.Faker('curator')

    class Meta:
        model=models.Student

class BookFactory(factory.django.DjangoModelFactory):
    author=factory.Faker('author')
    title=factory.Faker('sentence')
    start_date = factory.Faker('start_date')
    full_name = factory.SubFactory(StudentFactory)

    class Meta:
        model=models.Book

class PassportFactory(factory.django.DjangoModelFactory):
    series_number=factory.Faker('series_number')
    full_name = factory.SubFactory(StudentFactory)

    class Meta:
        model=models.Passport

class CourseFactory(factory.django.DjangoModelFactory):
    hours=factory.Faker('hours')
    title = factory.Faker('title')

    class Meta:
        model=models.Course

class CuratorFactory(factory.django.DjangoModelFactory):
    full_name=factory.Faker('full_name')
    department = factory.Faker('department')

    class Meta:
        model=models.Curator

class EnrollmentFactory(factory.django.DjangoModelFactory):
    student = factory.SubFactory(StudentFactory)
    course = factory.SubFactory(CourseFactory)
    enrollment_date=factory.Faker('date')

    class Meta:
        model=models.Enrollment