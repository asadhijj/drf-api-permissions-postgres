from django.urls import path
from .views import carsListView, carsDetailView, engineListView, engineDetailView

urlpatterns = [
    path("cars/", carsListView.as_view(), name="cars-list"),
    path("cars/<int:pk>", carsDetailView.as_view(), name="Fone-detail"),
    path("engine/", engineListView.as_view(), name="circuits-list"),
    path("engine/<int:pk>", engineDetailView.as_view(), name="engine-detail"),
]