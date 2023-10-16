from django.contrib.auth.models import User
from django.db import models


# Marketing Goal
class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    target_audience = models.TextField(null=True, blank=True)
    suggested_channels = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    industry_choices = [
        ('Agriculture', 'Agriculture'),
        ('Automotive', 'Automotive'),
        ('Aviation', 'Aviation'),
        ('Banking', 'Banking'),
        ('Biotechnology', 'Biotechnology'),
        ('Chemical', 'Chemical'),
        ('Construction', 'Construction'),
        ('Consulting', 'Consulting'),
        ('Consumer Goods', 'Consumer Goods'),
        ('Education', 'Education'),
        ('Energy', 'Energy'),
        ('Entertainment', 'Entertainment'),
        ('Finance', 'Finance'),
        ('Food & Beverage', 'Food & Beverage'),
        ('Healthcare', 'Healthcare'),
        ('Hospitality', 'Hospitality'),
        ('Information Technology', 'Information Technology'),
        ('Insurance', 'Insurance'),
        ('Logistics', 'Logistics'),
        ('Manufacturing', 'Manufacturing'),
        ('Marketing', 'Marketing'),
        ('Media', 'Media'),
        ('Medical Devices', 'Medical Devices'),
        ('Pharmaceuticals', 'Pharmaceuticals'),
        ('Real Estate', 'Real Estate'),
        ('Retail', 'Retail'),
        ('Services', 'Services'),
        ('Telecommunications', 'Telecommunications'),
        ('Transportation', 'Transportation'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other')
    ]

    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=200, null=True, blank=True, choices=industry_choices)
    strong_points = models.TextField(null=True, blank=True)
    weaknesses = models.TextField(null=True, blank=True)
    products_or_services = models.TextField(null=True, blank=True)
    target_audience = models.TextField(null=True, blank=True)
    competitors = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Campaign Model
class Campaign(models.Model):
    customer = models.ForeignKey(Customer, related_name='campaigns', on_delete=models.CASCADE)
    topic = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    goal = models.ForeignKey(Goal, related_name='campaigns', on_delete=models.SET_NULL, null=True, blank=True)
    budget = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.name} - {self.topic}'


# Marketing Material Model
class MarketingMaterial(models.Model):
    material_types = (
        ('blog', 'Blog'),
        ('email', 'Email'),
        ('newsletter', 'Newsletter'),
        # Add other types as needed
    )
    campaign = models.ForeignKey(Campaign, related_name='materials', on_delete=models.CASCADE)
    material_type = models.CharField(max_length=100, choices=material_types)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.campaign} - {self.material_type}'


class MaterialQuestion(models.Model):
    material = models.ForeignKey(MarketingMaterial, related_name='questions', on_delete=models.CASCADE)  # Changed field
    question = models.CharField(max_length=300)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.material.campaign} - {self.material.material_type} - {self.question}'
