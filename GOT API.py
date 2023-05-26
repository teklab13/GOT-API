import requests
import json
from win10toast import ToastNotifier
import sqlite3

character = input("Enter Character Name: ")

url = "https://api.gameofthronesquotes.xyz/v1/characters"
response = requests.get(url)
headers = response.headers
# print("Headers:", headers)
# status_code = response.status_code
# print("Status Code:", status_code)
#
if response.status_code == 200:
    d = response.json()
    for char in d:
        if char['name'].lower() == character.lower():
            quoutes = ", ".join(char['quotes'])
            print("Quotes:", quoutes)



            conn = sqlite3.connect('got.db')
            cursor = conn.cursor()


            cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                                          (name TEXT, quotes TEXT)''')
            cursor.execute("INSERT INTO characters VALUES (?, ?)",
                           (character, quoutes))

            conn.commit()
            conn.close()

            toaster = ToastNotifier()
            notification_title = "Character Information"
            notification_message = f"Name: {character}\nquotes: {quoutes}"
            toaster.show_toast(notification_title, notification_message)

            break
    else:
        print("Character is not available")
else:
    print("!")
# json_string = json.dumps(response.text)
# file_path = "tekla.json"
# with open(file_path, "w") as json_file:
#     json_file.write(json_string)
# print("JSON file created successfully.")