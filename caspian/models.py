from django.db import models


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


class Membership(models.Model):
    name = models.CharField(max_length=128)
    reporter = models.BooleanField(default=0)

    def __str__(self):
        return self.name


class User(models.Model):
    class Rank(models.TextChoices):
        NOT = '0', 'Not in Committee'
        FIRST = '1', 'First'
        SECOND = '2', 'Second'
        THIRD = '3', 'Third'

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


class Event(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=0)

    # f)    days: json or text
    # i)    user: belongs_to, nullable, on
    # delete = Set Null
    # ii)    name: string
    # iii)    description: text, nullable
    # iv)    date: date
    # v)    start: time, nullable
    # vi)    end: time, nullable
    # vii)    address: string, nullable
    # viii)    picture: string(path
    # to
    # file), nullable

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    topic = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


# Sponsor Class


class UserMembership(models.Model):
    class Status(models.TextChoices):
        PENDING = '1', 'Pending'
        REJECTED = '2', 'Rejected'
        APPROVED = '3', 'Approved'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.PENDING,
    )

# a)    event: belongs_to, on
# delete = CASCADE
# b)    user: belongs_to, on
# delete = CASCADE
# c)    membership: belongs_to, on
# delete = CASCADE
# d)    status: enum[1, 2, 3], default = 1
