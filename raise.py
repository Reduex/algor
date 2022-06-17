# # Bu Method ile exception yerine gelen tüm hataları ele alabilriz.

# # x = 10

# # if x > 5:
# #     raise Exception("X,5'den büyük değer alamaz")
# # else:
# #     print('Doğru bir bilgi girdiniz.')

# def check_password(psw):
#     import re # Bizim daha fazla "eğer" methpodu kullanabilmemeiz için regular Exception methodunu kullanmalıyız.
#     if len(psw) < 8:
#         raise Exception('Parola en az 7 karakter olmalıdır.')
#     elif not re.search('[a-z]', psw):
#         raise Exception('Parola küçük harf içermelidir.')
#     elif not re.search('[A-Z]', psw):
#         raise Exception('Parola da büyük harf olmalıdır.')
#     elif not re.search('[0-9]', psw):
#         raise Exception('Parola rakam içermelidir.')
#     elif not re.search('[_@$]', psw):
#         raise Exception('Parola da alpha numeric içermelidir.')
#     else:
#         print('Geçerli Parola Yukarıdaki Gibidir')

# password = "12345678aA@"    
# print('Parolada olan harf sayısı'),print(len(password))

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# finally:
#     print('validation tamamlandı.')

'''
 Hadi bir class ile de bir deneme yapalım..
'''

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            print('Validation tamamlandı...')
            print('"Name" alanına fazla karakter girdiniz.')
        else:
            self.name = name
            print('Validation tamamlandı')
            

p = Person('Onurrrrrrrrrrrrrr', 2005)