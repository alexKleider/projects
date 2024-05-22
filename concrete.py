#!/usr/bin/env python3

# File: concrete.py

"""
Thu 09 May 2024 08:06:46 AM PDT
@Cavin project
Calculate volume required for heat exchanger roof.
"""

from math import pi

# all values in cu ft
sona_vol = 0.5**2 * 41/12  
bases = (2 * 18/12 + 2 * 16/12) * 8/12

total = sona_vol + bases

print(f"Volume needed: {total:.1f} cu ft")

vol_used = 4 * 1.8

print(f"""If memory serves I used one sac of cement
probably 2 years old and very hardened but broke up
with effort leaving some chunks but quite usable.
I believe all together 4 batches were used and one
bucket of cement was left.
In theory then {vol_used} cu ft was used.
(vs estimated need of {total:.1f} cu ft)
Caviat: memory is poor, facts might well be wrong!!
""")
