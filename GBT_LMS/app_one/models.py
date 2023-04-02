from django.db import models

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    program_image = models.ImageField(upload_to='static/prorams/', blank=True, null=True)

    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    module_image = models.ImageField(upload_to='static/modules/', blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    text_lesson = models.TextField(blank=True, null=True)
    lesson_imgs = models.ImageField(upload_to='static/lessons/imgs',blank=True, null=True)
    lesson_vid = models.FileField(upload_to='static/lesson/video', blank=True, null=True)
    lesson_notes = models.FileField(upload_to='staticlesson/notes', blank=True, null=True)

    def __str__(self):
        return self.title
