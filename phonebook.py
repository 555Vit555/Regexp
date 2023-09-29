from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
   rows = csv.reader(f, delimiter=",")
   contacts_list = list(rows)
##pprint(contacts_list)
#pprint(contacts_list[1][0])
#contacts_list1 = list(filter(lambda x: x != '', contacts_list))
sorted_contacts_list = []
flattened_list = []
for i in contacts_list:
    i = list(filter(lambda x: x != '', i))
    
    i[0] = i[0].split(' ')
    print(i[0])
    # for sublist in sorted_contacts_list:
    #     print(sublist)
        #flattened_list.extend(sublist)
    #print(flattened_list)
        #print(i[0])
    sorted_contacts_list.append(i)
    

    
#     #i.remove('')
    
#     #print(i[0])
#     # if re.findall(r".{4}\s?[А-Я].{4}\s?[А-Я]",i[0]) is True:
#     #     i[0] = re.split(" ",i[0])
#     # for g in i:
#     #     if re.findall(r".{4}\s?[А-Я].{4}\s?[А-Я]", g):
    #         print(g)
    #print(i[0])
    # for g in i[0]:
    #     print(g)
    #print(i)
#     nested_list = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# extracted_list = [item for sublist in nested_list for item in sublist]
#sorted_contacts_list1 = [i for sublist in sorted_contacts_list for i in sublist]
#print(sorted_contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
  
# ## Вместо contacts_list подставьте свой список:
#   datawriter.writerows(contacts_list)


#######-----------------------------------------------------------------------------------
# import re

# def fix_phonebook(phonebook):
#     # Создаем словарь для хранения уникальных записей
#     unique_records = {}

#     for record in phonebook:
#         # Извлекаем Фамилию, Имя и Отчество из записи
#         name_match = re.match(r'([\w\s-]+),([\w\s-]+),([\w\s-]+)', record)
#         lastname = name_match.group(1).strip()
#         firstname = name_match.group(2).strip()
#         surname = name_match.group(3).strip()

#         # Приводим телефон к нужному формату
#         phone_match = re.search(r'(\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\s?доб.?\s?(\d+)?', record)
#         phone = "+7({}){}-{}-{}".format(phone_match.group(2), phone_match.group(3), phone_match.group(4), phone_match.group(5))
#         if phone_match.group(6):
#             phone += " доб.{}".format(phone_match.group(6))

#         # Объединяем записи о человеке в одну
#         key = (lastname, firstname, surname)
#         if key in unique_records:
#             unique_records[key]['phone'].append(phone)
#         else:
#             unique_records[key] = {'lastname': lastname, 'firstname': firstname, 'surname': surname, 'phone': [phone]}

#     # Формируем отформатированную адресную книгу
#     formatted_phonebook = []
#     for record in unique_records.values():
#         lastname = record['lastname']
#         firstname = record['firstname']
#         surname = record['surname']
#         phone = ', '.join(record['phone'])
#         formatted_record = "{},{},{},{}".format(lastname, firstname, surname, phone)
#         formatted_phonebook.append(formatted_record)

#     return formatted_phonebook