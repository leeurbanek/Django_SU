from django.urls import path

from . import views


urlpatterns = [
    path('enterprise', views.EnterprisePageView.as_view(), name='enterprise'),
    path('features', views.FeaturesPageView.as_view(), name='features'),
    path('index', views.IndexPageView.as_view(), name='index'),
    path('pricing', views.PricingPageView.as_view(), name='pricing'),
    path('signin', views.SigninPageView.as_view(), name='signin'),
    path('', views.IndexPageView.as_view(), name='index'),
]
