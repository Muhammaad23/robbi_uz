from django.db import models


class Mehmonhonlar(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)
    job_time = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

    # Add a field for the star rating
    STAR_RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    star_rating = models.IntegerField(choices=STAR_RATING_CHOICES)

    def __str__(self):
        return self.title
