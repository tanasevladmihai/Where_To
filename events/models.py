from django.contrib.gis.db import models
from django.utils import timezone
from django.conf import settings

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Event(models.Model):
    THEME_CHOICES = (
        ('culture', 'Culture'),
        ('volunteering', 'Volunteering'),
        ('entertainment', 'Entertainment'),
        ('education', 'Education'),
    )
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES)
    address = models.CharField(max_length=255)
    location = models.PointField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.location and self.address:
            from geopy.geocoders import GoogleV3
            geolocator = GoogleV3(api_key=settings.GOOGLE_MAPS_API_KEY)
            location = geolocator.geocode(self.address)
            if location:
                self.location = f"POINT({location.longitude} {location.latitude})"
        super().save(*args, **kwargs)

    def is_active(self):
        return self.end_date >= timezone.now()

    def __str__(self):
        return f"{self.name} - {self.city.name}"