import random


def generate_random_phone():
    phone = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(9, 9)))
    return f'+79{phone}'


def generate_random_name():
    name = ''.join(random.choice('абвгдежзиклмнопрстуфхцч') for i in range(1, 4))
    return f'А{name}жан'


def generate_random_lastname():
    lastname = ''.join(random.choice('абвгдежзиклмнопрстуфхцч') for i in range(1, 3))
    return f'И{lastname}беков'


def generate_random_address():
    house = ''.join(str(random.randint(0, 9)) for _ in range(random.randint(2, 2)))
    street = ''.join(random.choice('абвгдежзиклмнопрстуфхцч') for i in range(1, 4))
    return f'Улица {street}вая, дом {house}'
