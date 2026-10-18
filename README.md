# cpp102_week17_tud_1cpe-a
# Library Book Inventory System

Student Name: Allen Farrel Tud  
Student Number: 2601311  
Section: 1CPE-A

Project Description

This program manages library book inventory by storing book titles and their respective stock quantities. It allows users to view, add, borrow, and return books. It classifies each book's stock as AVAILABLE, LOW STOCK, or OUT OF STOCK and generates a numerical summary showing the total, average, lowest, and highest stock quantities, category counts, and overall inventory status.

Features

- View all stored book titles, stock quantities, and availability statuses.
- Add a new book with its title and initial quantity.
- Borrow a book and automatically decrease its stock by one.
- Return a book and automatically increase its stock by one.
- Classify book stocks as AVAILABLE, LOW STOCK, or OUT OF STOCK.
- Generate a numerical summary, including Total, Average, Min, Max, Category Counts, and Overall Status.
- Handle invalid menu choices, duplicate book titles, invalid quantities, and nonexistent book numbers.

Requirements: Python 3 (no external packages required)

How to Run: Open a terminal inside your project folder.

Type: `python device_monitor.py` (On macOS or Linux, type: `python3 device_monitor.py`)

------------------------------------------

[1] View Books  
[2] Add Book  
[3] Borrow Book  
[4] Return Book  
[5] Generate Summary  
[6] Exit

Enter choice: 1

LIBRARY BOOK INVENTORY
----------------------
Book 1 : Python Programming
Stock: 28
Status: AVAILABLE

Book 2 : Computer Fundamentals
Stock: 31
Status: AVAILABLE

Book 3 : Introduction to Electronics
Stock: 35
Status: AVAILABLE

Book 4 : Discrete Mathematics
Stock: 37
Status: AVAILABLE

Book 5 : Digital Logic Design
Stock: 29
Status: AVAILABLE


Enter "1" to return to the main menu or "2" to exit: 1

Known Limitations

Book titles and stock quantities are stored in memory, meaning changes are lost when the program closes.

The system does not track borrower information or borrowing history.

The return function increases the stock without checking whether the book was previously borrowed.

Reflection: The hardest part of this project was managing the inventory correctly across different functions, especially when borrowing and returning books and calculating the summary. I needed to ensure that stock quantities were updated correctly and that invalid inputs were handled properly. In the future, I would improve the system by adding file storage or a database to save inventory changes and by including borrower records for better library management.
