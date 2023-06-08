from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, )
    second_name = models.CharField(max_length=100, )
    phone = models.CharField(max_length=20, )
    email = models.CharField(max_length=50)
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f"{str(self.first_name)} {str(self.second_name)}"


class Opinion(models.Model):
    distro_name = models.CharField(max_length=100)
    rate = models.IntegerField()
    opinion = models.CharField(max_length=500)
    date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return f"{self.distro_name}. {self.rate}. {self.date}"


class Task(models.Model):
    expected_value = models.IntegerField()
    answer = models.IntegerField()
    prime_num = models.IntegerField()

    def __str__(self):
        return f"Expected: {self.expected_value}, Answer: {self.answer}"


class Page(models.Model):
    """Page"""
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
        verbose_name = 'New Page'
        verbose_name_plural = 'Page content'
        ordering = ('-nav_position',)

    def __str__(self):
        return f"id: {self.id}.  {self.title}"


class LatexFormula(models.Model):
    """For formulas page"""
    header = models.CharField(verbose_name="LaTeX Header", max_length=255, blank=False)
    description = models.TextField(verbose_name="LaTeX Description", max_length=1024, blank=True)
    formula = models.TextField(verbose_name="LaTeX Formula", max_length=1024, blank=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.header}"


class CodeExample(models.Model):
    """For Code Example Page"""
    header = models.CharField(verbose_name="Code Header", max_length=255, blank=False)
    code = models.TextField(verbose_name="Code", max_length=1024, blank=True)
    lang = models.CharField(verbose_name="Programming Language", max_length=255, blank=True, default='python')
    order = models.IntegerField(default=0)
    show = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f"{self.header} ({self.lang})"


class SoftExample(models.Model):
    programm_name = models.CharField(verbose_name="Programm Name", max_length=255, blank=False)
    icon_path = models.TextField(verbose_name="Icon Path", max_length=1024, blank=True)
   # icon_path = models.ImageField(blank=True)
    description = models.CharField(verbose_name="Description", max_length=255, blank=True, default='python')
    link = models.CharField(verbose_name="Link", max_length=255, blank=True, default='')

    def __str__(self):
        return f"{self.programm_name}"