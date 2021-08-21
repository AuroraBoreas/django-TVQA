from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

import datetime
year = datetime.datetime.today().year
month = datetime.datetime.today().month

pmod_name_validator = RegexValidator(r'[a-zA-Z]{2,3}[0-9]{2,3}', 'Only PMod name allowed(i.e: AG85)') # AG85, CHM75, SBL49
part_number_validator = RegexValidator(r'[a-zA-Z]{1}[0-9]{7}[a-zA-Z]{1}', 'Only PMod part number allowed(i.e: A5030081A)') #A5030081B

class PMod(models.Model):
    name           = models.CharField(max_length=6, validators=[pmod_name_validator], blank=True)
    part_number    = models.CharField(max_length=9, validators=[part_number_validator], blank=True)
    date_created   = models.DateTimeField(default=timezone.now)
    year_quotated  = models.IntegerField(default=year, blank=True, null=False)
    month_quotated = models.IntegerField(default=month, blank=True, null=False)
    unit_price     = models.DecimalField(decimal_places=2, max_digits=100)
    BOM_registered = models.BooleanField(default=False)
    export_to_csv  = models.BooleanField(default=False)

    def __repr__(self):
        return 'PMod {}'.format(self.name)