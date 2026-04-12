from django.db import models
from django.conf import settings
import os

class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='user_uploads/')
    name = models.CharField(max_length=255, blank=True)
    content_type = models.CharField(max_length=100, blank=True, null=True)
    size = models.BigIntegerField(default=0) # We added this!
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.name and self.file:
            self.name = os.path.basename(self.file.name)
            
        # Automatically save the file size
        if self.file and not self.size:
            try:
                self.size = self.file.size
            except Exception:
                pass
                
        if not self.content_type and self.file:
            ext = os.path.splitext(self.file.name)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                self.content_type = 'image'
            elif ext in ['.mp4', '.mov', '.avi', '.webm']:
                self.content_type = 'video'
            else:
                self.content_type = 'document'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
