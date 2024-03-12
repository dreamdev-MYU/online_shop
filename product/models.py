from django.db import models
from users.models import User, BaseModel
from django.core.validators import FileExtensionValidator


    


class Category(BaseModel):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

class Product(BaseModel):
    name = models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete = models.CASCADE, related_name='products')
    users = models.ForeignKey(User,on_delete=models.CASCADE, related_name='products')
    description = models.TextField(default='',null=True,blank=True)
    image = models.ImageField(upload_to = 'product_images/',null=True,blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png','jpg'])])
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='mahsulot'
        verbose_name_plural='mahsulotlar'
        