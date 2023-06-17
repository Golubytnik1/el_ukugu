from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    eid_card = models.CharField(max_length=9, unique=True)
    passport_number = models.CharField(max_length=14, unique=True)
    has_criminal_record = models.BooleanField(default=False)
    criminal_record_title = models.CharField(max_length=100, blank=True, null=True)
    criminal_record_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'