print ("This calculator will determine the milligrams of marijuana in homemade edibles that YOU have created. This is assuming each serving is equal in size.")

# The user is asked the percentage of THC
print ("What is the THC percentage of the marijuana? On average, most strains have 10% THC."),
thc = int(raw_input())

# The user is asked how much grams of marijuana they are using.
print ("How many grams of marijuana are in the recipe? Example: 1/8th of an ounce = 3.5 grams. 1 ounce = 28.3495 grams."), 
# 1 gram of marijuana has 1,000mg of dry weight
grams = int(raw_input())

# The user is asked how many servings.
print("How many servings were created?"),
serving = int(raw_input())

# Example: 10% THC of 1 gram (1,000mg) = 100mg. Dry weight / THC percentage / Serving 
total = grams * 1000 / thc / serving 

print ("Each serving will have %smg.") % (total)
