def convert_usd(usd_amount):
    usd_to_inr = 83  
    usd_to_eur = 0.92  
    usd_to_gbp = 0.76 
    inr = usd_amount * usd_to_inr
    eur = usd_amount * usd_to_eur
    gbp = usd_amount * usd_to_gbp
    return inr,eur,gbp
usd_amount = float(input("Enter the amount in USD: "))
inr,eur,gbp = convert_usd(usd_amount)
print(f"{usd_amount}:")
print(f"{inr:.2f} INR")
print(f"{eur:.2f} EUR")
print(f"{gbp:.2f} GBP")
