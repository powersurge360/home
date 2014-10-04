from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)


class Vendor(models.Model):
    name = models.CharField(max_length=400)
    price_range = models.CharField(max_length=300, blank=True)
    notes = models.TextField(blank=True)

    services = models.ManyToManyField(
        Service,
        related_name='vendors',
        null=True,
        blank=True,
    )


class Question(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True)

    vendor = models.ForeignKey(Vendor, related_name='questions')
