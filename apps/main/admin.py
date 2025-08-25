from django.contrib import admin
from apps.main.models import ( 
    Audience, FutureDream,FutureDreamItem, StepSection, StepItem, Interest, Ability,AboutSection,
    Training, TrainingComment, Contact, ContactInfo, About,Banner, BannerButton, BannerText,Region
)

admin.site.register(AboutSection)
admin.site.register(Banner)
admin.site.register(BannerButton)
admin.site.register(BannerText)
admin.site.register(Audience)
admin.site.register(FutureDream)
admin.site.register(FutureDreamItem)
admin.site.register(StepSection)
admin.site.register(StepItem)
admin.site.register(Interest)
admin.site.register(Ability)
admin.site.register(Training)
admin.site.register(TrainingComment)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(About)
admin.site.register(Region)
