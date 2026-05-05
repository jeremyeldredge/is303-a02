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