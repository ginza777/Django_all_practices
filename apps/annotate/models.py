from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class AuthorBook(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'book')

    def __str__(self):
        return f'{self.author} - {self.book}'
