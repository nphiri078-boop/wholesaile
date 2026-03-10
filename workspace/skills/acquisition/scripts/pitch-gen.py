#!/usr/bin/env python3
import sys
pitch_type = sys.argv[1] if len(sys.argv) > 1 else "default"
pitches = {
    "seller-finance": "Subject: Creative Seller Finance Opportunity\nHi [Seller],\nInterested in seller financing? No banks, flexible terms...",
    "default": "Hi [Seller], Let's discuss your property options including wholesale or finance..."
}
print(pitches.get(pitch_type, pitches["default"]))
