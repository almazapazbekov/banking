from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    citizenship = models.CharField(max_length=20, default='Кыргызстан', null=False, blank=False)
    birth_year = models.DateField(null=False, blank=False)
    work_place = models.CharField(max_length=30, null=False, blank=False)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'имя: {self.name}, гражданин: {self.citizenship}, г.р: {self.birth_year}, место работы:' \
               f' {self.work_place} --- {self.update_date}'


class Account(models.Model):
    number = models.IntegerField(max_length=16, unique=True, null=False, blank=False)
    account_type = models.IntegerField(default=1, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'#{self.number} -- {self.account_type} -- {self.client.name}'


class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'ФИО: {self.account} - сумма кредита: {self.sum} - дата:{self.date}'

