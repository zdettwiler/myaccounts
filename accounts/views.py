from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.db.models import Sum
from .forms import AddTransactionForm
from .models import Transaction
from datetime import datetime


class HomeDashboardView(View):
	template_name = 'accounts/dashboard.html'

	def get(self, request, month=datetime.now().month, year=datetime.now().year):
		totals = Transaction.TOTALS
		transactions = Transaction.objects.filter(date__year=year).filter(date__month=month).order_by('-date')

		for category in totals.keys():
			value = transactions.filter(category=category).aggregate(Sum('amount'))['amount__sum']
			if value == None:
				value = 0

			totals[category] = value

		return render(request, self.template_name, {'transactions': transactions, 'totals': totals, 'title': 'Your Dashboard'})



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
