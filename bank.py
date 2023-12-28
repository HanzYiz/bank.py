import json
import os
import platform
import time
import sys

def clear_terminal():
    current_platform = platform.system()
    if current_platform == 'Windows':
        os.system('cls')  # Membersihkan layar terminal di Windows
    else:
        os.system('clear')  # Membersihkan layar terminal di MacOS/Linux
def account():
    username = input("Masukan Username anda : ")
    password = input("Masukan Password anda : ")
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
    print("Akun berhasil di buat!")
    clear_terminal()

def login():
    with open('accounts.json', 'r') as file:
        account_data = json.load(file)

    userlog = input("Username yang ingin dimasuki: ")
    passlog = input("Password yang ingin dimasuki: ")

    if userlog in account_data and passlog == account_data[userlog]['password']:
        print("\nLogin Berhasil")
        time.sleep(5)
        clear_terminal()
        main()
    else:
        print("Invalid username dan password! Silahkan coba lagi\n")
        time.sleep(2)
        clear_terminal()
def tarik_saldo():
     with open('accounts.json', 'r+') as file:
        account_data = json.load(file)
        username = input("Masukkan username anda: ")
        if username in account_data:
            saldo = account_data[username]['balance']
            account = input("Masukkan Username transfer : ")
            nominal = int(input("Nominal yang ingin di transfer : "))
            minimal_transfer = 50000
            
            if nominal == minimal_transfer and nominal <= saldo:
                if account in account_data:
                    account_data[username]['balance'] -= nominal
                    account_data[account]['balance'] += nominal
                    with open('accounts.json', 'w') as file:
                        json.dump(account_data, file, indent=4)
                    print("Transfer berhasil!")
                    time.sleep(3)
                    clear_terminal()
                else:
                    print("Akun penerima tidak ditemukan!")
                    time.sleep(3)
                    clear_terminal()
            elif nominal < minimal_transfer:
                print(f"Minimal transfer adalah {minimal_transfer}")
                time.sleep(3)
                clear_terminal()
            else:
                print("Maaf, saldo tidak mencukupi!")
                time.sleep(3)
                clear_terminal()
        else:
            print("Username tidak ditemukan!")
            time.sleep(3)
            clear_terminal()


def deposit():
    with open('accounts.json', 'r+') as file:
        account_data = json.load(file)
        username = input("Masukkan username anda: ")
        addsaldo = int(input("Masukan saldo yang anda akan deposit : "))
        if username in account_data:
            account_data[username]['balance'] += addsaldo
            with open('accounts.json', 'w') as file:
                json.dump(account_data, file, indent=4)
            print("Berhasil menambahkan saldo!")
            time.sleep(5)
            clear_terminal()
        else:
            print("Username tidak ditemukan!\n")
            time.sleep(2)
            clear_terminal()
def transfer():
    with open('accounts.json', 'r+') as file:
        account_data = json.load(file)
        username = input("Masukkan username anda: ")
        if username in account_data:
            saldo = account_data[username]['balance']
            account = input("Masukkan Username transfer : ")
            nominal = int(input("Nominal yang ingin di transfer : "))
            if nominal <= saldo:
                if account in account_data:
                    account_data[username]['balance'] -= nominal
                    account_data[account]['balance'] += nominal
                    with open('accounts.json', 'w') as file:
                        json.dump(account_data, file, indent=4)
                    print("Transfer berhasil!\n")
                    time.sleep(5)
                else:
                    print("Akun penerima tidak ditemukan!\n")
                    time.sleep(2)
                    clear_terminal()
            else:
                print("Maaf saldo tidak mencukupi!\n")
                time.sleep(2)
                clear_terminal()
        else:
            print("Username tidak ditemukan!\n")
            time.sleep(2)
            clear_terminal()



def lihat_saldo():
    with open('accounts.json', 'r') as file:
        account_data = json.load(file)
        username = input("Masukkan username anda: ")
        if username in account_data:
            saldo = account_data[username]['balance']
            print("Saldo anda = ", saldo)
            time.sleep(5)
            clear_terminal()
        else:
            print("Username tidak ditemukan!")
            time.sleep(2)
            clear_terminal()

def logout():
    a = input("Apakah anda ingin benar-benar keluar ? atau balik ke menu akun login ? (Y/N) : ")
    if a == 'y' or a=='Y':
        sys.exit("Terimakasih telah menggunakan script HanzYiz")
        time.sleep(3)
        clear_terminal()
    elif a == 'n' or a=='N':
        punya_akun()
def main():
    while (1):
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
        elif pilihan == "3":
            transfer()
        elif pilihan == "4":
            lihat_saldo()
        elif pilihan == "5":
            logout()
        else :
            print("\nPilihan Anda Tidak Terdaftar\nSilahkan Coba Lagi.")
            time.sleep(2)
            clear_terminal()
def punya_akun():
    while (1):
        a = input("apakah anda sudah mempunyai akun ? (Y/N) : ")
        if a == "Y" or a == "y":
            login()
        elif a == "N" or a =="n":
            account()
        else:
            print("Pilihanmu salah, coba lagi.")
            time.sleep(3)
            clear_terminal()

while True:
    punya_akun()
