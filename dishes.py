import json

import fetcher


dishes = [
    {'level': 1, 'name': 'Popcorn', 'options': ['Dosa', 'Ketchup', 'Kofta', 'Bombay Sandwich', 'Falafel', 'Parfait']},
    {'level': 1, 'name': 'Dosa', 'options': ['Popcorn', 'Biryani', 'Croissant', 'Kathi Roll', 'Trifle', 'Spring roll']},
    {'level': 1, 'name': 'Potato chips/crisps', 'options': ['Rajma chawal', 'Popcorn', 'Kofta', 'Tacos', 'Stinky tofu', 'Banana Bread']},
    {'level': 1, 'name': 'Ketchup', 'options': ['Pizza', 'French Fries/chips', 'Tacos', 'Momo', 'Apple Pie', 'Parfait']},
    {'level': 1, 'name': 'Ice cream', 'options': ['Ketchup', 'Molten Chocolate Cake', 'Aloo matar', 'Sundae', 'Bruschetta', 'Apple Pie']},
    {'level': 1, 'name': 'Corn on the cob', 'options': ['Gobi manchurian', 'Dosa', 'Momo', 'Bombay Sandwich', 'Burrito', 'Parfait']},
    {'level': 1, 'name': 'Biscuit', 'options': ['Rajma chawal', 'Dosa', 'Doughnut', 'Pasty', 'Stinky tofu', 'Apple Pie']},
    {'level': 1, 'name': 'Chutney', 'options': ['Dal(cooked lentils)', 'Popcorn', 'Pastry', 'Dal bhat', 'Fish and chips', 'Apple Pie']},
    {'level': 1, 'name': 'Pizza', 'options': ['Idli', 'Dal(cooked lentils)', 'Croissant', 'Kofta', 'Fudge', 'Trifle']},
    {'level': 1, 'name': 'Butter Garlic Naan', 'options': ['Cheesecake', 'Samosa', 'Croissant', 'Litti Chokha', 'Nan-e barbari', 'Crêpe']},
    {'level': 1, 'name': 'Biryani', 'options': ['Dal(cooked lentils)', 'Chutney', 'Aloo matar', 'Bombay Sandwich', 'Banana Bread', 'Spring roll']},
    {'level': 1, 'name': 'Idli', 'options': ['Molten Chocolate Cake', 'Rajma chawal', 'Momo', 'Kofta', 'Burrito', 'Bruschetta']},
    {'level': 1, 'name': 'Samosa', 'options': ['Gobi manchurian', 'Popcorn', 'Soufflé au chocolat', 'Pasty', 'Frozen yogurt', 'French toast']},
    {'level': 1, 'name': 'Jalebi', 'options': ['Biscuit', 'Pizza', 'Chow mein', 'Pasty', 'BLT Sandwich', 'Bruschetta']},
    {'level': 1, 'name': 'Gobi manchurian', 'options': ['Samosa', 'Dal(cooked lentils)', 'Sundae', 'Chow mein', 'Fish and chips', 'Burrito']},
    {'level': 1, 'name': 'Cheesecake', 'options': ['Corn on the cob', 'Chutney', 'Kofta', 'Chow mein', 'Jeon', 'Hamburger']},
    {'level': 1, 'name': 'French Fries/chips', 'options': ['Idli', 'Samosa', 'Kathi Roll', 'Bombay Sandwich', 'French toast', 'Fudge']},
    {'level': 1, 'name': 'Molten Chocolate Cake', 'options': ['Samosa', 'French Fries/chips', 'Kofta', 'Soufflé au chocolat', 'Hamburger', 'Apple Pie']},
    {'level': 1, 'name': 'Rajma chawal', 'options': ['Dosa', 'Pizza', 'Spaghetti', 'Tacos', 'Trifle', 'Spring roll']},
    {'level': 1, 'name': 'Dal(cooked lentils)', 'options': ['Samosa', 'Gobi manchurian', 'Momo', 'Ravioli', 'Banana Bread', 'Trifle']},
    {'level': 2, 'name': 'Spaghetti', 'options': ['Biscuit', 'Butter Garlic Naan', 'Pastry', 'Sundae', 'Spring roll', 'Fudge']},
    {'level': 2, 'name': 'Tacos', 'options': ['Jalebi', 'Biscuit', 'Litti Chokha', 'Milkshake', 'Nan-e barbari', 'Fish and chips']},
    {'level': 2, 'name': 'Hummus', 'options': ['Gobi manchurian', 'French Fries/chips', 'Soufflé au chocolat', 'Tacos', 'BLT Sandwich', 'Spring roll']},
    {'level': 2, 'name': 'Doughnut', 'options': ['Molten Chocolate Cake', 'Butter Garlic Naan', 'Kofta', 'Ravioli', 'Falafel', 'French toast']},
    {'level': 2, 'name': 'Kofta', 'options': ['Samosa', 'Rajma chawal', 'Aloo matar', 'Doughnut', 'Fish and chips', 'Crêpe']},
    {'level': 2, 'name': 'Croissant', 'options': ['Ketchup', 'Popcorn', 'Milkshake', 'Pastry', 'Trifle', 'BLT Sandwich']},
    {'level': 2, 'name': 'Sundae', 'options': ['Butter Garlic Naan', 'Samosa', 'Spaghetti', 'Tacos', 'Stinky tofu', 'Nan-e barbari']},
    {'level': 2, 'name': 'Chocolate Chip Cookie', 'options': ['Idli', 'Samosa', 'Pastry', 'Dal bhat', 'Hamburger', 'Frozen yogurt']},
    {'level': 2, 'name': 'Milkshake', 'options': ['Samosa', 'Cheesecake', 'Pasty', 'Croissant', 'Crêpe', 'Trifle']},
    {'level': 2, 'name': 'Aloo matar', 'options': ['Butter Garlic Naan', 'Jalebi', 'Milkshake', 'Dal bhat', 'Fish and chips', 'Fudge']},
    {'level': 2, 'name': 'Bombay Sandwich', 'options': ['Chutney', 'Cheesecake', 'Croissant', 'Litti Chokha', 'Banana Bread', 'Frozen yogurt']},
    {'level': 2, 'name': 'Pastry', 'options': ['Chutney', 'French Fries/chips', 'Spaghetti', 'Tacos', 'Jeon', 'Banana Bread']},
    {'level': 2, 'name': 'Dal bhat', 'options': ['Ketchup', 'Potato chips/crisps', 'Sundae', 'Soufflé au chocolat', 'Stinky tofu', 'Fish and chips']},
    {'level': 2, 'name': 'Pasty', 'options': ['Popcorn', 'Butter Garlic Naan', 'Sundae', 'Litti Chokha', 'Nan-e barbari', 'French toast']},
    {'level': 2, 'name': 'Momo', 'options': ['Dosa', 'Idli', 'Kathi Roll', 'Sundae', 'Fish and chips', 'Fudge']},
    {'level': 2, 'name': 'Soufflé au chocolat', 'options': ['Rajma chawal', 'Jalebi', 'Dal bhat', 'Litti Chokha', 'Banana Bread', 'Jeon']},
    {'level': 2, 'name': 'Kathi Roll', 'options': ['Corn on the cob', 'Dosa', 'Pastry', 'Bombay Sandwich', 'BLT Sandwich', 'Fudge']},
    {'level': 2, 'name': 'Ravioli', 'options': ['Jalebi', 'Ketchup', 'Chow mein', 'Pastry', 'Apple Pie', 'Burrito']},
    {'level': 2, 'name': 'Litti Chokha', 'options': ['Samosa', 'Ketchup', 'Chocolate Chip Cookie', 'Chow mein', 'Bruschetta', 'Apple Pie']},
    {'level': 2, 'name': 'Chow mein', 'options': ['Gobi manchurian', 'Idli', 'Milkshake', 'Spaghetti', 'Nan-e barbari', 'Apple Pie']},
    {'level': 3, 'name': 'Stinky tofu', 'options': ['Chow mein', 'Kathi Roll', 'Fudge', 'BLT Sandwich', 'Pho', 'Sushi']},
    {'level': 3, 'name': 'French toast', 'options': ['Aloo matar', 'Litti Chokha', 'Hamburger', 'Crêpe', 'Ciabatta', 'Lasagna']},
    {'level': 3, 'name': 'Fish and chips', 'options': ['Tacos', 'Hummus', 'French toast', 'Spring roll', 'Pho', 'Ciabatta']},
    {'level': 3, 'name': 'Hamburger', 'options': ['Ravioli', 'Kathi Roll', 'Burrito', 'Falafel', 'Penang assam laksa', 'Sorbet']},
    {'level': 3, 'name': 'Spring roll', 'options': ['Pastry', 'Ravioli', 'Apple Pie', 'BLT Sandwich', 'Sorbet', 'Beguni']},
    {'level': 3, 'name': 'Crêpe', 'options': ['Momo', 'Pastry', 'Burrito', 'French toast', 'Roti canai', 'Penang assam laksa']},
    {'level': 3, 'name': 'Apple Pie', 'options': ['Croissant', 'Doughnut', 'Bruschetta', 'Banana Bread', 'Lasagna', 'Crab cake']},
    {'level': 3, 'name': 'Bruschetta', 'options': ['Tacos', 'Litti Chokha', 'Spring roll', 'Pita', 'Sorbet', 'Roti canai']},
    {'level': 3, 'name': 'Frozen yogurt', 'options': ['Pastry', 'Momo', 'French toast', 'Stinky tofu', 'Pesto', 'Shish kebab']},
    {'level': 3, 'name': 'Nan-e barbari', 'options': ['Chocolate Chip Cookie', 'Dal bhat', 'Crêpe', 'Jeon', 'Baklava', 'Baba Ganoush']},
    {'level': 3, 'name': 'Burrito', 'options': ['Ravioli', 'Hummus', 'Trifle', 'Nan-e barbari', 'Beguni', 'Pad Thai']},
    {'level': 3, 'name': 'Trifle', 'options': ['Milkshake', 'Chow mein', 'Frozen yogurt', 'Falafel', 'Baklava', 'Sushi']},
    {'level': 3, 'name': 'Falafel', 'options': ['Dal bhat', 'Pastry', 'Bruschetta', 'Apple Pie', 'Souvlaki', 'Crab cake']},
    {'level': 3, 'name': 'Parfait', 'options': ['Croissant', 'Sundae', 'Spring roll', 'Banana Bread', 'Roti canai', 'Fajitas']},
    {'level': 3, 'name': 'Jeon', 'options': ['Spaghetti', 'Pasty', 'Stinky tofu', 'Banana Bread', 'Souvlaki', 'Ciabatta']},
    {'level': 3, 'name': 'Banana Bread', 'options': ['Chocolate Chip Cookie', 'Bombay Sandwich', 'Fudge', 'Stinky tofu', 'Lasagna', 'Penang assam laksa']},
    {'level': 3, 'name': 'Fudge', 'options': ['Milkshake', 'Hummus', 'French toast', 'Stinky tofu', 'Ciabatta', 'Shish kebab']},
    {'level': 3, 'name': 'BLT Sandwich', 'options': ['Momo', 'Pastry', 'Bruschetta', 'Frozen yogurt', 'Ciabatta', 'Penang assam laksa']},
    {'level': 3, 'name': 'Pita', 'options': ['Sundae', 'Kathi Roll', 'Hamburger', 'Parfait', 'Souvlaki', 'Penang assam laksa']},
    {'level': 4, 'name': 'Pho', 'options': ['Apple Pie', 'Banana Bread', 'Pesto', 'Ciabatta', 'Peperonata', 'Macarons']},
    {'level': 4, 'name': 'Chocolate soufflé', 'options': ['Jeon', 'Nan-e barbari', 'Fajitas', 'Penang assam laksa', 'Pastiera', 'Ramen']},
    {'level': 4, 'name': 'Fajitas', 'options': ['Crêpe', 'French toast', 'Pho', 'Sorbet', 'Phanaeng curry', 'Churros']},
    {'level': 4, 'name': 'Lasagna', 'options': ['Falafel', 'Stinky tofu', 'Fajitas', 'Souvlaki', 'Macarons', 'Bunny chow']},
    {'level': 4, 'name': 'Baklava', 'options': ['Fish and chips', 'Pita', 'Beguni', 'Souvlaki', 'Macarons', 'Phanaeng curry']},
    {'level': 4, 'name': 'Ciabatta', 'options': ['Parfait', 'Stinky tofu', 'Shish kebab', 'Sushi', 'Phanaeng curry', 'Macarons']},
    {'level': 4, 'name': 'Sorbet', 'options': ['French toast', 'Hamburger', 'Baklava', 'Madeleines', 'Loubia', 'Ramen']},
    {'level': 4, 'name': 'Sushi', 'options': ['Parfait', 'Frozen yogurt', 'Ciabatta', 'Souvlaki', 'Ramen', 'Phanaeng curry']},
    {'level': 4, 'name': 'Penang assam laksa', 'options': ['Frozen yogurt', 'Bruschetta', 'Souvlaki', 'Ciabatta', 'Bagel', 'Avial']},
    {'level': 4, 'name': 'Shish kebab', 'options': ['Crêpe', 'Apple Pie', 'Chocolate soufflé', 'Pho', 'Paella', "Buddha's Delight"]},
    {'level': 4, 'name': 'Crab cake', 'options': ['Parfait', 'French toast', 'Sorbet', 'Fondue', 'Kimchi', 'Peperonata']},
    {'level': 4, 'name': 'Pad Thai', 'options': ['Nan-e barbari', 'BLT Sandwich', 'Ciabatta', 'Crab cake', 'Tempe goreng', 'Jell-O']},
    {'level': 4, 'name': 'Madeleines', 'options': ['Trifle', 'Banana Bread', 'Baklava', 'Beguni', 'Kimchi', 'Bunny chow']},
    {'level': 4, 'name': 'Roti canai', 'options': ['Fudge', 'Apple Pie', 'Chocolate soufflé', 'Pad Thai', 'Kimchi', 'Bunny chow']},
    {'level': 4, 'name': 'Baba Ganoush', 'options': ['Banana Bread', 'Apple Pie', 'Souvlaki', 'Baklava', 'Kimchi', 'Avial']},
    {'level': 4, 'name': 'Fondue', 'options': ['Nan-e barbari', 'Crêpe', 'Fajitas', 'Shish kebab', 'Phanaeng curry', 'Macarons']},
    {'level': 4, 'name': 'Pesto', 'options': ['BLT Sandwich', 'Pita', 'Pho', 'Sushi', 'Bunny chow', 'Kimchi']},
    {'level': 4, 'name': 'Beguni', 'options': ['Crêpe', 'French toast', 'Pad Thai', 'Chocolate soufflé', 'Jell-O', 'Paella']},
    {'level': 4, 'name': 'Souvlaki', 'options': ['Burrito', 'Apple Pie', 'Madeleines', 'Pesto', 'Patrode', 'Kimchi']},
    {'level': 5, 'name': 'Phanaeng curry', 'options': ['Fondue', 'Pad Thai', 'Kimchi', 'Patrode', 'Yakisoba', 'Nigiri']},
    {'level': 5, 'name': 'Ramen', 'options': ['Pesto', 'Lasagna', 'Macarons', 'Bunny chow', 'Nigiri', 'Chorizo']},
    {'level': 5, 'name': 'Jell-O', 'options': ['Crab cake', 'Roti canai', 'Kimchi', 'Avial', 'Zeytoon parvardeh', 'Éclair']},
    {'level': 5, 'name': 'Patrode', 'options': ['Crab cake', 'Chocolate soufflé', 'Loubia', 'Avial', 'Gyros', 'Zeytoon parvardeh']},
    {'level': 5, 'name': 'Paella', 'options': ['Roti canai', 'Souvlaki', 'Avial', 'Tempe goreng', 'Enchilada', 'Yakisoba']},
    {'level': 5, 'name': 'Bunny chow', 'options': ['Pho', 'Shish kebab', 'Kimchi', "Buddha's Delight", 'Focaccia', 'Panini']},
    {'level': 5, 'name': 'Macarons', 'options': ['Baklava', 'Lasagna', 'Pastiera', 'Ramen', 'Yorkshire Pudding', 'Ratatouille']},
    {'level': 5, 'name': 'Churros', 'options': ['Chocolate soufflé', 'Fondue', "Buddha's Delight", 'Bunny chow', 'Ice Cream Sandwich', 'Yakisoba']},
    {'level': 5, 'name': 'Peperonata', 'options': ['Penang assam laksa', 'Shish kebab', 'Avial', 'Patrode', 'Yorkshire Pudding', 'Goulash']},
    {'level': 5, 'name': 'Kimchi', 'options': ['Crab cake', 'Baklava', "Buddha's Delight", 'Macarons', 'Ratatouille', 'Focaccia']},
    {'level': 5, 'name': 'Bagel', 'options': ['Roti canai', 'Ciabatta', 'Macarons', 'Kimchi', 'Ratatouille', 'Éclair']},
    {'level': 5, 'name': 'Tempe goreng', 'options': ['Baba Ganoush', 'Pho', 'Macarons', 'Kimchi', 'Yorkshire Pudding', 'Poke']},
    {'level': 5, 'name': 'Loubia', 'options': ['Baklava', 'Baba Ganoush', 'Peperonata', 'Macarons', 'Panini', 'Enchilada']},
    {'level': 5, 'name': 'Avial', 'options': ['Penang assam laksa', 'Pad Thai', 'Ramen', 'Jell-O', 'Moussaka', 'Ratatouille']},
    {'level': 5, 'name': 'Pastiera', 'options': ['Shish kebab', 'Beguni', 'Phanaeng curry', 'Jell-O', 'Poke', 'Zeytoon parvardeh']},
    {'level': 5, 'name': "Buddha's Delight", 'options': ['Penang assam laksa', 'Lasagna', 'Ramen', 'Bunny chow', 'Calzone', 'Goulash']},
    {'level': 6, 'name': 'Massaman curry', 'options': ['Ramen', 'Loubia', 'Éclair', 'Enchilada', 'Dim Sum', 'Kunāfah']},
    {'level': 6, 'name': 'Poke', 'options': ['Paella', 'Tempe goreng', 'Gyros', 'Focaccia', 'Koshary', 'Gachas']},
    {'level': 6, 'name': 'Yakisoba', 'options': ['Bagel', 'Jell-O', 'Panini', 'Chorizo', 'Dim Sum', 'Tempe orek']},
    {'level': 6, 'name': 'Ice Cream Sandwich', 'options': ['Bagel', "Buddha's Delight", 'Chorizo', 'Poke', 'Kunāfah', 'Koliva']},
    {'level': 6, 'name': 'Turkish delight/Lokum', 'options': ['Jell-O', 'Bunny chow', 'Zeytoon parvardeh', 'Ice Cream Sandwich', 'Schnitzel', 'Koliva']},
    {'level': 6, 'name': 'Gyros', 'options': ['Patrode', 'Kimchi', 'Ratatouille', 'Yorkshire Pudding', 'Gua bao', 'Gachas']},
    {'level': 6, 'name': 'Calzone', 'options': ['Tempe goreng', 'Macarons', 'Moussaka', 'Enchilada', 'Gua bao', 'Dim Sum']},
    {'level': 6, 'name': 'Panini', 'options': ['Phanaeng curry', 'Pastiera', 'Moussaka', 'Massaman curry', 'Sekihan', 'Koshary']},
    {'level': 6, 'name': 'Chorizo', 'options': ['Avial', 'Tempe goreng', 'Ratatouille', 'Zeytoon parvardeh', 'Gachas', 'Okoshi']},
    {'level': 6, 'name': 'Corn dog', 'options': ['Macarons', 'Ramen', 'Chorizo', 'Calzone', 'Makdous', 'Schnitzel']},
    {'level': 6, 'name': 'Nigiri', 'options': ['Phanaeng curry', 'Ramen', 'Yakisoba', 'Goulash', 'Pesto Genovese', 'Carciofi alla Romana']},
    {'level': 6, 'name': 'Enchilada', 'options': ['Loubia', 'Churros', 'Goulash', 'Corn dog', 'Gazpacho de mango', 'Schnitzel']},
    {'level': 6, 'name': 'Focaccia', 'options': ['Loubia', 'Pastiera', 'Enchilada', 'Ice Cream Sandwich', 'Okoshi', 'Maakouda']},
    {'level': 6, 'name': 'Éclair', 'options': ['Churros', 'Bagel', 'Yorkshire Pudding', 'Poke', 'Cassata', 'Tiramisù']},
    {'level': 6, 'name': 'Zeytoon parvardeh', 'options': ['Ramen', 'Tempe goreng', 'Corn dog', 'Ice Cream Sandwich', 'Gazpacho de mango', 'Okoshi']},
    {'level': 6, 'name': 'Goulash', 'options': ['Macarons', 'Tempe goreng', 'Éclair', 'Focaccia', 'Maakouda', 'Carciofi alla Romana']},
    {'level': 6, 'name': 'Moussaka', 'options': ['Avial', 'Ramen', 'Yorkshire Pudding', 'Massaman curry', 'Sekihan', 'Okoshi']},
    {'level': 6, 'name': 'Ratatouille', 'options': ["Buddha's Delight", 'Loubia', 'Poke', 'Panini', 'Koliva', 'Dim Sum']},
    {'level': 6, 'name': 'Yorkshire Pudding', 'options': ['Bunny chow', 'Pastiera', 'Gyros', 'Poke', 'Tiramisù', 'Kunāfah']},
    {'level': 7, 'name': 'Gua bao', 'options': ['Nigiri', 'Gyros', 'Maakouda', 'Tempe orek', 'Som tam', 'Atsuage']},
    {'level': 7, 'name': 'Kunāfah', 'options': ['Goulash', 'Panini', 'Koliva', 'Tempe orek', 'Carciofi alla Giudía', 'Som tam']},
    {'level': 7, 'name': 'Dim Sum', 'options': ['Corn dog', 'Massaman curry', 'Carciofi alla Romana', 'Tiramisù', 'Shakshuka', 'Som tam']},
    {'level': 7, 'name': 'Schnitzel', 'options': ['Ice Cream Sandwich', 'Turkish delight/Lokum', 'Koshary', 'Tiramisù', 'Zaalouk', 'Shakshuka']},
    {'level': 7, 'name': 'Tempe orek', 'options': ['Ratatouille', 'Focaccia', 'Koshary', 'Gazpacho de mango', 'Ketoprak', 'Atsuage']},
    {'level': 7, 'name': 'Carciofi alla Romana', 'options': ['Focaccia', 'Éclair', 'Kunāfah', 'Maakouda', 'Ketoprak', 'Shakshuka']},
    {'level': 7, 'name': 'Koliva', 'options': ['Corn dog', 'Nigiri', 'Pesto Genovese', 'Schnitzel', 'Boribap', 'Torrone']},
    {'level': 7, 'name': 'Maakouda', 'options': ['Ice Cream Sandwich', 'Moussaka', 'Tiramisù', 'Kunāfah', 'Som tam', 'Tortas']},
    {'level': 7, 'name': 'Cassata', 'options': ['Éclair', 'Yorkshire Pudding', 'Carciofi alla Romana', 'Tempe orek', 'Torrone', 'Boribap']},
    {'level': 7, 'name': 'Sekihan', 'options': ['Panini', 'Nigiri', 'Schnitzel', 'Koshary', 'Tortas', 'Tong sui']},
    {'level': 7, 'name': 'Makdous', 'options': ['Corn dog', 'Nigiri', 'Cassata', 'Dim Sum', 'Clafoutis', 'Kateh']},
    {'level': 7, 'name': 'Okoshi', 'options': ['Goulash', 'Yakisoba', 'Gazpacho de mango', 'Cassata', 'Boribap', 'Crumble']},
    {'level': 7, 'name': 'Koshary', 'options': ['Gyros', 'Turkish delight/Lokum', 'Cassata', 'Gua bao', 'Milho frito', 'Carciofi alla Giudía']},
    {'level': 7, 'name': 'Tiramisù', 'options': ['Nigiri', 'Panini', 'Sekihan', 'Maakouda', 'Shakshuka', 'Badrijani']},
    {'level': 7, 'name': 'Gazpacho de mango', 'options': ['Corn dog', 'Yorkshire Pudding', 'Dim Sum', 'Koliva', 'Maharagwe', 'Tortas']},
    {'level': 7, 'name': 'Gachas', 'options': ['Enchilada', 'Moussaka', 'Pesto Genovese', 'Kunāfah', 'Torrone', 'Carciofi alla Giudía']},
    {'level': 8, 'name': 'Som tam', 'options': ['Koliva', 'Kunāfah', 'Crumble', 'Kateh', 'Tombet', 'Mayak gimbap']},
    {'level': 8, 'name': 'Tortas', 'options': ['Schnitzel', 'Pesto Genovese', 'Carciofi alla Giudía', 'Speculaas', 'Moin moin', 'Satay']},
    {'level': 8, 'name': 'Aburaage', 'options': ['Maakouda', 'Pesto Genovese', 'Tortas', 'Speculaas', 'Pastel de Belém', 'Mahjouba']},
    {'level': 8, 'name': 'Speculaas', 'options': ['Schnitzel', 'Makdous', 'Shakshuka', 'Milho frito', 'Jiaozi', 'Pavlova']},
    {'level': 8, 'name': 'Kateh', 'options': ['Gua bao', 'Sekihan', 'Carciofi alla Giudía', 'Speculaas', 'Sfogliatella', 'Poutine']},
    {'level': 8, 'name': 'Boribap', 'options': ['Pesto Genovese', 'Carciofi alla Romana', 'Zaalouk', 'Aburaage', 'Poutine', 'Barbacoa']},
    {'level': 8, 'name': 'Carciofi alla Giudía', 'options': ['Cassata', 'Dim Sum', 'Ketoprak', 'Torrone', 'Moin moin', 'Jiaozi']},
    {'level': 8, 'name': 'Crumble', 'options': ['Maakouda', 'Gachas', 'Tong sui', 'Amaretti', 'Moin moin', 'Sfogliatella']},
    {'level': 8, 'name': 'Shakshuka', 'options': ['Koshary', 'Schnitzel', 'Ketoprak', 'Crumble', 'Poutine', 'Revithia']},
    {'level': 8, 'name': 'Atsuage', 'options': ['Tempe orek', 'Schnitzel', 'Som tam', 'Clafoutis', 'Barbacoa', 'Mahjouba']},
    {'level': 8, 'name': 'Clafoutis', 'options': ['Makdous', 'Tiramisù', 'Badrijani', 'Milho frito', 'Revithia', 'Mahjouba']},
    {'level': 8, 'name': 'Ketoprak', 'options': ['Dim Sum', 'Kunāfah', 'Carciofi alla Giudía', 'Shakshuka', 'Poutine', 'Tombet']},
    {'level': 8, 'name': 'Amaretti', 'options': ['Sekihan', 'Schnitzel', 'Carciofi alla Giudía', 'Zaalouk', 'Ful medames', 'Börek']},
    {'level': 8, 'name': 'Milho frito', 'options': ['Sekihan', 'Koshary', 'Atsuage', 'Aburaage', 'Provoleta', 'Mayak gimbap']},
    {'level': 8, 'name': 'Tong sui', 'options': ['Pesto Genovese', 'Maakouda', 'Kateh', 'Torrone', 'Matbucha', 'Revithia']},
    {'level': 8, 'name': 'Maharagwe', 'options': ['Maakouda', 'Schnitzel', 'Tong sui', 'Tortas', 'Jiaozi', 'Provoleta']},
    {'level': 8, 'name': 'Zaalouk', 'options': ['Gachas', 'Makdous', 'Kateh', 'Aburaage', 'Revithia', 'Karē']},
    {'level': 8, 'name': 'Torrone', 'options': ['Carciofi alla Romana', 'Makdous', 'Som tam', 'Zaalouk', 'Jiaozi', 'Poutine']},
    {'level': 8, 'name': 'Badrijani', 'options': ['Makdous', 'Gachas', 'Maharagwe', 'Som tam', 'Tombet', 'Mayak gimbap']},
    {'level': 9, 'name': 'Tombet', 'options': ['Clafoutis', 'Boribap', 'Pastel de Belém', 'Mahjouba', 'Tteok', 'Manti']},
    {'level': 9, 'name': 'Pastel de Belém', 'options': ['Carciofi alla Giudía', 'Tortas', 'Barbacoa', 'Batagor', 'Tom yum goong', 'Poljički soparnik']},
    {'level': 9, 'name': 'Barbacoa', 'options': ['Ketoprak', 'Som tam', 'Tombet', 'Moin moin', 'Dondurma', 'Tteokbokki']},
    {'level': 9, 'name': 'Sfogliatella', 'options': ['Som tam', 'Ketoprak', 'Barbacoa', 'Mahjouba', 'Bulgogi', 'Bibimbap']},
    {'level': 9, 'name': 'Mayak gimbap', 'options': ['Speculaas', 'Tong sui', 'Matbucha', 'Sfogliatella', 'Rechta', 'Ogokbap']},
    {'level': 9, 'name': 'Matbucha', 'options': ['Speculaas', 'Maharagwe', 'Tombet', 'Jiaozi', 'Kepta duona', 'Bulgogi']},
    {'level': 9, 'name': 'Moin moin', 'options': ['Boribap', 'Tortas', 'Provoleta', 'Barbacoa', 'Poljički soparnik', 'Nougat']},
    {'level': 9, 'name': 'Börek', 'options': ['Crumble', 'Ketoprak', 'Pastel de Belém', 'Batagor', 'Kaiserschmarrn', 'Rechta']},
    {'level': 9, 'name': 'Jiaozi', 'options': ['Torrone', 'Atsuage', 'Poutine', 'Tombet', 'Churrasco', 'Tteokbokki']},
    {'level': 9, 'name': 'Batagor', 'options': ['Atsuage', 'Kateh', 'Jiaozi', 'Tombet', 'Arepas', 'Bulgogi']},
    {'level': 9, 'name': 'Provoleta', 'options': ['Maharagwe', 'Atsuage', 'Satay', 'Jiaozi', 'Prebranac', 'Ardei copți']},
    {'level': 9, 'name': 'Mahjouba', 'options': ['Som tam', 'Crumble', 'Provoleta', 'Jiaozi', 'Tteok', 'Fasole batută']},
    {'level': 9, 'name': 'Karē', 'options': ['Tortas', 'Zaalouk', 'Satay', 'Matbucha', 'Pastel de nata', 'Churrasco']},
    {'level': 9, 'name': 'Pavlova', 'options': ['Carciofi alla Giudía', 'Speculaas', 'Batagor', 'Provoleta', 'Kaiserschmarrn', 'Tom yum goong']},
    {'level': 9, 'name': 'Revithia', 'options': ['Clafoutis', 'Atsuage', 'Pavlova', 'Ful medames', 'Bulgogi', 'Fasole batută']},
    {'level': 9, 'name': 'Ful medames', 'options': ['Ketoprak', 'Milho frito', 'Karē', 'Börek', 'Bibimbap', 'Tteokbokki']},
    {'level': 9, 'name': 'Satay', 'options': ['Maharagwe', 'Speculaas', 'Mayak gimbap', 'Revithia', 'Ardei copți', 'Fasolada']},
    {'level': 9, 'name': 'Poutine', 'options': ['Tortas', 'Maharagwe', 'Revithia', 'Pavlova', 'Poljički soparnik', 'Tom yum goong']},
    {'level': 10, 'name': 'Tom yum goong', 'options': ['Shakshuka', 'Atsuage', 'Mayak gimbap', 'Matbucha', 'Kaiserschmarrn', 'Ogokbap']},
    {'level': 10, 'name': 'Pierogi', 'options': ['Zaalouk', 'Clafoutis', 'Barbacoa', 'Tombet', 'Ogokbap', 'Kaiserschmarrn']},
    {'level': 10, 'name': 'Ogokbap', 'options': ['Milho frito', 'Clafoutis', 'Poutine', 'Börek', 'Peixinhos da horta', 'Dondurma']},
    {'level': 10, 'name': 'Arepas', 'options': ['Aburaage', 'Kateh', 'Pavlova', 'Ful medames', 'Pierogi', 'Tteok']},
    {'level': 10, 'name': 'Tteok', 'options': ['Crumble', 'Speculaas', 'Pastel de Belém', 'Barbacoa', 'Manti', 'Ogokbap']},
    {'level': 10, 'name': 'Prebranac', 'options': ['Milho frito', 'Tortas', 'Ful medames', 'Pavlova', 'Kepta duona', 'Ogokbap']},
    {'level': 10, 'name': 'Tteokbokki', 'options': ['Tong sui', 'Kateh', 'Ful medames', 'Mayak gimbap', 'Pastel de nata', 'Bibimbap']},
    {'level': 10, 'name': 'Churrasco', 'options': ['Shakshuka', 'Aburaage', 'Barbacoa', 'Mahjouba', 'Kaiserschmarrn', 'Tteok']},
    {'level': 10, 'name': 'Fasolada', 'options': ['Tortas', 'Som tam', 'Provoleta', 'Satay', 'Dondurma', 'Nougat']},
    {'level': 10, 'name': 'Nougat', 'options': ['Zaalouk', 'Som tam', 'Moin moin', 'Tombet', 'Dondurma', 'Bibimbap']},
    {'level': 10, 'name': 'Kaiserschmarrn', 'options': ['Zaalouk', 'Amaretti', 'Barbacoa', 'Sfogliatella', 'Prebranac', 'Nougat']},
    {'level': 10, 'name': 'Ardei copți', 'options': ['Badrijani', 'Som tam', 'Ful medames', 'Batagor', 'Bibimbap', 'Peixinhos da horta']},
    {'level': 10, 'name': 'Dondurma', 'options': ['Crumble', 'Ketoprak', 'Matbucha', 'Sfogliatella', 'Kaiserschmarrn', 'Churrasco']},
    {'level': 10, 'name': 'Poljički soparnik', 'options': ['Crumble', 'Shakshuka', 'Karē', 'Börek', 'Fasole batută', 'Dondurma']},
    {'level': 10, 'name': 'Bibimbap', 'options': ['Zaalouk', 'Speculaas', 'Börek', 'Moin moin', 'Prebranac', 'Pierogi']},
    {'level': 10, 'name': 'Manti', 'options': ['Tortas', 'Badrijani', 'Provoleta', 'Mayak gimbap', 'Churrasco', 'Pierogi']},
    {'level': 10, 'name': 'Peixinhos da horta', 'options': ['Shakshuka', 'Kateh', 'Poutine', 'Sfogliatella', 'Kaiserschmarrn', 'Dondurma']},
    {'level': 10, 'name': 'Fasole batută', 'options': ['Badrijani', 'Boribap', 'Moin moin', 'Tombet', 'Dondurma', 'Arepas']},
    {'level': 10, 'name': 'Bulgogi', 'options': ['Badrijani', 'Shakshuka', 'Moin moin', 'Börek', 'Kepta duona', 'Peixinhos da horta']},
    {'level': 10, 'name': 'Kepta duona', 'options': ['Zaalouk', 'Boribap', 'Pastel de Belém', 'Ful medames', 'Fasolada', 'Rechta']},
    {'level': 10, 'name': 'Rechta', 'options': ['Badrijani', 'Milho frito', 'Poutine', 'Batagor', 'Dondurma', 'Ardei copți']}
]

quiz = []

for dish in dishes:
    dish['urls'] =  fetcher.fetch('dish', dish['name'])
    quiz.append(dish)

with open("output/dishes.json", "w") as f:
    f.write(json.dumps(quiz))
