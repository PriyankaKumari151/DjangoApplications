from django.contrib import admin
from .models import Room, Message
# Register your models here.
#password for the super user is admin@chat123

admin.site.register(Room)
admin.site.register(Message)