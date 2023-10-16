from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MarketingMaterial, MaterialQuestion

DEFAULT_QUESTIONS = {
    'all': [
        "What is the primary call to action?",
        "Who is the target audience?",
        "What is the tone of the material? (Formal, Informal, Professional, etc.)"
    ],
    'blog': [
        "What are the SEO Keywords?",
        "What should be the main takeaway for the reader?",
        "Should the blog post have sections? If yes, what should they be?"
    ],
    'email': [
        "Is there a special offer or promotion?",
        "What is the subject line?"
    ],
    'newsletter': [
        "What sections should be included in the newsletter?",
        "Is there any time-sensitive information?"
    ],
}


@receiver(post_save, sender=MarketingMaterial)
def create_material_questions(sender, instance, created, **kwargs):
    if created:
        material_type = instance.material_type
        common_questions = DEFAULT_QUESTIONS.get('all', [])
        specific_questions = DEFAULT_QUESTIONS.get(material_type, [])

        # Merge common and specific questions
        all_questions = common_questions + specific_questions

        for question_text in all_questions:
            MaterialQuestion.objects.create(
                material=instance,
                question=question_text,
                answer=""
            )
