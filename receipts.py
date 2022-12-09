import csv
from datetime import datetime

def main():
    current_date_and_time = datetime.now()
    PRODUCTS_INDEX=0
    products_dict=read_dict("products.csv", PRODUCTS_INDEX)
    
    # print(products_dict)
    PRODUCT_NUM_INDEX=0
    QUANTITY_INDEX=1
    total_quantity=0
    subtotal=0
    total_amount=0
    sales_tax=float(0.92)
    print()
    print("Hello! Welcome to your online shopping experience!")
    print()
    print("YOUR RECEIPT:")
    with open("request.csv", "rt") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            product_number = row_list[PRODUCT_NUM_INDEX]
            product_quantity = int(row_list[QUANTITY_INDEX])
            quantity=int(row_list[QUANTITY_INDEX])
            product_name = products_dict[product_number]
            print(f"{product_name[1]}: {product_quantity} @ {product_name[2]}")
            total_quantity += quantity
            subtotal +=float(quantity) * float(product_name[2])
            total_amount = subtotal + sales_tax
            
        print()
        print(f"Number of Items: {total_quantity}")
        # print(f"Sales Tax: {sales_tax}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax}")
        print(f"Total: ${total_amount}")
        print()
        print("Thank you for shopping with us today, come again soon!")
        print(f"{current_date_and_time:%A %I:%M %p}")

def read_dict(filename, key_column_index):

    dictionary= {}
    with open(filename, "rt") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)

        for row_list in reader:

            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()