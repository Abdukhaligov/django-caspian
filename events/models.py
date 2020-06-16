from django.db import models

from accounts.models import User


class Membership(models.Model):
    name = models.CharField(max_length=128)
    reporter = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=0)

    # f)    days: json or text
    #    i)    user: belongs_to, nullable, on delete = Set Null
    #    ii)    name: string
    #    iii)    description: text, nullable
    #    iv)    date: date
    #    v)    start: time, nullable
    #    vi)    end: time, nullable
    #    vii)    address: string, nullable
    #    viii)    picture: string(path to file), nullable

    def __str__(self):
        if self.active:
            return self.name + " (active)"
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    topic = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.membership.name


class Report(models.Model):
    class Status(models.TextChoices):
        PENDING = '1', 'Pending'
        REJECTED = '2', 'Rejected'
        APPROVED = '3', 'Approved'

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.SET_NULL)
    topic = models.ForeignKey(Topic, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    # file = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.PENDING,
    )

    def __str__(self):
        return self.name


class Voucher(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to='vouchers')
    link = models.CharField(max_length=512, blank=True, null=True)
    uniq = models.BooleanField(default=False)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.id)


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)

    # file = models.FilePathField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
