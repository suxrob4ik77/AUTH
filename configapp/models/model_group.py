from django.db import models
from ..models import *
from .auth_users import *

class Day(BaseModel):
    title=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title


class Rooms(BaseModel):
    title=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.title


class TableType(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

class TableStudent(BaseModel):
    start_time=models.TimeField()
    end_time = models.TimeField()
    room=models.ForeignKey(Rooms,on_delete=models.RESTRICT)
    type=models.ForeignKey(TableType,on_delete=models.RESTRICT)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.start_time.__str__()+" "+self.end_time.__str__()


class GroupStudent(BaseModel):
    title=models.CharField(max_length=50,unique=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    teacher=models.ManyToManyField(Teacher,related_name='teacher')
    table=models.ForeignKey(TableStudent,on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discriptions = models.CharField(max_length=500, null=True, blank=True)
    start_time=models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.title


