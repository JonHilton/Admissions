from django.contrib import admin
from admission.models import Patient

admin.site.register(Patient)

class PatientAdmin(admin.ModelAdmin):
	list_display = ('pt_first_name','pt_last_name','time_added')













































0
# Register your models here.
