from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="input1","input2","input3"

admin.site.register(Member,MemberAdmin)