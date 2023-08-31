from django.db import models

class Orders(models.Model):
    order_choices = (
        ('puyun', '补运'),
        ('pucaiku', '补财库'),
        ('kongzi', '孔子'),
        ('taisui', '太岁')
    )
    account = models.ForeignKey('users.AccountUser', on_delete=models.CASCADE)
    member = models.ForeignKey('users.Member', on_delete=models.CASCADE)
    order_type = models.CharField(max_length=255, choices=order_choices)
    
    def get_order_choices(self):
        return self.order_choices
    
    def __str__(self):
        return self.order_type
       