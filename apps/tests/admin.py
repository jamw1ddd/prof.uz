from django.contrib import admin
from apps.tests.models import (
    Test, Answer, TestResult,TestAbout,
    TestInterestItem, TestAbilityItem
)

admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(TestResult)
admin.site.register(TestAbout)
admin.site.register(TestInterestItem)
admin.site.register(TestAbilityItem)
