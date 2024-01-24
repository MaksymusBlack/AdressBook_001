from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        
   

class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            self.value = value
        else:
            raise ValueError
        
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
   
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

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


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

