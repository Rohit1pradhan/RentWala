from django.contrib import admin

from api.models import user, reset, activations, addhouse, varify_mail


# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = ['id','email_id','password','name','mobile_number','city']

@admin.register(reset)
class resetadmin(admin.ModelAdmin):
    list_display = ['id','user_id','OTP']

@admin.register(activations)
class activateadmin(admin.ModelAdmin):
    list_display = ['id','user_id','activation','current_city']

@admin.register(addhouse)
class addhouseadmin(admin.ModelAdmin):
    list_display = ['id','owner_id','house_type','rent','facing','area','conditions','facillities','city']

@admin.register(varify_mail)
class varify_mailadmin(admin.ModelAdmin):
    list_display = ['id','user_id','verify_otp']
