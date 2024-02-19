from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home,signup,signin

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.user_logout, name="logout"),  # Changed from 'logout/' to 'user_logout'
    path('forgetpass/', views.forgetpass, name="forgetpass"),
    path('employee/', views.employee, name="employee"),
    path('student/', views.student, name="student"),
    path('admino/', views.admino, name="admino"),
    path('attendance_entry/', views.attendance_entry, name="attendance_entry"),
    path('sms_alert/', views.sms_alert, name="sms_alert"),
    path('updation/', views.updation, name="updation"),
    path('timeadjustment/', views.timeadjustment, name="timeadjustment"),
    path('update/', views.update, name="update"),
    path('student_leave/', views.student_leave, name="student_leave"),
    #path('save_form/', views.save_form, name="save_form"),
]