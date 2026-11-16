# Grocery Store Management System

A Python 3 console billing application for a grocery store that handles customer purchases, real-time stock management, discount & GST calculation, and file logging.

---

## 📋 Problem Summary

The application allows a cashier to:
1. Select items and quantities from the grocery inventory.
2. Validate item availability and check against current stock.
3. Calculate subtotal, apply discounts (10% on Rs. 1000 or more), and calculate GST (5% on discounted amount).
4. Reduce inventory stock after billing.
5. Append every bill to `bills.txt` and save updated stock to `stock.txt`.
6. View real-time stock at any point.
7. Refill inventory stock to replenish items when quantities run low.
8. Add brand new items to the inventory dynamically with custom price and initial stock.
9. Edit prices of existing items in the inventory with immediate effect on subsequent bills.

### Inventory Specification
| Item | Price | Initial Stock |
|---|---|---|
| **Rice** | Rs. 50/kg | 100 |
| **Sugar** | Rs. 45/kg | 50 |
| **Milk** | Rs. 30/L | 40 |
| **Oil** | Rs. 150/L | 20 |

### Billing Rules
- **Discount:** 10% discount if subtotal $\ge$ Rs. 1000. Otherwise 0%.
- **GST:** 5% on the amount after discount.
- **Total:** `Amount after discount + GST`

---

## 🚀 How to Run

Run with Python 3:

```bash
python main.py
```
*(or `python grocery_store.py`)*

To run the automated test suite:
```bash
python test_cases.py
```

---

## 🧪 Test Cases & Expected Outputs

### Test Case 1: Normal Input
- **Menu option:** 1 (New bill)
- **Input:** `Rice: 2, Milk: 3`
  - Rice: $2 \times 50 = 100$
  - Milk: $3 \times 30 = 90$
  - Subtotal: $190.00$
  - Discount: $0.00$
  - GST (5%): $9.50$
  - Total: Rs. $199.50$
- **Expected Output:**
  ```
  Subtotal: 190.00 | Discount: 0.00 | GST (5%): 9.50 | Total: Rs. 199.50
  ```

### Test Case 2: Boundary / Minimum Input
- **Menu option:** 1 (New bill)
- **Input:** `Oil: 4, Rice: 8` (Subtotal exactly 1000)
  - Oil: $4 \times 150 = 600$
  - Rice: $8 \times 50 = 400$
  - Subtotal: $1000.00$
  - Discount (10%): $100.00$
  - Amount after discount: $900.00$
  - GST (5%): $45.00$
  - Total: Rs. $945.00$
- **Expected Output:**
  ```
  Subtotal: 1000.00 | Discount (10%): 100.00 | GST (5%): 45.00 | Total: Rs. 945.00
  ```

### Test Case 3: Invalid Input
- **Menu option:** 1 (New bill)
- **Input:**
  - `Item: Butter, Quantity: 2`
  - `Item: Milk, Quantity: 50`
- **Expected Output:**
  ```
  Item 'Butter' not found in inventory.
  Insufficient stock for Milk. Available: 40
  ```

### Test Case 4: Different Valid Scenario
- **(a) Menu option 1 (New bill):** `Sugar: 10, Milk: 5`
  - Sugar: $10 \times 45 = 450$
  - Milk: $5 \times 30 = 150$
  - Subtotal: $600.00$
  - Discount: $0.00$
  - GST (5%): $30.00$
  - Total: Rs. $630.00$
  - **Output (a):**
    ```
    Subtotal: 600.00 | Discount: 0.00 | GST (5%): 30.00 | Total: Rs. 630.00
    ```
- **(b) Menu option 2 (View stock):**
  - **Output (b):**
    ```
    Rice: 100 | Sugar: 40 | Milk: 35 | Oil: 20
    ```

---

## 📂 File Structure

- `main.py` - Core application file with complete billing, inventory, and file-handling logic.
- `grocery_store.py` - Alternative entry point.
- `test_cases.py` - Automated test suite covering all specified test cases and boundary conditions.
- `bills.txt` - Receipt log file storing all generated bills with itemized breakdowns.
- `stock.txt` - Stock persistence file storing current stock counts.
