from django import forms
from .models import Transaction, Category


class AddTransactionForm(forms.ModelForm):
	item = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-sm'
		}
	))
	payee = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-sm'
		}
	))
	date = forms.DateField(widget=forms.SelectDateWidget(
		# attrs={
		# 	'class': 'form-control form-control-sm'
		# }
	))
	category = forms.CharField(widget=forms.Select(
		choices=Transaction.CATEGORIES,
		attrs={
			'class': 'form-control form-control-sm'
		}
	))
	amount = forms.DecimalField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control form-control-sm'
		}
	))

	class Meta:
		model = Transaction
		fields = '__all__'


class AddCategoryForm(forms.ModelForm):
	label = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-sm',
			'placeholder': 'Label'
		}
	))
	label_short = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control form-control-sm',
			'placeholder': 'SHCT'
		}
	))
	allowance = forms.DecimalField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control form-control-sm',
			'placeholder': 'allowance'
		}
	))
	inc_exp = forms.BooleanField(required=False, label='Inc./Exp.', widget=forms.CheckboxInput(
		attrs={
			'class': 'form-check-input'
		}
	))

	class Meta:
		model = Category
		fields = '__all__'
