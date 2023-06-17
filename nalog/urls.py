from django.urls import path
from .views import PersonNalogListView, PersonNalogDetailView

urlpatterns = [
    path('person_nalog/', PersonNalogListView.as_view(), name='person-nalog-list'),
    path('person_nalog/<int:pk>/', PersonNalogDetailView.as_view(), name='person-nalog-detail'),
]