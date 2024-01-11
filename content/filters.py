import django_filters
from .models import Product
from django_filters.widgets import BooleanWidget, RangeWidget
from django.forms.widgets import TextInput
from django import forms
from django.db import models

class ProductFilter(django_filters.FilterSet):
    SITE_TYPE_CHOICES = (
        (0, 'facebook'),
        (1, 'instagram'),
        (2, 'pinterest'),
    )

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    option_ads_type = [
        ('video', 'Video'),
        ('photo', 'Photo'),
        ('both', 'Both'),
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
        ('cAll', 'CAll'),
    ]
    gender_options = [
        ('male or Female', 'Male or Female'),
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    technology_options = [
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
    country_choices = [
        ('united States', 'United States'),
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
    categories_choices = [
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
    ]
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
    
    ads_type = django_filters.ChoiceFilter(field_name='ads_type', choices=option_ads_type, empty_label='All', initial='All')
    button = django_filters.ChoiceFilter(field_name='button', choices=option_button, empty_label = 'All', initial='All')
    gender = django_filters.ChoiceFilter(field_name='gender', choices=gender_options, empty_label= 'All', initial='All')
    technology = django_filters.ChoiceFilter(field_name='technology', choices=technology_options, empty_label ='All', initial='All')
    categories = django_filters.ChoiceFilter(field_name='categories', choices=categories_choices, empty_label ='All', initial='All')
    countries = django_filters.ChoiceFilter(field_name='countries', choices=country_choices, empty_label ='All', initial='All')
    ship_from = django_filters.ChoiceFilter(field_name='ship_from', choices=ship_from_choices, empty_label ='All', initial='All')
    language = django_filters.ChoiceFilter(field_name='language', choices=option_language, empty_label ='All', initial='All') 
    age__gt = django_filters.NumberFilter(field_name='age', lookup_expr 
    ='gte', label='Age min', widget=TextInput(attrs={'placeholder': 'Min','type': 'number'}))
    age__lt = django_filters.NumberFilter(field_name='age', lookup_expr 
    = 'lte', label='Age max', widget=TextInput(attrs={'placeholder': 'Min','type': 'number'}))
    
    
    created_at__gt = django_filters.DateFromToRangeFilter(field_name='created_at', lookup_expr 
    ='gte', label='Date min', widget=TextInput(attrs={'type': 'date'}))
    created_at__lt = django_filters.DateFromToRangeFilter(field_name='created_at', lookup_expr 
    = 'lte', label='Date max', widget=TextInput(attrs={'type': 'date'}))
    
    
    facebook_comment__gt = django_filters.NumberFilter(field_name='facebook_comment', lookup_expr 
    ='gte', label='Comment min', widget=TextInput(attrs={'placeholder': 'Min', 'type': 'number'}))
    facebook_comment__lt = django_filters.NumberFilter(field_name='facebook_comment', lookup_expr 
    = 'lte', label='Comment max', widget=TextInput(attrs={'placeholder': 'Max', 'type': 'number'}))
    
    
    aliexpress_price__gt = django_filters.NumberFilter(field_name='aliexpress_price', lookup_expr 
    ='gte', label='Price min', widget=TextInput(attrs={'placeholder': 'Min', 'type': 'number'}))
    aliexpress_price__lt = django_filters.NumberFilter(field_name='aliexpress_price', lookup_expr 
    = 'lte', label='Price max', widget=TextInput(attrs={'placeholder': 'Max', 'type': 'number'}))
    
    
    facebook_like__gt = django_filters.NumberFilter(field_name='facebook_like', lookup_expr 
    ='gte', label='Likes min', widget=TextInput(attrs={'placeholder': 'Min', 'type': 'number'}))
    facebook_like__lt = django_filters.NumberFilter(field_name='facebook_like', lookup_expr 
    = 'lte', label='Likes max', widget=TextInput(attrs={'placeholder': 'Max', 'type': 'number'}))
    
    
    site_type = django_filters.ChoiceFilter(choices=SITE_TYPE_CHOICES, field_name='site_type', empty_label='All', initial='All')
    ordering = django_filters.ChoiceFilter(label='Order', choices=CHOICES, method = 'filter_by_order', empty_label='any', initial='any')
    class Meta:
        model = Product
        fields = {
            'name':['icontains'],
        }
        
        fields =  ['site_type', 'created_at__gt', 'created_at__lt', 'facebook_like__gt',  'facebook_like__lt', 'aliexpress_price__gt', 'aliexpress_price__lt', 'ads_type', 'facebook_comment__gt', 'facebook_comment__lt','age__gt', 'age__lt', 'categories', 'gender', 'technology', 'countries', 'ship_from', 'language', 'button']
        
    
    def filter_by_order(self, queryset, name, value):
        expression = 'updated_at' if value == 'ascending' else '-updated_at'
        return queryset.order_by(expression)