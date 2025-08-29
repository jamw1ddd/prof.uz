from django.contrib import admin
from apps.professions.models import (
    Profession,  ProfessionAbility, ProfessionDetail,ProfessionAbilityItem,
    ProfessionBlock, GoodBadSection, BadBlock, BadItem, Subject,
    GoodBlock, GoodItem,WhereWorks, WorkLogo,ProfessionCategory
)

admin.site.register(Profession)
admin.site.register(ProfessionAbility)
admin.site.register(ProfessionAbilityItem)
admin.site.register(ProfessionDetail)
admin.site.register(ProfessionBlock)
admin.site.register(GoodBadSection)
admin.site.register(GoodBlock)
admin.site.register(GoodItem)
admin.site.register(BadBlock)
admin.site.register(BadItem)
admin.site.register(Subject)
admin.site.register(WhereWorks)
admin.site.register(WorkLogo)
admin.site.register(ProfessionCategory)
