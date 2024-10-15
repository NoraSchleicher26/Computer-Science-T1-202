# Amazon free shipping eligibility system
# Prime customers OR pruchases of over $25
# Under 18, you need parent consent to purchase

def free_shipping(prime, cost, age, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True): #Could possibly be 3 point question on test
        print("Free Shipping applied!")
    else:
        print("Inelligible for free shipping...")

p = True
cos = 100
a = 80
con = False

free_shipping(p, cos, a, con)