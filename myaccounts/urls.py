from django.contrib import admin
from django.urls import path
from accounts.views import HomeDashboardView, AddTransactionView

urlpatterns = [
	path('', HomeDashboardView.as_view(), name='dashboard'),
	path('<int:month>/<int:year>/', HomeDashboardView.as_view(), name='dashboard'),
	path('add', AddTransactionView.as_view(), name='add_transaction'),


	# path('admin/', admin.site.urls),
]
