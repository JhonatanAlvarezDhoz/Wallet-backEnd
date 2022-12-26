from django.db import models
from apps.user.models import User

# Create your models here.

class Category(models.Model):

    name_category = models.CharField(max_length=50, null=False, blank=False, default='Comments')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f"{self.name_category}"




class Opinion(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)
    opinion_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)

    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opinions'

    def __str__(self):
        return f"{self.opinion_category} {self.title} {self.is_active} {self.user}"


"""REVIEW = models.CharField(max_length=30, default='Review')
    COMMENTS = models.CharField(max_length=30, default="Comments") 
    SUGGESTIONS = models.CharField(max_length=30, default="suggestions") 
    BAD_SERVICE = models.CharField(max_length=30, default="Bad Service") 
    COMPLAINTS = models.CharField(max_length=30, default="Complaints ") """