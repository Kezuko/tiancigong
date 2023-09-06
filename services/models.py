from django.db import models
from django.utils import timezone

class Orders(models.Model):
    order_choices = (
        ('补运', '补运'),
        ('补财库', '补财库'),
        ('拜孔子', '拜孔子'),
        ('安太岁', '安太岁'),
        ('接财神', '接财神'),
        ('拜天狗', '拜天狗'),
        ('拜無鬼', '拜無鬼'),
        ('拜天宫', '拜天宫')
    )
    progress = (
        ("In Progress","In Progress"),
        ("Completed","Completed")
    )
    account = models.ForeignKey('users.AccountUser', on_delete=models.CASCADE)
    member = models.ManyToManyField('users.Member')
    order_type = models.CharField(max_length=255, choices=order_choices)
    status = models.CharField(max_length=50, choices=progress, default="In Progress")
    order_number = models.CharField(max_length=12, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_order_choices(self):
        return self.order_choices
        
    def get_progress(self):
        return self.progress
    
    def __str__(self):
        return self.order_type
       