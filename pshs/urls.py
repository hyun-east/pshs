from django.urls import path

from . import views

app_name = 'pshs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('attendance/', views.attendance, name='attendance'),
    path('assembly/', views.assembly, name='assembly'),
    path('assembly/<int:assembly_id>/', views.assembly_detail, name = 'assembly_detail'),
    path('assembly/create/', views.assembly_create, name='assembly_create'),
    path('assembly/<int:assembly_id>/allow', views.allow_email, name='allow'),
    path('assembly/<int:assembly_id>/disallow', views.disallow_email, name='disallow'),
    path('attendance/create/', views.attendance_create, name='attendance_create'),
    path('attendance/jasup/<int:attendance_id>/',views.jasup, name='jasup' ),
    path('attendance/classroom/<int:attendance_id>/',views.classroom, name='classroom' ),
    path('attendance/assemble/<int:attendance_id>/',views.assemble, name='assemble' ),
    path('attendance/absent/<int:attendance_id>/', views.absent, name='absent'),
    path('attendance/all/jasup', views.all_jasup, name='all_jasup'),
    path('attendance/all/classroom', views.all_classroom, name='all_classroom'),
    path('attendance/all/assemble', views.all_assemble, name='all_assemble'),
    path('recurit/', views.recurit, name='recurit'),
    path('recurit/<int:recurit_id>', views.recurit_detail, name='recurit_detail'),
    path('recurit/create/', views.recurit_create, name='recurit_create'),
    path('apply/create/<int:recurit_id>/', views.apply_create, name='apply_create'),
    path('delete/question/<int:question_id>', views.delete_question, name='delete_question'),
    path('delete/assembly/<int:assembly_id>', views.delete_assembly, name='delete_assembly'),
    path('delete/recurit/<int:recurit_id>', views.delete_recurit, name='delete_recurit'),
    path('delete/attendance/<int:attendance_id>', views.delete_attendance, name='delete_attendance'),
]