from django.contrib import admin
from django.urls import path
from st_form_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index'),
    path('update/<int:id>', updateView, name='update'),
    path('delete/<int:id>', deleteView, name='delete'),
]
