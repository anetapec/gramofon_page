from django.db import models

       
class HeadPage(models.Model):
    image_logo = models.ImageField(upload_to="image", null=True, blank=True)
    image_background = models.ImageField(upload_to="image", null=True, blank=True)


class Local(models.Model):
    
    title_local = models.CharField(max_length=20, verbose_name="Nazwa lokalu")
    note_local= models.CharField(max_length=100, null=True)
    image_base = models.ImageField(upload_to="image", null=True, blank=True)

    title_page = models.CharField(max_length=20, null=True)
    street = models.CharField(max_length=20, null=True)
    note_short =  models.CharField(max_length=100, null=True)
    dance_room_title = models.CharField(max_length=20, null=True, blank=True)
    dance_room_note = models.TextField(max_length=800, null=True, blank=True)
    dance_room_img= models.ImageField(upload_to="image", null=True, blank=True)
    toilet_title = models.CharField(max_length=20, null=True, blank=True)
    toilet_note = models.TextField(max_length=500, null=True, blank=True)
    toilet_img= models.ImageField(upload_to="image", null=True, blank=True)
    kitchen_title = models.CharField(max_length=20, null=True, blank=True)
    kitchen_note = models.TextField(max_length=500, null=True, blank=True)
    kitchen_img= models.ImageField(upload_to="image", null=True, blank=True)
    banquet_hall_title = models.CharField(max_length=20, null=True, blank=True)
    banquet_hall_note = models.TextField(max_length=800, null=True, blank=True)
    banquet_hall_img =  models.ImageField(upload_to="image", null=True, blank=True)
    equipment_title = models.CharField(max_length=20, null=True, blank=True)
    equipment_note = models.TextField(max_length=500, null=True, blank=True)
    equipment_img = models.ImageField(upload_to="image", null=True, blank=True)

    

    # def __str__(self):
        
        # if self.number_of_levels is not None:
            # return f" Lokal {self.number_of_levels} poziomowy o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 
        # return f"Lokal o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 

    def __str_(self):
        return self.title_local
    

