from django.shortcuts import render
# from django.contrib.auth import authenticate , login
# from django.views import generic
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Expenses, GroupMember, Group, User


class AddUserExpenses(View):
    
    @login_required
    def post(self, request):
        paid_by = request.POST.get('user_id')
        paid_to = = request.POST.get('group_id')
        amount = request.POST.get('amount')
        meta = request.POST.get('meta')
        exp = Expenses(user=user_id, group=paid_to,meta=meta)
        try:
            exp.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("Expense by {paid_by} Successfully Added to {paid_to}")

class CreateGroup(View):

    @login_required
    def post(self, request):
        created_by = request.POST.get('created_by')
        name = = request.POST.get('group_name')
        meta = request.POST.get('meta')
        grp = Group(created_by=created_by, name==name,meta=meta)
        try:
            grp.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("'{name}' Successfully Created")

class AddTOGroup(View):

    @login_required
    def post(self, request):
        user_id = request.POST.get('user_id')
        group_id = = request.POST.get('group_id')
        meta = request.POST.get('meta')
        grpMmbr = GroupMember(user=user_id, group=group_id)
        try:
            grpMmbr.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse("Successfully Added to {group_id}")

class ShowBalance(View):

    @login_required
    def post(request, user_id):
        group_id = request.POST.get('group_id')
        if not group_id:
            balance1 = Expenses.objects.filter(group=group_id).exclude(user=user_id).aggregate(Sum("amount"))
            balance2 = Expenses.objects.filter(group=group_id, user=user_id).aggregate(Sum("amount"))
            return (balance1 - balance2)/n
        balance1 = Expenses.objects.filter().exclude(user=user_id).aggregate(Sum("amount"))
        balance2 = Expenses.objects.filter(user=user_id).aggregate(Sum("amount"))
        return (balance1 - balance2)/n

