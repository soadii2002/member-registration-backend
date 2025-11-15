from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    college = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=200)
    cv = models.FileField(upload_to='cvs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
