from django.http import HttpResponse
from django.shortcuts import render
from testapp.models import User


# Create your views here.
def testdb(request):
    userlist = User.objects.all()
    str = ''
    for user in userlist:
        str += (user.name+',')
    return HttpResponse('查询结果：'+str)