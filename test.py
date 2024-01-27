from collections import UserDict

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def __iter__(self, batch_size=1):
        keys = list(self.data.keys())
        num_keys = len(keys)
        start = 0

        while start < num_keys:
            end = min(start + batch_size, num_keys)
            yield {key: self.data[key] for key in keys[start:end]}
            start = end

# Приклад використання:
address_book = AddressBook()
address_book.update({"contact1": "John Doe", "contact2": "Jane Doe", "contact3": "Bob Smith", "contact4": "Alice Smith"})

# Вивід N записів за одну ітерацію
for batch in address_book:
    print(batch)