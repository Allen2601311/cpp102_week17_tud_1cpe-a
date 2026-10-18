# Test Cases – Library Book Inventory System

Tested by: Allen Farrel Tud
Date: october 18, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Display five initial books and their stock levels | Five books displayed with stocks 28, 31, 35, 37, and 29; all are AVAILABLE | Pass |
| TC02 | Choose 2, enter `Computer Networks`, quantity `10` | Book added successfully | Book added successfully with stock 10 | Pass |
| TC03 | Choose 2, enter `Computer Networks` | Reject duplicate book title | Displays "Book already exists." | Pass |
| TC04 | Choose 2, enter `abc` as quantity | Reject non-numeric quantity | Displays "Invalid quantity. Enter a whole number." | Pass |
| TC05 | Choose 3, enter book number `1` | Borrow one book and reduce stock by 1 | Stock decreases from 28 to 27 | Pass |
| TC06 | Choose 4, enter book number `1` | Return one book and increase stock by 1 | Stock increases from 28 to 29 | Pass |
| TC07 | Choose 3, enter book number `99` | Reject invalid book number | Displays "Book number does not exist." | Pass |
| TC08 | Choose 5 using initial inventory | Display correct inventory summary | Total: 160, Average: 32.00, Lowest: 28, Highest: 37, Status: NORMAL | Pass |
| TC09 | Enter menu choice `9` | Display an error and show the menu again | Displays "Invalid choice. Please try again." | Pass |
| TC10 | Choose 6 | Display exit message and terminate program | Displays "Thank you for using the Library Book Inventory System." | Pass |

## Bugs Found and Fixed

No bugs were confirmed as fixed during testing. One possible improvement is to prevent returning a book that was not previously borrowed, because the current program increases the stock without checking borrowing records.

**Note:** The actual results above are based on the program's code. Run each test and confirm the results before submitting.
