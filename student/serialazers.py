from rest_framework import serializers
from student import models
# from student.models import Curator

class Curator(serializers.ModelSerializer):
    class Meta:
        model = models.Curator
        fields = '__all__'

class Student(serializers.ModelSerializer):
    curator = Curator(read_only=True)
    curator_id = serializers.IntegerField(required=False, allow_null=True)
    class Meta:
        model=models.Student
        fields = '__all__'

class Book(serializers.ModelSerializer):
    full_name=Student(read_only=True)
    full_name_id=serializers.IntegerField(required=False,allow_null=True)
    class Meta:
        model=models.Book
        fields = '__all__'

class Passport(serializers.ModelSerializer):
    full_name = Student(read_only=True)
    full_name_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Passport
        fields = '__all__'

class Enrollment(serializers.ModelSerializer):

    class Meta:
        model = models.Enrollment
        fields = '__all__'

class Course(serializers.ModelSerializer):
    full_name = Student(read_only=True)
    full_name_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Course
        fields = '__all__'

