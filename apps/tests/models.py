from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TestAbout(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="media/test_about/")
    notification_icon = models.ImageField(upload_to="media/test_notifications/")
    notification_title = models.CharField(max_length=255, blank=True,null=True)
    notification_text = models.TextField(blank=True,null=True)


class Test(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question[:20]

class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="media/test_answers/", blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    
class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    interest_text = models.TextField(blank=True, null=True)
    ability_text = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="media/test_results/")

    def __str__(self):
        return self.title


class TestInterestItem(models.Model):
    result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    text = models.CharField(max_length=255)


class TestAbilityItem(models.Model):
    result = models.ForeignKey(TestResult, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=3, decimal_places=1)
    text = models.CharField(max_length=255)