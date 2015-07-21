from django.shortcuts import render
from member.models import *


def index(request):
    admins  = Member.objects.filter(is_admin=True)
    members = Member.objects.filter(is_admin=False)
    
    return render(request, 'member/index.html', {'admins': admins, 'members': members})


def show(request, member_id):
    #TODO : Handle ObjectDoesNotExist
    member = Member.objects.get(id=member_id)

    return render(request, 'member/show.html', {'member': member})


