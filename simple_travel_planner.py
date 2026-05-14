# ====================================================================
# PROJECT: Global Travel Budget Planner & Currency Predictor
# AUTHOR: Rawfu Siam
# DATE    : May 13, 2026
# ====================================================================

import random
import pyjokes

# --------------------------------------------------------------------
# System Greeting
# --------------------------------------------------------------------
print("==================================================")
print("         🌐 GLOBAL TRAVEL BUDGET PLANNER          ")
print("==================================================")

# Generating an interactive startup icebreaker
system_joke = pyjokes.get_joke()
print(f"System Boot up successful. Quick joke: {system_joke}\n")

# --------------------------------------------------------------------
# Parameter Ingestion Pipeline
# --------------------------------------------------------------------
traveler_name = input("Enter traveler name: ")
target_destination = input("Enter dream destination city (e.g., Tokyo/Osaka/Kyoto): ")
raw_savings_bdt = input("Enter total vacation savings in local currency (BDT): ")

# --------------------------------------------------------------------
# Discount Simulation & Currency Exchange Engine
# --------------------------------------------------------------------
# Convert string input data to floating decimals for calculations
clean_savings_bdt = float(raw_savings_bdt)

# Asset Arbitrage: Converting Bangladeshi Taka (BDT) to Japanese Yen (JPY) 
exchange_rate_jpy = 1.33
total_funds_jpy = clean_savings_bdt * exchange_rate_jpy

flight_discount_percent = random.randint(5, 25)

# --------------------------------------------------------------------
# The Final Formatted Trip Itinerary Report
# --------------------------------------------------------------------
print("\n==================================================")
print("             🎯 OFFICIAL TRIP ITINERARY            ")
print("==================================================")
print(f"👤 Traveler Profile:      {traveler_name}")
print(f"📍 Destination Hub:       {target_destination}")
print(f"💰 Initial Capital:      {clean_savings_bdt} BDT")
print(f"💴 Converted Funds:      {total_funds_jpy} JPY")
print(f"✈️ Lucky Airline Deal:   {flight_discount_percent}% OFF Next Flight booking!")
print("==================================================")
print("          Safe travels! Project Complete.         ")
print("==================================================")
