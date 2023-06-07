from django.db import models


class Person(models.Model):
    # foss_person
    first_name = models.CharField(max_length=100, )
    second_name = models.CharField(max_length=100, )
    phone = models.CharField(max_length=20, )
    email = models.CharField(max_length=50)
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f"{str(self.first_name)} {str(self.second_name)}"


class Opinion(models.Model):
    # foss_opinion
    distro_name = models.CharField(max_length=100)
    rate = models.IntegerField()
    opinion = models.CharField(max_length=500)
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f"{self.distro_name}. {self.rate}. {self.date}"


class Task(models.Model):
    # foss_task
    expected_value = models.IntegerField()
    answer = models.IntegerField()
    prime_num = models.IntegerField()

    def __str__(self):
        return f"Expected: {self.expected_value}, Answer: {self.answer}"


class Page(models.Model):
    title = models.CharField(verbose_name='Page title', max_length=255, default="SampleTitle")
    header = models.CharField(verbose_name="Page header", max_length=255, default="SampleHeader", blank=True)
    nav = models.CharField(verbose_name='href', max_length=255, default="href")
    nav_position = models.IntegerField(verbose_name='Nav prior. (0 - exclude)', default=0, )
    content = models.TextField(verbose_name='Page content', default='')
    stylesheet = models.TextField(verbose_name='stylesheet content', default='main.css', max_length=255, blank=True)
    javascript = models.TextField(verbose_name='javascript', default='', max_length=255, blank=True)
    has_form = models.BooleanField(default=False)
    form_type = models.TextField(verbose_name='form type', default='', max_length=255, blank=True)
    current_date = models.DateTimeField(verbose_name="Edition date", auto_now=True)

    class Meta:
        verbose_name = 'Current page content'
        verbose_name_plural = 'Page content'
        ordering = ('-nav_position',)

    def __str__(self):
        return f"id: {self.id}.  {self.title}"
