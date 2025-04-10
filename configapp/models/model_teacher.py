from django.db  import models
from .auth_users import *

class Course(BaseModel):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title


#Xodimlarning darajasini belgilash uchun
class Departments(BaseModel):
    title=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    descriptions=models.CharField(max_length=500,null=True,blank=True)
    search_fields=['user__phone','user__full_name']

    def __str__(self):
        return self.title


#Xodimlarning darajasini saqlash uchun yuqoridagilarni
class Teacher(BaseModel):
    user=models.OneToOneField(User,on_delete=models.RESTRICT,related_name="user")
    departments=models.ManyToManyField(Departments,related_name='get_department')
    course=models.ManyToManyField(Course,related_name='get_course')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    discriptions=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.user.phone
