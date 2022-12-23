from django.db import models
from apps.user.models import User

# Create your models here.

class Category(models.Model):

    class OpinionCategory(models.TextChoices):

        REVIEW = 'REVIEW', 'Review'
        COMMENTS = "COMMENTS", "Comments"
        SUGGESTIONS = "SUGGESTIONS", "suggestions"
        BAD_SERVICE = "BAD SERVICE", "Bad Service"
        COMPLAINTS = "COMPLAINTS", "Complaints " 

    category = models.CharField(
        max_length=100, choices=OpinionCategory.choices)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.category}"



class Opinion(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)
    opinion_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opinions'

    def __str__(self):
        return f"{self.opinion_category} {self.title} {self.is_active}"
