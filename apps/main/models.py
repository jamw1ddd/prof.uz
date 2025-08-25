from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to="media/banners/")

    def __str__(self):
        return self.title

class BannerButton(models.Model):
    section = models.ForeignKey(Banner, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)


class BannerText(models.Model):
    section = models.ForeignKey(Banner, on_delete=models.CASCADE)
    text = models.TextField()


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description_title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="media/project/")

    def __str__(self):
        return self.title

class Audience(models.Model):
    project = models.ForeignKey(AboutSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)


class FutureDream(models.Model):
    title = models.CharField(max_length=255,default="Kelajakdagi orzularim")


class FutureDreamItem(models.Model):
    dream = models.ForeignKey(FutureDream,on_delete=models.CASCADE)
    child_profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/futuredream/")

    def __str__(self):
        return self.child_profession

class StepSection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class StepItem(models.Model):
    section = models.ForeignKey(StepSection, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    text = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="picture/step_icons/") 

    def __str__(self):
        return f"{self.number} {self.text}"

class Interest(models.Model):
    title = models.CharField(max_length=255, default="Sizdagi qiziqishlar")
    name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    #chiziq htmlda bo'ladi width: {{ obj.score|floatformat:1|divisibleby:10 }}%
    def __str__(self):
        return f"{self.name} - {self.score}"

class Ability(models.Model):
    name = models.CharField(max_length=255)
    score = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.name} - {self.score}"

    
class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
class Training(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="media/training/", blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class TrainingComment(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.training.title}"

    
class Contact(models.Model):
    text = models.TextField(blank=True)
    location = models.URLField()


class ContactInfo(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100) 
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class About(models.Model):
    text = models.TextField()


class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="media/about_images/")

