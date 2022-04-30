from django.test import SimpleTestCase
from django.urls import resolve, reverse

from . import views


# Create your tests here.

class EnterprisePageTests(SimpleTestCase):
    """"""
    def setUp(self):
        url = reverse('enterprise')
        self.response = self.client.get(url)

    def test_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_use_enterprise_template(self):
        self.assertTemplateUsed(self.response, 'enterprise.html')

    def test_url_resolves_EnterprisePageView(self):
        view = resolve('/enterprise')
        self.assertEqual(
            view.func.__name__, views.EnterprisePageView.as_view().__name__
        )


class FeaturesPageTests(SimpleTestCase):
    """"""
    def setUp(self):
        url = reverse('features')
        self.response = self.client.get(url)

    def test_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_use_features_template(self):
        self.assertTemplateUsed(self.response, 'features.html')

    def test_url_resolves_FeaturesPageView(self):
        view = resolve('/features')
        self.assertEqual(
            view.func.__name__, views.FeaturesPageView.as_view().__name__
        )


class IndexPageTests(SimpleTestCase):
    """"""
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_use_index_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_url_resolves_IndexPageView(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__, views.IndexPageView.as_view().__name__
        )


class PricingPageTests(SimpleTestCase):
    """"""
    def setUp(self):
        url = reverse('pricing')
        self.response = self.client.get(url)

    def test_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_use_pricing_template(self):
        self.assertTemplateUsed(self.response, 'pricing.html')

    def test_url_resolves_PricingPageView(self):
        view = resolve('/pricing')
        self.assertEqual(
            view.func.__name__, views.PricingPageView.as_view().__name__
        )
