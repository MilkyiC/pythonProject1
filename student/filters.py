import django_filters
from django.template.defaultfilters import title

import student.models
from django.db.models import Q

class Student (django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name='date_of_birth',label='Дата рождения')
    # curator = django_filters.CharFilter(field_name='curator__department',lookup_expr='icontains',label='')
    available=django_filters.BooleanFilter(method='filter_available',label='Наличие книг у студента')
    available_passport = django_filters.BooleanFilter(method='passport_available', label='Наличие паспорта')
    term=django_filters.CharFilter(method='filter_term',label='')

    class Meta:
        model=student.models.Student
        fields=['full_name','available']

    def filter_available (self,queryset,name,title):
        if title is None:
            return queryset
        if title:
            return queryset.filter(book__title__gt=0)
        return queryset.filter(book__title=0)

    def fiter_term (self,queryset,name, value):
        criteria=Q()
        for term in value.split():
            criteria &=Q(full_name__icontains=term) |Q(department__icontains=term)
        return queryset.filter(criteria).distinct()

    def passport_available (self,queryset,name,series_number):
        if series_number is None:
            return queryset
        if series_number:
            return queryset.filter(passport__series_number__gt=0)
        return queryset.filter(passport__series_number=0)

