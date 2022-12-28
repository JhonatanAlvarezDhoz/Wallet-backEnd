from django.db import models
from apps.user.models import User

# Create your models here.
class QRCategory(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False , blank=False, default=None)
    
    class Meta:
        verbose_name = 'QRCategory'
        verbose_name_plural = 'QRCategories'

    def create_ctaegory_for_default(self):
        QRCategory.objects.create()

    def __str__(self):
        return f"{self.name}"



class QRrecord(models.Model):
    name = models.CharField(max_length=255)
    value = models.TextField()
    is_active = models.BooleanField(default=True)
    qr_category = models.ForeignKey(QRCategory, on_delete=models.CASCADE, null=False, blank=False, default=None)

    class Meta:
        verbose_name = 'QRrecord'
        verbose_name_plural = 'QRrecords'

    def __str__(self):
        return f"{self.qr_category} {self.name} "