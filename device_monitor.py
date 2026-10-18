book_stocks = [28, 31, 35, 37, 29]
book_names = ["Python Programming","Computer Fundamentals","Introduction to Electronics","Discrete Mathematics","Digital Logic Design"]


def main_menu():
    while True:
        print("\nLIBRARY BOOK INVENTORY SYSTEM")
        print("----------------------------------")
        print("[1] View Books")
        print("[2] Add Book")
        print("[3] Borrow Book")
        print("[4] Return Book")
        print("[5] Generate Summary")
        print("[6] Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            kill_program()
        else:
            print("Invalid choice. Please try again.")


def kill_program():
    print("Thank you for using the Library Book Inventory System.")
    raise SystemExit


def return_menu():
    choice2 = input(
        '\nEnter "1" to return to the main menu or "2" to exit: '
    ).strip()

    if choice2 == "1":
        return
    elif choice2 == "2":
        kill_program()
    else:
        print("Invalid option. Returning to the main menu.")


def classify_book(stock):
    if stock == 0:
        return "OUT OF STOCK"
    elif stock <= 2:
        return "LOW STOCK"
    else:
        return "AVAILABLE"


def view_books():
    print("\nLIBRARY BOOK INVENTORY")
    print("----------------------")

    for i in range(len(book_names)):
        print("Book", i + 1, ":", book_names[i])
        print("Stock:", book_stocks[i])
        print("Status:", classify_book(book_stocks[i]))
        print()

    return_menu()


def add_book():
    new_name = input("Enter book title: ").strip()

    if new_name == "":
        print("Invalid book title.")
        return_menu()
        return

    for existing_name in book_names:
        if existing_name.lower() == new_name.lower():
            print("Book already exists.")
            return_menu()
            return

    quantity_text = input("Enter initial quantity: ").strip()

    if not quantity_text.isdigit():
        print("Invalid quantity. Enter a whole number.")
        return_menu()
        return

    new_quantity = int(quantity_text)

    if new_quantity <= 0:
        print("Quantity must be greater than zero.")
        return_menu()
        return

    book_names.append(new_name)
    book_stocks.append(new_quantity)

    print("Book added successfully.")
    return_menu()


def view_inventory_for_selection():
    print("\nAVAILABLE BOOK LIST")
    print("-------------------")

    for i in range(len(book_names)):
        print(
            str(i + 1) + ". " + book_names[i]
            + " - Stock: " + str(book_stocks[i])
        )


def borrow_book():
    if len(book_names) == 0:
        print("No books in the inventory.")
        return_menu()
        return

    view_inventory_for_selection()

    book_number = input("Enter book number to borrow: ").strip()

    if not book_number.isdigit():
        print("Invalid book number.")
        return_menu()
        return

    index = int(book_number) - 1

    if index < 0 or index >= len(book_names):
        print("Book number does not exist.")
    elif book_stocks[index] == 0:
        print("Book is out of stock.")
    else:
        book_stocks[index] -= 1
        print("Book borrowed successfully.")
        print("Remaining stock:", book_stocks[index])

    return_menu()


def return_book():
    if len(book_names) == 0:
        print("No books in the inventory.")
        return_menu()
        return

    view_inventory_for_selection()

    book_number = input("Enter book number to return: ").strip()

    if not book_number.isdigit():
        print("Invalid book number.")
        return_menu()
        return

    index = int(book_number) - 1

    if index < 0 or index >= len(book_names):
        print("Book number does not exist.")
    else:
        book_stocks[index] += 1
        print("Book returned successfully.")
        print("Updated stock:", book_stocks[index])

    return_menu()


def calculate_total(stocks):
    total = 0

    for stock in stocks:
        total += stock

    return total


def calculate_average(stocks):
    if len(stocks) == 0:
        return 0

    return calculate_total(stocks) / len(stocks)


def find_lowest(stocks):
    if len(stocks) == 0:
        return 0

    lowest = stocks[0]

    for stock in stocks:
        if stock < lowest:
            lowest = stock

    return lowest


def find_highest(stocks):
    if len(stocks) == 0:
        return 0

    highest = stocks[0]

    for stock in stocks:
        if stock > highest:
            highest = stock

    return highest


def count_category(stocks, category):
    count = 0

    for stock in stocks:
        if classify_book(stock) == category:
            count += 1

    return count


def calculate_percentage(count, total):
    if total == 0:
        return 0

    return count / total * 100


def generate_summary():
    if len(book_names) == 0:
        print("No books in the inventory.")
        return_menu()
        return

    total = calculate_total(book_stocks)
    average = calculate_average(book_stocks)
    lowest = find_lowest(book_stocks)
    highest = find_highest(book_stocks)

    available = count_category(book_stocks, "AVAILABLE")
    low_stock = count_category(book_stocks, "LOW STOCK")
    out_of_stock = count_category(book_stocks, "OUT OF STOCK")
    total_titles = len(book_names)

    print("\nLIBRARY INVENTORY SUMMARY")
    print("-------------------------")
    print("Different book titles:", total_titles)
    print("Total books in stock:", total)
    print("Average stock per title: {:.2f}".format(average))
    print("Lowest stock:", lowest)
    print("Highest stock:", highest)

    print("\nINVENTORY CLASSIFICATION")
    print("------------------------")
    print("AVAILABLE: {} ({:.2f}%)".format(
        available,
        calculate_percentage(available, total_titles)
    ))
    print("LOW STOCK: {} ({:.2f}%)".format(
        low_stock,
        calculate_percentage(low_stock, total_titles)
    ))
    print("OUT OF STOCK: {} ({:.2f}%)".format(
        out_of_stock,
        calculate_percentage(out_of_stock, total_titles)
    ))

    if out_of_stock > 0:
        status = "ATTENTION REQUIRED"
    elif low_stock > 0:
        status = "MONITOR INVENTORY"
    else:
        status = "NORMAL"

    print("\nOverall Status:", status)
    return_menu()


if __name__ == "__main__":
    try:
        main_menu()
    except SystemExit:
        pass