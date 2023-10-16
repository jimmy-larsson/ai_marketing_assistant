from django.core.management import call_command
import os

def generate_chatgpt_query(campaign):
    customer = campaign.customer
    goal = campaign.goal

    query_parts = [
        f"Generate a {goal.name} marketing material for {customer.name}.",
        f"Topic: {campaign.topic}",
        f"Strong Points of Customer: {customer.strong_points}",
        f"Products/Services: {customer.products_or_services}"
    ]

    return "\n".join(query_parts)

def load_mock_data_from_json():
    # Path to JSON files
    base_dir = os.path.dirname(os.path.abspath(__file__))
    goals_path = os.path.join(base_dir, 'mock-data/goals.json')
    customers_path = os.path.join(base_dir, 'mock-data/customers.json')
    campaigns_path = os.path.join(base_dir, 'mock-data/campaigns.json')

    # Load data using Django's call_command
    call_command('loaddata', goals_path, verbosity=0)
    call_command('loaddata', customers_path, verbosity=0)
    call_command('loaddata', campaigns_path, verbosity=0)

    print('Mock data loaded successfully from JSON files.')