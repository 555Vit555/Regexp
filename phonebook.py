from pprint import pprint
import re
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout.encoding = 'utf-8'
with open("phonebook_raw.csv", encoding="utf-8") as f:
   rows = csv.reader(f, delimiter=",")
   contacts_list = list(rows)

pattern= r"(\['?[А-Я]{1}[а-я]+'?\]?),?\s?('?[А-Я]{1}[а-я]+'?\]?)?,?\s?('?[А-Я]{1}[а-я]+'?\]?)?"

pattern_tel = r"[']{1}(\+7|8)\s?(\(?\d{3})\)?\-?\s?(\d{3})\s?\-?(\d{2})\s?\-?(\d{2})(\s?\-?\(?.доб\.)?\s?(\d+)?" 
sorted_contacts_list = []
unique_records = {}
result_phonebook = []
sorted_contacts_list.append(contacts_list[0])

for record in contacts_list:
        #print(record)
    
        name_match = re.match(pattern, str(record))
        i = []
        
        if name_match:
            lastname = name_match.group(1).strip("[]'")
            firstname = name_match.group(2).strip("[]'")
            if name_match.group(3):
                surname = name_match.group(3).strip("[]'")
            i = (lastname + ',' + firstname + ',' + surname + ',').split(',')
            i = i + record[3:5]
            sorted_contacts_list.append(i)
             # Приводим телефон к нужному формату
        
            phone_match = re.search(pattern_tel, str(record))
            if phone_match is not None:
                
                phone = "+7({}){}-{}-{}".format(phone_match.group(2), phone_match.group(3), phone_match.group(4), phone_match.group(5))
                if phone_match.group(7):
                    phone += " доб.{}".format(phone_match.group(7))
            else:    phone = ""  
            #print(record[3])
            # Добавляем организации, должность и мыло
            organization = record[3]
            position = record[4]
            email = record[6]
        #         # Объединяем записи о человеке в одну
            key = (lastname, firstname, surname)
            if key in unique_records:
                unique_records[key]['phone'].append(phone)
                unique_records[key]['phone'].append(position)
            else:
                unique_records[key] = {'lastname': lastname, 'firstname': firstname, 'surname': surname, 'organization': organization, 'position': position,'phone': [phone], 'email': email}
            
            # Формируем отформатированную адресную книгу
            formatted_phonebook = []
            for record in unique_records.values():
                lastname = record['lastname']
                firstname = record['firstname']
                surname = record['surname']
                organization = record['organization']
                position = record['position']
                phone = ', '.join(record['phone'])
                email = record['email']
                formatted_record = "{},{},{},{},{},{},{}".format(lastname, firstname, surname, organization, position, phone, email)
                formatted_phonebook.append(formatted_record)
#print(formatted_phonebook[0])
for i in formatted_phonebook:
    #print(list(i.split(',')))
    result_phonebook.append(list(i.split(',')))

#print(result_phonebook)        




# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter='\n')
  

  datawriter.writerow(result_phonebook)


