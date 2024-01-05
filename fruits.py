import json

import fetcher


fruits = [
    {'level': 1, 'name': 'Apple', 'options': ['Cherry', 'Papaya', 'Tamarind', 'Peach', 'Plantain', 'Fig']},
    {'level': 1, 'name': 'Banana', 'options': ['Date', 'Papaya', 'Peach', 'Plum', 'Kaffir Lime', 'Raspberry']},
    {'level': 1, 'name': 'Mango', 'options': ['Strawberry', 'Guava', 'Pear', 'Pomegranate', 'Raspberry', 'Jackfruit']},
    {'level': 1, 'name': 'Grape', 'options': ['Watermelon', 'Papaya', 'Tamarind', 'Blueberry', 'Cranberry', 'Longan']},
    {'level': 1, 'name': 'Coconut', 'options': ['Grape', 'Date', 'Blackberry', 'Pomegranate', 'Musk Melon', 'Lime']},
    {'level': 1, 'name': 'Guava', 'options': ['Papaya', 'Mango', 'Pear', 'Pomegranate', 'Lime', 'Fig']},
    {'level': 1, 'name': 'Date', 'options': ['Cherry', 'Grape', 'Lemon', 'Lychee', 'Rambutan', 'Jackfruit']},
    {'level': 1, 'name': 'Cherry', 'options': ['Coconut', 'Papaya', 'Pear', 'Peach', 'Jackfruit', 'Mandarine']},
    {'level': 1, 'name': 'Watermelon', 'options': ['Mango', 'Banana', 'Pineapple', 'Kiwifruit', 'Plantain', 'Musk Melon']},
    {'level': 1, 'name': 'Papaya', 'options': ['Watermelon', 'Date', 'Orange', 'Pineapple', 'Rambutan', 'Mulberry']},
    {'level': 1, 'name': 'Strawberry', 'options': ['Cherry', 'Guava', 'Lychee', 'Pear', 'Rambutan', 'Mulberry']},
    {'level': 2, 'name': 'Kiwifruit', 'options': ['Papaya', 'Strawberry', 'Pineapple', 'Pomegranate', 'Mandarine', 'Musk Melon']},
    {'level': 2, 'name': 'Orange', 'options': ['Strawberry', 'Guava', 'Pineapple', 'Blueberry', 'Kaffir Lime', 'Fig']},
    {'level': 2, 'name': 'Lychee', 'options': ['Watermelon', 'Papaya', 'Olive', 'Tamarind', 'Cantaloupe', 'Mandarine']},
    {'level': 2, 'name': 'Pear', 'options': ['Strawberry', 'Banana', 'Peach', 'Kiwifruit', 'Kaffir Lime', 'Mandarine']},
    {'level': 2, 'name': 'Peach', 'options': ['Banana', 'Guava', 'Pear', 'Tamarind', 'Mandarine', 'Longan']},
    {'level': 2, 'name': 'Lemon', 'options': ['Grape', 'Strawberry', 'Lychee', 'Pear', 'Fig', 'Cranberry']},
    {'level': 2, 'name': 'Plum', 'options': ['Grape', 'Watermelon', 'Lychee', 'Avocado', 'Mulberry', 'Lime']},
    {'level': 2, 'name': 'Olive', 'options': ['Papaya', 'Date', 'Lemon', 'Pineapple', 'Rambutan', 'Kaffir Lime']},
    {'level': 2, 'name': 'Pineapple', 'options': ['Guava', 'Grape', 'Orange', 'Kiwifruit', 'Cranberry', 'Jackfruit']},
    {'level': 2, 'name': 'Pomegranate', 'options': ['Papaya', 'Grape', 'Plum', 'Pineapple', 'Lime', 'Mulberry']},
    {'level': 2, 'name': 'Tamarind', 'options': ['Cherry', 'Apple', 'Pomegranate', 'Plum', 'Mulberry', 'Rambutan']},
    {'level': 2, 'name': 'Avocado', 'options': ['Strawberry', 'Apple', 'Olive', 'Blueberry', 'Kaffir Lime', 'Rambutan']},
    {'level': 2, 'name': 'Blackberry', 'options': ['Mango', 'Grape', 'Avocado', 'Orange', 'Raspberry', 'Longan']},
    {'level': 2, 'name': 'Blueberry', 'options': ['Apple', 'Date', 'Blackberry', 'Pear', 'Mandarine', 'Jackfruit']},
    {'level': 3, 'name': 'Plantain', 'options': ['Peach', 'Kiwifruit', 'Cranberry', 'Longan', 'Goji Berry', 'Clementine']},
    {'level': 3, 'name': 'Cantaloupe', 'options': ['Pineapple', 'Orange', 'Fig', 'Rambutan', 'Mangosteen', 'Star fruit']},
    {'level': 3, 'name': 'Lime', 'options': ['Olive', 'Pomegranate', 'Cantaloupe', 'Cranberry', 'Star fruit', 'Mangosteen']},
    {'level': 3, 'name': 'Jackfruit', 'options': ['Pineapple', 'Blueberry', 'Fig', 'Longan', 'Honeydew', 'Goji Berry']},
    {'level': 3, 'name': 'Fig', 'options': ['Olive', 'Blackberry', 'Cantaloupe', 'Raspberry', 'Star fruit', 'Tangerine']},
    {'level': 3, 'name': 'Cranberry', 'options': ['Pear', 'Tamarind', 'Mandarine', 'Longan', 'Honeydew', 'Cacao']},
    {'level': 3, 'name': 'Mandarine', 'options': ['Pineapple', 'Peach', 'Cranberry', 'Kaffir Lime', 'Mangosteen', 'Apricot']},
    {'level': 3, 'name': 'Musk Melon', 'options': ['Blueberry', 'Olive', 'Cantaloupe', 'Jackfruit', 'Goji Berry', 'Honeydew']},
    {'level': 3, 'name': 'Mulberry', 'options': ['Pineapple', 'Plum', 'Raspberry', 'Plantain', 'Cacao', 'Clementine']},
    {'level': 3, 'name': 'Raspberry', 'options': ['Blackberry', 'Orange', 'Plantain', 'Cranberry', 'Cacao', 'Star fruit']},
    {'level': 3, 'name': 'Longan', 'options': ['Olive', 'Blueberry', 'Rambutan', 'Musk Melon', 'Clementine', 'Mangosteen']},
    {'level': 3, 'name': 'Kaffir Lime', 'options': ['Olive', 'Tamarind', 'Longan', 'Cantaloupe', 'Mangosteen', 'Star fruit']},
    {'level': 3, 'name': 'Rambutan', 'options': ['Lychee', 'Peach', 'Raspberry', 'Longan', 'Mangosteen', 'Passionfruit']},
    {'level': 4, 'name': 'Passionfruit', 'options': ['Longan', 'Mulberry', 'Honeydew', 'Tangerine', 'African Cherry Orange', 'Grapefruit']},
    {'level': 4, 'name': 'Mangosteen', 'options': ['Cantaloupe', 'Lime', 'Clementine', 'Tangerine', 'Galia Melon', 'Redcurrant']},
    {'level': 4, 'name': 'Clementine', 'options': ['Rambutan', 'Longan', 'Tangerine', 'Dragonfruit', 'Durian', 'Tamarillo']},
    {'level': 4, 'name': 'Tangerine', 'options': ['Musk Melon', 'Lime', 'Mangosteen', 'Passionfruit', 'Blackcurrant', 'African Cherry Orange']},
    {'level': 4, 'name': 'Honeydew', 'options': ['Mandarine', 'Lime', 'Tangerine', 'Dragonfruit', 'Galia Melon', 'Tamarillo']},
    {'level': 4, 'name': 'Star fruit', 'options': ['Fig', 'Lime', 'Mangosteen', 'Passionfruit', 'Grapefruit', 'Rose Apple']},
    {'level': 4, 'name': 'Nectarine', 'options': ['Rambutan', 'Cranberry', 'Star fruit', 'Dragonfruit', 'Tamarillo', 'African Cherry Orange']},
    {'level': 4, 'name': 'Blood Orange', 'options': ['Jackfruit', 'Cantaloupe', 'Cacao', 'Nectarine', 'Gooseberry', 'Galia Melon']},
    {'level': 4, 'name': 'Apricot', 'options': ['Longan', 'Mandarine', 'Mangosteen', 'Nectarine', 'Gooseberry', 'African Cherry Orange']},
    {'level': 4, 'name': 'Cacao', 'options': ['Musk Melon', 'Longan', 'Tangerine', 'Honeydew', 'African Cherry Orange', 'Durian']},
    {'level': 4, 'name': 'Dragonfruit', 'options': ['Fig', 'Raspberry', 'Honeydew', 'Blood Orange', 'Gooseberry', 'Durian']},
    {'level': 4, 'name': 'Goji Berry', 'options': ['Kaffir Lime', 'Musk Melon', 'Clementine', 'Dragonfruit', 'Tamarillo', 'Redcurrant']},
    {'level': 5, 'name': 'Rose Apple', 'options': ['Honeydew', 'Tangerine', "Buddha's Hand", 'Loganberry', 'Huckleberry', 'Cloudberry']},
    {'level': 5, 'name': 'Blackcurrant', 'options': ['Passionfruit', 'Tangerine', 'Rose Apple', 'Grapefruit', 'Breadfruit', 'Cherimoya']},
    {'level': 5, 'name': 'Durian', 'options': ['Apricot', 'Blood Orange', 'Tamarillo', 'Blackcurrant', 'White Currant', 'Cherimoya']},
    {'level': 5, 'name': 'Grapefruit', 'options': ['Goji Berry', 'Honeydew', 'African Cherry Orange', 'Redcurrant', 'Cloudberry', 'Cherimoya']},
    {'level': 5, 'name': 'Tamarillo', 'options': ['Honeydew', 'Blood Orange', 'Rose Apple', 'Gooseberry', 'Breadfruit', 'Acai']},
    {'level': 5, 'name': 'Redcurrant', 'options': ['Star fruit', 'Dragonfruit', "Buddha's Hand", 'Grapefruit', 'Acai', 'Cactus Pear']},
    {'level': 5, 'name': "Buddha's Hand", 'options': ['Goji Berry', 'Mangosteen', 'Durian', 'African Cherry Orange', 'Cloudberry', 'Chicoo']},
    {'level': 5, 'name': 'Gooseberry', 'options': ['Tangerine', 'Honeydew', 'Tamarillo', 'Blackcurrant', 'Acai', 'Satsuma']},
    {'level': 5, 'name': 'African Cherry Orange', 'options': ['Star fruit', 'Passionfruit', 'Durian', 'Tamarillo', 'Huckleberry', 'Acai']},
    {'level': 5, 'name': 'Loganberry', 'options': ['Mangosteen', 'Star fruit', 'Blackcurrant', 'Gooseberry', 'Satsuma', 'Cloudberry']},
    {'level': 5, 'name': 'Galia Melon', 'options': ['Apricot', 'Honeydew', 'Grapefruit', 'Durian', 'Satsuma', 'Breadfruit']},
    {'level': 6, 'name': 'Huckleberry', 'options': ['African Cherry Orange', 'Grapefruit', 'Breadfruit', 'Pomelo', 'Sugar Apple', 'Kumquat']},
    {'level': 6, 'name': 'Cherimoya', 'options': ['African Cherry Orange', 'Tamarillo', 'Pomelo', 'Satsuma', 'Red Medlar', 'Honeyberry']},
    {'level': 6, 'name': 'Breadfruit', 'options': ['Blackcurrant', 'Tamarillo', 'Acai', 'Huckleberry', 'Jujube', 'Juniper Berry']},
    {'level': 6, 'name': 'Cactus Pear', 'options': ['Blackcurrant', 'Redcurrant', 'Cloudberry', 'Cherimoya', 'Jujube', 'Feijoa']},
    {'level': 6, 'name': 'Pomelo', 'options': ['Durian', 'Grapefruit', 'Cactus Pear', 'Huckleberry', 'Jujube', 'Red Medlar']},
    {'level': 6, 'name': 'Chicoo', 'options': ['Galia Melon', 'Loganberry', 'Cherimoya', 'Cloudberry', 'Sugar Apple', 'Honeyberry']},
    {'level': 6, 'name': 'Acai', 'options': ['Durian', 'Grapefruit', 'Cactus Pear', 'White Currant', 'Honeyberry', 'Loquat']},
    {'level': 6, 'name': 'White Currant', 'options': ['Rose Apple', 'Gooseberry', 'Acai', 'Huckleberry', 'Sugar Apple', 'Red Medlar']},
    {'level': 6, 'name': 'Cloudberry', 'options': ['African Cherry Orange', 'Blackcurrant', 'White Currant', 'Cactus Pear', 'Jujube', 'Feijoa']},
    {'level': 6, 'name': 'Satsuma', 'options': ['Gooseberry', 'African Cherry Orange', 'Breadfruit', 'Cherimoya', 'Kiwano', 'Feijoa']},
    {'level': 7, 'name': 'Feijoa', 'options': ['Pomelo', 'Breadfruit', 'Surinam Cherry', 'Red Medlar', 'Tangelo', 'Lanzones']},
    {'level': 7, 'name': 'Jujube', 'options': ['Chicoo', 'Huckleberry', 'Kiwano', 'Kumquat', 'Cempedak', 'Jostaberry']},
    {'level': 7, 'name': 'Surinam Cherry', 'options': ['Cloudberry', 'Cactus Pear', 'Kiwano', 'Kumquat', 'Elderberry', 'Boysenberry']},
    {'level': 7, 'name': 'Juniper Berry', 'options': ['Chicoo', 'Cloudberry', 'Red Medlar', 'Honeyberry', 'Boysenberry', 'Black Sapote']},
    {'level': 7, 'name': 'Loquat', 'options': ['White Currant', 'Pomelo', 'Kiwano', 'Surinam Cherry', 'Elderberry', 'Tangelo']},
    {'level': 7, 'name': 'Kumquat', 'options': ['Cactus Pear', 'White Currant', 'Kiwano', 'Honeyberry', 'Cempedak', 'Salak']},
    {'level': 7, 'name': 'Kiwano', 'options': ['Pomelo', 'Satsuma', 'Sugar Apple', 'Honeyberry', 'Cempedak', 'Tangelo']},
    {'level': 7, 'name': 'Honeyberry', 'options': ['Breadfruit', 'Cactus Pear', 'Feijoa', 'Jujube', 'Cempedak', 'Elderberry']},
    {'level': 7, 'name': 'Sugar Apple', 'options': ['Breadfruit', 'White Currant', 'Feijoa', 'Loquat', 'Bilberry', 'Jostaberry']},
    {'level': 7, 'name': 'Red Medlar', 'options': ['Cloudberry', 'White Currant', 'Surinam Cherry', 'Juniper Berry', 'Boysenberry', 'Cempedak']},
    {'level': 8, 'name': 'Tangelo', 'options': ['Red Medlar', 'Kumquat', 'Boysenberry', 'Salak', 'Soursop', 'Sapote']},
    {'level': 8, 'name': 'Bilberry', 'options': ['Feijoa', 'Honeyberry', 'Elderberry', 'Jostaberry', 'Acerola', 'American Mayapple']},
    {'level': 8, 'name': 'Black Sapote', 'options': ['Sugar Apple', 'Red Medlar', 'Boysenberry', 'Salak', 'Damson', 'Sapodilla']},
    {'level': 8, 'name': 'Boysenberry', 'options': ['Juniper Berry', 'Loquat', 'Bilberry', 'Jostaberry', 'Jabuticaba', 'Damson']},
    {'level': 8, 'name': 'Jostaberry', 'options': ['Jujube', 'Surinam Cherry', 'Bilberry', 'Lanzones', 'Canistel', 'Persimmon']},
    {'level': 8, 'name': 'Lanzones', 'options': ['Juniper Berry', 'Kiwano', 'Salak', 'Bilberry', 'Yuzu', 'Damson']},
    {'level': 8, 'name': 'Salak', 'options': ['Red Medlar', 'Honeyberry', 'Bilberry', 'Jostaberry', 'Damson', 'Jabuticaba']},
    {'level': 8, 'name': 'Elderberry', 'options': ['Honeyberry', 'Sugar Apple', 'Lanzones', 'Jostaberry', 'Sapote', 'Soursop']},
    {'level': 8, 'name': 'Cempedak', 'options': ['Honeyberry', 'Loquat', 'Lanzones', 'Bilberry', 'Sapodilla', 'Acerola']},
    {'level': 8, 'name': 'Quince', 'options': ['Jujube', 'Honeyberry', 'Tangelo', 'Boysenberry', 'Acerola', 'Yuzu']},
    {'level': 9, 'name': 'Soursop', 'options': ['Quince', 'Elderberry', 'Persimmon', 'Yuzu', 'Aratiles', 'Akebi']},
    {'level': 9, 'name': 'Damson', 'options': ['Boysenberry', 'Salak', 'Yuzu', 'Sapote', 'Araza', 'Aratiles']},
    {'level': 9, 'name': 'Persimmon', 'options': ['Salak', 'Bilberry', 'American Mayapple', 'Sapodilla', 'Abiu', 'Araza']},
    {'level': 9, 'name': 'Canistel', 'options': ['Quince', 'Salak', 'American Mayapple', 'Damson', 'Araza', 'Ackee']},
    {'level': 9, 'name': 'Jabuticaba', 'options': ['Jostaberry', 'Tangelo', 'Sapote', 'Acerola', 'Lulo', 'Araza']},
    {'level': 9, 'name': 'Acerola', 'options': ['Boysenberry', 'Jostaberry', 'Damson', 'Soursop', 'Java Plum', 'Lulo']},
    {'level': 9, 'name': 'Yuzu', 'options': ['Quince', 'Bilberry', 'Persimmon', 'Canistel', 'Coco de mer', 'Medlar']},
    {'level': 9, 'name': 'American Mayapple', 'options': ['Elderberry', 'Cempedak', 'Sapodilla', 'Persimmon', 'Coco de mer', 'Araza']},
    {'level': 9, 'name': 'Sapodilla', 'options': ['Salak', 'Lanzones', 'Persimmon', 'American Mayapple', 'Java Plum', 'Aratiles']},
    {'level': 9, 'name': 'Sapote', 'options': ['Bilberry', 'Lanzones', 'American Mayapple', 'Sapodilla', 'Coco de mer', 'Ackee']},
    {'level': 10, 'name': 'Medlar', 'options': ['Jostaberry', 'Quince', 'Acerola', 'Yuzu', 'Akebi', 'Ackee']},
    {'level': 10, 'name': 'Ackee', 'options': ['Salak', 'Elderberry', 'Yuzu', 'Sapodilla', 'Aratiles', 'Lulo']},
    {'level': 10, 'name': 'Abiu', 'options': ['Boysenberry', 'Quince', 'Yuzu', 'Soursop', 'Aratiles', 'Medlar']},
    {'level': 10, 'name': 'Lulo', 'options': ['Cempedak', 'Salak', 'Acerola', 'Soursop', 'Aratiles', 'Ackee']},
    {'level': 10, 'name': 'Aratiles', 'options': ['Tangelo', 'Cempedak', 'Damson', 'Jabuticaba', 'Java Plum', 'Araza']},
    {'level': 10, 'name': 'Araza', 'options': ['Black Sapote', 'Salak', 'Jabuticaba', 'Persimmon', 'Abiu', 'Medlar']},
    {'level': 10, 'name': 'Akebi', 'options': ['Bilberry', 'Black Sapote', 'Yuzu', 'American Mayapple', 'Coco de mer', 'Medlar']},
    {'level': 10, 'name': 'Katmon', 'options': ['Salak', 'Quince', 'Jabuticaba', 'Damson', 'Coco de mer', 'Akebi']},
    {'level': 10, 'name': 'Coco de mer', 'options': ['Bilberry', 'Lanzones', 'Yuzu', 'American Mayapple', 'Akebi', 'Aratiles']},
    {'level': 10, 'name': 'Java Plum', 'options': ['Jostaberry', 'Cempedak', 'Persimmon', 'Sapote', 'Lulo', 'Araza']}
]

quiz = []

for fruit in fruits:
    fruit['urls'] =  fetcher.fetch('fruit', fruit['name'])
    quiz.append(fruit)

with open("output/fruit.json", "w") as f:
    f.write(json.dumps(quiz))
