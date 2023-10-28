# urls file created
# cpy urls.py of todobackend
from django.urls import path
from .views import TodoGetCreate,TodoUpdateDlt

urlpatterns = [
    path('',TodoGetCreate.as_view()),
    path('<int:pk>',TodoUpdateDlt.as_view()) #pk means primary key
]