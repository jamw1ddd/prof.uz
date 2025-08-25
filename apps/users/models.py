from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
        ("en", "English")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default="default")
    font_size = models.CharField(max_length=10, choices=FONT_SIZE_CHOICES, default="1x")
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default="uz")

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shaxsiy_text = models.CharField(max_length=255, default="Shaxsiy")
    created_at = models.DateTimeField(auto_now_add=True)
    shablon_text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - Resume"

class PersonalInfo(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    birthdate = models.DateField()
    picture = models.ImageField(upload_to="media/resume_photos/")
    
    GENDER_CHOICES = (
        ("male", "Erkak"),
        ("female", "Ayol"),
    )
    jins = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school_finish = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    school_class = models.CharField(max_length=50)
    letter = models.CharField(max_length=10)

    def __str__(self):
        return self.school


class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    LANGUAGE_CHOICES = (
        ("native", "Ona tili"),
        ("english", "Ingliz tili"),
        ("other", "Boshqa til"),
    )
    language_type1 = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    language_type2 = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    language_type3 = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    work = models.BooleanField(default=False)
    work_name = models.CharField(max_length=200, blank=True, null=True)
    profession = models.CharField(max_length=200, blank=True, null=True)
    when = models.CharField(max_length=100, blank=True, null=True)
    work_duration = models.CharField(max_length=100, blank=True, null=True)
    about_work = models.TextField(blank=True, null=True)


class Career(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    profession = models.CharField(max_length=200)
    profession_category = models.CharField(max_length=200)


class ResumeTemplate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    preview = models.ImageField(upload_to="media/resume_templates/")
    file = models.FileField(upload_to="media/resume_template_files/", blank=True, null=True)

    def __str__(self):
        return self.title

class LandingResume(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="media/landing_resume/")

    def __str__(self):
        return self.title

class LandingResumeBlock(models.Model):
    landing_resume = models.ForeignKey(LandingResume, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="media/landing_resume_icons/")
    text = models.TextField()

    def __str__(self):
        return self.title
    
class ResumeStep(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class ResumeStepItem(models.Model):
    step = models.ForeignKey(ResumeStep, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="picture/resume_steps/icons/")
    text = models.TextField()


class ResumeInfo(models.Model):
    title = models.CharField(max_length=200,default="Professional rezume bu:")
    picture = models.ImageField(upload_to="media/resume_info", blank=True, null=True)
    text = models.TextField(blank=True)
    text2 = models.TextField(blank=True)

    
class Profile(models.Model):
    shaxsiy_text = models.CharField(max_length=255, default="Shaxsiy ma'lumotim")
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    class_name = models.CharField(max_length=50, blank=True, null=True)
    letter = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    old_password = models.CharField(max_length=128, blank=True, null=True)
    new_password = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
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

    def __str__(self):
        return f"{self.name} {self.surname}"