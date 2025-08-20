from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[('easy','Easy'),('medium','Medium'),('hard','Hard')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
