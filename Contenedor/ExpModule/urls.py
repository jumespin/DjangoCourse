from django.urls import path
from ExpModule.views import IndexView, AutorView

urlpatterns = [
    path('', IndexView),
    path('autor/<int:id>', AutorView)
]