from django.db import models

# Create your models here.


class Photo(models.Model):

    image = models.ImageField()
    discription = models.CharField(max_length=30, blank=True)  # 설명
    # blank는 빈칸으로 나두어도 된다는 속성
