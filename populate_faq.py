
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alburaq_project.settings')
django.setup()

from apps.faq.models import FAQCategory, FAQ

def populate_faqs():
    # Clear existing
    FAQ.objects.all().delete()
    FAQCategory.objects.all().delete()
    
    # 1. General Questions
    general_cat, _ = FAQCategory.objects.get_or_create(slug='general')
    
    # Set Translations for Category
    general_cat.set_current_language('en')
    general_cat.name = "General Information"
    general_cat.save()
    
    general_cat.set_current_language('ar')
    general_cat.name = "معلومات عامة"
    general_cat.save()
    
    # FAQ 1
    faq1, _ = FAQ.objects.get_or_create(category=general_cat, order=1)
    
    faq1.set_current_language('en')
    faq1.question = "What services does Al Buraq Group provide?"
    faq1.answer = "We provide comprehensive international trade solutions including product sourcing, quality control, air/sea/land shipping, and customs clearance services from China to the world."
    faq1.save()
    
    faq1.set_current_language('ar')
    faq1.question = "ما هي الخدمات التي تقدمها مجموعة البراق؟"
    faq1.answer = "نقدم حلولاً شاملة للتجارة الدولية تشمل البحث عن المصادر، مراقبة الجودة، الشحن الجوي والبحري والبري، وخدمات التخليص الجمركي من الصين إلى جميع أنحاء العالم."
    faq1.save()

    # FAQ 2
    faq2, _ = FAQ.objects.get_or_create(category=general_cat, order=2)
    
    faq2.set_current_language('en')
    faq2.question = "Where are you located?"
    faq2.answer = "Our headquarters are in Yiwu, China, with branch offices in Guangzhou and other major cities. We also have agents in various countries."
    faq2.save()
    
    faq2.set_current_language('ar')
    faq2.question = "أين تقع مكاتبكم؟"
    faq2.answer = "يقع مقرنا الرئيسي في مدينة إيوو، الصين، ولدينا مكاتب فرعية في قوانغتشو ومدن رئيسية أخرى. كما لدينا وكلاء في العديد من الدول."
    faq2.save()

    # 2. Shipping
    shipping_cat, _ = FAQCategory.objects.get_or_create(slug='shipping')
    
    shipping_cat.set_current_language('en')
    shipping_cat.name = "Shipping & Delivery"
    shipping_cat.save()
    
    shipping_cat.set_current_language('ar')
    shipping_cat.name = "الشحن والتوصيل"
    shipping_cat.save()
    
    # FAQ 3
    faq3, _ = FAQ.objects.get_or_create(category=shipping_cat, order=1)
    
    faq3.set_current_language('en')
    faq3.question = "How long does shipping take?"
    faq3.answer = "Shipping times vary by method: Air freight typically takes 5-10 days, while sea freight takes 25-45 days depending on the destination."
    faq3.save()
    
    faq3.set_current_language('ar')
    faq3.question = "كم يستغرق الشحن؟"
    faq3.answer = "تختلف مدة الشحن حسب الطريقة: الشحن الجوي يستغرق عادة 5-10 أيام، بينما يستغرق الشحن البحري 25-45 يوماً حسب الوجهة."
    faq3.save()

    # FAQ 4
    faq4, _ = FAQ.objects.get_or_create(category=shipping_cat, order=2)
    
    faq4.set_current_language('en')
    faq4.question = "Do you provide tracking numbers?"
    faq4.answer = "Yes, once your shipment is dispatched, we provide a tracking number that you can use on our 'Track Shipment' page."
    faq4.save()
    
    faq4.set_current_language('ar')
    faq4.question = "هل توفرون أرقام تتبع؟"
    faq4.answer = "نعم، بمجرد شحن بضائعك، نزودك برقم تتبع يمكنك استخدامه في صفحة 'تتبع الشحنة' على موقعنا."
    faq4.save()

    print("FAQs populated successfully!")

if __name__ == '__main__':
    populate_faqs()
