#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# create a second list of strings
for farm in farms:
    print("farm name is: " + farm.get("name"))
print("\nOur loop has ended.") # print when loop has finished

    #jif x not in approved_vendors:   # if x does not appear within the list approved_vendors
     #   print(" - NOT AN APPROVED VENDOR!", end="")
