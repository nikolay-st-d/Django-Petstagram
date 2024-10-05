from django.urls import path, include

import petstagram.common.views
from petstagram.pets import views

urlpatterns = [
    path('add/', views.pet_add_page, name='add-pet'),

    path('', include(
        [
            path('<str:username>/pet/<slug:pet_slug>/', views.pet_details_page, name='pet-details'),
            path('<str:username>/pet/<slug:pet_slug>/edit/', views.pet_edit_page, name='edit-pet'),
            path('<str:username>/pet/<slug:pet_slug>/delete/', views.pet_delete_page, name='delete-pet'),
        ]
    ))]

