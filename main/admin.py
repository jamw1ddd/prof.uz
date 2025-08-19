from django.contrib import admin
from .models import (
    IntroSection, IntroButton, IntroText,
    ProjectSection, Audience, Starter,
    FutureDream, StepSection, StepItem, Interest, Ability,
    ProfessionCategory, Subject, Profession, ProfessionDetail,
    ProfessionBlock, ProfessionAbility, AbilityItem,
    GoodBadSection, BadItem, GoodItem, MoneySection, MoneyBlock,
    WhereWorks, TestAbout, Test, Answer, TestResult, InterestItem,
    Training, TrainingComment, Resume, PersonalInfo, Education, Language,
    WorkExperience, Career, ResumeTemplate, LandingResume, LandingResumeBlock,
    ResumeStep, ResumeStepItem, ResumeInfo, ProfessionAbilityItem,
    Profile, Contact, ContactInfo, About, Register
)

admin.site.register(Starter)
admin.site.register(IntroSection)
admin.site.register(IntroButton)
admin.site.register(IntroText)
admin.site.register(ProjectSection)
admin.site.register(Audience)
admin.site.register(FutureDream)
admin.site.register(StepSection)
admin.site.register(StepItem)
admin.site.register(Interest)
admin.site.register(Ability)
admin.site.register(ProfessionCategory)
admin.site.register(Subject)
admin.site.register(Profession)
admin.site.register(ProfessionDetail)
admin.site.register(ProfessionBlock)
admin.site.register(ProfessionAbility)
admin.site.register(AbilityItem)
admin.site.register(GoodBadSection)
admin.site.register(BadItem)
admin.site.register(GoodItem)
admin.site.register(MoneySection)
admin.site.register(MoneyBlock)
admin.site.register(WhereWorks)
admin.site.register(TestAbout)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(TestResult)
admin.site.register(InterestItem)
admin.site.register(Training)
admin.site.register(TrainingComment)
admin.site.register(Resume)
admin.site.register(PersonalInfo)
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
admin.site.register(ProfessionAbilityItem)
admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(About)
admin.site.register(Register)
