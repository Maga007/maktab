from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    title = models.CharField('Ismi', max_length=255)
    image = models.ImageField('Rasmi', blank=True, null=True)
    content = models.TextField('O\'qituvchi haqida')
    position = models.CharField('Lavozimi', max_length=100)
    phone = models.IntegerField('Tel raqami', default="+998 99 999-99-99")
    sertificat = models.BooleanField('Sertifikat', default=False)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    
class Circle(models.Model):
    title = models.CharField('Nomi', max_length=255)
    image = models.ImageField('Rasmi', blank=True, null=True)
    content = models.TextField('to\'garak haqida')
    phone = models.IntegerField('Tel raqami', default='+998 (99) 999-99-99')
    price = models.IntegerField('Narxi', null=True)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'circle'
        verbose_name_plural = 'circles'

    
class New(models.Model):
    title = models.CharField('Nomi', max_length=255)
    image = models.ImageField('Rasmi', blank=True, null=True)
    content = models.TextField('Yangilik haqida')
    date = models.DateTimeField('Sana', default=timezone.now)
    country = models.BooleanField('Chet el bilan shartnoma', default=False)

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'

class Info(models.Model):
    title = models.CharField('Maktab yo\'nalishi haqida qisqacha', max_length=255, null=True)
    student = models.IntegerField('O\'quvchilar soni', default=0)
    certif = models.IntegerField('Sertifikatli o\'qituvchilar soni', default=0)
    teacher = models.IntegerField('O\'qituvchilar soni', default=0)
    klas = models.IntegerField('Sinflar soni', default=0)
    date = models.DateTimeField('sanasi', default=timezone.now)

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'infos'


class Instagram(models.Model):
    title = models.CharField('Nomi', max_length=255)
    image = models.ImageField('Rasm', blank=True, null=False)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'Instagram'
        verbose_name_plural = 'Instagrams'


class Meeting(models.Model):
    title = models.CharField('Nomi', max_length=255)
    image = models.ImageField('Rasm', blank=True, null=False)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'

    
class Event(models.Model):
    title = models.CharField('Nomi', max_length=255)
    image = models.ImageField('Rasm', blank=True, null=False)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'


class Director(models.Model):
    title = models.CharField('Nomi', max_length=255)
    content = models.TextField('Director haqida', null=True)
    email = models.EmailField('Email', blank=True, null=False)
    image = models.ImageField('Rasm', blank=True, null=False)
    birthday = models.DateTimeField('tug\'ilgan sanasi', null=True)
    phone = models.CharField('Telefoni', max_length=255, blank=True, null=False)
    address = models.CharField('Adresi', max_length=255, blank=True, null=False)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'director'
        verbose_name_plural = 'directors'

