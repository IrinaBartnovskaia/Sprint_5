from faker import Faker

faker = Faker()

def generate_valid_registration_data():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return name, email, password  # Возвращаем кортеж

def generate_registration_data_with_invalid_passwords():
    name = faker.name()
    email = faker.email()
    password = faker.password(length=2, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return name, email, password