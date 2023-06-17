from rest_framework import serializers
from .models import PersonNalog

class PersonNalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonNalog
        fields = ('first_name', 'last_name', 'bank_title', 'passport_number_nalog', 'has_tax_arrears',
                  'amount_tax_arrears', 'amount_insurance_premiums')