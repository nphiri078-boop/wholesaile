#!/usr/bin/env python3
import sys
if len(sys.argv) != 4:
    print("Usage: ./mao-calc.py <ARV> <repairs> <fee>")
    sys.exit(1)
arv, repairs, fee = map(float, sys.argv[1:])
mao = arv * 0.7 - repairs - fee
print(f"MAO: ${mao:,.2f}")
