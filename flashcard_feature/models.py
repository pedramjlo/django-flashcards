from django.db import models

class Category(models.Model):
    class ColorChoice(models.TextChoices):
        RED = 'red', 'Red'
        BLUE = 'blue', 'Blue'
        GREEN = 'green', 'Green'
        YELLOW = 'yellow', 'Yellow'
        ORANGE = 'orange', 'Orange'
        PURPLE = 'purple', 'Purple'

    title = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=ColorChoice.choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Flashcard(models.Model):

    front_title = models.CharField(max_length=100)
    back_title = models.CharField(max_length=100)
    back_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_pinned = models.BooleanField(default=False)
    is_learned = models.BooleanField(default=False)

    def __str__(self):
        return self.front_title
