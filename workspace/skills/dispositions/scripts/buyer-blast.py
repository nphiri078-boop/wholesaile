#!/usr/bin/env python3
buyers = ["Buyer1 <buyer1@ex.com>", "Buyer2 <buyer2@ex.com>"]
message = "New deal: [Address] $[price] wholesale. Reply to bid!"
print("Simulating buyer blast:")
for b in buyers:
    print(f"To {b}: {message}")
