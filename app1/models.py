from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=50)
    edition=models.CharField(max_length=10)
    genre=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.book_name} by {self.author_name}"
