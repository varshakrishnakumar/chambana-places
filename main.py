import random

visited_total = ["NAYA", "The Bread Company", "Signature Grill", "Ko Fusion (Downtown)", "Ko Fusion (Urbana)", "Nando Milano", "Cravings", "Culver's", "Sakanaya", "Pizzeria Antica", "Kohinoor", "Mia Za's", "Manolo's", "Noodles and Company", "The Himalayan Chimney", "Basil Thai", "Chipotle", "Bangkok Thai", "Spoon House", "Mid Summer Lounge", "Jip Bap", "Sushi Ichiban", "Paris Super Crepes", "Ambar", "Taco Bell", "Burger King", "Subway", "Chopstix", "Jerusalem", "Red Herring Vegetarian", "McDonald's", "Legends", "Siam Terrace"]
unvisited_total = ["Black Dog Smoke House", "Baxters American Grill", "Houlihan's", "Maize Mexican Grill", "Seven Saints", "Timpone's", "Watson's Shack & Rail", "Maize at the Station", "Bunny's Tavern", "Wood N' Hog Barbeque", "Big Grove Tavern", "Cactus Grill", "Sticky Rice", "Spice Box", "Tres Nopales", "Silvercreek", "Crane Alley", "Perkins", "Fat Sandwich Company", "Bab Plus", "Fiesta Cafe", "Cowboy Monkey", "Manzella's Italian Patio", "Masijta Grill", "Golden Wheat", "Neil St Blues", "Jurassic Grill", "Burrito King", "K Bowl Inc.", "A-Ri_Rang", "Guido's Bar and Grill", "The Empanadas House", "Wingstop", "Sushi Kame", "Merry Ann's", "Papa Del's", "Zen Thai", "Golden Harbor Authentic Chinese", "Hamilton Walker's", "Golden Wok", "Lao Sze Chuan", "D.P. Dough", "Vinny's", "Rosati's", "Peking", "Jupiter's Pizzeria", "Steak 'n Shake", "Dairy Queen", "Rainbow Garden", "That Burger Joint", "Garbanzo Mediterranean", "Esquire Lounge", "Oozu Ramen", "Lai Lai Wok", "Hot Wok Express", "Fat City Bar and Grill", "Jet's Pizza", "Manadrin Wok", "Miga", "Potbelly Sandwich", "Moki Sushi", "Jimmy John's", "Stango Cuisine", "QDOBA Mexican", "Cracked", "Four Breakfast", "Little Caesars", "Pho Noodle Station", "Cafe Sababa", "Spicy Tang", "Tropical Smoothie Cafe", "Kung Fu BBQ", "Aunty Lee's", "Blaze", "Murphy's", "Huaraches Moroleon", "Barrelhouse 34", "Shwarma Joint"]

all_restaurants = visited_total + unvisited_total

print("To run code smoothly, type in the numbers associated with your choice")
start = input("Do you want to try unvisited places(1), visited places(2), or either(3)?")


if start == "3":
    theme_3 = input("What theme: Family(3.1), Date Night(3.2), Friends(3.3), Upscale(3.4), Cheap and Fast(3.5), Doesn't Matter(3.6)?")
    if theme_3 == "3.1":
        all_1 = ["Ko Fusion (Downtown)", "Nando Milano", "Cravings", "Kohinoor", "The Himalayan Chimney", "Ambar", "Maze at The Station", "Seven Saints", "Black Dog Smoke House", "Baxter's American Grill", "Houlihan's", "Maize Mexican Grill", "Seven Saints", "Timpone's", "Watson's Shack & Rail", "Bunny's Tavern", "Big Grove Tavern", "Cactus Grill", "Sticky Rice", "Tres Nopales", "Silvercreek", "Crane Alley", "Fiesta Cafe", "Cowboy Monkey", "Manzella's Italian Patio", "Masijta Grill", "Neil St Blues", "Guido's Bar and Grill", "Sushi Kame", "Papa Del's", "Hamilton Walker's", "Lao Sze Chuan", "Jupiter's Pizzeria", "Steak 'n Shake", "Rainbow Garden", "That Burger Joint", "Esquire Lounge", "Miga", "Moki Sushi", "Stango Cuisine", "Murphy's", "Huaraches Moroleon"]
        print(random.choice(all_1))
    if theme_3 == "3.2":
        all_2 = ["NAYA", "The Bread Company", "Sakanaya", "Ko Fusion (Downtown)", "Nando Milano", "Big Grove Tavern", "Neil St. Blues", "Hamilton Walker's", "The Himalayan Chimney", "Bunny's Tavern", "Legends", "Barrelhouse 34", "Punch! Bar & Lounge", "Black Dog Smoke House", "Zen Thai", "Crane Alley"]
        print(random.choice(all_2))
    if theme_3 == "3.3":
        all_3 = ["The Bread Company", "Ko Fusion (Urbana)", "Cravings", "Culver's", "Pizzeria Antica", "Kohinoor", "Mia Za's", "Manolo's", "Basil Thai", "Bangkok Thai", "Spoon House", "Mid Summer Lounge", "Suchi Ichiban", "Paris Super Crepes", "Ambar", "Jerusalem", "Legends", "Murphy's", "Black Dog Smoke House", "Baxters American Grill", "Houlihan's", "Maize Mexican Grill", "Seven Saints", "Timpone's", "Watson's Shack & Rail", "Maize at the Station", "Bunny's Tavern", "Wood N' Hog Barbeque", "Big Grove Tavern", "Cactus Grill", "Sticky Rice", "Spice Box", "Tres Nopales", "Silvercreek", "Crane Alley", "Perkins", "Fat Sandwich Company", "Bab Plus", "Fiesta Cafe", "Cowboy Monkey", "Manzella's Italian Patio", "Masijta Grill", "Golden Wheat", "Neil St Blues", "Jurassic Grill", "Burrito King", "K Bowl Inc.", "A-Ri_Rang", "Guido's Bar and Grill", "The Empanadas House", "Wingstop", "Sushi Kame", "Merry Ann's", "Papa Del's", "Zen Thai", "Golden Harbor Authentic Chinese", "Hamilton Walker's", "Golden Wok", "Lao Sze Chuan", "Vinny's", "Rosati's", "Peking", "Jupiter's Pizzeria", "Steak 'n Shake", "Rainbow Garden", "That Burger Joint", "Garbanzo Mediterranean", "Esquire Lounge", "Oozu Ramen", "Lai Lai Wok", "Hot Wok Express", "Fat City Bar and Grill", "Jet's Pizza", "Manadrin Wok", "Miga", "Potbelly Sandwich", "Moki Sushi", "Stango Cuisine", "QDOBA Mexican", "Cracked", "Four Breakfast", "Pho Noodle Station", "Cafe Sababa", "Spicy Tang", "Tropical Smoothie Cafe", "Kung Fu BBQ", "Aunty Lee's", "Blaze", "Murphy's", "Huaraches Moroleon", "Barrelhouse 34", "Shwarma Joint"]
        print(random.choice(all_3))
    if theme_3 == "3.4":
        print("Coming Soon")
    if theme_3 == "3.5":
        all_4 = ["Signature Grill", "Cravings", "Mia Za's", "Manolo's", "Noodles and Company", "Chipotle", "Jip Bap", "Spoon House", "Taco Bell", "Burger King", "Subway", "Chopstix", "McDonald's", "Bab Plus", "Dairy Queen", "Steak and Shake", "Vinny's", "Cracked", "Four Breakfast", "Shwarma Joint"]
        print(random.choice(all_4))
    if theme_3 == "3.6":
        print(random.choice(all_restaurants))

if start == "2":
    theme_2 = input("What theme: Family(2.1), Date Night(2.2), Friends(2.3), Upscale(2.4), Cheap and Fast(2.5), Doesn't Matter(2.6)?")
    if theme_2 == "2.1":
        visited_1 = ["Ko Fusion (Downtown)", "Nando Milano", "Cravings", "Kohinoor", "The Himalayan Chimney", "Ambar"]
        print(random.choice(visited_1))
    if theme_2 == "2.2":
        visited_2 = ["NAYA", "The Bread Company", "Sakanaya", "Ko Fusion (Downtown)", "Nando Milano"]
        print(random.choice(visited_2))
    if theme_2 == "2.3":
        visited_3 = ["The Bread Company", "Ko Fusion (Urbana)", "Cravings", "Kohinoor", "Mia Za's", "Manolo's", "Basil Thai", "Bangkok Thai", "Spoon House", "Mid Summer Lounge", "Suchi Ichiban", "Paris Super Crepes", "Ambar", "Jerusalem", "Legends"]
        print(random.choice(visited_3))
    if theme_2 == "2.4":
        print("Coming Soon")
    if theme_2 == "2.5":
        visited_4 = ["Signature Grill", "Cravings", "Mia Za's", "Manolo's", "Noodles and Company", "Chipotle", "Jip Bap", "Spoon House", "Taco Bell", "Burger King", "Subway", "Chopstix", "McDonald's"]
        print(random.choice(visited_4))
    if theme_2 == "2.6":
        print(random.choice(visited_total))

if start == "1":
    theme_1 = input("What theme: Family(1.1), Date Night(1.2), Friends(1.3), Upscale(1.4), Cheap and Fast(1.5), Doesn't Matter(1.6)?")
    if theme_1 == "1.1":
        unvisited_1 = ["Maze at The Station", "Seven Saints", "Black Dog Smoke House", "Baxter's American Grill", "Houlihan's", "Maize Mexican Grill", "Seven Saints", "Timpone's", "Watson's Shack & Rail", "Bunny's Tavern", "Big Grove Tavern", "Cactus Grill", "Sticky Rice", "Tres Nopales", "Silvercreek", "Crane Alley", "Fiesta Cafe", "Cowboy Monkey", "Manzella's Italian Patio", "Masijta Grill", "Neil St Blues", "Guido's Bar and Grill", "Sushi Kame", "Papa Del's", "Hamilton Walker's", "Lao Sze Chuan", "Jupiter's Pizzeria", "Steak 'n Shake", "Rainbow Garden", "That Burger Joint", "Esquire Lounge", "Miga", "Moki Sushi", "Stango Cuisine", "Murphy's", "Huaraches Moroleon"]
        print(random.choice(unvisited_1))
    if theme_1 == "1.2":
        unvisited_2 = ["Big Grove Tavern", "Neil St. Blues", "Hamilton Walker's", "Bunny's Tavern", "Barrelhouse 34", "Punch! Bar & Lounge", "Black Dog Smoke House", "Zen Thai", "Crane Alley"]
        print(random.choice(unvisited_2))
    if theme_1 == "1.3":
        unvisited_3 = ["Culver's", "Murphy's", "Black Dog Smoke House", "Baxters American Grill", "Houlihan's", "Maize Mexican Grill", "Seven Saints", "Timpone's", "Watson's Shack & Rail", "Maize at the Station", "Bunny's Tavern", "Wood N' Hog Barbeque", "Big Grove Tavern", "Cactus Grill", "Sticky Rice", "Spice Box", "Tres Nopales", "Silvercreek", "Crane Alley", "Perkins", "Fat Sandwich Company", "Bab Plus", "Fiesta Cafe", "Cowboy Monkey", "Manzella's Italian Patio", "Masijta Grill", "Golden Wheat", "Neil St Blues", "Jurassic Grill", "Burrito King", "K Bowl Inc.", "A-Ri_Rang", "Guido's Bar and Grill", "The Empanadas House", "Wingstop", "Sushi Kame", "Merry Ann's", "Papa Del's", "Zen Thai", "Golden Harbor Authentic Chinese", "Hamilton Walker's", "Golden Wok", "Lao Sze Chuan", "Vinny's", "Rosati's", "Peking", "Jupiter's Pizzeria", "Steak 'n Shake", "Rainbow Garden", "That Burger Joint", "Garbanzo Mediterranean", "Esquire Lounge", "Oozu Ramen", "Lai Lai Wok", "Hot Wok Express", "Fat City Bar and Grill", "Jet's Pizza", "Manadrin Wok", "Miga", "Potbelly Sandwich", "Moki Sushi", "Stango Cuisine", "QDOBA Mexican", "Cracked", "Four Breakfast", "Pho Noodle Station", "Cafe Sababa", "Spicy Tang", "Tropical Smoothie Cafe", "Kung Fu BBQ", "Aunty Lee's", "Blaze", "Murphy's", "Huaraches Moroleon", "Barrelhouse 34", "Shwarma Joint"]
        print(random.choice(unvisited_3))
    if theme_1 == "1.4":
        print("Coming Soon")
    if theme_1 == "1.5":
        unvisited_4 = ["Bab Plus", "Dairy Queen", "Steak and Shake", "Vinny's", "Cracked", "Four Breakfast", "Shwarma Joint"]
        print(random.choice(unvisited_4))
    if theme_1 == "1.6":
        print(random.choice(unvisited_total))
    



















