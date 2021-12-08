users = {}
emails = ['abcd@gmail.com', 'efgh@outlook.com', 'xyz@hotmail.com']

# list -> concatenação dos e-mails na tupla
# enumerate -> numerar cada email
tupla = list(enumerate(emails))

for values in range(0,len(tupla)):
    print("Email: ", tupla[values][1])
    users[tupla[values]] = [input("Digite o nome: "), input("Digite o nível: ")]

for (values, data) in users.items():
    print("Usuario.:", data[0])
    print("Email...:", data[1])
    print("Nome....:", data[0])
    print("Nível...:", data[1])

