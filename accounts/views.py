from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from .forms import AddTransactionForm
from .models import Transaction
from datetime import datetime


class HomeDashboardView(View):
	template_name = 'accounts/dashboard.html'

	def get(self, request, month=datetime.now().month, year=datetime.now().year):
		transactions = Transaction.objects.filter(date__year=year).filter(date__month=month).order_by('-date')

		return render(request, self.template_name, {'transactions': transactions, 'title': 'Your Dashboard'})



class AddTransactionView(View):
	template_name = 'accounts/add_transaction.html'

	def get(self, request):
		form = AddTransactionForm()
		return render(request, self.template_name, {'form': form, 'title': 'Add a Transaction'})

	def post(self, request):
		form = AddTransactionForm(request.POST)
		if form.is_valid():
			form.save()

		messages.add_message(request, messages.SUCCESS, 'You have created a new transaction!')
		return redirect('dashboard')
