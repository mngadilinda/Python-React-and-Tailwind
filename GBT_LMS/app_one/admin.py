from django.contrib import admin
from .models import Program, Module, Lesson

# Register your models here.

admin.site.register(Program)
admin.site.register(Module)
admin.site.register(Lesson)