from django.test import TestCase
from .models import Customer, Campaign, Goal
from .utils import generate_chatgpt_query

class MarketingAppTestCase(TestCase):
    def setUp(self):
        self.goal = Goal.objects.create(name='Increase Sales', description='To boost product sales.')
        self.customer = Customer.objects.create(name='Acme Corp', strong_points='Innovative, Reliable', products_or_services='Gadgets')
        self.campaign = Campaign.objects.create(customer=self.customer, topic='Summer Sale', goal=self.goal)

    def test_generate_chatgpt_query(self):
        query = generate_chatgpt_query(self.campaign)
        expected_query = (
            "Generate a Increase Sales marketing material for Acme Corp.\n"
            "Topic: Summer Sale\n"
            "Strong Points of Customer: Innovative, Reliable\n"
            "Products/Services: Gadgets"
        )
        self.assertEqual(query, expected_query)
