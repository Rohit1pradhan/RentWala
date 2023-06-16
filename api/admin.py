from django.contrib import admin

from api.models import user, reset, activations, varify_mail, addhouse


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
    list_display = ['id','owner_name','owner_contect_number','house_type','rent','house_facing','area','conditions','Facilities','city','picture1','picture2','picture3']

@admin.register(varify_mail)
class varify_mailadmin(admin.ModelAdmin):
    list_display = ['id','user_id','verify_otp']
