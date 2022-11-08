import datetime
from credit.models import Account, Client, Credit

client_1 = Client.objects.create(name='Berdiev N.D', citizenship='KG', birth_year=datetime.date(1994, 1, 1),
                                 work_place='Codify')
client_2 = Client.objects.create(name='Apazbekov A.A', citizenship='KG', birth_year=datetime.date(2001, 1, 10),
                                 work_place='Codify')

account_1_1 = Account.objects.create(number=12345, account_type=1, client=client_1)
account_1_2 = Account.objects.create(number=123456, account_type=2, client=client_1)

account_2_1 = Account.objects.create(number=1234567, account_type=1, client=client_2)
account_2_2 = Account.objects.create(number=12345678, account_type=2, client=client_2)

credit_1_1 = Credit.objects.create(sum=10100, account=account_1_1)
credit_1_2 = Credit.objects.create(sum=10200, account=account_1_2)
credit_2_1 = Credit.objects.create(sum=20100, account=account_2_1)
credit_2_2 = Credit.objects.create(sum=20200, account=account_2_2)
