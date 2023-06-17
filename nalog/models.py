from django.db import models

class PersonNalog(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bank_title = models.CharField(max_length=100, blank=True, null=True)
    passport_number_nalog = models.CharField(max_length=14, unique=True)
    has_tax_arrears = models.BooleanField(default=False)
    amount_tax_arrears = models.PositiveIntegerField(default=0, null=True)
    amount_insurance_premiums = models.PositiveIntegerField(default=0, null=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'