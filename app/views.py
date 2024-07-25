from django.shortcuts import render
from app.models import *
# Create your views here.
def equi_joins(request):
    LEDO=Emp.objects.select_related('deptno').all()
    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)