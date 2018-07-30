from django import forms
from .models import Transaction


class AddTransactionForm(forms.ModelForm):
	item = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	payee = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	date = forms.DateField(widget=forms.SelectDateWidget(
		# attrs={
		# 	'class': 'form-control'
		# }
	))
	category = forms.CharField(widget=forms.Select(
		choices=Transaction.CATEGORIES,
		attrs={
			'class': 'form-control'
		}
	))
	amount = forms.DecimalField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control'
		}
	))

	class Meta:
		model = Transaction
		fields = '__all__'
