from django.urls import path

from ads.views import AdView, AdDetailView, AdUploadImageView

urlpatterns = [
    path('', AdView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/upload_image', AdUploadImageView.as_view()),

]