from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/name/<filename>
    return f'media/{instance.sub_group}/{filename}'

# Create your models here.
class Sparepart(models.Model):
    sub_group_name = (
        ('camera', 'camera'),
        ('robot', 'robot'),
        ('bearing', 'bearing'),
        ('controller', 'controller'),
        ('common','common'),
        )

    name = models.CharField(max_length=50)
    sub_group = models.CharField(max_length=20,null=True,choices=sub_group_name)
    part_number = models.CharField(max_length=50,null=True,unique=True)
    qty = models.PositiveIntegerField()
    maker = models.CharField(max_length=50)
    registered_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = user_directory_path,unique=True)

    def __str__(self):
        return self.name