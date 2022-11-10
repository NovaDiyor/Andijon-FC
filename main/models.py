from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    status = models.IntegerField(
        choices=(
            (1, 'admin'),
            (2, 'user')
        ), default=2)
    country = models.CharField(max_length=210)


class Staff(models.Model):
    status = {
        (1, 'trainer'),
        (2, 'physiotherapist'),
        (3, 'doctor'),
        (4, 'goalkeeper-trainer'),
        (5, 'admin')
    }
    name = models.CharField(max_length=210)
    sur_name = models.CharField(max_length=210)
    birth = models.DateField()
    image = models.ImageField(upload_to='staff/')


class Players(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    number = models.IntegerField()
    TYPES = {
        (1, 'forward'),
        (2, 'midfielder'),
        (3, 'defender'),
        (4, 'goalkeeper'),
    }
    position = models.IntegerField(default=1, choices=TYPES)
    captain = models.BooleanField(default=False)
    sub_captain = models.BooleanField()


class Passes(models.Model):
    all = models.IntegerField()
    successful = models.IntegerField()


class Long(models.Model):
    all = models.IntegerField()
    successful = models.IntegerField()


class Helps(models.Model):
    all = models.IntegerField()
    successful = models.IntegerField()


class Kross(models.Model):
    all = models.IntegerField()
    successful = models.IntegerField()


class Fc(models.Model):
    players = models.ManyToManyField(Players)
    staff = models.ManyToManyField(Staff)
    name = models.CharField(max_length=210)
    logo = models.ImageField(upload_to='fc/')


class Club(models.Model):
    logo = models.ImageField(upload_to='fc/')
    name = models.CharField(max_length=210)
    trainer = models.CharField(max_length=210)


class Advertiser(models.Model):
    logo = models.ImageField(upload_to='advertiser/')
    url = models.URLField()


class News(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()


class Videos(models.Model):
    videos = models.FileField(upload_to='video/')
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    is_top = models.BooleanField(default=False)


class Info(models.Model):
    insta = models.URLField()
    telegram = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    facebook = models.URLField()
    phone = models.IntegerField()
    email = models.EmailField()
    bio = models.TextField()
    logo = models.ImageField(upload_to='info/')


class About(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='academy/')
    text = models.TextField()
    title = models.TextField()


class Preview(models.Model):
    guest = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='guest')
    host = models.ForeignKey(Fc, on_delete=models.CASCADE, related_name='host')
    date = models.DateTimeField()


class Squad(models.Model):
    team = models.ManyToManyField(Players)
    match_day = models.IntegerField()
    game = models.ForeignKey(Preview, on_delete=models.CASCADE)


class Line(models.Model):
    team = models.ManyToManyField(Players)
    squad_list = models.ForeignKey(Squad, on_delete=models.CASCADE)


class Substitute(models.Model):
    squad = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='player_out')
    line = models.ForeignKey(Line, on_delete=models.CASCADE, related_name='player_on')
    minute = models.IntegerField()
    seconds = models.IntegerField()


class Game(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    guest_goal = models.IntegerField(null=True, blank=True)
    host_goal = models.IntegerField(null=True, blank=True)
    match_day = models.CharField(max_length=255)
    passion = models.FloatField()
    kross = models.ForeignKey(Kross, on_delete=models.CASCADE)
    passes = models.ForeignKey(Passes, on_delete=models.CASCADE)
    long_passes = models.ForeignKey(Long, on_delete=models.CASCADE)
    helps = models.ForeignKey(Helps, on_delete=models.CASCADE)
    subs = models.ForeignKey(Substitute, on_delete=models.CASCADE, null=True, blank=True)


class Size(models.Model):
    name = models.IntegerField(choices=(
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'XL'),
        (5, 'XXL'),
        (6, '3XL'),
    ))
    available = models.BooleanField(default=True)


class Images(models.Model):
    image = models.ImageField(upload_to='media/')


class Product(models.Model):
    image = models.ManyToManyField(Images)
    bonus = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    text = models.TextField()
    size = models.ManyToManyField(Size)
    rating = models.IntegerField(choices=(
        (0, 'no rating'),
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    ), default=0)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Region(models.Model):
    name = models.CharField(max_length=210)


class Order(models.Model):
    order_item = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    email = models.EmailField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.CharField(max_length=210)
