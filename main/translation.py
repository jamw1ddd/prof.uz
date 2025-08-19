from modeltranslation.translator import register, TranslationOptions
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

@register(Starter)
class StarterTranslationOptions(TranslationOptions):
    fields = ( "content", ) 

@register(IntroSection)
class IntroSectionTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(IntroButton)
class IntroButtonTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(IntroText)
class IntroTextTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(ProjectSection)
class ProjectSectionTranslationOptions(TranslationOptions):
    fields = ("subtitle", "title", "description_title", "description")


@register(Audience)
class AudienceTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(FutureDream)
class FutureDreamTranslationOptions(TranslationOptions):
    fields = ("title", "child_profession")


@register(StepSection)
class StepSectionTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(StepItem)
class StepItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Interest)
class InterestTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Ability)
class AbilityTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ProfessionCategory)
class ProfessionCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Profession)
class ProfessionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ProfessionDetail)
class ProfessionDetailTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(ProfessionBlock)
class ProfessionBlockTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(ProfessionAbility)
class ProfessionAbilityTranslationOptions(TranslationOptions):
    fields = ("label", "title", "description")


@register(ProfessionAbilityItem)
class AbilityItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(GoodBadSection)
class GoodBadSectionTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(BadItem)
class BadItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(GoodItem)
class GoodItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(MoneySection)
class MoneySectionTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(MoneyBlock)
class MoneyBlockTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(WhereWorks)
class WhereWorksTranslationOptions(TranslationOptions):
    fields = ("title", "text", "video_text")


@register(TestAbout)
class TestAboutTranslationOptions(TranslationOptions):
    fields = (
        "title", "text",
        "notification_title", "notification_text",
        "button_text",
    )

@register(Test)
class TestTranslationOptions(TranslationOptions):
    fields = ("question",)

@register(Answer)
class AnswerTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(TestResult)
class TestResultTranslationOptions(TranslationOptions):
    fields = ("title", "text", "interest_text", "ability_text")


@register(InterestItem)
class InterestItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(AbilityItem)
class AbilityItemTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Training)
class TrainingTranslationOptions(TranslationOptions):
    fields = ("title", "text",)


@register(TrainingComment)
class TrainingCommentTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Resume)
class ResumeTranslationOptions(TranslationOptions):
    fields = ("shaxsiy_text", "shablon_text")


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ("city", "region", "school", "school_class", "letter")


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(WorkExperience)
class WorkExperienceTranslationOptions(TranslationOptions):
    fields = ("work_name", "profession", "when", "work_duration", "about_work")


@register(Career)
class CareerTranslationOptions(TranslationOptions):
    fields = ("profession", "profession_category")


@register(ResumeTemplate)
class ResumeTemplateTranslationOptions(TranslationOptions):
    fields = ("title", "description",)


@register(LandingResume)
class LandingResumeTranslationOptions(TranslationOptions):
    fields = ("title", "description", "button_text")


@register(LandingResumeBlock)
class LandingResumeBlockTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(ResumeStep)
class ResumeStepTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(ResumeStepItem)
class ResumeStepItemTranslationOptions(TranslationOptions):
    fields = ("title", "text")


@register(ResumeInfo)
class ResumeInfoTranslationOptions(TranslationOptions):
    fields = ("title", "text", "text2", "button_text")


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ("shaxsiy_text", "city", "region", "school", "class_name", "letter", "button_text", "password_button_text")


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ("text", "location")


@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("text",)

@register(Register)
class RegisterTranslationOptions(TranslationOptions):
    fields = ("city", "region", "school", "class_name", "letter", "button_text")