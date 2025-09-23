from django.contrib import admin

from home.models import Availability, Profile,  BankAccount

# Register your models here.
admin.site.register(Availability)
admin.site.register(Profile)

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_editable = ('balance',)
    search_fields = ('user__username',)