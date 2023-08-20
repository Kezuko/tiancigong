from django.contrib import admin
from .models import AccountUser, Member

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                "fields": ['account','name','eng_date_of_birth']
            }
        )
    ]

admin.site.register(Member, MemberAdmin)
admin.site.register(AccountUser)
