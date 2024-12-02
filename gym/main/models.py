from email.policy import default

import django.utils.timezone
from django.db import models



class Groups(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название группы', default='karamba')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Группа мышц'
        verbose_name_plural = 'Группы мышц'

class TrenirovkaGroup(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата тренировки', default=django.utils.timezone.now())

    def __str__(self):
        return str(self.date) + str(self.group)

    class Meta:
        verbose_name = 'Тренировка группа'
        verbose_name_plural = 'Тренировки группа'

class Upragneniya(models.Model):

    class GroupMuscular(models.TextChoices):
        GROUP1 = '1', 'Грудь'
        GROUP2 = '2', 'Спина'
        GROUP3 = '3', 'Ноги'
        GROUP4 = '4', 'Трицепс'
        GROUP5 = '5', 'Бицепс'
        GROUP6 = '6', 'Плечи'
        GROUP7 = '7', 'Шея'
        GROUP8 = '8', 'Пресс'



    name = models.CharField(max_length=300, default='Без названия', verbose_name='Название упражнения')

    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    group_muscular = models.CharField(choices=GroupMuscular.choices, default=GroupMuscular.GROUP1, max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Trenirovka(models.Model):
    class Levels(models.TextChoices):
        LEVEL1 = '0', 'Легкий'
        LEVEL2 = '1', 'Средний'
        LEVEL3 = '2', 'Тяжелый'
        LEVEL4 = '3', 'Проходка'


    class Status(models.TextChoices):
        STATUS1 = '0', 'Не выполнено'
        STATUS2 = '1', 'Выполнено'
    date = models.DateField(verbose_name='Дата тренировки', default=django.utils.timezone.now())
    name = models.ForeignKey(to=Upragneniya, on_delete=models.CASCADE)
    group = models.ForeignKey(to=Groups, on_delete=models.CASCADE, default='1', verbose_name='Группы мышц')
    max_weight = models.CharField(max_length=100, default='0', verbose_name='Максимальный вес')
    amount1 = models.IntegerField(verbose_name='Количество подходов разминка', default=2)
    povtor1 = models.IntegerField(verbose_name='Количество повторений разминка', default=6)
    povtor2 = models.IntegerField(verbose_name='Количество повторений тренировка', default=4)
    amount2 = models.IntegerField(verbose_name='Количество подходов тренировка', default=4)
    level = models.CharField(choices=Levels.choices, default=Levels.LEVEL1, max_length=50)
    status = models.CharField(choices=Status.choices, default=Status.STATUS1, max_length=50)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'