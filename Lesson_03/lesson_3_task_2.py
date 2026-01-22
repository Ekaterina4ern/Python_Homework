from smartphone import Smartphone

catalog = []

catalog.append(Smartphone(brand='Apple', model='iPhone 14 Pro Max', phone_number='+79123456789'))
catalog.append(Smartphone(brand='Samsung', model='Galaxy S23 Ultra', phone_number='+79987654321'))
catalog.append(Smartphone(brand='Xiaomi', model='Redmi Note 11', phone_number='+79111111111'))
catalog.append(Smartphone(brand='Huawei', model='P50 Pro', phone_number='+79222222222'))
catalog.append(Smartphone(brand='Nokia', model='3310', phone_number='+79333333333'))

for item in catalog:
    print(f'{item.brand} - {item.model}. Номер телефона: {item.phone_number}')