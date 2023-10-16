from django.shortcuts import render, get_object_or_404

from .models import Customer, Campaign, Goal, MarketingMaterial, MaterialQuestion


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
    marketing_materials = MarketingMaterial.objects.filter(campaign=campaign)

    # Create a dictionary where the keys are MarketingMaterial objects
    # and the values are lists of MaterialQuestion objects related to that MarketingMaterial.
    material_to_questions = {}
    for material in marketing_materials:
        material_questions = MaterialQuestion.objects.filter(material=material)
        material_to_questions[material] = material_questions

    context = {
        'campaign': campaign,
        'goals': goals,
        'marketing_materials': marketing_materials,
        'material_to_questions': material_to_questions,
    }

    return render(request, 'marketing/campaign_detail.html', context)
