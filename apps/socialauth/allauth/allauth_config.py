# django allauth
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
ALL_AUTH_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.linkedin',
    'allauth.socialaccount.providers.yandex',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',

]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '601157397888-clt1ome27em9r6rb0up9tc2emp51fo6c.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    'facebook': {
        'APP': {
            'client_id': '625659939610720',
            'secret': '70df3f0cb34fad4a968719300ddebe54',
            'key': ''
        },
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',

    },
    'github': {
        'APP': {
            'client_id': '151e0179dae600e45341',
            'secret': '770335cff69bbb45efd52f7bf483e849cc59ce88',
            'key': ''
        },

    },
    "apple": {
        "APP": {
            # Your service identifier.
            'client_id': "com.<your domain>.social-login-1234",

            # The Key ID (visible in the "View Key Details" page).
            "secret": "sociallogintest1234",

            "key": "ABCDEF",

            "certificate_key": """----BEGIN PRIVATE KEY----
            KJASDHKASDHKASJHDASKJHDKJASHDHJA----END PRIVATE KEY----"""
        }
    }
}

SITE_ID = 1

# login redirect url
LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000/socialauth/'
LOGOUT_REDIRECT_URL = 'http://127.0.0.1:8000/socialauth/'

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
