budget = float(input())
season = input()

location = ""
accomodation = ""

if budget <= 1000:
    accomodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65* budget
        print(f"{location} - {accomodation} - {price:.2f}")
    if season == "Winter":
        location = "Morocco"
        price = 0.45 * budget
        print(f"{location} - {accomodation} - {price:.2f}")
elif 1000 < budget <= 3000:
    accomodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.80* budget
        print(f"{location} - {accomodation} - {price:.2f}")
    if season == "Winter":
        location = "Morocco"
        price = 0.60 * budget
        print(f"{location} - {accomodation} - {price:.2f}")
elif budget > 3000:
    accomodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = 0.90* budget
        print(f"{location} - {accomodation} - {price:.2f}")
    if season == "Winter":
        location = "Morocco"
        price = 0.90 * budget
        print(f"{location} - {accomodation} - {price:.2f}")