import json
import os
import platform

def clear_terminal():
    current_platform = platform.system()
    if current_platform == 'Windows':
        os.system('cls')  # Membersihkan layar terminal di Windows
    else:
        os.system('clear')  # Membersihkan layar terminal di MacOS/Linux
def account():
    username = input("Masukan Username anda : ")
    password = input ("Masukan Password anda : ")
    balance = 0 
    account_data = {
        'username': username,
        'password': password,
        'balance': balance
    }
    
    with open('accounts.json', 'r+') as file:
        all_accounts = json.load(file)
        all_accounts[username] = account_data
        file.seek(0)
        json.dump(all_accounts, file, indent=4)
        file.truncate()
    clear_terminal()
def login():
    with open('account.json', 'r') as file:
        account_data = json.load(file)
    while True:
        userlog = input("Username yang ingin di masuki : ")
        passlog = input("Password yang ingin di masuki : ")
        if userlog == account_data['username'] and passlog == account_data['password']:
            print("\nLogin Berhasil")
            clear_terminal()
        else :
            print("Invalid username dan password! silahkan coba lagi")
def tarik_saldo ():
    global saldo
    with open('account.json', 'r') as file:
        account_data = json.load(file)
    minimal_tarik = 50000
    jumlah_tarik = int(input("Jumlah uang yang akan ditarik : "))
    if account_data['balance'] >= minimal_tarik:
        account_data['balance'] -= minimal_tarik
        saldo = account_data['balance']
        with open('account.json', 'w') as file:
            account_data = json.load(file)
    else :
        print("Saldo tidak mencukupi!")

def deposit():
    global saldo
    with open('account.json', 'r') as file:
        account_data = json.load(file)
    addsaldo = int(input("Masukan saldo yang anda akan deoposit : "))
    account_data['balance'] += addsaldo
    with open('account.json', 'w') as file:
        account_data = json.load(file)
    clear_terminal()
def Transfer():
    with open('account.json', 'r') as file:
        all_accounts = json.load(file)
    saldo = account_data['balance']
    account = input("Masukan Username transfer : ")
    nominal = int(input("Nominal yang ingin di transfer : "))
    if nominal >= account_data['balance']:
        if account == account_data['username']:
            saldo += nominal

        

def main():
    print("=======================================")
    print("|   Selamat datang di bank HanzYiz    |")
    print("=======================================")
    print("|              Menu Utama             |")
    print("=======================================")
    print("|  1. Tarik saldo                     |")
    print("|  2. Deposit saldo                   |")
    print("|  3. Transfer                        |")
    print("|  4. Lihat Saldo                     |")
    print("|  5. Logout                          |")
    print("=======================================")
    pilihan = input("Masukan Pilihan anda 1/2/3/4/5 : ")
    
    if pilihan == "1":
        tarik_saldo()
    elif pilihan == "2":
        deposit()
account()
login()