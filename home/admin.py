from django.contrib import admin

from home.models import Availability, Golfer, Profile,  BankAccount, UserProfile

# Register your models here.
admin.site.register(Availability)
admin.site.register(Profile)

admin.site.register(Golfer)
admin.site.register(UserProfile)
@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_editable = ('balance',)
    search_fields = ('user__username',)