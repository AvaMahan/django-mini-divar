from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    phone=models.CharField(max_length=15)
    image=models.ImageField(upload_to='ads/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
