from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    """
        This class represents a model of a language.
    """
    name = models.CharField(max_length=64)
    header = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    """
        This class represents a model of a restaurant.
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    ico = models.IntegerField(blank=True)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    """
        This class represents a model of a branch connected to a restaurant.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    address = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    description = models.TextField(blank=True)
    opening_hours = models.TextField(blank=True)

    def __str__(self):
        return self.restaurant.name + ' - ' + self.address

class Role(models.Model):
    """
        This class represents a role of a employee.
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
        This class represents a category of product, which can also be a subcategory.
    """
    parent_category = models.ForeignKey('self', blank=True,  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Category ' + str(self.pk)

class CategoryName(models.Model):
    """
        This class represents a category in certain language.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name

class New(models.Model):
    """
        This class represents a model of a news in certain restaurant.
    """
    date_time = models.DateTimeField()

    def __str__(self):
        return 'New - ' + str(self.date_time)

class NewName(models.Model):
    """
        This class represents a new in certain language.
    """
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    header = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.header

class Order(models.Model):
    """
        This class represents an order from a certain branch.
    """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    person = models.CharField(max_length=256)
    address = models.TextField()

    def __str__(self):
        return self.person + ' - ' + str(self.date_time)

class Reservation(models.Model):
    """
        This class represents an order from a certain branch.
    """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    person = models.CharField(max_length=256)
    table = models.IntegerField()

    def __str__(self):
        return self.person + ' - ' + str(self.date_time) + ' - ' + str(self.table)

class Menu(models.Model):
    """
        This class represents some menu.
    """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.FileField(blank=True)

    def __str__(self):
        return str(self.pk) + ' on branch: ' + self.branch.address

class MenuName(models.Model):
    """
        This class represents certain menu in a given language.
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Unit(models.Model):
    """
        This class represents a unit.
    """
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return 'Unit ' + str(self.pk)

class UnitName(models.Model):
    """
        This class represents a unit in given language.
    """
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Employee(models.Model):
    """
        This class represent an employee in some branch.
    """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=256)
    phone = models.CharField(max_length=16, blank=True)
    mail = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname

class Item(models.Model):
    """
        This class represent some kind of product of selling.
    """
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    image = models.FileField(blank=True)
    amount = models.FloatField()

    def __str__(self):
        return 'Item ' + str(self.pk)

class ItemName(models.Model):
    """
        This class represents item in given language with proper price.
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price = models.IntegerField()
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
        This class represents item included in some menu.
    """
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return 'Item ' + str(self.item.pk) + 'in menu ' + str(self.menu.pk)

class Allergen(models.Model):
    """
        This class represents allergens food can contain.
    """
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return 'Allergen ' + str(self.pk)

class AllergenName(models.Model):
    """
        This class represents allergens food can contain in certain language.
    """
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    class Meta:
        unique_together = ('allergen', 'language',)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    """
        This class represents item in certain order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return 'Item ' + str(self.item.pk) + 'in order ' + str(self.order.pk)

class ItemAllergen(models.Model):
    """
        This class represents allergen in certain item.
    """
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return 'Allergen ' + str(self.allergen.pk) + 'in item ' + str(self.item.pk)

class MainPictures(models.Model):
    """
        This class represents main images, for example at top level page.
    """
    image = models.FileField()

    def __str__(self):
        return self.image.url

class ReservationConfig(models.Model):
    """
        This class represents keywords for reservation page in certain language.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    header = models.CharField(max_length=128)
    table_number_text = models.CharField(max_length=256)
    time_from_text = models.CharField(max_length=256)

    def __str__(self):
        return self.header

class ContactConfig(models.Model):
    """
        This class represents keywords for contact page in certain language.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    header = models.CharField(max_length=128)
    description_text = models.CharField(max_length=128)
    image_map = models.FileField(blank=True)
    image_restaurant = models.FileField(blank=True)

    def __str__(self):
        return self.header

class Contact(models.Model):
    """
        This class contains contents of a description.
    """
    contact_config = models.ForeignKey(ContactConfig, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.contact_config.header

class AboutUsConfig(models.Model):
    """
       This class represents keywords for "about us" page in certain language.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    header = models.CharField(max_length=128)
    description_text = models.CharField(max_length=128)
    fotogallery_text = models.CharField(max_length=128)

    def __str__(self):
        return self.header

class AboutUs(models.Model):
    """
        This class contains contents of a description.
    """
    aboutus_config = models.ForeignKey(AboutUsConfig, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.aboutus_config.header

class IntroConfig(models.Model):
    """
       This class represents keywords for "intro" page in certain language.
    """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    header = models.CharField(max_length=128)
    introduction_text = models.CharField(max_length=128)
    news_text = models.CharField(max_length=128)

    def __str__(self):
        return self.header

class Intro(models.Model):
    """
        This class contains contents of a description.
    """
    intro_config = models.ForeignKey(IntroConfig, on_delete=models.CASCADE)
    introduction = models.TextField()

    def __str__(self):
        return self.intro_config.header
