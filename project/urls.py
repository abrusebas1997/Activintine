from django.urls import path, include
from project.views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView, Home


urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('list_of_activities/', ActivityListView.as_view(), name='activity-list-project'),
    path('new_project/', ActivityCreateView.as_view(), name='activity-create-project'),
    path('<str:slug>/', ActivityDetailView.as_view(), name='activity-details-project'),
    path('edit/<int:pk>/', ActivityUpdateView.as_view(), name='activity-update-project'),
    path('delete/<int:pk>', ActivityDeleteView.as_view(), name='activity-delete-project'),

]
