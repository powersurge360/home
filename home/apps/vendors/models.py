from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=400)
    price_range = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )
    notes = models.TextField(blank=True)
    selected = models.BooleanField(default=False)

    services = models.ManyToManyField(
        Service,
        related_name='vendors',
    )

    def __unicode__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )

    seasons = models.ManyToManyField(
        Season,
        related_name='menu_items',
        blank=True,
    )
    vendor = models.ForeignKey(Vendor, related_name='vendor')
    menu_category = models.ForeignKey(MenuCategory, related_name='menu_items')

    def __unicode__(self):
        return self.name
