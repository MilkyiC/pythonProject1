"""
URL configuration for student_db project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.db import router
from django.urls import path
from student import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router=DefaultRouter()

router.register('students',views.StudentApi,basename='students')
router.register('books',views.BookApi,basename='books')
router.register('curators',views.CuratorApi,basename='curators')
router.register('courses',views.CourseApi,basename='courses')
router.register('enrollments',views.EnrollmentApi,basename='enrollments')
router.register('passports',views.PassportApi,basename='passports')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first_view/',views.FirstView.as_view(),name='first_view'),
    path('schema/',SpectacularAPIView.as_view(),name='schema'),
    path('swagger/',SpectacularSwaggerView.as_view(),name='schema'),
    path('student_list/',views.StudentList.as_view(),name='student_list'),
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('students/<int:pk>/',views.StudentDetail.as_view(),name='student_detail'),
    path('students/<int:pk>/update/',views.StudentUpdate.as_view(),name='student_update'),
    path('students/<int:pk>/delete/',views.StudentDelete.as_view(),name='student_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+router.urls
