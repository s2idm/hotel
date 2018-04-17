from settings.base import SITE_DOMAIN # import the settings file

def admin_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'SITE_DOMAIN': SITE_DOMAIN}