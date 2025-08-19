from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Starter(models.Model):
    content = models.TextField(verbose_name="Kontent")
    picture = models.ImageField(upload_to="picture/starter/", blank=True, null=True, verbose_name="Rasm")

    def __str__(self):
        return f"Starter - {self.content[:30]}"

class UserSettings(models.Model):
    FONT_SIZE_CHOICES = [
        ("1x", "Normal"),
        ("1.5x", "Kattaroq"),
        ("2x", "Juda katta"),
    ]

    THEME_CHOICES = [
        ("default", "Oddiy rang"),
        ("chernobely", "Oq-qora"),
    ]

    LANGUAGE_CHOICES = [
        ("uz", "O‘zbek"),
        ("ru", "Русский"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default="default")
    font_size = models.CharField(max_length=10, choices=FONT_SIZE_CHOICES, default="1x")
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default="uz")

    def __str__(self):
        return f"{self.user.username} sozlamalari"


class IntroSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # buttonlarni ko‘paytirib bo‘lishi uchun alohida model
    # IntroSection bilan bog‘lanadi
    class Meta:
        verbose_name = "Intro Section"
        verbose_name_plural = "Intro Sections"

    def __str__(self):
        return self.title

class IntroButton(models.Model):
    section = models.ForeignKey(IntroSection, on_delete=models.CASCADE, related_name="buttons")
    text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.section.title} - {self.text}"

class IntroText(models.Model):
    section = models.ForeignKey(IntroSection, on_delete=models.CASCADE, related_name="texts")
    text = models.TextField()

    def __str__(self):
        return f"{self.section.title} - {self.text[:30]}"

class ProjectSection(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name="Kichik sarlavha")  # Mening kelajagim o'z qo'limda
    title = models.CharField(max_length=255, verbose_name="Sarlavha")  # Loyiha haqida
    description_title = models.CharField(max_length=255, verbose_name="Asosiy sarlavha")  # Qobiliyat va imkoniyat...
    description = models.TextField(verbose_name="Izoh / Matn")
    image = models.ImageField(upload_to="picture/project/", blank=True, null=True, verbose_name="Rasm")

    def __str__(self):
        return self.title

class Audience(models.Model):
    project = models.ForeignKey(ProjectSection, on_delete=models.CASCADE, related_name="audiences")
    name = models.CharField(max_length=100, verbose_name="Nomi")  # Ota-onalarga
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ikonka (class yoki emoji)")

    def __str__(self):
        return self.name

class FutureDream(models.Model):
    title = models.CharField(max_length=255, verbose_name="Bo'lim sarlavhasi", default="Kelajakni hozirdan quring")
    child_profession = models.CharField(max_length=255, verbose_name="Matn")  # Men katta bo'lsam shifokor bo'laman
    image = models.ImageField(upload_to="picture/future/", blank=True, null=True, verbose_name="Rasm")

    def __str__(self):
        return self.child_profession

class StepSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class StepItem(models.Model):
    section = models.ForeignKey(StepSection, on_delete=models.CASCADE, related_name="steps")
    number = models.PositiveIntegerField()
    text = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="picture/step_icons/", blank=True, null=True) 

    def __str__(self):
        return f"{self.number}. {self.text}"

class Interest(models.Model):
    name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=3, decimal_places=1)  # masalan: 8.7

    def __str__(self):
        return f"{self.name} - {self.score}"

class Ability(models.Model):
    name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.name} - {self.score}"

class ProfessionCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=255)   # Masalan: Shifokor, Dasturchi
    slug = models.SlugField(unique=True)      # URL uchun qulay
    image = models.ImageField(upload_to="picture/professions/main/", blank=True, null=True)
    category = models.ManyToManyField(ProfessionCategory, related_name="professions")
    subjects = models.ManyToManyField(Subject, related_name="professions")

    def __str__(self):
        return self.name

class ProfessionDetail(models.Model):
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE, related_name="detail")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="picture/professions/details/")

    def __str__(self):
        return f"Detail of {self.profession.name}"


class ProfessionBlock(models.Model):
    detail = models.ForeignKey(ProfessionDetail, on_delete=models.CASCADE, related_name="blocks")
    icon = models.ImageField(upload_to="picture/profession_icons/", blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.detail.profession.name})"


class ProfessionAbility(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="abilities")
    picture = models.ImageField(upload_to="picture/profession/abilities/")
    label = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.profession.name} - {self.title}"


class ProfessionAbilityItem(models.Model):
    ability = models.ForeignKey(ProfessionAbility, on_delete=models.CASCADE, related_name="items")
    icon = models.ImageField(upload_to="picture/profession/abilities/icons/")
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ability.profession.name} - {self.text}"


class GoodBadSection(models.Model):
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE, related_name="good_bad")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.profession.name} - Good/Bad"


class BadBlock(models.Model):
    section = models.ForeignKey(GoodBadSection, related_name="bad_blocks", on_delete=models.CASCADE)
    main_icon = models.CharField(max_length=100)

    def __str__(self):
        return f"Bad Block for {self.section.profession.name}"


class BadItem(models.Model):
    block = models.ForeignKey(BadBlock, related_name="items", on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class GoodBlock(models.Model):
    section = models.ForeignKey(GoodBadSection, related_name="good_blocks", on_delete=models.CASCADE)
    main_icon = models.CharField(max_length=100)

    def __str__(self):
        return f"Good Block for {self.section.profession.name}"


class GoodItem(models.Model):
    block = models.ForeignKey(GoodBlock, related_name="items", on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class MoneySection(models.Model):
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE, related_name="money")
    image = models.ImageField(upload_to='picture/money/', blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.profession.name} - Money"


class MoneyBlock(models.Model):
    section = models.ForeignKey(MoneySection, related_name="blocks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return f"{self.section.profession.name} - {self.title}"


class WhereWorks(models.Model):
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE, related_name="where_works")
    title = models.CharField(max_length=255)
    text = models.TextField()
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    video_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profession.name} - Where Works"


class WorkLogo(models.Model):
    section = models.ForeignKey(WhereWorks, related_name="logos", on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="picture/logos/")

    def __str__(self):
        return f"{self.section.profession.name} - Logo"
    
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TestAbout(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="picture/test_about/", blank=True, null=True)

    # Notification (bitta)
    notification_icon = models.ImageField(upload_to="test_about/notifications/", blank=True, null=True)
    notification_title = models.CharField(max_length=255, blank=True)
    notification_text = models.TextField(blank=True)

    # Button (bitta)
    button_url = models.URLField(blank=True)
    button_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Test(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question[:50]

class Answer(models.Model):
    test = models.ForeignKey(Test, related_name="answers", on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="picture/answers/", blank=True, null=True)
    is_correct = models.BooleanField(default=False)  # kerak bo‘lsa javob to‘g‘ri yoki yo‘qligini belgilang

    def __str__(self):
        return self.text if self.text else f"Answer to {self.test.id}"
    
class TestResult(models.Model):
    test = models.ForeignKey("Test", related_name="results", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    interest_text = models.TextField(blank=True, null=True)
    ability_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class InterestItem(models.Model):
    result = models.ForeignKey(TestResult, related_name="interests", on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="picture/interests/", blank=True, null=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class AbilityItem(models.Model):
    result = models.ForeignKey(TestResult, related_name="abilities", on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="picture/abilities/", blank=True, null=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
    
class Training(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="training/videos/", blank=True, null=True)  # video saqlash
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class TrainingComment(models.Model):
    training = models.ForeignKey(Training, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.training.title}"

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume")
    shaxsiy_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Shablon tanlash
    shablon_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - Resume"

# Shaxsiy ma'lumotlar
class PersonalInfo(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name="personal_info")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    birthdate = models.DateField()
    picture = models.ImageField(upload_to="picture/resumes/photos/", blank=True, null=True)
    
    GENDER_CHOICES = (
        ("male", "Erkak"),
        ("female", "Ayol"),
    )
    jins = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname}"

# Ta'lim
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="educations")
    school_finish = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    school_class = models.CharField(max_length=50, blank=True, null=True)
    letter = models.CharField(max_length=10, blank=True, null=True)  # masalan: "A sinf"

    def __str__(self):
        return f"{self.school} - {self.city}"

# Til bilish
class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="languages")
    LANGUAGE_CHOICES = (
        ("native", "Ona tili"),
        ("english", "Ingliz tili"),
        ("other", "Boshqa til"),
    )
    language_type = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    name = models.CharField(max_length=100, blank=True, null=True)  # agar 'other' bo'lsa

    def __str__(self):
        return self.language_type

# Ish tajribasi
class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="work_experiences")
    work = models.BooleanField(default=False)
    work_name = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    when = models.CharField(max_length=100, blank=True, null=True)  # masalan: 2020-2023
    work_duration = models.CharField(max_length=100, blank=True, null=True) # masalan: 3 yil
    about_work = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.work_name if self.work_name else "No work"

# Kariera
class Career(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name="career")
    profession = models.CharField(max_length=200)
    profession_category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.profession} ({self.profession_category})"

# Shablonlar
class ResumeTemplate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    preview = models.ImageField(upload_to="picture/resumes/templates/")  # shablon rasmi
    file = models.FileField(upload_to="picture/resumes/templates/files/", blank=True, null=True)  # pdf/docx template

    def __str__(self):
        return self.title

class LandingResume(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="picture/landing_resume/")
    button_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class LandingResumeBlock(models.Model):
    landing_resume = models.ForeignKey(LandingResume, on_delete=models.CASCADE, related_name="blocks")
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="picture/landing_resume/icons/")
    text = models.TextField()

    def __str__(self):
        return self.title
    
class ResumeStep(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class ResumeStepItem(models.Model):
    step = models.ForeignKey(ResumeStep, on_delete=models.CASCADE, related_name="items")
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="picture/resume_steps/icons/")
    text = models.TextField()

    class Meta:
        ordering = ['number']  # step tartib bilan chiqishi uchun

    def __str__(self):
        return f"{self.number}. {self.title}"

class ResumeInfo(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="picture/resume_pictures/", blank=True, null=True)
    text = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default="Batafsil")

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    # Shaxsiy ma'lumotlar
    shaxsiy_text = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    letter = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    button_text = models.CharField(max_length=50, default="Saqlash")

    # Parolni yangilash
    old_password = models.CharField(max_length=128, blank=True, null=True)
    new_password = models.CharField(max_length=128, blank=True, null=True)
    password_button_text = models.CharField(max_length=50, default="Parolni yangilash")

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Contact(models.Model):
    text = models.TextField(blank=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Contact info ({self.location})"

class ContactInfo(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="infos")
    icon = models.CharField(max_length=100)  # masalan: FontAwesome icon nomi
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return "About section"


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="images")
    picture = models.ImageField(upload_to="picture/about_pictures/")

    def __str__(self):
        return f"Image for {self.about.id}"

class Register(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    letter = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    password_repeat = models.CharField(max_length=128)
    button_text = models.CharField(max_length=50, default="Kirish")

    def __str__(self):
        return f"{self.name} {self.surname}"