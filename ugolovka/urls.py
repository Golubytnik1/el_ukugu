from django.urls import path
from .views import PersonListView, PersonDetailView

urlpatterns = [
    path('person/', PersonListView.as_view(), name='person-list'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
]
