from django.shortcuts import render, get_object_or_404

from .models import Customer, Campaign, Goal, MarketingMaterial


def customer_list_view(request):
    customers = Customer.objects.all()
    return render(request, 'marketing/customer_list.html', {'customers': customers})


def customer_detail_view(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    campaigns = customer.campaigns.all()

    context = {
        'customer': customer,
        'campaigns': campaigns,
    }

    return render(request, 'marketing/customer_detail.html', context)


def campaign_detail_view(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    goals = Goal.objects.filter(campaigns=campaign)
    marketing_material = campaign.materials.all()

    context = {
        'campaign': campaign,
        'goals': goals,
        'marketing_materials': marketing_material,
    }

    return render(request, 'marketing/campaign_detail.html', context)
