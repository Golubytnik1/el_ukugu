from rest_framework import generics, permissions
from .models import Person
from .serializers import PersonSerializer

class PersonListView(generics.ListAPIView):
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Person.objects.all()
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        eid_card = self.request.query_params.get('eid_card', None)
        passport_number = self.request.query_params.get('passport_number', None)
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        if last_name:
            queryset = queryset.filter(last_name=last_name)
        if eid_card:
            queryset = queryset.filter(eid_card=eid_card)
        if passport_number:
            queryset = queryset.filter(passport_number=passport_number)

        return queryset

class PersonDetailView(generics.RetrieveAPIView):
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Person.objects.all()
