from django.db import models
from django.utils.safestring import mark_safe


class Region(models.Model):
    mask = models.CharField(max_length=128, blank=True, null=True)
    cc = models.CharField(max_length=8, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    name_ru = models.CharField(max_length=128, blank=True, null=True)
    description_ru = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class User(models.Model):
    def avatar_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.avatar.url)

    avatar_tag.short_description = 'Image'
    avatar_tag.allow_tags = True

    class Rank(models.TextChoices):
        NOT = '0', 'Not in Committee'
        FIRST = '1', 'First'
        SECOND = '2', 'Second'
        THIRD = '3', 'Third'

    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    reference = models.ForeignKey(Reference, on_delete=models.SET_NULL, blank=True, null=True)
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)
    public = models.BooleanField(default=1)
    rank = models.CharField(
        max_length=1,
        choices=Rank.choices,
        default=Rank.NOT,
    )

    # m)	links: json or text, nullable

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    company = models.CharField(max_length=128, blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)

    # f)    links: json or text, nullable

    def __str__(self):
        return self.name

