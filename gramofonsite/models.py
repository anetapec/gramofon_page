from django.db import models

       
class HeadPage(models.Model):
    logo_image = models.ImageField(upload_to="image", null=True, blank=True)
    background_image = models.ImageField(upload_to="image", null=True, blank=True)


class Local(models.Model):
    
    title_local = models.CharField(max_length=20)
    local_note = models.CharField(max_length=100, null=True)
    image_base = models.ImageField(upload_to="image", null=True, blank=True)

    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    short_note =  models.CharField(max_length=100, null=True)
    dance_room_title = models.CharField(max_length=20, null=True, blank=True)
    note_dance_room = models.TextField(max_length=800, null=True, blank=True)
    img_dance_room= models.ImageField(upload_to="image", null=True, blank=True)
    toilet_title = models.CharField(max_length=20, null=True, blank=True)
    note_toilet = models.TextField(max_length=500, null=True, blank=True)
    img_toilet= models.ImageField(upload_to="image", null=True, blank=True)
    kitchen_title = models.CharField(max_length=20, null=True, blank=True)
    note_kitchen = models.TextField(max_length=500, null=True, blank=True)
    img_ktchen= models.ImageField(upload_to="image", null=True, blank=True)
    # def __str__(self):
        
        # if self.number_of_levels is not None:
            # return f" Lokal {self.number_of_levels} poziomowy o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 
        # return f"Lokal o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 

    def __str_(self):
        return self.title_local
    

