from django.db import models


class Local(models.Model):
    title = models.CharField(max_length=20)
    number_of_levels = models.PositiveIntegerField(blank=True, null=True,  default=0)
    area = models.PositiveSmallIntegerField(default=200)
    nunber_of_people = models.PositiveSmallIntegerField(default=60)
    more_info = models.TextField(null=True, blank=True, default="")
    # image = models.ImageField(upload_to="image", null=True, blank=True)
    # # title_page = models.CharField(max_length=20, null=True)
    # # street = models.CharField(max_length=20, null=True)
    # describe = models.OneToOneField(ShortDescribe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        
        if self.number_of_levels is not None:
            return f" Lokal {self.number_of_levels} poziomowy o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 
        return f"Lokal o powierzchni {self.area} m2 do {self.nunber_of_people} osób." 

