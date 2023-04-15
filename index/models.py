from django.db import models

# Create your models here.

### ORM Object relational mapping - ứng với một bảng trong database là 1 class trong python
# ứng với 1 dòng dữ liệu trong bảng là 1 object trong python
class GroupProduct(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    group = models.ForeignKey(GroupProduct, on_delete=models.CASCADE, null=True)

# python manage.py makemigrations - tạo file lưu sự thay đổi
# python manage.py migrate - đưa thay đổi lên sql server

# python manage.py shell - vào những câu lệnh của django qua terminal