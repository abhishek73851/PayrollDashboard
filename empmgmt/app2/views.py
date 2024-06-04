from django.shortcuts import render
from .forms import EmpSelectionForm
from .models import EmpAttendance, EmpTax


def index(request):
    gross_pay = None
    net_pay = None

    if request.method == "POST":
        form = EmpSelectionForm(request.POST)
        if form.is_valid():
            empnum = form.cleaned_data["empnum"]
            month = form.cleaned_data["month"]
            try:
                emp_attendance = EmpAttendance.objects.get(empnum=empnum, month=month)
                emp_tax = EmpTax.objects.filter(empnum=empnum).first()
                if emp_tax:
                    tax_rate = (
                        emp_tax.it_tax
                    )  # Assuming tax_rate is a field in the EmpTax model
                    gross_pay = emp_attendance.calculate_gross_pay()
                    net_pay = emp_attendance.calculate_net_pay(tax_rate)
                    gross_pay = f"{gross_pay:.2f}"
                    net_pay = f"{net_pay:.2f}"
                else:
                    form.add_error(
                        None, "Tax information not found for the selected employee."
                    )
            except EmpAttendance.DoesNotExist:
                form.add_error(None, "Employee number or month does not exist.")
    else:
        form = EmpSelectionForm()

    return render(
        request,
        "index.html",
        {
            "form": form,
            "gross_pay": gross_pay,
            "net_pay": net_pay,
        },
    )
