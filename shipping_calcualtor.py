"""
Jeremy Eldredge - IS 303
A02 - Shipping Calculator

Calculates shipping cost based on package weight and destination.

Inputs:
-  Customer name
-  Package weight
-  Destination zone

Processes:
- Validate weight (must be positive)
- Validate zone (must be local, regional, or national)
- Determine base rate from weight tier (under 2 lbs, 2-10 lbs, over 10 lbs)
- Apply zone multiplier (local = 1.0, regional = 1.5, national = 2.5)
- Calculate total shipping cost

Outputs:
-  Customer name
-  Package weight
-  Destination zone
-  Total shipping cost
"""

# collect inputs
customer_name = input("Customer name: ")
package_weight = input("Package weight (lbs): ")
package_destination = input("Package destination: ")

process = True

# validate weight
weight_is_int = package_weight.isdigit()
if weight_is_int == True:
    package_weight = int(package_weight)
weight_is_reasonable = False
if weight_is_int == True and package_weight > 0:
    weight_is_reasonable = True

# validate destination
package_destination = package_destination.lower()
destination_is_valid = False
if package_destination == "local" or package_destination == "regional" or package_destination == "national":
    destination_is_valid = True

# error messages
if weight_is_int == False or weight_is_int == False:
    print("Invalid weight entered. Enter a whole number above 0.")
    process = False

if destination_is_valid == False:
    print("Invalid destination entered. Enter local, regional, or national")
    process = False

# determine package base rate, zone multiplier, and output
if process == True:
    base_rate = 0
    if package_weight >= 10:
        base_rate = 15
    elif package_weight > 2:
        base_rate = 10
    else:
        base_rate = 5

    # determine zone multiplier
    zone_multiplier = 0
    if package_destination == "national":
        zone_multiplier = 2.5
    elif package_destination == "regional":
        zone_multiplier = 1.5
    else:
        zone_multiplier = 1

    # calculate shipping cost
    shipping_cost = base_rate + (package_weight * zone_multiplier)

    print(f"Customer name: {customer_name}\n"
          f"Package weight: {package_weight} | Package destination: {package_destination}\n"
          f"Distance rate: ${zone_multiplier:.2f}/lb\n"
          f"Shipping cost: ${shipping_cost:.2f}")