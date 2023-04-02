from django.urls import path
from app_one import views

urlpatterns = [
    path('programs', views.ProgramList.as_view()),
    path('program/<int:pk>', views.ProgramDetail.as_view()),
    path('modules', views.ModuleList.as_view()),
    path('module/<int:id>', views.ModuleDetail.as_view()),
    path('lessons', views.LessonList.as_view()),
    path('lesson/<int:id>', views.LessonDetail.as_view()),
]
