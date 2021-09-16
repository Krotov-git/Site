from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
] # Данный паттерн практически полностью идентичен тому, что мы использовали в прошлом уроке,
    # однако есть одно важное отличие:
    # во время использования классовых представлений в конце названия представления добавляется as_view().