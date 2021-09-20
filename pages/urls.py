from django.urls import path
from .views import HomePageView, AboutPageView, TestPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', TestPageView.as_view(), name='test'),
    path('home/', HomePageView.as_view(), name='home'),
] # Данный паттерн практически полностью идентичен тому, что мы использовали в прошлом уроке,
    # однако есть одно важное отличие:
    # во время использования классовых представлений в конце названия представления добавляется as_view().