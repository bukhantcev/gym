from datetime import datetime

from django import template

register = template.Library()

@register.filter(name='razminka1')
def razminka1(value):
    return round(int(value)*0.45)
@register.filter(name='razminka2')
def razminka2(value):
    return round(int(value)*0.55)
@register.filter(name='razminka3')
def razminka3(value):
    return round(int(value)*0.65)
@register.filter(name='tren1')
def tren1(value):
    return round(int(value)*0.6)
@register.filter(name='tren2')
def tren2(value):
    return round(int(value)*0.75)
@register.filter(name='tren3')
def tren3(value):
    return round(int(value)*0.9)




@register.filter(name='weekday')
def weekday(value: datetime):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье',]
    return days[value.weekday()]



@register.filter(name='razm_podhod1')
def razm1(value):
    return round(int(value) + 1)

@register.filter(name='razm_podhod2')
def razm2(value):
    return round(int(value) + 2)

@register.filter(name='razm_podhod3')
def razm3(value):
    return round(int(value) + 3)


@register.filter(name='tren_podhod1')
def podhod1(value):
    return round(int(value) - 1)

@register.filter(name='tren_podhod2')
def podhod2(value):
    return round(int(value) - 2)

@register.filter(name='tren_podhod3')
def podhod3(value):
    return round(int(value) - 3)


@register.filter(name='tren_povtor1')
def tren_povtor1(value):
    return round(int(value)*0.75)

@register.filter(name='tren_povtor2')
def tren_povtor2(value):
    return round(int(value) * 0.5)

@register.filter(name='tren_povtor3')
def tren_povtor3(value):
    return round(int(value) * 0.25)