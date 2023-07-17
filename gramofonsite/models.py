from django.db import models

class ShortDescribe(models.Model):
    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    # area = Local.area
    # rooms =  models.Choices
    # def __str__(self):
        # return f"{self.title_page} \t {self.street}"

    def __str__(self):
        return self.title_page













#    name = models.CharField(max_length=20)
#    photo = models.ImageField(upload_to="image", null=True, blank=True)
#    discrabe = models.TextField(null=True, blank=True, default="")
#    add = models.ManyToManyField(Local)
       
class Local(models.Model):
    title = models.CharField(max_length=20)
    number_of_levels = models.PositiveIntegerField(blank=True, null=True,  default=0)
    area = models.PositiveSmallIntegerField(default=200)
    nunber_of_people = models.PositiveSmallIntegerField(default=60)
    more_info = models.TextField(null=True, blank=True, default="")
    image = models.ImageField(upload_to="image", null=True, blank=True)
    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    note = models.ForeignKey(ShortDescribe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        if self.number_of_levels is not None:
            return f" Lokal {self.number_of_levels} poziomowy o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 
        return f"Lokal o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 

    # def __str_(self):
        # return self.title
    

class Room(models.Model):
    DANCE_ROOM = "Dance"
    TOILET = "WC"
    KITCHEN = "Cook"

    ROOMS = [
        (DANCE_ROOM, "Sala Taneczna"),
        (TOILET, "Toaleta"),
        (KITCHEN, "Kuchnia",)
    ]
    description = models.CharField(max_length=500, choices=ROOMS, default=DANCE_ROOM)
    image = models.ImageField(upload_to="image", null=True, blank=True)
    note = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self): 
        return self.description



    








