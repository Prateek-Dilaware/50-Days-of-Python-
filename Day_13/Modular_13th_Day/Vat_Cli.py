# User interface 
from Mod.Vat_Cal import price_and_vat

def user_input():
    while True:
        try :
            price = float(input("Enter the price of item : "))
            vat = float(input("Enter the vat : "))
            return price_and_vat(price,vat)
        except ValueError:
            print("Invalid input. Please enter a number for the price and vat.")
            
def main():
    total_price = user_input()
    print(f"The total price is {total_price:.2f}")

if __name__ == "__main__":
    main()