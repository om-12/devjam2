from django.contrib import admin
from .models import Rentyourhouse
from .models import rent_payee

admin.site.register(Rentyourhouse)

admin.site.register(rent_payee)