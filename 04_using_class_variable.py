
class bank:
    bank_name = "National Bank"

    @classmethod
    def change_bank_name(cls , name):
        cls.bank_name = name

b1 = bank()
b2 = bank()

print("Initial Bank Name:" , b1.bank_name)
print("Initial Bank Name:" , b2.bank_name)

bank.change_bank_name("State Bank.")


print("After Changing:" , b1.bank_name)
print("After Changing:" , b1.bank_name)