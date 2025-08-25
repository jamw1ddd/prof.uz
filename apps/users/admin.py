from django.contrib import admin
from apps.users.models import ( 
    Profile, UserSettings,Resume, PersonalInfo, Education, Language,
    WorkExperience, Career, ResumeTemplate, LandingResume, LandingResumeBlock,
    ResumeStep, ResumeStepItem, ResumeInfo, Register
)

admin.site.register(Profile)
admin.site.register(UserSettings)
admin.site.register(Register)
admin.site.register(PersonalInfo)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Language)
admin.site.register(WorkExperience)
admin.site.register(Career)
admin.site.register(ResumeTemplate)
admin.site.register(LandingResume)
admin.site.register(LandingResumeBlock)
admin.site.register(ResumeStep)
admin.site.register(ResumeStepItem)
admin.site.register(ResumeInfo)
