from django.contrib import admin
from .models import Customer, Campaign, Goal, MarketingMaterial

admin.site.register(Customer)
admin.site.register(Campaign)
admin.site.register(Goal)
admin.site.register(MarketingMaterial)
