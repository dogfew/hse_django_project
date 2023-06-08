from django.db import models


class Sign(models.Model):
    condition = models.CharField(default="Дано число", blank=True, max_length=128)
    number = models.FloatField(verbose_name='Float Number')
    sign = models.IntegerField()
    sign_text = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Number: {self.number}. Date: {self.created_at}"
