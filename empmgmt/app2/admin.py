from django.contrib import admin
from .models import Emp, EmpAttendance, EmpBasicPay, EmpTax

# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ("empnum", "empname")


class EmpAttendanceAdmin(admin.ModelAdmin):
    list_display = ["empnum", "month", "numofdays"]


class EmpBasicPayAdmin(admin.ModelAdmin):
    list_display = ["empnum", "basicpay"]


class EmpTaxAdmin(admin.ModelAdmin):
    list_display = ["empnum", "it_tax"]


admin.site.register(Emp, EmpAdmin)
admin.site.register(EmpAttendance, EmpAttendanceAdmin)
admin.site.register(EmpBasicPay, EmpBasicPayAdmin)
admin.site.register(EmpTax, EmpTaxAdmin)
