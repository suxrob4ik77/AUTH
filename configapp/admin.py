from django.contrib import admin
from .models import *

admin.site.register([Course,Department,GroupStudent,Teacher,User,Student,TableStudent,Rooms,TableType])

