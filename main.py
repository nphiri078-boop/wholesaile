#!/usr/bin/env python3
"""
Wholesale Real Estate Deal Manager
Core workflow: Lead → Analyze → Make Offer → Assign to Investor → Track Profit
Save as: main.py
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# --------------------------
# Data Storage Setup
# --------------------------
DATA_FILE = "wholesale_data.json"

def load_data() -> Dict:
    """Load saved data from JSON file"""
    default = {
        "leads": [],
        "investors": [],
        "deals": []
    }
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def save_data(data: Dict):
    """Save data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

# --------------------------
# Core Calculations
# --------------------------
def calculate_offer(arv: float, repair_cost: float, strategy: str = "70%") -> float:
    """
    Calculate maximum allowable offer (MAO)
    Standard wholesaling rule: 70% of ARV minus repairs
    """
    if strategy == "70%":
        mao = (arv * 0.70) - repair_cost
    elif strategy == "65%":
        mao = (arv * 0.65) - repair_cost
    else:
        mao = arv - repair_cost - 10000  # Custom fallback
    return round(max(mao, 0), 2)

def calculate_spread(contract_price: float, assignment_fee: float) -> float:
    """Calculate net profit spread"""
    return round(assignment_fee, 2)

# --------------------------
# Lead Management
# --------------------------
def add_lead(data: Dict):
    print("\n--- Add New Property Lead ---")
    address = input("Full Property Address: ").strip()
    property_type = input("Type (Single Family/Multi/Commercial): ").strip()
    seller_name = input("Seller Name: ").strip()
    seller_phone = input("Seller Phone: ").strip()
    arv = float(input("Estimated ARV (After Repair Value): R"))
    repair_cost = float(input("Estimated Repairs: R"))
    motivation = input("Seller Motivation (e.g. Divorce, Behind on Taxes): ").strip()

    lead = {
        "id": len(data["leads"]) + 1,
        "address": address,
        "type": property_type,
        "seller_name": seller_name,
        "seller_phone": seller_phone,
        "arv": arv,
        "repair_cost": repair_cost,
        "mao": calculate_offer(arv, repair_cost),
        "motivation": motivation,
        "status": "New Lead",
        "added": datetime.now().isoformat()
    }
    data["leads"].append(lead)
    save_data(data)
    print(f"✅ Lead added! Max Offer: R{lead['mao']:,.2f}")

# --------------------------
# Investor Management
# --------------------------
def add_investor(data: Dict):
    print("\n--- Add New Cash Investor ---")
    name = input("Investor Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    criteria = input("Buying Criteria (e.g. 3 beds <R500k JHB): ").strip()

    investor = {
        "id": len(data["investors"]) + 1,
        "name": name,
        "phone": phone,
        "email": email,
        "criteria": criteria,
        "added": datetime.now().isoformat()
    }
    data["investors"].append(investor)
    save_data(data)
    print("✅ Investor added successfully")

# --------------------------
# Deal Pipeline
# --------------------------
def create_deal(data: Dict):
    print("\n--- Create New Wholesale Deal ---")
    if not data["leads"]:
        print("❌ No leads found! Add a lead first.")
        return

    print("\nAvailable Leads:")
    for l in data["leads"]:
        print(f"#{l['id']} | {l['address']} | MAO: R{l['mao']:,.2f}")

    lead_id = int(input("\nSelect Lead ID: "))
    lead = next((l for l in data["leads"] if l["id"] == lead_id), None)
    if not lead:
        print("❌ Invalid Lead ID")
        return

    contract_price = float(input(f"Agreed Contract Price (max R{lead['mao']:,.2f}): R"))
    assignment_fee = float(input("Your Assignment Fee: R"))
    investor_id = int(input("Select Investor ID (enter 0 to skip): ")) or None

    investor = next((i for i in data["investors"] if i["id"] == investor_id), None) if investor_id else None

    deal = {
        "id": len(data["deals"]) + 1,
        "address": lead["address"],
        "arv": lead["arv"],
        "repair_cost": lead["repair_cost"],
        "contract_price": contract_price,
        "assignment_fee": assignment_fee,
        "spread": calculate_spread(contract_price, assignment_fee),
        "investor": investor["name"] if investor else "Unassigned",
        "status": "Under Contract",
        "created": datetime.now().isoformat()
    }

    data["deals"].append(deal)
    lead["status"] = "Converted to Deal"
    save_data(data)
    print(f"✅ Deal created! Profit: R{deal['spread']:,.2f}")

# --------------------------
# Reports & Views
# --------------------------
def show_pipeline(data: Dict):
    print("\n" + "="*60)
    print("📊 WHOLESALE DEAL PIPELINE")
    print("="*60)
    print(f"{'ID':<3} {'Address':<30} {'Status':<18} {'Profit':>12}")
    print("-"*60)
    total = 0
    for d in data["deals"]:
        print(f"{d['id']:<3} {d['address'][:28]:<30} {d['status']:<18} R{d['spread']:>10,.2f}")
        total += d["spread"]
    print("-"*60)
    print(f"TOTAL POTENTIAL PROFIT: R{total:>10,.2f}")
    print("="*60)

# --------------------------
# Main Menu
# --------------------------
def main():
    print("🏡 WHOLESALE REAL ESTATE MANAGER")
    print(f"Loaded: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    data = load_data()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Add New Property Lead")
        print("2. Add Cash Investor")
        print("3. Create New Deal")
        print("4. View Deal Pipeline")
        print("5. Exit")

        choice = input("\nEnter choice (1-5): ").strip()

        if choice == "1":
            add_lead(data)
        elif choice == "2":
            add_investor(data)
        elif choice == "3":
            create_deal(data)
        elif choice == "4":
            show_pipeline(data)
        elif choice == "5":
            print("👋 Goodbye! Data saved automatically.")
            break
        else:
            print("❌ Invalid choice — try again")

if __name__ == "__main__":
    main()
