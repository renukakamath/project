from django.db import models

# Create your models here.



from django.db import models
import string, random

def generate_shortcode(length=6):
    """Generate a random short code."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_shortcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"

