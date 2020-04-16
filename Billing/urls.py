from django.urls import path
from .views import *

urlpatterns = [
   path('lforms/', LegalFormList.as_view(), name='lforms_list_url'),
   path('lform/Create/', LegalFormCreate.as_view(), name='lform_create_url'),
   path('lform/<int:id>/', LegalFormDetails.as_view(), name='lform_details_url'),
   path('lform/<int:id>/update/', LegalFormUpdate.as_view(), name='lform_update_url'),
   path('lform/<int:id>/delete/', LegalFormDelete.as_view(), name='lform_delete_url'),
   path('orgs/', OrgList.as_view(), name='orgs_list_url'),
   path('org/Create/', OrgCreate.as_view(), name='org_create_url'),
   path('org/<int:id>/', OrgDetails.as_view(), name='org_details_url'),
   path('org/<int:id>/update/', OrgUpdate.as_view(), name='org_update_url'),
   path('org/<int:id>/delete/', OrgDelete.as_view(), name='org_delete_url'),
]
