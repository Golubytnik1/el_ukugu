from rest_framework import generics, permissions
from .models import PersonNalog
from .serializers import PersonNalogSerializer

class PersonNalogListView(generics.ListAPIView):
    serializer_class = PersonNalogSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = PersonNalog.objects.all()
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        bank_title = self.request.query_params.get('bank_title', None)
        passport_number_nalog = self.request.query_params.get('passport_number_nalog', None)
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        if last_name:
            queryset = queryset.filter(last_name=last_name)
        if bank_title:
            queryset = queryset.filter(eid_card=bank_title)
        if passport_number_nalog:
            queryset = queryset.filter(passport_number=passport_number_nalog)

        return queryset

class PersonNalogDetailView(generics.RetrieveAPIView):
    serializer_class = PersonNalogSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return PersonNalog.objects.all()
