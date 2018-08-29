from django.contrib import admin
from django.urls import path
from accounts.views import HomeDashboardView, AddTransactionView, BudgetView, AddCategoryView, UpdateCategoryView

urlpatterns = [
	path('', HomeDashboardView.as_view(), name='dashboard'),
	path('<int:month>/<int:year>/', HomeDashboardView.as_view(), name='dashboard'),
	path('add', AddTransactionView.as_view(), name='add_transaction'),

	path('budget', BudgetView.as_view(), name='budget'),
	path('budget/add', AddCategoryView.as_view(), name='add_category'),
	path('budget/update/<int:categ_id>', UpdateCategoryView.as_view(), name='update_category'),


	# path('admin/', admin.site.urls),
]
