# from audioop import reverse
from django.urls import reverse

from django.test import TestCase
from student import factories, models

class StudentTestCase(TestCase):
    def setUp(self):
        self.student=factories.StudentFactory

    def test_get_student_list(self):
        url=reverse('student_list')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['students'].count(),models.Student.objects.count())
        print(response.context['students'].count(), models.Student.objects.count())

    def test_get_student_detail(self):
        url=reverse('student_detail', kwargs={'pk':self.student.pk})
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_get_student_update(self):
        url=reverse('student_update', kwargs={'pk':self.student.pk})
        old_full_name=self.student.full_name
        old_date_of_birth=self.student.date_of_birth
        response=self.client.post(url,{'full_name':'new_full_name','date_of_birth':'new_date_of_birth'})
        self.student.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertNotEquals(self.student.full_name,old_full_name)

    def test_get_student_delete(self):
        url=reverse('student_delete', kwargs={'pk':self.student.pk})
        old_student_count=models.Student.objects.count()
        response=self.client.delete(url)
        self.assertEqual(response.status_code,302)
        self.assertGreater(old_student_count,models.objects.count())

    def test_get_student_create(self):
        url=reverse('student_create')
        old_student_count=models.Student.objects.count()
        data = {
            'full_name': 'Студент',
            'date_of_birth': 2011-11-28,
            'curator_id': 4,
        }
        response=self.client.post(url)
        self.assertEqual(response.status_code,200)
        self.assertGreater(models.objects.count(),old_student_count+1)

