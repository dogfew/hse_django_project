from django.db import models


class NumberGuess(models.Model):
    number = models.FloatField()
    guess = models.CharField(max_length=10)
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Number: {self.number}, Guess: {self.guess}, Correct: {self.is_correct}"
