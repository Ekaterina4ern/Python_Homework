from mailing import Mailing
from address import Address

to_addr = Address(index=123456, city="Москва", street="Ленина", house=10, apartment=5)
from_addr = Address(index=654321, city="Санкт-Петербург", street="Невский проспект", house=20, apartment=10)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="TRACK123456"
)

print(f"""
Отправление {mailing.track}
из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}
в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}.
Стоимость {mailing.cost} рублей.
""")