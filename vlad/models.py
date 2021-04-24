from django.db import models
from users.models import User
from reports.models import ExcelFile


class VladModels(models.Model):
    from_whom = models.ForeignKey(User, max_length=64, verbose_name='От кого', on_delete=models.CASCADE)
    user_exel_file = models.ForeignKey(ExcelFile, verbose_name='Файл пользователя', on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Было добавлено')

    def __str__(self):
        return f'{self.from_whom} отправил файл {self.user_exel_file} в {self.add_time}'

    class Meta:
        verbose_name = 'заказ посетителей'
        verbose_name_plural = 'заказы посетителей'
