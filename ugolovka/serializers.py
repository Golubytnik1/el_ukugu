from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'eid_card', 'passport_number', 'has_criminal_record',
                  'criminal_record_title', 'criminal_record_description')