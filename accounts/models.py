from django.db import models
from datetime import date


class Transaction(models.Model):
	RENTBILLS = 'REBI'
	HOUSEHOLD = 'HSHD'
	TRAVEL = 'TRVL'
	GIVING = 'GVNG'
	FOOD = 'FOOD'
	LEISURE = 'LESR'
	BOOKS = 'BOOK'
	SAVINGS = 'SVGS'
	OTHER = 'OTHR'
	UNDEFINED = 'UNDF'
	TOTALS = {
		'REBI': 0,
		'HSHD': 0,
		'TRVL': 0,
		'GVNG': 0,
		'FOOD': 0,
		'LESR': 0,
		'BOOK': 0,
		'SVGS': 0,
		'OTHR': 0,
		'UNDF': 0,
	}
	CATEGORIES = (
		(RENTBILLS, 'Rent/Bills'),
		(HOUSEHOLD, 'Household'),
		(TRAVEL, 'Travel'),
		(GIVING, 'Giving'),
		(FOOD, 'Food'),
		(LEISURE, 'Leisure'),
		(BOOKS, 'Books'),
		(SAVINGS, 'Savings'),
		(OTHER, 'Other'),
		(UNDEFINED, 'Undefined (define later)')
    )

	item = models.CharField(max_length=200, blank=False)
	payee = models.CharField(max_length=200, blank=False)
	date = models.DateField(default=date.today, blank=False)
	category = models.CharField(max_length=4, choices=CATEGORIES, blank=False, default=UNDEFINED)
	amount = models.DecimalField(max_digits=8, decimal_places=2, blank=False)

	def __str__(self):
		return self.item

class Category(models.Model):
	label = models.CharField(max_length=50, blank=False)
	label_short = models.CharField(max_length=5, blank=False)
	allowance = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
	inc_exp = models.BooleanField(default=False)
