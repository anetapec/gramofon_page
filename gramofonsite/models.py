from django.db import models

       
class Local(models.Model):
    logo_image = models.ImageField(upload_to="image", null=True, blank=True)
    title_local = models.CharField(max_length=20)
    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    number_of_levels = models.PositiveIntegerField(blank=True, null=True,  default=0)
    area = models.PositiveSmallIntegerField(default=200)
    nunber_of_people = models.PositiveSmallIntegerField(default=60)
    more_info = models.CharField(max_length=20, null=True)
    image_base = models.ImageField(upload_to="image", null=True, blank=True)
    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    dance_room_title = models.CharField(max_length=20, null=True)
    note_dance_room = models.TextField(max_length=500, null=True)
    img_dance_room= models.ImageField(upload_to="image", null=True, blank=True)
    note_toilet = models.TextField(max_length=500, null=True)
    img_toilet= models.ImageField(upload_to="image", null=True, blank=True)
    note_kitchen = models.TextField(max_length=500, null=True)
    img_ktchen= models.ImageField(upload_to="image", null=True, blank=True)
    def __str__(self):
        
        if self.number_of_levels is not None:
            return f" Lokal {self.number_of_levels} poziomowy o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 
        return f"Lokal o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 

    # def __str_(self):
        # return self.title
    

