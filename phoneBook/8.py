def print_result(PB):
	print()
	i = 1
	for abonent in PB:
		print(i,'.',end=' ',sep='')
		i+=1
		print("Фамилия: "	,abonent['Фамилия']	,end="\t")
		print("Имя: "		,abonent['Имя']		,end="\t")
		print("Телефон: "	,abonent['Телефон']	,end="\t")
		print("Описание: "	,abonent['Описание'],end="")

def find_by_lastname(PB,lastName):
	res = []
	for abonent in PB:
		if abonent['Фамилия'] == lastName:
			res.append(abonent)
	return res

def find_by_number(PB,number):
	res = []
	for abonent in PB:
		if abonent['Телефон'] == number:
			res.append(abonent)
	return res

def change_number(PB,lastName,newNumber):
	fined = find_by_lastname(PB,lastName)
	if len(fined) == 0:
		return "Не найден"
	else:
		for abonent in fined:
			abonent['Телефон'] = newNumber
	return "Успешно"
	
def add_user(PB,userData):
	fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
	record = dict(zip(fields, userData.split(',')))
	record['Описание'] += '\n'
	PB.append(record)
	return "Успешно"

def delete_by_lastname(PB,lastName):
	forDelete = []
	for abonent in PB:
		if abonent['Фамилия'] == lastName:
			forDelete.append(abonent)
	if len(forDelete) != 0:
		for value in forDelete:
			PB.remove(value)
		return "Успешно"
	return "Не найден"

def work_with_phonebook():
	choice=show_menu()

	phone_book=read_txt('phonebook.txt')

	while (choice!=8):

		if choice==1:
			print_result(phone_book)
		elif choice==2:
			last_name=input('lastname ')
			print(find_by_lastname(phone_book,last_name))
		elif choice==3:
			number=input('number ')
			print(find_by_number(phone_book,number))
		elif choice==4:
			last_name=input('lastname ')
			new_number=input('new  number ')
			print(change_number(phone_book,last_name,new_number))
		elif choice==5:
			user_data=input('new data (last name,first name,number,other)')
			print(add_user(phone_book,user_data))
		elif choice==6:
			last_name=input('lastname ')
			print(delete_by_lastname(phone_book,last_name))
		elif choice==7:
			print(write_txt('phonebook.txt',phone_book))

		choice=show_menu()

def show_menu():
	print("\n\nВыберите необходимое действие:\n"
		  "1. Отобразить весь справочник\n"
		  "2. Найти абонента по фамилии\n"
		  "3. Найти абонента по номеру телефона\n"
		  "4. Изменить данные\n"
		  "5. Добавить абонента в справочник\n"
		  "6. Удалить абонента\n"
		  "7. Сохранить справочник в текстовом формате\n"
		  "8. Закончить работу")
	choice = int(input())
	return choice

def read_txt(filename): 

	phone_book=[]

	fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	with open(filename,'r',encoding='utf-8') as phb:

		for line in phb:
			if len(line) > 1:
				record = dict(zip(fields, line.split(',')))
				phone_book.append(record)	

	return phone_book

def write_txt(filename , phone_book):

	with open('phonebook.txt','w',encoding='utf-8') as phout:

		for i in range(len(phone_book)):

			s=''
			for v in phone_book[i].values():

				s = s + v + ','

			phout.write(f'{s[:-1]}\n')
	return "Успешно"

work_with_phonebook()