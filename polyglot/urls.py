from django.urls import path
from .views import *

urlpatterns = [
    path('binyans/', BinyanList.as_view(), name='binyans_list_url'),
    path('binyan/create/', BinyanCreate.as_view(), name='binyan_create_url'),
    path('binyan/<int:id>/', BinyanDetails.as_view(), name='binyan_details_url'),
    path('binyan/<int:id>/update/', BinyanUpdate.as_view(), name='binyan_update_url'),
    path('binyan/<int:id>/delete/', BinyanDelete.as_view(), name='binyan_delete_url'),
    path('pos/', POSList.as_view(), name='pos_list_url'),
    path('pos/create/', POSCreate.as_view(), name='pos_create_url'),
    path('pos/<int:id>/', POSDetails.as_view(), name='pos_details_url'),
    path('pos/<int:id>/update/', POSUpdate.as_view(), name='pos_update_url'),
    path('pos/<int:id>/delete/', POSDelete.as_view(), name='pos_delete_url'),
    path('ruswords/', RusWordsList.as_view(), name='ruswords_list_url'),
    path('rusword/<int:id>/', RusWordDetails.as_view(), name='rusword_detail_url'),
    path('rusword/create/', RusWordCreate.as_view(), name='rusword_create_url'),
    path('rusword/<int:id>/update/', RusWordUpdate.as_view(), name='rusword_update_url'),
    path('rusword/<int:id>/delete/', RusWordDelete.as_view(), name='rusword_delete_url'),
    path('roots/', HebrewRootsList.as_view(), name='hebrewroots_list_url'),
    path('root/create/', HebrewRootCreate.as_view(), name='hebrewroot_create_url'),
    path('root/<int:id>/', HebrewRootDetails.as_view(), name='hebrewroot_details_url'),
    path('root/<int:id>/update/', HebrewRootUpdate.as_view(), name='hebrewroot_update_url'),
    path('root/<int:id>/delete/', HebrewRootDelete.as_view(), name='hebrewroot_delete_url'),
    path('theme/', ThemeList.as_view(), name='themes_list_url'),
    path('theme/create/', ThemeCreate.as_view(), name='theme_create_url'),
    path('theme/<int:id>/', ThemeDetails.as_view(), name='theme_details_url'),
    path('theme/<int:id>/update/', ThemeUpdate.as_view(), name='theme_update_url'),
    path('theme/<int:id>/delete/', ThemeDelete.as_view(), name='theme_delete_url'),
    path('preposition/', PrepositionList.as_view(), name='prep_list_url'),
    path('preposition/create/', PrepositionCreate.as_view(), name='prep_create_url'),
    path('preposition/<int:id>/', PrepositionDetailes.as_view(), name='prep_details_url'),
    path('preposition/<int:id>/update/', PrepositionUpdate.as_view(), name='prep_update_url'),
    path('preposition/<int:id>/delete/', PrepositionDelete.as_view(), name='prep_delete_url'),
    path('pronoun/', PronounList.as_view(), name='pron_list_url'),
    path('pronoun/create/', PronounCreate.as_view(), name='pron_create_url'),
    path('pronoun/<int:id>/', PronounDetailes.as_view(), name='pron_details_url'),
    path('pronoun/<int:id>/update/', PronounUpdate.as_view(), name='pron_update_url'),
    path('pronoun/<int:id>/delete/', PronounDelete.as_view(), name='pron_delete_url'),
    path('symbols/', HebrewSymbols.as_view(), name='symbols_list_url'),
    path('symbols/<int:id>/', HebrewSymbol.as_view(), name='symbol_details_url'),

]
