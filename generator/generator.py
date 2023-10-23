from random import randint


from data.data import Person, Color, Date
from faker import Faker

fake = Faker()

def generated_person():
    yield Person(
        full_name=fake.name() + " " + fake.name(),
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        age=randint(10, 80),
        salary=randint(10000, 100000),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address().replace('\n', ' ').replace('\r', ''),
        permanent_address=fake.address().replace('\n', ' ').replace('\r', ''),
        mobile=fake.msisdn(),
    )
def generated_file():
    path = rf'C:\pythonProject\registration_form\testfile.txt'
    file = open(path,'w+')
    file.write(f'Hello World')
    file.close()
    return file.name,path


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00"
    )
