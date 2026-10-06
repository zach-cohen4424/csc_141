# I thought of three rivers and the states they run through. Then use loops to print the rivers and states.

rivers = {
    "susquehanna": "pennsylvania",
    "potomac": "maryland",
    "delaware": "pennsylvania"
}

for river, state in rivers.items():
    print("The " + river.title() + " runs through " + state.title() + ".")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nStates:")
for state in rivers.values():
    print(state.title())