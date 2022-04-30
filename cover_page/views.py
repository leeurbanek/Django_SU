from django.views.generic import TemplateView


# Create your views here.

class EnterprisePageView(TemplateView):
    """"""
    template_name = 'enterprise.html'


class FeaturesPageView(TemplateView):
    """"""
    template_name = 'features.html'


class IndexPageView(TemplateView):
    """"""
    template_name = 'index.html'


class PricingPageView(TemplateView):
    """"""
    template_name = 'pricing.html'


class SigninPageView(TemplateView):
    """"""
    template_name = 'signin.html'
