from cms.models import SocialMedia


def social_media_accounts(self):
    social_media_accounts = SocialMedia.objects.first()
    return {"social_media_accounts": social_media_accounts}
