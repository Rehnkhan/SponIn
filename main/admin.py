from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Sponsor, Adrequest, Campaign
# Register your models here.

class MyUserAdmin(UserAdmin):
    model = MyUser

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('user_type', 'sponsor', 'influencer', 'profile_picture')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'sponsor', 'influencer'),
        }),
    )

    def delete_model(self, request, obj):
        if obj.sponsor:
            obj.sponsor.delete()
        if obj.influencer:
            print(obj.influencer)
            obj.influencer.delete()
        
        super().delete_model(request, obj)

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Sponsor)
admin.site.register(Adrequest)
admin.site.register(Campaign)