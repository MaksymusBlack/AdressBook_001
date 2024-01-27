from collections import UserDict
from datetime import date, datetime

class Field:
    def __init__(self, value):
        self.value = value
    

    ## Якщо я правильно зрозумів завдання, тут теж мають бути property та setter
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
            self.__value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        
   

class Phone(Field):
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if value.isdigit() and len(value) == 10:
            self.__value = value
        else:
            raise ValueError
        
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value
    

    ##  Клас для дня народження
class Birthday(Field):
    def __init__(self, value):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = datetime.strptime(value, '%d.%m.%Y')

    
    def __str__(self):
        return str(self.__value.strftime('%d %B %Y'))
    
    

class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        if birthday:
            self.birthday = Birthday(birthday) 
   
    ##    Додавання телефону 
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))            

    ##   Видалення номеру 
    def remove_phone(self, number):
        self.phones.remove(Phone(number))
    
    ##   Функція зміни номеру, з попередньою валідацією нового номера та вийнятком, якщо не було знайдено старий номер у списку
    def edit_phone(self, old_number, new_number):
        self.phones[self.phones.index(Phone(old_number))] = Phone(new_number)

    ##   Функція для пошуку номера телефону
    def find_phone(self, number):
        if Phone(number) in self.phones:
            return Phone(number)
        else:
            print("Number is not found")

   ## Функція для розрахунку кількості днів до наступного дня народження
    def days_to_birthday(self):
        current_day = date.today()
        current_birthday =  date(year=current_day.year, month=self.birthday.value.month, day=self.birthday.value.day)
        if current_day > current_birthday:
            current_birthday =  date(year=current_day.year + 1, month=self.birthday.value.month, day=self.birthday.value.day)
        number_of_days = current_birthday - current_day
        return f" Days to the next birthday: {number_of_days.days}"
    

    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    ## Ця частина для того, щоб при ітерації частина self.data[key] видавала коректне значення, і у випадку, якщо є день народження, його теж відображатиме
    def __repr__(self):
        if self.birthday != None:
            return f"phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
        return f"phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    ##   Додавання нового контакту
    def add_record(self, record): 
        self.data.update({record.name.value : record})

    ##   Пошук номеру телефона
    def find(self, name):
        try:      
           return self.data[name]
        except KeyError:
            print("The name is not in the Address Book")

   ## Видалення контакта
    def delete(self, name):
        try:
            del self.data[name]
        except KeyError:
            print("The name is not in the Address Book")
    
    ##  Ітератор за одну ітерацію повертає уявлення для N записів.
    def __iter__(self, N = 1):
        keys = list(self.data.keys())
        num_keys = len(keys)
        start = 0
        while start < num_keys:
            end = min(start + N, num_keys)
            yield {key: self.data[key] for key in keys[start:end]}
            start = end
