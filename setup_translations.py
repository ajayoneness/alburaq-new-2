import os
import struct

def output_mofile(msg_dict, output_file):
    messages = []
    for msgid, msgstr in msg_dict.items():
        # Include header (empty msgid)
        messages.append((msgid.encode('utf-8'), msgstr.encode('utf-8')))
    messages.sort()
    count = len(messages)
    header_size = 7 * 4
    ids_offset = header_size
    strs_offset = ids_offset + (8 * count)
    
    keys_blob = bytearray()
    key_descriptors = []
    current_key_off = strs_offset + (8 * count)
    
    for mid, mstr in messages:
        l = len(mid)
        key_descriptors.append((l, current_key_off))
        keys_blob.extend(mid)
        keys_blob.append(0)
        current_key_off += l + 1
        
    vals_blob = bytearray()
    val_descriptors = []
    current_val_off = current_key_off
    
    for mid, mstr in messages:
        l = len(mstr)
        val_descriptors.append((l, current_val_off))
        vals_blob.extend(mstr)
        vals_blob.append(0)
        current_val_off += l + 1
        
    with open(output_file, 'wb') as f:
        f.write(struct.pack('<I', 0x950412de))
        f.write(struct.pack('<I', 0))
        f.write(struct.pack('<I', count))
        f.write(struct.pack('<I', ids_offset))
        f.write(struct.pack('<I', strs_offset))
        f.write(struct.pack('<I', 0))
        f.write(struct.pack('<I', 0))
        for l, o in key_descriptors: f.write(struct.pack('<II', l, o))
        for l, o in val_descriptors: f.write(struct.pack('<II', l, o))
        f.write(keys_blob)
        f.write(vals_blob)

# Common strings to ensure consistency
common_strings = {
    # Keys
}

# ARABIC
translations_ar = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\nPlural-Forms: nplurals=6; plural=n==0 ? 0 : n==1 ? 1 : n==2 ? 2 : n%100>=3 && n%100<=10 ? 3 : n%100>=11 && n%100<=99 ? 4 : 5;\n",
    
    # === Generic ===
    "Available": "متاح",
    "Countries": "الدول",
    "Tips": "نصائح",
    "and Experiences": "وتجارب",
    "Read More": "اقرأ المزيد",
    "Other": "أخرى",
    "All Tips": "جميع النصائح",
    "Coming soon...": "قريباً...",
    "Download": "تحميل",
    "Catalog": "الكتالوج",
    "Download Catalog": "تحميل الكتالوج",
    "Contact Us": "تواصل معنا",
    "WhatsApp": "واتساب",
    "kg": "كجم",
    
    # === Views (flash messages) ===
    "Registration successful! Welcome to AL BURAQ GROUP.": "تم التسجيل بنجاح! مرحباً بك في مجموعة البراق.",
    "Welcome back!": "مرحباً بعودتك!",
    "You have been logged out.": "تم تسجيل خروجك.",
    "Profile updated successfully!": "تم تحديث الملف الشخصي بنجاح!",
    "Product added to cart": "تمت إضافة المنتج إلى السلة",
    "Item removed from cart": "تمت إزالة المنتج من السلة",
    "Your cart is empty": "سلة التسوق فارغة",
    
    # === Navigation & Base ===
    "Home": "الرئيسية",
    "About Us": "من نحن",
    "Services": "خدماتنا",
    "Our Services": "خدماتنا",
    "Our": "خدماتنا",
    "Store": "المتجر",
    "Tracking": "تتبع الشحنات",
    "FAQ": "الأسئلة الشائعة",
    "Contact": "اتصل بنا",
    "Login": "تسجيل الدخول",
    "Logout": "تسجيل الخروج",
    "Profile": "الملف الشخصي",
    "Quick Links": "روابط سريعة",
    "All rights reserved.": "جميع الحقوق محفوظة.",
    "Made with": "صنع بـ",
    "in China": "في الصين",
    "Chat on WhatsApp": "دردشة عبر واتساب",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "شريكك الموثوق للتجارة الدولية والخدمات اللوجستية من الصين إلى العالم.",
    "Our Telegram Channels": "قنواتنا على تليجرام",
    
    # === Home Page ===
    "AL BURAQ GROUP - International Trade & Logistics": "مجموعة البراق - التجارة الدولية والخدمات اللوجستية",
    "Your Gateway to": "بوابتك إلى",
    "Global Trade": "التجارة العالمية",
    "Specialized in international trade, sourcing, and logistics from China to the world. Quality products, reliable shipping, exceptional service.": "متخصصون في التجارة الدولية والتوريد والخدمات اللوجستية من الصين إلى العالم. منتجات عالية الجودة، شحن موثوق، وخدمة استثنائية.",
    "Browse Store": "تصفح المتجر",
    "Track Shipment": "تتبع الشحنة",
    "Years Experience": "سنوات من الخبرة",
    "Products": "منتجاتنا",
    "Happy Clients": "عملاء سعداء",
    "Countries Served": "الدول المخدومة",
    "Comprehensive trade and logistics solutions for your business": "حلول تجارية ولوجستية شاملة لأعمالك",
    "Comprehensive trade and logistics solutions tailored to your needs": "حلول تجارية ولوجستية شاملة مصممة خصيصاً لاحتياجاتك",
    
    # Services
    "Air Shipping": "الشحن الجوي",
    "Fast and reliable air freight services for time-sensitive shipments. Ideal for urgent orders and high-value goods that need quick delivery worldwide.": "خدمات الشحن الجوي السريعة والموثوقة للشحنات الحساسة للوقت. مثالية للطلبات العاجلة والبضائع ذات القيمة العالية التي تحتاج إلى تسليم سريع في جميع أنحاء العالم.",
    "Fast and reliable air freight services for time-sensitive shipments worldwide.": "خدمات شحن جوي سريعة وموثوقة للشحنات الحساسة للوقت في جميع أنحاء العالم.",
    "Sea Shipping": "الشحن البحري",
    "Cost-effective sea freight solutions for bulk and large shipments.": "حلول شحن بحري فعالة من حيث التكلفة للشحنات الضخمة والكبيرة.",
    "Cost-effective ocean freight for bulk shipments. Perfect for large orders where time is flexible but cost efficiency is paramount.": "شحن بحري فعال من حيث التكلفة للشحنات الضخمة. مثالي للطلبات الكبيرة حيث يكون الوقت مرنًا ولكن الكفاءة من حيث التكلفة هي الأهم.",
    "Land Shipping": "الشحن البري",
    "Efficient rail and road transport connecting China to Central Asia and Europe.": "نقل فعال بالسكك الحديدية والطرق يربط الصين بآسيا الوسطى وأوروبا.",
    "Sourcing": "المصادر والتوريد",
    "Expert product sourcing from verified Chinese manufacturers and suppliers.": "توريد منتجات خبير من مصنعين وموردين صينيين تم التحقق منهم.",
    "Quality Control": "مراقبة الجودة",
    "Rigorous quality inspection to ensure products meet your standards.": "فحص صارم للجودة لضمان تلبية المنتجات لمعاييرك.",
    "Packing & Assembly": "التغليف والتجميع",
    "Professional packaging and assembly services for your products.": "خدمات تغليف وتجميع احترافية لمنتجاتك.",
    "Documentation": "التوثيق",
    "Complete customs clearance and documentation handling.": "تخليص جمركي كامل ومعالجة الوثائق.",
    "24/7 Support": "دعم على مدار الساعة",
    "Dedicated support team available round the clock for assistance.": "فريق دعم مخصص متاح على مدار الساعة للمساعدة.",
    "View All Services": "عرض جميع الخدمات",
    
    # Categories & Agents
    "Product": "تصنيفات",
    "Categories": "المنتجات",
    "Explore our wide range of wholesale products from China": "استكشف مجموعتنا الواسعة من المنتجات بالجملة من الصين",
    "products": "منتجات",
    "Categories coming soon...": "التصنيفات قريباً...",
    "Browse All Products": "تصفح جميع المنتجات",
    "Our Agents": "وكلاؤنا",
    "Agents": "حول العالم",
    "We are proud at Al Buraq Group to have a network of agents and partners in several countries around the world...": "نفخر في مجموعة البراق بشبكة وكلاء وشركاء في عدة دول حول العالم...",
    "Team Members:": "فريق العمل:",
    "More agents coming soon...": "قريباً سنضيف المزيد من الوكلاء...",
    "Join Al Buraq Agents": "انضم لوكلاء البراق",
    
    # Why Choose Us
    "Why Choose": "لماذا تختار",
    "With over 10 years of experience in international trade...": "مع أكثر من 10 سنوات من الخبرة في التجارة الدولية...",
    "Quality Guaranteed": "جودة مضمونة",
    "Rigorous quality control on all products": "مراقبة جودة صارمة على جميع المنتجات",
    "Competitive Prices": "أسعار تنافسية",
    "Direct factory prices without middlemen": "أسعار المصنع مباشرة بدون وسطاء",
    "Global Shipping": "شحن عالمي",
    "Delivery to 50+ countries worldwide": "التسليم لأكثر من 50 دولة حول العالم",
    "Dedicated Support": "دعم مخصص",
    "Multilingual team available 24/7": "فريق متعدد اللغات متاح 24/7",
    
    # Tracking Section Home
    "Track Your Shipment": "تتبع شحنتك",
    "Enter tracking number...": "أدخل رقم التتبع...",
    "Track Now": "تتبع الآن",
    "Need help? Contact us directly:": "تحتاج مساعدة؟ اتصل بنا مباشرة:",
    
    # Offices & CTA
    "Offices": "مكاتبنا",
    "Visit our offices in China for personalized service": "تفضل بزيارة مكاتبنا في الصين للحصول على خدمة مخصصة",
    "Ready to Start Your Import Business?": "هل أنت مستعد لبدء أعمال الاستيراد الخاصة بك؟",
    "Join thousands of satisfied clients who trust AL BURAQ GROUP for their sourcing and logistics needs.": "انضم إلى آلاف العملاء الراضين الذين يثقون في مجموعة البراق لاحتياجاتهم من التوريد والخدمات اللوجستية.",
    "Create Account": "إنشاء حساب",

    # === About Page ===
    "Get to Know": "التعرّف أكثر على",
    "AL BURAQ Team": "فريق مجموعة البراق",
    "We are proud at AL BURAQ GROUP to have a professional team with diverse expertise in international trade, sourcing, shipping, and industrial equipment. Our team works together to provide the best solutions for our clients and build long-term partnerships based on trust, quality, and professionalism.": "نفتخر في مجموعة البراق بفريق عمل احترافي يضم خبرات متنوعة في مجالات التجارة الدولية، التوريد، الشحن، والمعدات الصناعية. يعمل فريقنا بروح واحدة لتقديم أفضل الحلول لعملائنا وبناء شراكات طويلة الأمد قائمة على الثقة والجودة والاحترافية.",
    "Management": "الإدارة",
    "AL BURAQ Team Members": "فريق عمل مجموعة البراق",
    "About": "عن",
    "Your trusted partner for international trade and logistics from China": "شريكك الموثوق للتجارة الدولية والخدمات اللوجستية من الصين إلى العالم",
    "Established in China": "تأسست في الصين",
    "Over 20 Years of Excellence": "أكثر من 20 عامًا من التميز",
    "Our Story": "قصتنا",
    "AL BURAQ GROUP was founded with a vision to bridge the gap between Chinese manufacturers and international buyers...": "تأسست مجموعة البراق برؤية واضحة تهدف إلى سد الفجوة بين المصنعين الصينيين والمشترين الدوليين...",
    "Our Vision": "رؤيتنا",
    "To be the world's most trusted bridge between Chinese manufacturers and global businesses...": "أن نكون الجسر الأكثر موثوقية في العالم بين المصنعين الصينيين والشركات العالمية...",
    "Our Mission": "مهمتنا",
    "To provide comprehensive trade solutions that empower businesses worldwide...": "تقديم حلول تجارية شاملة تمكن الشركات في جميع أنحاء العالم...",
    "Our Core Values": "قيمنا الجوهرية",
    "Trust": "الثقة",
    "Building lasting relationships through honesty and integrity": "بناء علاقات دائمة من خلال الصدق والنزاهة",
    "Quality": "الجودة",
    "Uncompromising standards in every product we handle": "معايير صارمة في كل منتج نتعامل معه",
    "Innovation": "الابتكار",
    "Continuously improving our processes and services": "تحسين مستمر لعملياتنا وخدماتنا",
    "Global Reach": "الانتشار العالمي",
    "Serving clients in over 50 countries worldwide": "نخدم عملاء في أكثر من 50 دولة حول العالم",
    "CEO & Founder": "المدير التنفيذي والمؤسس",
    "Chief Executive Officer": "الرئيس التنفيذي",
    "Operations Manager": "مدير العمليات",
    "Head of Operations": "رئيس العمليات",
    "Sales Director": "مدير المبيعات",
    "Head of Sales": "رئيس قسم المبيعات",
    "Ready to Work With Us?": "هل أنت مستعد للعمل معنا؟",
    "Contact our team today and let's discuss your sourcing needs.": "تواصل مع فريقنا اليوم ودعنا نناقش احتياجاتك من التوريد.",

    # === Tracking Page ===
    "Estimated Arrival Date": "تاريخ الوصول المتوقع",
    "Packages": "الطرود",
    "Weight": "الوزن",
    "Tracking History": "سجل التتبع",
    "No updates available at this time.": "لا توجد تحديثات متاحة حالياً.",
    "Forgot your tracking number?": "نسيت رقم التتبع؟",
    "Contact our support team and we'll help you find your shipment.": "تواصل مع فريق الدعم وسنساعدك في العثور على شحنتك.",
    "Shipment delayed?": "تأخرت الشحنة؟",
    "Contact us for updates on any delayed shipments.": "تواصل معنا للحصول على تحديثات حول أي شحنات متأخرة.",
    "Need help?": "تحتاج مساعدة؟",
    "Our team is available 24/7 to help you.": "فريقنا متاح 24/7 لمساعدتك.",
    
    # === Become Agent Page ===
    "Join AL BURAQ Agents": "انضم لوكلاء البراق",
    "Join the Network of": "انضم إلى شبكة",
    "AL BURAQ Agents": "وكلاء البراق",
    "The Captain in China": "القبطان في الصين",
    "Join the AL BURAQ GROUP agent network – The Captain in China, and become part of an integrated international trade system that provides you with direct access to the best factories, equipment, and logistics solutions from China to all parts of the world.": "انضم إلى شبكة وكلاء مجموعة البراق – القبطان في الصين، وكن جزءاً من منظومة تجارة دولية متكاملة توفر لك الوصول المباشر إلى أفضل المصانع والمعدات والحلول اللوجستية من الصين إلى مختلف أنحاء العالم.",
    "We don't just offer products, but long-term partnerships built on trust, quality, and continuous support to achieve mutual success.": "نحن لا نقدم مجرد منتجات، بل شراكات طويلة الأمد مبنية على الثقة، الجودة، والدعم المستمر لتحقيق النجاح المشترك.",
    "Partnership": "شراكة",
    "Requirements": "المتطلبات",
    "To ensure a successful and sustainable partnership, AL BURAQ GROUP applies clear criteria for selecting its authorized agents:": "لضمان شراكة ناجحة ومستدامة، تعتمد مجموعة البراق معايير واضحة لاختيار وكلائها المعتمدين:",
    "Commitment to import at least 60 trucks, tractors, or heavy equipment annually": "الالتزام باستيراد ما لا يقل عن 60 شاحنة أو جرار أو معدات ثقيلة سنوياً",
    "or equivalent industrial products.": "أو ما يعادلها من المنتجات الصناعية.",
    "Secure an initial amount of $5,000": "تأمين مبلغ أولي قدره 5000 دولار",
    "to start official procedures and provide the agent with necessary information and documents. This amount is counted towards a total deposit of $50,000.": "لبدء الإجراءات الرسمية وتزويد الوكيل بالمعلومات والوثائق اللازمة. هذا المبلغ يُحتسب ضمن قيمة عربون إجمالي قدره 50,000 دولار.",
    "After completing the procedures": "بعد استكمال الإجراءات",
    ", the agent commits to paying the remaining deposit to reach a total of $50,000, which is later deducted from the value of future orders.": "، يلتزم الوكيل بدفع بقية العربون ليصبح الإجمالي 50,000 دولار، ويُخصم هذا المبلغ لاحقاً من قيمة الطلبات المستقبلية.",
    "When the remaining balance": "عند انخفاض الرصيد المتبقي",
    "with the company drops below $10,000, the account must be topped up with an additional amount of at least $40,000 to ensure smooth continued supply.": "لدى الشركة إلى أقل من 10,000 دولار، يجب إعادة تعبئة الحساب بمبلغ إضافي لا يقل عن 40,000 دولار لضمان استمرار التوريد بسلاسة.",
    "To view all types of equipment and machinery available in detail, you can download the complete catalog from here.": "للاطلاع على جميع أنواع المعدات والآلات المتوفرة لدينا بالتفصيل، يمكنكم تحميل الكتالوج الكامل من هنا.",
    "Catalogs are being prepared...": "الكتالوجات قيد الإعداد...",
    "Are you ready to join?": "هل أنت مستعد للانضمام؟",
    "Contact us now via WhatsApp to discuss the partnership opportunity and answer all your questions": "تواصل معنا الآن عبر واتساب لمناقشة فرصة الشراكة والإجابة على جميع استفساراتك",
    "Contact Us via WhatsApp": "تواصل معنا عبر واتساب",
    
    # === Service Detail & Import Tips ===
    "Prices are subject to weekly updates based on market and logistics conditions": "الأسعار قابلة للتحديث أسبوعياً حسب السوق والظروف اللوجستية",
    "Import Tips": "نصائح الاستيراد",
    "and Import Experiences": "وتجارب الاستيراد",
    "The world of import and international trade is full of details that may seem simple but directly affect the success of the shipment and the profitability of the project": "عالم الاستيراد والتجارة الدولية مليء بالتفاصيل التي قد تبدو بسيطة لكنها تؤثر بشكل مباشر على نجاح الشحنة وربحية المشروع",
    "We are preparing more useful tips and experiences": "نقوم بإعداد المزيد من النصائح والتجارب المفيدة",
    "From our long experience...": "من خلال خبرتنا الطويلة...",
    "We share with you the most important tips and practical experiences that help you make the right decisions and avoid costly mistakes in the world of shipping and sourcing from China": "نشارك معكم أهم النصائح والتجارب العملية التي تساعدكم على اتخاذ قرارات صحيحة وتجنب الأخطاء المكلفة في عالم الشحن والتوريد من الصين",
    "Consult Our Experts": "استشر خبراءنا",
    "AL BURAQ – The Captain in China": "البراق – القبطان في الصين",
    "Professional management, complete transparency, and peace of mind at every stage": "إدارة احترافية، وضوح كامل، وراحة بالك في كل مرحلة",
    "Contact Us Now": "تواصل معنا الآن",
    "Need more information?": "هل تحتاج لمزيد من المعلومات؟",
    "Our team is ready to answer all your questions": "فريقنا جاهز للإجابة على جميع استفساراتك",
    
    # === Other common fields handled in previous file ===
    "Dashboard": "لوحة التحكم",
    "Welcome,": "مرحباً،",
    "Manage your account and orders": "إدارة حسابك وطلباتك",
    # ... (other existing keys can be assumed or re-added if space permits)
}

# ENGLISH (Source)
translations_en = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    # English acts as the source, so we map to itself or leave empty. 
    # For completeness/fallback:
    "Home": "Home",
    "About Us": "About Us",
    "Services": "Services",
    "Contact": "Contact",
    # ... mostly self-mapping
}

# FRENCH
translations_fr = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    # General
    "Home": "Accueil",
    "About Us": "À propos",
    "No updates available at this time.": "Aucune mise à jour disponible pour le moment.",
    "Services": "Services",
    "Our Services": "Nos Services",
    "Store": "Boutique",
    "Tracking": "Suivi",
    "FAQ": "FAQ",
    "Contact": "Contact",
    "Login": "Connexion",
    "Logout": "Déconnexion",
    "Profile": "Profil",
    "Quick Links": "Liens rapides",
    "All rights reserved.": "Tous droits réservés.",
    "Made with": "Fait avec",
    "in China": "en Chine",
    "Chat on WhatsApp": "Discuter sur WhatsApp",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "Votre partenaire de confiance pour le commerce international, le sourcing et la logistique de la Chine vers le monde.",
    "Our Telegram Channels": "Nos chaînes Telegram",
    "Coming soon...": "Bientôt disponible...",
    
    # Home
    "AL BURAQ GROUP - International Trade & Logistics": "GROUPE AL BURAQ - Commerce International & Logistique",
    "Your Gateway to": "Votre passerelle vers",
    "Global Trade": "Le Commerce Mondial",
    "Browse Store": "Parcourir la boutique",
    "Track Shipment": "Suivre l'envoi",
    "Years Experience": "Années d'expérience",
    "Products": "Produits",
    "Happy Clients": "Clients satisfaits",
    "Countries Served": "Pays desservis",
    
    # Tracking
    "Estimated Arrival Date": "Date d'arrivée estimée",
    "Packages": "Colis",
    "Weight": "Poids",
    "kg": "kg",
    "Tracking History": "Historique de suivi",
    "Forgot your tracking number?": "Numéro de suivi oublié ?",
    "Contact our support team and we'll help you find your shipment.": "Contactez notre équipe de support et nous vous aiderons à trouver votre envoi.",
    "Shipment delayed?": "Envoi retardé ?",
    "Contact us for updates on any delayed shipments.": "Contactez-nous pour des mises à jour sur les envois retardés.",
    "Need help?": "Besoin d'aide ?",
    "Our team is available 24/7 to help you.": "Notre équipe est disponible 24/7 pour vous aider.",
    "Contact Us": "Contactez-nous",
    
    # Become Agent
    "Join AL BURAQ Agents": "Devenir Agent AL BURAQ",
    "Join the Network of": "Rejoignez le réseau des",
    "AL BURAQ Agents": "Agents AL BURAQ",
    "The Captain in China": "Le Capitaine en Chine",
    "Partnership": "Partenariat",
    "Requirements": "Exigences",
    "Download": "Télécharger",
    "Catalog": "Catalogue",
    "Download Catalog": "Télécharger le catalogue",
    "Are you ready to join?": "Êtes-vous prêt à nous rejoindre ?",
    "Contact Us via WhatsApp": "Contactez-nous via WhatsApp",

    # Services & Tips
    "Available": "Disponible",
    "Countries": "Pays",
    "Tips": "Conseils",
    "and Experiences": "et Expériences",
    "Read More": "Lire la suite",
    "Other": "Autre",
    "All Tips": "Tous les conseils",
    "Import Tips": "Conseils d'importation",
    "Consult Our Experts": "Consultez nos experts",
    "Need more information?": "Besoin de plus d'informations ?",
    "Our team is ready to answer all your questions": "Notre équipe est prête à répondre à toutes vos questions",
}

# CHINESE (Simplified)
translations_zh_hans = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    "Home": "首页",
    "About Us": "关于我们",
    "Services": "服务",
    "Our Services": "我们的服务",
    "Store": "商店",
    "Tracking": "追踪",
    "FAQ": "常见问题",
    "Contact": "联系我们",
    "Login": "登录",
    "Logout": "退出",
    "Profile": "个人资料",
    "Quick Links": "快速链接",
    "All rights reserved.": "版权所有。",
    "Made with": "制作于",
    "in China": "中国",
    "Chat on WhatsApp": "WhatsApp聊天",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "您值得信赖的中国通往世界的国际贸易、采购和物流合作伙伴。",
    "Our Telegram Channels": "我们的 Telegram 频道",
    "Coming soon...": "即将推出...",
    "AL BURAQ GROUP - International Trade & Logistics": "AL BURAQ GROUP - 国际贸易与物流",
    "Your Gateway to": "通往",
    "Global Trade": "全球贸易的门户",
    "Browse Store": "浏览商店",
    "Track Shipment": "追踪货物",
    "Years Experience": "多年经验",
    "Products": "产品",
    "Happy Clients": "满意客户",
    "Countries Served": "服务国家",
    "Estimated Arrival Date": "预计到达日期",
    "Packages": "包裹",
    "Weight": "重量",
    "kg": "公斤",
    "Tracking History": "追踪历史",
    "No updates available at this time.": "目前没有更新。",
    "Forgot your tracking number?": "忘记追踪号码？",
    "Contact our support team and we'll help you find your shipment.": "联系我们的支持团队，我们将帮助您找到您的货物。",
    "Shipment delayed?": "货物延误？",
    "Contact us for updates on any delayed shipments.": "联系我们获取延误货物的最新信息。",
    "Need help?": "需要帮助？",
    "Our team is available 24/7 to help you.": "我们的团队24/7为您提供帮助。",
    "Contact Us": "联系我们",
    "Join AL BURAQ Agents": "加入 AL BURAQ 代理",
    "Join the Network of": "加入网络",
    "AL BURAQ Agents": "AL BURAQ 代理",
    "The Captain in China": "由于中国队长",
    "Partnership": "合作伙伴关系",
    "Requirements": "要求",
    "Download": "下载",
    "Catalog": "目录",
    "Download Catalog": "下载目录",
    "Are you ready to join?": "准备好加入了吗？",
    "Contact Us via WhatsApp": "通过 WhatsApp 联系我们",
    "Available": "可用",
    "Countries": "国家",
    "Tips": "提示",
    "and Experiences": "和经验",
    "Read More": "阅读更多",
    "Other": "其他",
    "All Tips": "所有提示",
    "Import Tips": "进口提示",
    "Consult Our Experts": "咨询我们的专家",
    "Need more information?": "需要更多信息？",
    "Our team is ready to answer all your questions": "我们的团队随时准备回答您的所有问题",
}

# TURKISH
translations_tr = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    "Home": "Anasayfa",
    "About Us": "Hakkımızda",
    "Services": "Hizmetler",
    "Our Services": "Hizmetlerimiz",
    "Store": "Mağaza",
    "Tracking": "Takip",
    "FAQ": "SSS",
    "Contact": "İletişim",
    "Login": "Giriş",
    "Logout": "Çıkış",
    "Profile": "Profil",
    "Quick Links": "Hızlı Bağlantılar",
    "All rights reserved.": "Tüm hakları saklıdır.",
    "Made with": "ile yapıldı",
    "in China": "Çin'de",
    "Chat on WhatsApp": "WhatsApp'ta Sohbet",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "Çin'den dünyaya uluslararası ticaret, tedarik ve lojistik için güvenilir ortağınız.",
    "Our Telegram Channels": "Telegram Kanallarımız",
    "Coming soon...": "Çok yakında...",
    "AL BURAQ GROUP - International Trade & Logistics": "AL BURAQ GRUBU - Uluslararası Ticaret ve Lojistik",
    "Your Gateway to": "Kapınız",
    "Global Trade": "Küresel Ticaret",
    "Browse Store": "Mağazayı Gez",
    "Track Shipment": "Kargo Takibi",
    "Years Experience": "Yıllık Tecrübe",
    "Products": "Ürünler",
    "Happy Clients": "Mutlu Müşteriler",
    "Countries Served": "Hizmet Verilen Ülkeler",
    "Estimated Arrival Date": "Tahmini Varış Tarihi",
    "Packages": "Paketler",
    "Weight": "Ağırlık",
    "kg": "kg",
    "Tracking History": "Takip Geçmişi",
    "No updates available at this time.": "Şu anda güncelleme yok.",
    "Forgot your tracking number?": "Takip numaranızı mı unuttunuz?",
    "Contact our support team and we'll help you find your shipment.": "Destek ekibimizle iletişime geçin, kargonuzu bulmanıza yardımcı olalım.",
    "Shipment delayed?": "Kargo gecikti mi?",
    "Contact us for updates on any delayed shipments.": "Geciken kargolar hakkında bilgi almak için bizimle iletişime geçin.",
    "Need help?": "Yardıma mı ihtiyacınız var?",
    "Our team is available 24/7 to help you.": "Ekibimiz size yardımcı olmak için 7/24 hizmetinizdedir.",
    "Contact Us": "Bize Ulaşın",
    "Join AL BURAQ Agents": "AL BURAQ Acentelerine Katılın",
    "Join the Network of": "Ağına Katılın",
    "AL BURAQ Agents": "AL BURAQ Acenteleri",
    "The Captain in China": "Çin'deki Kaptan",
    "Partnership": "Ortaklık",
    "Requirements": "Gereksinimler",
    "Download": "İndir",
    "Catalog": "Katalog",
    "Download Catalog": "Kataloğu İndir",
    "Are you ready to join?": "Katılmaya hazır mısınız?",
    "Contact Us via WhatsApp": "WhatsApp üzerinden bize ulaşın",
    "Available": "Mevcut",
    "Countries": "Ülkeler",
    "Tips": "İpuçları",
    "and Experiences": "ve Deneyimler",
    "Read More": "Daha Fazla Oku",
    "Other": "Diğer",
    "All Tips": "Tüm İpuçları",
    "Import Tips": "İthalat İpuçları",
    "Consult Our Experts": "Uzmanlarımıza Danışın",
    "Need more information?": "Daha fazla bilgiye mi ihtiyacınız var?",
    "Our team is ready to answer all your questions": "Ekibimiz tüm sorularınızı yanıtlamaya hazır",
}

# SPANISH
translations_es = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    "Home": "Inicio",
    "About Us": "Sobre Nosotros",
    "Services": "Servicios",
    "Our Services": "Nuestros Servicios",
    "Store": "Tienda",
    "Tracking": "Rastreo",
    "FAQ": "Preguntas Frecuentes",
    "Contact": "Contacto",
    "Login": "Iniciar Sesión",
    "Logout": "Cerrar Sesión",
    "Profile": "Perfil",
    "Quick Links": "Enlaces Rápidos",
    "All rights reserved.": "Todos los derechos reservados.",
    "Made with": "Hecho con",
    "in China": "en China",
    "Chat on WhatsApp": "Chatear en WhatsApp",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "Su socio de confianza para el comercio internacional, compras y logística desde China al mundo.",
    "Our Telegram Channels": "Nuestros Canales de Telegram",
    "Coming soon...": "Próximamente...",
    "AL BURAQ GROUP - International Trade & Logistics": "GRUPO AL BURAQ - Comercio Internacional y Logística",
    "Your Gateway to": "Su Puerta a",
    "Global Trade": "Comercio Global",
    "Browse Store": "Explorar Tienda",
    "Track Shipment": "Rastrear Envío",
    "Years Experience": "Años de Experiencia",
    "Products": "Productos",
    "Happy Clients": "Clientes Felices",
    "Countries Served": "Países Servidos",
    "Estimated Arrival Date": "Fecha Estimada de Llegada",
    "Packages": "Paquetes",
    "Weight": "Peso",
    "kg": "kg",
    "Tracking History": "Historial de Rastreo",
    "No updates available at this time.": "No hay actualizaciones disponibles en este momento.",
    "Forgot your tracking number?": "¿Olvidó su número de rastreo?",
    "Contact our support team and we'll help you find your shipment.": "Contacte a nuestro equipo de soporte y le ayudaremos a encontrar su envío.",
    "Shipment delayed?": "¿Envío retrasado?",
    "Contact us for updates on any delayed shipments.": "Contáctenos para actualizaciones sobre envíos retrasados.",
    "Need help?": "¿Necesita ayuda?",
    "Our team is available 24/7 to help you.": "Nuestro equipo está disponible 24/7 para ayudarle.",
    "Contact Us": "Contáctenos",
    "Join AL BURAQ Agents": "Únase a los Agentes de AL BURAQ",
    "Join the Network of": "Únase a la Red de",
    "AL BURAQ Agents": "Agentes de AL BURAQ",
    "The Captain in China": "El Capitán en China",
    "Partnership": "Asociación",
    "Requirements": "Requisitos",
    "Download": "Descargar",
    "Catalog": "Catálogo",
    "Download Catalog": "Descargar Catálogo",
    "Are you ready to join?": "¿Estás listo para unirte?",
    "Contact Us via WhatsApp": "Contáctenos vía WhatsApp",
    "Available": "Disponible",
    "Countries": "Países",
    "Tips": "Consejos",
    "and Experiences": "y Experiencias",
    "Read More": "Leer Más",
    "Other": "Otro",
    "All Tips": "Todos los Consejos",
    "Import Tips": "Consejos de Importación",
    "Consult Our Experts": "Consulte a Nuestros Expertos",
    "Need more information?": "¿Necesita más información?",
    "Our team is ready to answer all your questions": "Nuestro equipo está listo para responder a todas sus preguntas",
}

# ITALIAN
translations_it = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    "Home": "Home",
    "About Us": "Chi Siamo",
    "Services": "Servizi",
    "Our Services": "I Nostri Servizi",
    "Store": "Negozio",
    "Tracking": "Tracciamento",
    "FAQ": "FAQ",
    "Contact": "Contatti",
    "Login": "Accedi",
    "Logout": "Esci",
    "Profile": "Profilo",
    "Quick Links": "Link Rapidi",
    "All rights reserved.": "Tutti i diritti riservati.",
    "Made with": "Fatto con",
    "in China": "in Cina",
    "Chat on WhatsApp": "Chatta su WhatsApp",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "Il tuo partner di fiducia per il commercio internazionale, il sourcing e la logistica dalla Cina al mondo.",
    "Our Telegram Channels": "I Nostri Canali Telegram",
    "Coming soon...": "Prossimamente...",
    "AL BURAQ GROUP - International Trade & Logistics": "GRUPPO AL BURAQ - Commercio Internazionale e Logistica",
    "Your Gateway to": "La tua porta per",
    "Global Trade": "Commercio Globale",
    "Browse Store": "Sfoglia Negozio",
    "Track Shipment": "Traccia Spedizione",
    "Years Experience": "Anni di Esperienza",
    "Products": "Prodotti",
    "Happy Clients": "Clienti Soddisfatti",
    "Countries Served": "Paesi Serviti",
    "Estimated Arrival Date": "Data di Arrivo Stimata",
    "Packages": "Pacchi",
    "Weight": "Peso",
    "kg": "kg",
    "Tracking History": "Cronologia Tracciamento",
    "No updates available at this time.": "Nessun aggiornamento disponibile al momento.",
    "Forgot your tracking number?": "Hai dimenticato il numero di tracciamento?",
    "Contact our support team and we'll help you find your shipment.": "Contatta il nostro team di supporto e ti aiuteremo a trovare la tua spedizione.",
    "Shipment delayed?": "Spedizione in ritardo?",
    "Contact us for updates on any delayed shipments.": "Contattaci per aggiornamenti su eventuali spedizioni in ritardo.",
    "Need help?": "Hai bisogno di aiuto?",
    "Our team is available 24/7 to help you.": "Il nostro team è disponibile 24/7 per aiutarti.",
    "Contact Us": "Contattaci",
    "Join AL BURAQ Agents": "Unisciti agli Agenti AL BURAQ",
    "Join the Network of": "Unisciti alla Rete di",
    "AL BURAQ Agents": "Agenti AL BURAQ",
    "The Captain in China": "Il Capitano in Cina",
    "Partnership": "Partnership",
    "Requirements": "Requisiti",
    "Download": "Scarica",
    "Catalog": "Catalogo",
    "Download Catalog": "Scarica Catalogo",
    "Are you ready to join?": "Sei pronto a unirti?",
    "Contact Us via WhatsApp": "Contattaci via WhatsApp",
    "Available": "Disponibile",
    "Countries": "Paesi",
    "Tips": "Suggerimenti",
    "and Experiences": "ed Esperienze",
    "Read More": "Leggi di più",
    "Other": "Altro",
    "All Tips": "Tutti i Suggerimenti",
    "Import Tips": "Suggerimenti per l'Importazione",
    "Consult Our Experts": "Consulta i Nostri Esperti",
    "Need more information?": "Hai bisogno di maggiori informazioni?",
    "Our team is ready to answer all your questions": "Il nostro team è pronto a rispondere a tutte le tue domande",
}

# RUSSIAN
translations_ru = {
    "": "Content-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n",
    "Home": "Главная",
    "About Us": "О нас",
    "Services": "Услуги",
    "Our Services": "Наши услуги",
    "Store": "Магазин",
    "Tracking": "Отслеживание",
    "FAQ": "FAQ",
    "Contact": "Контакты",
    "Login": "Войти",
    "Logout": "Выйти",
    "Profile": "Профиль",
    "Quick Links": "Быстрые ссылки",
    "All rights reserved.": "Все права защищены.",
    "Made with": "Сделано с",
    "in China": "в Китае",
    "Chat on WhatsApp": "Чат в WhatsApp",
    "Your trusted partner for international trade, sourcing, and logistics from China to the world.": "Ваш надежный партнер по международной торговле, закупкам и логистике из Китая в мир.",
    "Our Telegram Channels": "Наши Telegram каналы",
    "Coming soon...": "Скоро...",
    "AL BURAQ GROUP - International Trade & Logistics": "AL BURAQ GROUP - Международная торговля и логистика",
    "Your Gateway to": "Ваши ворота в",
    "Global Trade": "Глобальную торговлю",
    "Browse Store": "Обзор магазина",
    "Track Shipment": "Отследить груз",
    "Years Experience": "Лет опыта",
    "Products": "Продукты",
    "Happy Clients": "Довольные клиенты",
    "Countries Served": "Обслуживаемые страны",
    "Estimated Arrival Date": "Ожидаемая дата прибытия",
    "Packages": "Посылки",
    "Weight": "Вес",
    "kg": "кг",
    "Tracking History": "История отслеживания",
    "No updates available at this time.": "В настоящее время обновлений нет.",
    "Forgot your tracking number?": "Забыли номер отслеживания?",
    "Contact our support team and we'll help you find your shipment.": "Свяжитесь с нашей службой поддержки, и мы поможем вам найти ваш груз.",
    "Shipment delayed?": "Груз задерживается?",
    "Contact us for updates on any delayed shipments.": "Свяжитесь с нами для получения обновлений по задержанным грузам.",
    "Need help?": "Нужна помощь?",
    "Our team is available 24/7 to help you.": "Наша команда доступна 24/7, чтобы помочь вам.",
    "Contact Us": "Свяжитесь с нами",
    "Join AL BURAQ Agents": "Присоединяйтесь к агентам AL BURAQ",
    "Join the Network of": "Присоединяйтесь к сети",
    "AL BURAQ Agents": "Агенты AL BURAQ",
    "The Captain in China": "Капитан в Китае",
    "Partnership": "Партнерство",
    "Requirements": "Требования",
    "Download": "Скачать",
    "Catalog": "Каталог",
    "Download Catalog": "Скачать каталог",
    "Are you ready to join?": "Вы готовы присоединиться?",
    "Contact Us via WhatsApp": "Свяжитесь с нами через WhatsApp",
    "Available": "Доступно",
    "Countries": "Страны",
    "Tips": "Советы",
    "and Experiences": "и опыт",
    "Read More": "Читать далее",
    "Other": "Другое",
    "All Tips": "Все советы",
    "Import Tips": "Советы по импорту",
    "Consult Our Experts": "Проконсультируйтесь с нашими экспертами",
    "Need more information?": "Нужна дополнительная информация?",
    "Our team is ready to answer all your questions": "Наша команда готова ответить на все ваши вопросы",
}

if __name__ == "__main__":
    import os
    
    # List of languages and their dictionaries
    langs = [
        ('ar', translations_ar),
        ('en', translations_en),
        ('fr', translations_fr),
        ('zh-hans', translations_zh_hans),
        ('tr', translations_tr),
        ('es', translations_es),
        ('it', translations_it),
        ('ru', translations_ru),
    ]

    base_dir = os.getcwd()
    
    for lang_code, translation_dict in langs:
        # Create directory if it doesn't exist
        locale_dir = os.path.join(base_dir, 'locale', lang_code, 'LC_MESSAGES')
        os.makedirs(locale_dir, exist_ok=True)
        
        # Output .mo file
        output_file = os.path.join(locale_dir, 'django.mo')
        output_mofile(translation_dict, output_file)
        
        print(f"Compiled translations for {lang_code} to {output_file}")
