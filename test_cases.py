"""
Automated Test Suite for Grocery Store Management System
Validates all 4 test cases given in the specification + Stock Refill + Add New Item + Edit Price.
"""

import subprocess
import os
import sys

def run_test(test_num, name, input_text, expected_substrings):
    print(f"\n--- Running Test Case {test_num}: {name} ---")
    proc = subprocess.run(
        [sys.executable, "main.py"],
        input=input_text,
        text=True,
        capture_output=True,
        cwd=r"d:\GSMS"
    )
    stdout = proc.stdout
    print("STDOUT OUTPUT:")
    print(stdout.strip())
    
    passed = True
    for expected in expected_substrings:
        if expected in stdout:
            print(f"[PASS] Found: '{expected}'")
        else:
            print(f"[FAIL] Missing expected output: '{expected}'")
            passed = False

    return passed

def main():
    # Remove previous test files if any
    for f in ["bills.txt", "stock.txt"]:
        path = os.path.join(r"d:\GSMS", f)
        if os.path.exists(path):
            os.remove(path)

    results = []

    # Test Case 1: Normal Input
    # Menu option 1 (New bill)
    # Rice: 2, Milk: 3
    # Expected: Subtotal: 190.00 | Discount: 0.00 | GST (5%): 9.50 | Total: Rs. 199.50
    t1_input = "1\nRice: 2, Milk: 3\ndone\n6\n"
    r1 = run_test(1, "Normal Input (Rice: 2, Milk: 3)", t1_input, [
        "Subtotal: 190.00 | Discount: 0.00 | GST (5%): 9.50 | Total: Rs. 199.50"
    ])
    results.append(("Test Case 1", r1))

    # Also test separate prompt lines for Test Case 1:
    t1_alt_input = "1\nRice\n2\nMilk\n3\ndone\n6\n"
    r1_alt = run_test("1 (Alt interactive)", "Rice then 2, Milk then 3", t1_alt_input, [
        "Subtotal: 190.00 | Discount: 0.00 | GST (5%): 9.50 | Total: Rs. 199.50"
    ])
    results.append(("Test Case 1 (Interactive)", r1_alt))

    # Test Case 2: Boundary / Minimum Input
    # Menu option 1 (New bill)
    # Oil: 4, Rice: 8 (subtotal exactly 1000)
    # Expected: Subtotal: 1000.00 | Discount (10%): 100.00 | GST (5%): 45.00 | Total: Rs. 945.00
    t2_input = "1\nOil: 4, Rice: 8\ndone\n6\n"
    r2 = run_test(2, "Boundary / Minimum Input (Oil: 4, Rice: 8)", t2_input, [
        "Subtotal: 1000.00 | Discount (10%): 100.00 | GST (5%): 45.00 | Total: Rs. 945.00"
    ])
    results.append(("Test Case 2", r2))

    # Test Case 3: Invalid Input
    # Menu option 1 (New bill)
    # Item: Butter, Quantity: 2
    # Item: Milk, Quantity: 50
    # Expected:
    # Item 'Butter' not found in inventory.
    # Insufficient stock for Milk. Available: 40
    t3_input = "1\nItem: Butter, Quantity: 2\nItem: Milk, Quantity: 50\ndone\n6\n"
    r3 = run_test(3, "Invalid Input (Butter: 2, Milk: 50)", t3_input, [
        "Item 'Butter' not found in inventory.",
        "Insufficient stock for Milk. Available: 40"
    ])
    results.append(("Test Case 3", r3))

    # Also test interactive invalid input for Test Case 3:
    t3_alt_input = "1\nButter\n2\nMilk\n50\ndone\n6\n"
    r3_alt = run_test("3 (Alt interactive)", "Butter 2, Milk 50", t3_alt_input, [
        "Item 'Butter' not found in inventory.",
        "Insufficient stock for Milk. Available: 40"
    ])
    results.append(("Test Case 3 (Interactive)", r3_alt))

    # Test Case 4: Different Valid Scenario
    # (a) Menu option 1 (New bill): Sugar: 10, Milk: 5
    # (b) Menu option 2 (View stock)
    # Expected:
    # (a) Subtotal: 600.00 | Discount: 0.00 | GST (5%): 30.00 | Total: Rs. 630.00
    # (b) Rice: 100 | Sugar: 40 | Milk: 35 | Oil: 20
    t4_input = "1\nSugar: 10, Milk: 5\ndone\n2\n6\n"
    r4 = run_test(4, "Different Valid Scenario + View Stock", t4_input, [
        "Subtotal: 600.00 | Discount: 0.00 | GST (5%): 30.00 | Total: Rs. 630.00",
        "Rice: 100 | Sugar: 40 | Milk: 35 | Oil: 20"
    ])
    results.append(("Test Case 4", r4))

    # Also test inline format for Test Case 4:
    t4_inline_input = "(a) Menu option 1 (New bill): Sugar: 10, Milk: 5\n(b) Menu option 2 (View stock)\n6\n"
    r4_inline = run_test("4 (Inline Menu Format)", "(a) Menu option 1... (b) Menu option 2...", t4_inline_input, [
        "Subtotal: 600.00 | Discount: 0.00 | GST (5%): 30.00 | Total: Rs. 630.00",
        "Rice: 100 | Sugar: 40 | Milk: 35 | Oil: 20"
    ])
    results.append(("Test Case 4 (Inline)", r4_inline))

    # Test Case 5: Stock Refill Option
    # Refill Milk by 20 units and Rice by 50 units, then View Stock
    # Initial: Rice: 100, Sugar: 50, Milk: 40, Oil: 20
    # Expected after refill: Rice: 150 | Sugar: 50 | Milk: 60 | Oil: 20
    t5_input = "3\nMilk: 20\nRice: 50\ndone\n2\n6\n"
    r5 = run_test(5, "Refill Stock Feature", t5_input, [
        "Refilled Milk by 20. New stock: 60",
        "Refilled Rice by 50. New stock: 150",
        "Rice: 150 | Sugar: 50 | Milk: 60 | Oil: 20"
    ])
    results.append(("Test Case 5 (Refill Stock)", r5))

    # Test Case 6: Add New Item Feature
    # Add 'Butter' (Price: 60, Initial Stock: 30)
    # Bill 5 Butter: Subtotal = 300.00, Discount = 0.00, GST = 15.00, Total = Rs. 315.00
    # View stock: Butter should now have 25 in stock
    t6_input = "4\nButter\n60\n30\ndone\n1\nButter: 5\ndone\n2\n6\n"
    r6 = run_test(6, "Add New Item & Bill It", t6_input, [
        "Added 'Butter' to inventory (Price: Rs. 60.00, Initial Stock: 30).",
        "Subtotal: 300.00 | Discount: 0.00 | GST (5%): 15.00 | Total: Rs. 315.00",
        "Butter: 25"
    ])
    results.append(("Test Case 6 (Add New Item)", r6))

    # Test Case 7: Edit Price Feature
    # Update Rice price from 50 to 60
    # Bill 2 Rice at new price: 2 * 60 = 120.00, GST = 6.00, Total = Rs. 126.00
    t7_input = "5\nRice: 60\ndone\n1\nRice: 2\ndone\n6\n"
    r7 = run_test(7, "Edit Item Price & Bill at New Price", t7_input, [
        "Updated price for Rice from Rs. 50.00 to Rs. 60.00.",
        "Subtotal: 120.00 | Discount: 0.00 | GST (5%): 6.00 | Total: Rs. 126.00"
    ])
    results.append(("Test Case 7 (Edit Price)", r7))

    # Verify bills.txt and stock.txt exist and are updated
    print("\n--- Verifying File Handling ---")
    bills_path = r"d:\GSMS\bills.txt"
    stock_path = r"d:\GSMS\stock.txt"
    
    if os.path.exists(bills_path) and os.path.getsize(bills_path) > 0:
        print("[PASS] bills.txt exists and contains bill records.")
    else:
        print("[FAIL] bills.txt is missing or empty.")

    if os.path.exists(stock_path) and os.path.getsize(stock_path) > 0:
        print("[PASS] stock.txt exists and contains updated stock.")
    else:
        print("[FAIL] stock.txt is missing or empty.")

    print("\n================ TEST SUMMARY ================")
    all_passed = True
    for name, status in results:
        status_str = "PASSED" if status else "FAILED"
        print(f"{name}: {status_str}")
        if not status:
            all_passed = False

    print("==============================================")
    if all_passed:
        print("ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print("SOME TESTS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    main()
