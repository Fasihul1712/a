from django.db import models

class Siswa(models.Model):
    no = models.CharField(max_length=12 , unique=True, primary_key=True)
    makanan = models.CharField(max_length=100)
    minuman = models.CharField(max_length=200)
    date_created= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural="Hanymari"
