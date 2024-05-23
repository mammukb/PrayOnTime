from django.urls import path,include
from django.contrib import admin
from django.urls import path
from prayapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),

]