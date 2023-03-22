from django.conf import settings
from django.db import models


class Member(models.Model):
    name = models.CharField('team member', max_length=50)
    number = models.IntegerField('number')
    email = models.CharField('team member', max_length=50)
    position = models.CharField('member position', max_length=50)
    bdate = models.DateTimeField('birth date')

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    place = models.CharField(max_length=50)


class Tour(models.Model):
    name = models.CharField('Tour name', max_length=60)
    description = models.TextField('Tour description')
    started = models.DateTimeField('Started date')
    duration = models.IntegerField('Tour duration')
    price = models.IntegerField('Tour price')
    image = models.ImageField('Tour image', upload_to='tours/')
    # customer = models.ManyToManyField(Customer)

    def __str__(self):
        return self.name


class OrderTour(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    # orders =

    def __str__(self):
        return self.tour.name


class Hotel(models.Model):
    name = models.CharField('Hotel name', max_length=60)
    city = models.CharField('Hotel city', max_length=60)
    price = models.IntegerField('Price for one person')
    hotelClass = models.IntegerField('Class of the hotel')
    image = models.ImageField('Tour image', upload_to='hotels/')

    def __str__(self):
        return self.name


class OrderHotel(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel.name


# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.user.name