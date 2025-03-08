import json
import os
accounts_json = {"site": "",
"email": "",
"password": ""
}
def verify_accountfile():
    try:
        if not os.path.isfile("accounts.json"):
            write_accountfile()
            print("Archivo accounts.json agregado al path")
        if os.stat("accounts.json").st_size == 0:
            write_accountfile()
            print("Estructura json establecida")
        return True
    except Exception as jsone:
        print(f"Exepcion en accountsfile {jsone}")
def write_accountfile():
    with open("accounts.json", "w", encoding="utf-8") as file:
        json.dump(accounts_json, file, indent=4)
