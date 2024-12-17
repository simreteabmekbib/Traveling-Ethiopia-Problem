# Example Data
cities = [
    'Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle', 'Dire Dawa', 'Harar', 'Jimma', 'Debre Birhan', 'Axum'
]
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275), ('Dire Dawa', 445), ('Jimma', 345)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180), ('Axum', 600)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300), ('Axum', 250)],
    'Hawassa': [('Addis Ababa', 275), ('Jimma', 200)],
    'Mekelle': [('Gondar', 300), ('Axum', 200)],
    'Dire Dawa': [('Addis Ababa', 445), ('Harar', 55)],
    'Harar': [('Dire Dawa', 55), ('Debre Birhan', 400)],
    'Jimma': [('Addis Ababa', 345), ('Hawassa', 200)],
    'Debre Birhan': [('Harar', 400), ('Axum', 500)],
    'Axum': [('Bahir Dar', 600), ('Gondar', 250), ('Mekelle', 200), ('Debre Birhan', 500)]
}

# cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
# roads = {
# 'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
# 'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
# 'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
# 'Hawassa': [('Addis Ababa', 275)],
# 'Mekelle': [('Gondar', 300)]
# }
