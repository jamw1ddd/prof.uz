from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class ProfessionCategory(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/professions/")
    category = models.ForeignKey(ProfessionCategory, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProfessionDetail(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="media/professions_details/")


class ProfessionBlock(models.Model):
    detail = models.ForeignKey(ProfessionDetail, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="media/profession_blocks/")
    title = models.CharField(max_length=255)
    text = models.TextField()


class ProfessionAbility(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="media/profession_abilities/")
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()


class ProfessionAbilityItem(models.Model):
    ability = models.ForeignKey(ProfessionAbility, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to="media/profession_abilities_icons/")
    text = models.CharField(max_length=255)


class GoodBadSection(models.Model):
    profession = models.OneToOneField(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


class BadBlock(models.Model):
    section = models.ForeignKey(GoodBadSection, on_delete=models.CASCADE)
    main_icon = models.CharField(max_length=100)


class BadItem(models.Model):
    block = models.ForeignKey(BadBlock, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    text = models.CharField(max_length=255)


class GoodBlock(models.Model):
    section = models.ForeignKey(GoodBadSection, on_delete=models.CASCADE)
    main_icon = models.CharField(max_length=100)


class GoodItem(models.Model):
    block = models.ForeignKey(GoodBlock, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)
    text = models.CharField(max_length=255)


class MoneySection(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/money/')
    title = models.CharField(max_length=255)
    text = models.TextField()


class MoneyItem(models.Model):
    section = models.ForeignKey(MoneySection, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()


class WhereWorks(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    video = models.FileField(upload_to="media/videos")
    video_text = models.TextField(blank=True, null=True)


class WorkLogo(models.Model):
    section = models.ForeignKey(WhereWorks, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="media/logos/")
