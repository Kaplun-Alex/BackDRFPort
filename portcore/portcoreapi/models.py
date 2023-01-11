from django.db import models

class Categories(models.Model):
    
    name_of_category = models.CharField(max_length=30)

    def __str__(self):
        return self.name_of_category

class Description(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    about_field = models.CharField(max_length=4096, null=True)

    def __str__(self):
        return self.about_field



