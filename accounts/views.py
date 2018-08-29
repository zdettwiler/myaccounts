from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.db.models import Sum
from .forms import AddTransactionForm, AddCategoryForm
from .models import Transaction, Category
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


class BudgetView(View):
	template_name = 'accounts/budget.html'

	def get(self, request):
		categories_income = Category.objects.filter(inc_exp=True)
		categories_expenditure = Category.objects.filter(inc_exp=False)
		total_income = categories_income.aggregate(Sum('allowance'))['allowance__sum']
		total_expenditure = categories_expenditure.aggregate(Sum('allowance'))['allowance__sum']

		forms_expenditure = []
		for categ in categories_expenditure:
			forms_expenditure.append(AddCategoryForm(instance=categ))

		form_add_category = AddCategoryForm()

		return render(request, self.template_name, {
			'categories_income': categories_income,
			'categories_expenditure': categories_expenditure,
			'total_income': total_income,
			'total_expenditure': total_expenditure,
			'forms_expenditure': forms_expenditure,
			'form_add_category': form_add_category,
			'title': 'Your Budget'
		})


class AddCategoryView(View):
	def post(self, request):
		form = AddCategoryForm(request.POST)
		if form.is_valid():
			form.save()

		messages.add_message(request, messages.SUCCESS, 'You have created a new category!')
		return redirect('budget')

class UpdateCategoryView(View):
	def post(self, request, categ_id):
		categ = Category.objects.get(pk=categ_id)
		form = AddCategoryForm(request.POST, instance=categ)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "You have update the 'name' category!")
		else:
			messages.add_message(request, messages.DANGER, "Error updating the 'name' category!")

		return redirect('budget')
