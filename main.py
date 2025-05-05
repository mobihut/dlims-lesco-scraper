from dlims_scraper import verify_license
from lesco_scraper import get_bill_details

def main():
    choice = input("Konsi service chahte hain? (1: DLIMS License, 2: LESCO Bill): ")
    
    if choice == '1':
        cnic = input("CNIC dijiye (without dashes): ")
        license_number = input("License number dijiye: ")
        result = verify_license(cnic, license_number)
        print(result)
    elif choice == '2':
        reference = input("LESCO reference number dijiye: ")
        result = get_bill_details(reference)
        print(result)
    else:
        print("Ghalat chuno. 1 ya 2 daaliye.")

if __name__ == "__main__":
    main()
