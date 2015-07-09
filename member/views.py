from django.shortcuts import render
from member.models import *


def index(request):
    #TODO : Order By...
    members = Member.objects.all()
    
    return render(request, 'member/index.html', {'members': members})


def show(request, member_id):
    #TODO : Handle ObjectDoesNotExist
    member = Member.objects.get(id=member_id)

    return render(request, 'member/show.html', {'member': member})


