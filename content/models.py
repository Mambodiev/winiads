from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.signals import user_logged_in
from django.utils.text import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from allauth.account.signals import email_confirmed
import stripe
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import mark_safe
from cloudinary.models import CloudinaryField


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()
    
    
# stripe.api_key = settings.STRIPE_SECRET_KEY

User = get_user_model()

class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium
    slug = models.SlugField()
    stripe_price_id = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pricings"


class Subscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

    @property
    def is_active(self):
        return self.status == "active" or self.status == "trialing"

    class Meta:
        verbose_name_plural = "3 Subscriptions"


class Category(models.Model):
    CATEGORIES_CHOICES = (
        ('Home Appliances', 'Home Appliances'),
        ('Computer and Office', 'Computer and Office'),
        ('Home & Garden', 'Home & Garden'),
        ('Sports & Entertainment', 'Sports & Entertainment'),
        ('Education & Office Supplies', 'Education & Office Supplies'),
        ('Toys & Hobbies', 'Toys & Hobbies'),
        ('Security & Protection', 'Security & Protection'),
        ('Automobiles & Motorcycles', 'Automobiles & Motorcycles'),
        ('Lights & Lighting', 'Lights & Lighting'),
        ('Consumer Electronics', 'Consumer Electronics'),
        ('Beauty & Health', 'Beauty & Health'),
        ('Shoes', 'Shoes'),
        ('Luggage & Bags', 'Luggage & Bags'),
        ('Electronic Components & Supplies', 'Electronic Components & Supplies'),
        ('Tools', 'Tools'),
        (' Mother & Kids', ' Mother & Kids'),
        ('Furniture', 'Furniture'),
        ('Jewelry & Accessories', 'Jewelry & Accessories'),
        ('Watches', 'Watches'),
        ('Hair Extensions and Wigs', 'Hair Extensions and Wigs'),
        ('Virtual Goods', 'Virtual Goods'),
        ('Novelty and Special Use', 'Novelty and Special Use'),
        ('Weddings and Events', 'Weddings and Events'),
        ('Women’s Clothing', 'Women’s Clothing'),
        ('Men’s Clothing', 'Men’s Clothing'),
        ('Apparel Accessories', 'Apparel Accessories'),
        ('Underwear and Sleepwears', 'Underwear and Sleepwears'),
        ('Cellphones & Telecommunications', 'Cellphones & Telecommunications'),
    )

    name = models.CharField(choices=CATEGORIES_CHOICES, max_length=100, default='Beauty & Health')   
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    COUNTRIES_CHOICES = [
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True,choices=COUNTRIES_CHOICES, default='United States')
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False, null=True, blank=True)
    
   
    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"


class Product(models.Model):
    SITE_TYPE_CHOICES = (
        (0, 'facebook'),
        (1, 'instagram'),
        (2, 'pinterest'),
    )
    draft_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    technologies_choices = [
        ('shopify', 'Shopify'),
        ('wooCommerce', 'WooCommerce'),
        ('cart functionality', 'Cart Functionality'),
        ('magento', 'magento'),
        ('salesforce commerce cloud', 'Salesforce Commerce Cloud'),
        ('prestashop', 'PrestaShop'),
        ('vtex', 'VTEX'),
        ('bigcommerce', 'Bigcommerce'),
        ('ibm websphere commerce', 'IBM Websphere Commerce'),
        ('sap commerce cloud', 'SAP Commerce Cloud'),
        ('shopware', 'Shopware'),
        ('shoptet', 'Shoptet'),
        ('opencart', 'OpenCart'),
        ('nopcommerce', 'nopcommerce'),
        ('oracle commerce', 'Oracle Commerce'),
        ('intershop', 'Intershop'),
        ('hybris', 'Hybris'),
        ('zen cart', 'Zen Cart'),
        ('oracle commerce cloud', 'Oracle Commerce Cloud'),
        ('lightspeed ecom', 'Lightspeed eCom'),
        ('epages', 'EPages'),
        ('cloudcart', 'CloudCart'),
        ('kajabi', 'Kajabi'),
        ('loja integrada', 'Loja Integrada'),
        ('oxid eshop', 'OXID eShop'),
        ('riskified', 'Riskified'),
        ('x-cart', 'X-Cart'),
        ('commerce server', 'Commerce Server'),
        ('drupal commerce', 'Drupal Commerce'),
        ('oscommerce', 'osCommerce'),
        ('91app', '91App'),
        ('nuvemshop', 'Nuvemshop'),
        ('mycashflow', 'Mycashflow'),
        ('ticimax', 'Ticimax'),
        ('ecwid', 'Ecwid'),
        ('gambio', 'Gambio'),
        ('craft commerce', 'Craft Commerce'),
        ('ideasoft', 'Ideasoft'),
        ('ceres', 'Ceres'),
        ('t-soft', 'T-Soft'),
        ('storeden', 'Storeden'),
        ('vtex integrated store', 'VTEX Integrated Store'),
        ('ccv shop', 'CCV Shop'),
        ('big cartel', 'Big Cartel'),
        ('miva', 'Miva'),
        ('irroba', 'Irroba'),
        ('volusion', 'Volusion'),
        ('yepcomm', 'Yepcomm'),
        ('xtcommerce', 'xtCommerce'),
        ('ec-cube', 'EC-CUBE'),
    ]
    option_ads = [
        ('faceBook', 'FaceBook'),
        ('instagram', 'Instagram'),
        ('tiktok', 'Tiktok'),
    ]
    option_ads_type = [
        ('video', 'Video'),
        ('photo', 'Photo'),
        ('both', 'Both'),
    ]
    gender_options = [
        ('male or Female', 'Male or Female'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    option_language = [
        ('english', 'English'),
        ('armenian', 'Armenian'),
        ('belarusian', 'Belarusian'),
        ('bengali', 'Bengali'),
        ('bosnia', 'Bosnia'),
        ('bulgarian', 'Bulgarian'),
        ('bumese', 'Bumese'),
        ('catalan', 'Catalan'),
        ('central Kurdish', 'Central Kurdish'),
        ('croatian', 'Croatian'),
        ('czech', 'Czech'),
        ('danish', 'Danish'),
        ('dutch', 'Dutch'),
        ('estonian', 'Estonian'),
        ('finnish', 'Finnish'),
        ('french', 'French'),
        ('georgian', 'Georgian'),
        ('german', 'German'),
        ('gujarati', 'Gujarati'),
        ('haitian', 'Haitian'),
        ('hebrew', 'Hebrew'),
        ('hindi', 'Hindi'),
        ('hungarian', 'Hungarian'),
        ('indonesian', 'Indonesian'),
        ('italian', 'Italian'),
        ('japanese', 'Japanese'),
        ('javanese', 'Javanese'),
        ('kannada', 'Kannada'),
        ('kazakh', 'Kazakh'),
        ('khmer', 'Khmer'),
        ('korean', 'Korean'),
        ('latvian', 'Latvian'),
        ('lithuanian', 'Lithuanian'),
        ('maithili', 'Maithili'),
        ('malay', 'Malay'),
        ('malayalam', 'Malayalam'),
        ('mandarin Chinese', 'Mandarin Chinese'),
        ('marathi', 'Marathi'),
        ('modern Greek', 'Modern Greek'),
        ('nepali', 'Nepali'),
        ('north Azerbaijani', 'North Azerbaijani'),
        ('northern Uzbek', 'Northern Uzbek'),
        ('norwegian bokmål', 'Norwegian bokmål'),
        ('norwegian Nynorsk', 'Norwegian Nynorsk'),
        ('oriya', 'Oriya'),
        ('persian', 'Persian'),
        ('polish', 'Polish'),
        ('portuguese', 'Portuguese'),
        ('romanian', 'Romanian'),
        ('russian', 'Russian'),
        ('Serbian', 'Serbian'),
        ('slovak', 'Slovak'),
        ('slovenian', 'Slovenian'),
        ('somali', 'Somali'),
        ('spanish', 'Spanish'),
        ('sudanese', 'Sudanese'),
        ('swahili', 'Swahili'),
        ('swedish', 'Swedish'),
        ('tagalog', 'Tagalog'),
        ('tajik', 'Tajik'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('thai', 'Thai'),
        ('tibetan', 'Tibetan'),
        ('turkish', 'Turkish'),
        ('turkmen', 'Turkmen'),
        ('uighur', 'Uighur'),
        ('ukrainian', 'Ukrainian'),
        ('urdu', 'Urdu'),
        ('vietnamese', 'Vietnamese'),
    ]
    option_button = [
        ('buy now', 'Buy Now'),
        ('shop now', 'Shop Now'),
        ('learn more', 'Learn More'),
        ('Grab Yours', 'Grab Yours'),
        ('sign up', 'Sign Up'),
        ('send message', 'Send Message'),
        ('book now', 'Book Now'),
        ('install now', 'Install Now'),
        ('get directions', 'Get Directions'),
        ('watch more', 'Watch More'),
        ('view', 'View'),
        ('apply now', 'Apply Now'),
        ('like this page', 'Like This Page'),
        ('download', 'Download'),
        ('get offer', 'Get Offer'),
        ('get tickets', 'Get Tickets'),
        ('play game', 'Play Game'),
        ('try it', 'Try It'),
        ('contact us', 'Contact Us'),
        ('send whatsapp message', 'Send Whatsapp Message'),
        ('get quote', 'Get Quote'),
        ('call now', 'Call Now'),
        ('donate now', 'Donate Now'),
        ('buy tickets', 'Buy Tickets'),
        ('listen now', 'Listen Now'),
        ('subscribe', 'Subscribe'),
        ('get show times', 'Get Show Times'),
        ('view event', 'View Event'),
        ('see menu', 'See Menu'),
        ('read', 'Read'),
        ('use app', 'Use App'),
        ('order now', 'Order Now'),
        ('request time', 'Request Time'),
        ('join', 'Join'),
        ('open link', 'Open Link'),
        ('start order', 'Start Order'),
        ('install app', 'Install App'),
        ('get your code', 'Get Your Code'),
        ('see more', 'See More'),
        ('play now', 'Play Now'),
        ('see details', 'See Details'),
        ('open camera', 'Open Camera'),
        ('sell now', 'Sell Now'),
        ('buy', 'Buy'),
        ('about this website', 'About This Website'),
        ('messsage', 'Messsage'),
        ('follow', 'Follow'),
        ('try it', 'Try it'),
        ('like page', 'Like Page'),
        ('donate', 'Donate'),
        ('watch video', 'Watch Video'),
        ('visit website', 'Visit Website'),
        ('register now', 'Register Now'),
        ('email now', 'Email Now'),
        ('use offer', 'Use Offer'),
        ('add to profil', 'Add To Profil'),
        ('turn on', 'Turn On'),
        ('invite friends', 'Invite Friends'),
        ('see more', 'see more'),
        ('visit instagram profile', 'Visit Instagram Profile'),
        ('go live', 'go live'),
        ('add to cart', 'Add To Cart'),
        ('vote now', 'Vote Now'),
        ('intrested', 'Intrested'),
        ('see all events', 'See All Events'),
        ('save', 'Save'),
        ('search', 'Search'),
        ('remind me', 'Remind Me'),
        ('watch yours', 'Watch Yours'),
        ('save offer', 'Save Offer'),
        ('get deal', 'Get Deal'),
        ('get reminded', 'Get Reminded'),
        ('book test drive', 'Book Test Drive'),
        ('call', 'Call'),
    ]
    countries_choices = [
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    categories_choices = (
        ('Tools & Home Improvement', 'tools & home improvement'),
        ("Women's Fashion", "women's fashion"),
        ("Men's Fashion", "men's fashion"),
        ('Phones & Telecommunications', 'phones & telecommunications'),
        ('Computer, Office & Security', 'computer, office & security'),
        ('Consumer Electronics', 'consumer electronics'),
        ('Jewelry & Watches', 'jewelry & watches'),
        ('Home, Pet & Appliances', 'home, pet & appliances'),
        ('Bags & Shoes', 'bags & shoes'),
        ('Toys , Kids & Babies', 'toys , kids & babies'),
        ('Outdoor Fun & Sports', 'outdoor fun & sports'),
        ('Beauty, Health & Hair', 'beauty, health & hair'),
        ('Automobiles & Motorcycles', 'automobiles & motorcycles'),
        ('Home & Garden', 'home & garden'),
        ('Sports & Entertainment', 'sports & entertainment')
        
    )
    ship_from_choices = [
        ('Afghanistan', 'Afghanistan'),
        ('Aland Islands', 'Aland Islands'),
        ('Albania', 'Albania'),
        ('Aldemey', 'Aldemey'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armemia', 'Armemia'),
        ('Aruba', 'Aruba'),
        ('Ascension Island', 'Ascension Island'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Virgin Islands(British)', 'Virgin Islands(British)'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cap Verte', 'Cap Verte'),
        ('Caribbean Netherlands', 'Caribbean Netherlands'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Cental African Republic', 'Cental African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'),
        ('Costa Rica', 'Costa Rica'),
        ('Côte d’Ivoire', 'Côte d’Ivoire'),
        ('Croatia', 'Croatia'),
        ('Curacao', 'Curacao'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica Dominican Republic', 'Dominica Dominican Republic'),
        ('East Timor (Timor-Leste)', 'East Timor (Timor-Leste)'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkand Islands(Malvinas)', 'Falkand Islands(Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('The Gambia', 'The Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guan', 'Guan'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('French Guyana', 'French Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Hong Kong, China', 'Hong Kong, China'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea', 'Korea'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ("Laos People's Democratic Republic", "Laos People's Democratic Republic"),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao(China)', 'Macao(China)'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar (Burma)', 'Myanmar (Burma)'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Islands', 'Norfolk Islands'),
        ('North Macedonia', 'North Macedonia'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Other Country', 'Other Country'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Moldova', 'Moldova'),
        ('Romania', 'Romania'),
        ('Russia Federation', 'Russia Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Barthelemy', 'Saint Barthelemy'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Martin', 'Saint Martin'),
        ('St Pierre and Miquelon', 'St Pierre and Miquelon'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Sint Maarten', 'Sint Maarten'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Sudan, South', 'Sudan, South'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Taiwan, China', 'Taiwan, China'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Mainland, China', 'Mainland, China'),
    ]
    pricing_tiers = models.ManyToManyField(Pricing, blank=True)
    name_of_product = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    shopify_price = models.DecimalField(max_digits=10, decimal_places=2, help_text = "Product price from shopify")
    shopify_links = models.TextField(blank=True, null=True, help_text = "A link that will take to a single the store")
    links_to_ads = models.TextField(blank=True, null=True, help_text = "A link that will take to ads")
    # name_of_store = models.ForeignKey(Store, related_name='store_name', blank=True, null=True, on_delete=models.PROTECT)
    categories = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    product_thumbnail = CloudinaryField('image', default='https://res.cloudinary.com/dvc5exd3c/image/upload/v1694866008/Image-Coming-Soon_rsuykv.png')
    video_links = models.TextField( blank=True, null=True)
    aliexpress_price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, help_text = "Product price from aliexpress")
    aliexpress_order = models.IntegerField(default=0, help_text = "Amount of aliexpress order generated")
    countries = models.CharField(max_length=250, blank=True, null=True, choices=countries_choices, default='United States')
    categories = models.CharField(max_length=250, blank=True, null=True, choices=categories_choices, default='tools & home improvement')
    ship_from = models.CharField(max_length=250, blank=True, null=True, choices=ship_from_choices, default='Hong Kong, China')
    ads_type = models.CharField(max_length=250, blank=True, null=True, choices=option_ads_type, default='video')
    gender = models.CharField(max_length=250, blank=True, null=True, choices=gender_options, default='male or Female')
    technology = models.CharField(max_length=250, blank=True, null=True, choices=technologies_choices, default='shopify')
    language= models.CharField(max_length=250, blank=True, null=True, choices=option_language, default='english')
    button = models.CharField(max_length=250, blank=True, null=True, choices=option_button, default='buy now')
    facebook_like = models.IntegerField(default=0, help_text = "Amount of facebook like")
    facebook_comment = models.IntegerField(default=0, help_text = "Amount of comment generated")
    facebook_views = models.IntegerField(default=0, help_text = "Amount of views generated")
    facebook_shares = models.IntegerField(blank=True, null=True, default=0, help_text = "Amount of shares generated")
    facebook_love = models.IntegerField(default=0, help_text = "Amount of facebook love")
    facebook_wow = models.IntegerField(default=0, help_text = "Amount of facebook wow")
    facebook_care = models.IntegerField(default=0, help_text = "Amount of facebook care")
    facebook_angry = models.IntegerField(default=0, help_text = "Amount of facebook angry")
    facebook_haha = models.IntegerField(default=0, help_text = "Amount of facebook haha")
    facebook_sad = models.IntegerField(default=0, help_text = "Amount of facebook sad")
    # links_to_others_stores = RichTextUploadingField(blank=True, null=True,help_text = "A link that will take to the store", )
    # links_to_others_suppliers = RichTextUploadingField(blank=True, null=True,)
    text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    read_more_text_that_comes_with_ads = RichTextUploadingField(blank=True, null=True)
    number_of_store_selling = models.IntegerField(default=0, help_text = "Amount of store selling the product", blank=True)
    number_of_suppliers_selling= models.IntegerField( default=0, help_text = "Amount of suppliers selling the product")
    created_at = models.DateField(default=timezone.now)
    is_faceBook = models.BooleanField(default=False)
    is_pinterest = models.BooleanField(default=False)
    is_tiktok = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    has_photo = models.BooleanField(default=True)
    product_status = models.CharField(max_length=10, choices=draft_options, default='draft')
    price_margin = models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text = "Profit you get from this product")
    updated_at = AutoDateTimeField(default=timezone.now)
    aliexpress_total_sale = models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text = "Amount of aliexpress sale generated")
    site_type = models.IntegerField(choices=SITE_TYPE_CHOICES, default=0)    
    first_related_post = models.ForeignKey(
        'self', related_name='first_related', on_delete=models.SET_NULL, blank=True, null=True)
    second_related_post = models.ForeignKey(
        'self', related_name='second_related', on_delete=models.SET_NULL, blank=True, null=True)
    third_related_post = models.ForeignKey(
        'self', related_name='third_related', on_delete=models.SET_NULL, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("content:product-detail", kwargs={"slug": self.slug})
    
    def get_update_url(self):
        return reverse("staff:product-update", kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse("staff:product-delete", kwargs={'pk': self.pk})


    @property
    def imageURL(self):
        try:
            url = self.image_store.url
        except:
            url = ''
        print('URL:', url)
        return url

    def __str__(self):
        return f'{self.name_of_product} (${self.aliexpress_price})' 
    

    def save(self, *args, **kwargs):
         
        self.price_margin = self.shopify_price - self.aliexpress_price 

        self.aliexpress_total_sale = self.aliexpress_order * self.shopify_price

        super().save(*args, **kwargs)

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.product_thumbnail.url}" width = "50"/>')
        
    img_preview.short_description = 'Product Image'
    img_preview.allow_tags = True


    def __str__(self):
        return self.name_of_product

    def get_absolute_url(self):
        return reverse("content:product-detail", kwargs={"slug": self.slug})

    class Meta:
            verbose_name_plural = "1. Products" 
            ordering = ["-updated_at"]


class OrderItem(models.Model):
    order = models.ForeignKey(
        "Order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    updated_at = AutoDateTimeField(default=timezone.now)

    
    
class OtherShopifyLinks(models.Model):
    countries_choices = [
        ('United States', 'United States'),
        ('United Kingdom', 'United Kingdom'),
        ('Canada', 'Canada'),
        ('Australia', 'Australia'),
        ('New Zealand', 'New Zealand'),
        ('Sweden', 'Sweden'),
        ('Denmark', 'Denmark'),
        ('Iceland', 'Iceland'),
        ('Norway', 'Norway'),
        ('Finland', 'Finland'),
        ('The Netherlands', 'The Netherlands'),
        ('Ireland', 'Ireland'),
        ('Germany', 'Germany'),
        ('South Korea', 'South Korea'),
        ('Switzerland', 'Switzerland'),
        ('Belgium', 'Belgium'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('France', 'France'),
        ('Spain', 'Spain'),
        ('Portugal', 'Portugal'),
        ('Austria', 'Austria'),
        ('Hungary', 'Hungary'),
        ('Poland', 'Poland'),
        ('Czech Republic', 'Czech Republic'),
        ('UAE', 'UAE'),
        ('South Africa', 'South Africa'),
        ('The Philippines', 'The Philippines'),
        ('Japan', 'Japan'),
        ('Singapore', 'Singapore'),
        ('Argentina', 'Argentina'),
        ('Mexico', 'Mexico'),
    ]
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    link =models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the Other Shopify Links")
    name = models.CharField(max_length=100)   
    countries = models.CharField(max_length=250, blank=True, null=True, choices=countries_choices, default='United States')
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = "Other Shopify Links"
    def __str__(self):
        return self.name

class Store(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, blank=True, null=True,)
    name = models.CharField(max_length=100)
    store_links =models.TextField(blank=True, null=True, help_text = "link that will take to ads")
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)    
        
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Stores" 


    
class OtherAliexpressSuppliersLinks(models.Model):
    supply_country_choices = [
        ('Hong Kong, China', 'Hong Kong, China'),
        ('Afghanistan', 'Afghanistan'),
        ('Aland Islands', 'Aland Islands'),
        ('Albania', 'Albania'),
        ('Aldemey', 'Aldemey'),
        ('Algeria', 'Algeria'),
        ('American Samoa', 'American Samoa'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antigua and Barbuda', 'Antigua and Barbuda'),
        ('Argentina', 'Argentina'),
        ('Armemia', 'Armemia'),
        ('Aruba', 'Aruba'),
        ('Ascension Island', 'Ascension Island'),
        ('Australia', 'Australia'),
        ('Austria', 'Austria'),
        ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'),
        ('Bahrain', 'Bahrain'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'),
        ('Belize', 'Belize'),
        ('Benin', 'Benin'),
        ('Bermuda', 'Bermuda'),
        ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'),
        ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'),
        ('Botswana', 'Botswana'),
        ('Brazil', 'Brazil'),
        ('Virgin Islands(British)', 'Virgin Islands(British)'),
        ('Brunei', 'Brunei'),
        ('Bulgaria', 'Bulgaria'),
        ('Burkina Faso', 'Burkina Faso'),
        ('Burundi', 'Burundi'),
        ('Cambodia', 'Cambodia'),
        ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'),
        ('Cap Verte', 'Cap Verte'),
        ('Caribbean Netherlands', 'Caribbean Netherlands'),
        ('Cayman Islands', 'Cayman Islands'),
        ('Cental African Republic', 'Cental African Republic'),
        ('Chad', 'Chad'),
        ('Chile', 'Chile'),
        ('Christmas Island', 'Christmas Island'),
        ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'),
        ('Colombia', 'Colombia'),
        ('Comoros', 'Comoros'),
        ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'),
        ('Costa Rica', 'Costa Rica'),
        ('Côte d’Ivoire', 'Côte d’Ivoire'),
        ('Croatia', 'Croatia'),
        ('Curacao', 'Curacao'),
        ('Cyprus', 'Cyprus'),
        ('Czech Republic', 'Czech Republic'),
        ('Denmark', 'Denmark'),
        ('Djibouti', 'Djibouti'),
        ('Dominica Dominican Republic', 'Dominica Dominican Republic'),
        ('East Timor (Timor-Leste)', 'East Timor (Timor-Leste)'),
        ('Ecuador', 'Ecuador'),
        ('Egypt', 'Egypt'),
        ('El Salvador', 'El Salvador'),
        ('Equatorial Guinea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'),
        ('Estonia', 'Estonia'),
        ('Ethiopia', 'Ethiopia'),
        ('Falkand Islands(Malvinas)', 'Falkand Islands(Malvinas)'),
        ('Faroe Islands', 'Faroe Islands'),
        ('Fiji', 'Fiji'),
        ('Finland', 'Finland'),
        ('France', 'France'),
        ('Gabon', 'Gabon'),
        ('The Gambia', 'The Gambia'),
        ('Georgia', 'Georgia'),
        ('Germany', 'Germany'),
        ('Gibraltar', 'Gibraltar'),
        ('Greece', 'Greece'),
        ('Grenada', 'Grenada'),
        ('Guan', 'Guan'),
        ('Guatemala', 'Guatemala'),
        ('Guernsey', 'Guernsey'),
        ('Guinea', 'Guinea'),
        ('Guinea-Bissau', 'Guinea-Bissau'),
        ('Guyana', 'Guyana'),
        ('French Guyana', 'French Guyana'),
        ('Haiti', 'Haiti'),
        ('Honduras', 'Honduras'),
        ('Hungary', 'Hungary'),
        ('Iceland', 'Iceland'),
        ('India', 'India'),
        ('Indonesia', 'Indonesia'),
        ('Iraq', 'Iraq'),
        ('Ireland', 'Ireland'),
        ('Israel', 'Israel'),
        ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'),
        ('Japan', 'Japan'),
        ('Jersey', 'Jersey'),
        ('Jordan', 'Jordan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'),
        ('Korea', 'Korea'),
        ('Kosovo', 'Kosovo'),
        ('Kuwait', 'Kuwait'),
        ('Kyrgyzstan', 'Kyrgyzstan'),
        ("Laos People's Democratic Republic", "Laos People's Democratic Republic"),
        ('Latvia', 'Latvia'),
        ('Lebanon', 'Lebanon'),
        ('Lesotho', 'Lesotho'),
        ('Liberia', 'Liberia'),
        ('Libya', 'Libya'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lithuania', 'Lithuania'),
        ('Luxembourg', 'Luxembourg'),
        ('Macao(China)', 'Macao(China)'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Malaysia', 'Malaysia'),
        ('Maldives', 'Maldives'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marshall Islands', 'Marshall Islands'),
        ('Martinique', 'Martinique'),
        ('Mauritania', 'Mauritania'),
        ('Mauritius', 'Mauritius'),
        ('Mayotte', 'Mayotte'),
        ('Mexico', 'Mexico'),
        ('Micronesia', 'Micronesia'),
        ('Monaco', 'Monaco'),
        ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'),
        ('Montserrat', 'Montserrat'),
        ('Morocco', 'Morocco'),
        ('Mozambique', 'Mozambique'),
        ('Myanmar (Burma)', 'Myanmar (Burma)'),
        ('Namibia', 'Namibia'),
        ('Nauru', 'Nauru'),
        ('Nepal', 'Nepal'),
        ('Netherlands', 'Netherlands'),
        ('Netherlands Antilles', 'Netherlands Antilles'),
        ('New Caledonia', 'New Caledonia'),
        ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'),
        ('Niger', 'Niger'),
        ('Nigeria', 'Nigeria'),
        ('Niue', 'Niue'),
        ('Norfolk Islands', 'Norfolk Islands'),
        ('North Macedonia', 'North Macedonia'),
        ('Norway', 'Norway'),
        ('Oman', 'Oman'),
        ('Other Country', 'Other Country'),
        ('Pakistan', 'Pakistan'),
        ('Palau', 'Palau'),
        ('Panama', 'Panama'),
        ('Papua New Guinea', 'Papua New Guinea'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Philippines', 'Philippines'),
        ('Poland', 'Poland'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Moldova', 'Moldova'),
        ('Romania', 'Romania'),
        ('Russia Federation', 'Russia Federation'),
        ('Rwanda', 'Rwanda'),
        ('Saint Barthelemy', 'Saint Barthelemy'),
        ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'),
        ('Saint Lucia', 'Saint Lucia'),
        ('Saint Martin', 'Saint Martin'),
        ('St Pierre and Miquelon', 'St Pierre and Miquelon'),
        ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'),
        ('San Marino', 'San Marino'),
        ('Sao Tome and Principe', 'Sao Tome and Principe'),
        ('Saudi Arabia', 'Saudi Arabia'),
        ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'),
        ('Seychelles', 'Seychelles'),
        ('Sierra Leone', 'Sierra Leone'),
        ('Singapore', 'Singapore'),
        ('Sint Maarten', 'Sint Maarten'),
        ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'),
        ('Solomon Islands', 'Solomon Islands'),
        ('Somalia', 'Somalia'),
        ('South Africa', 'South Africa'),
        ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'),
        ('Sudan', 'Sudan'),
        ('Sudan, South', 'Sudan, South'),
        ('Suriname', 'Suriname'),
        ('Swaziland', 'Swaziland'),
        ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'),
        ('Taiwan, China', 'Taiwan, China'),
        ('Tajikistan', 'Tajikistan'),
        ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'),
        ('Togo', 'Togo'),
        ('Tonga', 'Tonga'),
        ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('Tunisia', 'Tunisia'),
        ('Turkey', 'Turkey'),
        ('Turkmenistan', 'Turkmenistan'),
        ('Tuvalu', 'Tuvalu'),
        ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('United Kingdom', 'United Kingdom'),
        ('United States', 'United States'),
        ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Vanuatu', 'Vanuatu'),
        ('Vatican City', 'Vatican City'),
        ('Venezuela', 'Venezuela'),
        ('Vietnam', 'Vietnam'),
        ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe'),
        ('Mainland, China', 'Mainland, China'),
    ]
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    link =models.CharField(blank=True, null=True, max_length=500, help_text = "A link that will take to a single the Other Aliexpress Suppliers Links")
    name = models.CharField(max_length=100)   
    created_at = models.DateField(default=timezone.now)
    country= models.CharField(max_length=100, blank=True, null=True, choices=supply_country_choices, default='Hong Kong, China')  
    price= models.DecimalField(default=0, max_digits=10, decimal_places=2, help_text = "Aliexpress price")
    updated_at = AutoDateTimeField(default=timezone.now) 
    class Meta:
        verbose_name_plural = "Other Aliexpress Suppliers Links"
    def __str__(self):
        return self.name
    
    
class AliexpressOrderGrowth(models.Model):

    order_choices = [
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True, choices=order_choices,)

    def __str__(self):
        return  self.name

    class Meta:
            verbose_name_plural = "Aliexpress Order Growth" 


class Gender(models.Model):

    gender_choices = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Unkwon', 'Unknown'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='genders')
    gender_number = models.IntegerField(blank=True, null=True, help_text = "ads gender number group range")
    name = models.CharField(max_length=100, blank=True, null=True,choices=gender_choices, default='Female' )
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    def __str__(self):
        return  self.name


class Age(models.Model):

    age_choices = [
        ('13-17', '13-17'),
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('65+', '65+'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True, help_text = "ads age group range")
    name = models.CharField(max_length=100, blank=True, null=True, choices=age_choices, default='25-34')
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.name) 


class Like(models.Model):

    like_choices = [
        ('Jan', 'Jan'),
        ('Feb', 'Feb'),
        ('Mar', 'Mar'),
        ('Apr', 'Apr'),
        ('May', 'May'),
        ('Jun', 'Jun'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.IntegerField(blank=True, null=True, help_text = "ads like range")
    name = models.CharField(max_length=100, blank=True, null=True, choices=like_choices, default='Jan')
    created_at = models.DateField(default=timezone.now)
    updated_at = AutoDateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.name)
    


class City(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    population = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = ("Cities")

    def __str__(self):
        return self.name
    
    
class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos')
    vimeo_id = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"]    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content:video-detail", kwargs={
            "video_slug": self.slug,
            "slug": self.product.slug
        })


def pre_save_product(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


def pre_save_video(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


def post_email_confirmed(request, email_address, *args, **kwargs):
    user = User.objects.get(email=email_address.email)
    free_trial_pricing = Pricing.objects.get(name='Free Trial')
    subscription = Subscription.objects.create(
        user=user, 
        pricing=free_trial_pricing
    )
    # stripe_customer = stripe.Customer.create(
    #     email=user.email
    # )
    # stripe_subscription = stripe.Subscription.create(
    #     customer=stripe_customer["id"],
    #     items=[{'price': 'django-free-trial'}],
    #     trial_period_days=7
    # )
    # subscription.status = stripe_subscription["status"]  # trialing
    # subscription.stripe_subscription_id = stripe_subscription["id"]
    # subscription.save()
    # user.stripe_customer_id = stripe_customer["id"]
    user.save()


# def user_logged_in_receiver(sender, user, **kwargs):
#     subscription = user.subscription
#     sub = stripe.Subscription.retrieve(subscription.stripe_subscription_id)

    # subscription.status = sub["status"]
    # subscription.save()






# user_logged_in.connect(user_logged_in_receiver)
email_confirmed.connect(post_email_confirmed)
pre_save.connect(pre_save_product, sender=Product)
pre_save.connect(pre_save_video, sender=Video)


