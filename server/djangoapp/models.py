from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)
    country = models.CharField(max_length=50)

    def __str__(self):
        return  "Name: " + self.name + ", " + \
                "Description: " + self.description + ", " + \
                "Country:" + self.country 

# <HINT> Create a Car Model model `class CarModel(models.Model):`:

# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'WAGON'
    VEHICLE_MODE = [
        (SEDAN, 'SEDAN'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON')
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = name = models.CharField(null=False, max_length=30, default='car model')
    delaer_id = models.IntegerField(default=0)
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_MODE, default=SEDAN)
    year = models.DateField()

    # Create a toString method for object string representation
    def __str__(self):
        return "Car Make: " + str(self.car_make) + ", " + \
               "Name: " + self.name + ", " + \
               "Dealer: " + str(self.delaer_id) + ", " + \
               "Vehicle Type: " + self.vehicle_type + ". " + \
                "Year: " + str(self.year) 

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
        self.sentiment = ""
        self.id = ""

    def __str__(self):
        return "Reviews: " + self.review 

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
