from django.db import models


class Emp(models.Model):
    empnum = models.AutoField(primary_key=True)
    empname = models.CharField(max_length=100)


class EmpBasicPay(models.Model):
    empnum = models.ForeignKey(Emp, on_delete=models.CASCADE)
    basicpay = models.DecimalField(max_digits=10, decimal_places=2)


class EmpAttendance(models.Model):
    MONTH_CHOICES = [
        ("January", "January"),
        ("February", "February"),
        ("March", "March"),
        ("April", "April"),
        ("May", "May"),
        ("June", "June"),
        ("July", "July"),
        ("August", "August"),
        ("September", "September"),
        ("October", "October"),
        ("November", "November"),
        ("December", "December"),
    ]

    empnum = models.ForeignKey(Emp, on_delete=models.CASCADE)
    month = models.CharField(max_length=50, choices=MONTH_CHOICES)
    numofdays = models.IntegerField()

    def get_basic_pay(self):
        try:
            basic_pay_entry = EmpBasicPay.objects.get(empnum=self.empnum)
            return basic_pay_entry.basicpay
        except EmpBasicPay.DoesNotExist:
            return 0

    def calculate_gross_pay(self):
        basic_pay = self.get_basic_pay()
        return (basic_pay / 30) * self.numofdays

    def calculate_net_pay(self, tax_rate):
        gross_pay = self.calculate_gross_pay()
        it_tax = gross_pay * (tax_rate / 100)
        return gross_pay - it_tax


class EmpTax(models.Model):
    empnum = models.ForeignKey(Emp, on_delete=models.CASCADE)
    it_tax = models.DecimalField(max_digits=5, decimal_places=2)
