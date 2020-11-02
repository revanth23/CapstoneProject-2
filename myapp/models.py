from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=30)
    review = models.TextField()
    rating = models.CharField(max_length=20)
    pub_date = models.DateField()
    def __str__(self):
        return self.title