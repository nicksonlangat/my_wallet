from django.urls import path 
from . import views
from  . views import HomePageView 
app_name = "profiles"

urlpatterns = [
    path('', HomePageView.as_view(), name ='home'), 
    path("account_status/", views.index, name = "account_status"),
    path ("money_transfer/", views.money_transfer, name = "money_transfer"),
    path ("loan_app/", views.loan, name = "loan_app"),
    path ("settings/", views.settings, name = "settings"),
    path ("edit_details/", views.edit_details, name = "edit_details"),
    path ("delete_account/", views.delete_account, name = "delete_account")
]
