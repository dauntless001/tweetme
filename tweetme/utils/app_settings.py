import os

def get_app_settings():
    return os.getenv('DJANGO_SETTINGS_MODULE', 'tweetme.settings.dev')