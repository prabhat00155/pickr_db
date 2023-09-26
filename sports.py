import fetcher


sports = [
    {'level': 1, 'name': 'Football', 'options': ['Cricket', 'Volleyball', 'Darts', 'Hockey', 'Motorcycle racing', 'Squash']},
    {'level': 1, 'name': 'Tennis', 'options': ['Golf', 'Arm Wrestling', 'Kushti', 'Ice hockey', 'Water polo', 'Badminton']},
    {'level': 1, 'name': 'Cricket', 'options': ['Arm Wrestling', 'Hockey', 'Kushti', 'Tug of War', 'Trampolining', 'Foosball']},
    {'level': 1, 'name': 'Formula 1', 'options': ['Swimming', 'Cricket', 'Sprint', 'Kushti', 'Motorcycle racing', 'Water polo']},
    {'level': 1, 'name': 'Rugby', 'options': ['Volleyball', 'Cycling', 'Kho kho', 'Netball', 'Sumo', 'Hurdling']},
    {'level': 1, 'name': 'Baseball', 'options': ['Tennis', 'Boxing', 'American Football', 'Bowling', 'Hurdling', 'Snowboarding']},
    {'level': 1, 'name': 'Hockey', 'options': ['Golf', 'Basketball', 'Darts', 'Polo', 'Standup paddleboarding', 'Squash']},
    {'level': 1, 'name': 'Basketball', 'options': ['Horse Racing', 'Boxing', 'Tug of War', 'Kushti', 'Hurdling', 'Water polo']},
    {'level': 1, 'name': 'Volleyball', 'options': ['Horse Racing', 'Cricket', 'Sprint', 'Kickboxing', 'Standup paddleboarding', 'Snowboarding']},
    {'level': 1, 'name': 'Arm Wrestling', 'options': ['Badminton', 'Cricket', 'Kite flying', 'American Football', 'Rafting', 'Snowboarding']},
    {'level': 1, 'name': 'Golf', 'options': ['Cycling', 'Tennis', 'Netball', 'Kabaddi', 'Standup paddleboarding', 'Snowboarding']},
    {'level': 1, 'name': 'Table Tennis', 'options': ['Cycling', 'Arm Wrestling', 'Kickboxing', 'Tug of War', 'Squash', 'Motorcycle racing']},
    {'level': 1, 'name': 'Boxing', 'options': ['Cricket', 'Basketball', 'Darts', 'Kushti', 'Parasailing', 'Motorcycle racing']},
    {'level': 1, 'name': 'Badminton', 'options': ['Table Tennis', 'Rugby', 'Karate', 'Snooker', 'Paragliding', 'Kayaking']},
    {'level': 1, 'name': 'Archery', 'options': ['Hockey', 'Arm Wrestling', 'Rock climbing', 'Sprint', 'Water polo', 'Snowboarding']},
    {'level': 1, 'name': 'Swimming', 'options': ['Football', 'Volleyball', 'Ice hockey', 'Kushti', 'Squash', 'Australian football']},
    {'level': 1, 'name': 'Cycling', 'options': ['Archery', 'Badminton', 'Tug of War', 'Kho kho', 'Paragliding', 'Snowboarding']},
    {'level': 1, 'name': 'Horse Racing', 'options': ['Basketball', 'Badminton', 'Bowling', 'Kushti', 'Trampolining', 'Parasailing']},
    {'level': 2, 'name': 'Netball', 'options': ['Horse Racing', 'Volleyball', 'Darts', 'Kushti', 'Trampolining', 'Rafting']},
    {'level': 2, 'name': 'American Football', 'options': ['Basketball', 'Tennis', 'Kabaddi', 'Polo', 'Trampolining', 'Parasailing']},
    {'level': 2, 'name': 'Kickboxing', 'options': ['Basketball', 'Horse Racing', 'Bowling', 'Kushti', 'Hurdling', 'Sumo']},
    {'level': 2, 'name': 'Ice hockey', 'options': ['Formula 1', 'Horse Racing', 'Sprint', 'Carrom', 'Rafting', 'Australian football']},
    {'level': 2, 'name': 'Kho kho', 'options': ['Football', 'Badminton', 'Kushti', 'Snooker', 'Parasailing', 'Water polo']},
    {'level': 2, 'name': 'Kabaddi', 'options': ['Boxing', 'Cycling', 'Polo', 'Karate', 'Sumo', 'Australian football']},
    {'level': 2, 'name': 'Polo', 'options': ['Horse Racing', 'Golf', 'Carrom', 'Netball', 'Paragliding', 'Powerlifting']},
    {'level': 2, 'name': 'Bowling', 'options': ['Golf', 'Horse Racing', 'Rock climbing', 'Kite flying', 'Australian football', 'Motorcycle racing']},
    {'level': 2, 'name': 'Darts', 'options': ['Boxing', 'Golf', 'Kabaddi', 'Sprint', 'Trampolining', 'Squash']},
    {'level': 2, 'name': 'Snooker', 'options': ['Football', 'Boxing', 'Sprint', 'Kho kho', 'Powerlifting', 'Australian football']},
    {'level': 2, 'name': 'Tug of War', 'options': ['Cricket', 'Formula 1', 'Snooker', 'Kho kho', 'Powerlifting', 'Kayaking']},
    {'level': 2, 'name': 'Carrom', 'options': ['Boxing', 'Table Tennis', 'Kite flying', 'Kickboxing', 'Parasailing', 'Squash']},
    {'level': 2, 'name': 'Kite flying', 'options': ['Swimming', 'Football', 'Polo', 'Kickboxing', 'Trampolining', 'Motorcycle racing']},
    {'level': 2, 'name': 'Gymnastics', 'options': ['Horse Racing', 'Basketball', 'Kite flying', 'Karate', 'Motorcycle racing', 'Standup paddleboarding']},
    {'level': 2, 'name': 'Karate', 'options': ['Volleyball', 'Table Tennis', 'Kabaddi', 'Netball', 'Standup paddleboarding', 'Paragliding']},
    {'level': 2, 'name': 'Kushti', 'options': ['Cricket', 'Baseball', 'Rock climbing', 'American Football', 'Standup paddleboarding', 'Rafting']},
    {'level': 2, 'name': 'Rock climbing', 'options': ['Volleyball', 'Basketball', 'Darts', 'Ice hockey', 'Kayaking', 'Powerlifting']},
    {'level': 2, 'name': 'Sprint', 'options': ['Archery', 'Formula 1', 'Ice hockey', 'Snooker', 'Parasailing', 'Powerlifting']},
    {'level': 3, 'name': 'Water polo', 'options': ['Rock climbing', 'Kickboxing', 'Trampolining', 'Motorcycle racing', 'Beach volleyball', 'Pole vault']},
    {'level': 3, 'name': 'Squash', 'options': ['Rock climbing', 'Darts', 'Snowboarding', 'Hurdling', 'Thumb wrestling', 'Elephant polo']},
    {'level': 3, 'name': 'Australian football', 'options': ['American Football', 'Karate', 'Foosball', 'Rafting', 'Thumb wrestling', 'Alpine skiing']},
    {'level': 3, 'name': 'Snowboarding', 'options': ['Kickboxing', 'Darts', 'Paragliding', 'Motorcycle racing', 'Segway polo', 'Elephant polo']},
    {'level': 3, 'name': 'Powerlifting', 'options': ['American Football', 'Polo', 'Foosball', 'Water polo', 'Fencing', 'Beach volleyball']},
    {'level': 3, 'name': 'Foosball', 'options': ['Karate', 'Kabaddi', 'Rafting', 'Parasailing', 'Segway polo', 'Rowing']},
    {'level': 3, 'name': 'Sumo', 'options': ['Kite flying', 'Tug of War', 'Foosball', 'Australian football', 'Segway polo', 'Beach volleyball']},
    {'level': 3, 'name': 'Paragliding', 'options': ['Netball', 'Darts', 'Sumo', 'Water polo', 'Sailing', 'Pole vault']},
    {'level': 3, 'name': 'Trampolining', 'options': ['American Football', 'Kho kho', 'Kayaking', 'Hurdling', 'Elephant polo', 'Paintball']},
    {'level': 3, 'name': 'Hurdling', 'options': ['Snooker', 'Rock climbing', 'Paragliding', 'Sumo', 'Beach volleyball', 'Hang gliding']},
    {'level': 3, 'name': 'Kayaking', 'options': ['Ice hockey', 'Netball', 'Rafting', 'Motorcycle racing', 'Segway polo', 'Paintball']},
    {'level': 3, 'name': 'Rafting', 'options': ['Kickboxing', 'Gymnastics', 'Squash', 'Parasailing', 'Alpine skiing', 'Fencing']},
    {'level': 3, 'name': 'Parasailing', 'options': ['Kabaddi', 'Karate', 'Snowboarding', 'Trampolining', 'Beach volleyball', 'Fencing']},
    {'level': 3, 'name': 'Standup paddleboarding', 'options': ['Kushti', 'Karate', 'Sumo', 'Australian football', 'Elephant polo', 'Alpine skiing']},
    {'level': 3, 'name': 'Motorcycle racing', 'options': ['Darts', 'Kushti', 'Powerlifting', 'Parasailing', 'Fencing', 'Sailing']},
    {'level': 4, 'name': 'Rowing', 'options': ['Foosball', 'Parasailing', 'Thumb wrestling', 'Alpine skiing', 'Woodball', 'Softball']},
    {'level': 4, 'name': 'Roller hockey', 'options': ['Foosball', 'Hurdling', 'Sailing', 'Beach volleyball', 'Yak polo', 'Hammer throw']},
    {'level': 4, 'name': 'Paintball', 'options': ['Motorcycle racing', 'Parasailing', 'Pole vault', 'Hang gliding', 'Softball', 'Bicycle polo']},
    {'level': 4, 'name': 'Elephant polo', 'options': ['Rafting', 'Snowboarding', 'Fencing', 'Rowing', 'Underwater rugby', 'Shuffleboard']},
    {'level': 4, 'name': 'Segway polo', 'options': ['Australian football', 'Standup paddleboarding', 'Elephant polo', 'Rowing', 'Bicycle polo', 'Scootering']},
    {'level': 4, 'name': 'Beach volleyball', 'options': ['Kayaking', 'Australian football', 'Paintball', 'Rowing', 'Softball', 'Shuffleboard']},
    {'level': 4, 'name': 'Sailing', 'options': ['Parasailing', 'Powerlifting', 'Thumb wrestling', 'Roller hockey', 'Bocce', 'Cornhole']},
    {'level': 4, 'name': 'Hang gliding', 'options': ['Powerlifting', 'Kayaking', 'Fencing', 'Roller hockey', 'Scootering', 'Underwater rugby']},
    {'level': 4, 'name': 'Pole vault', 'options': ['Standup paddleboarding', 'Trampolining', 'Fencing', 'Elephant polo', 'Hammer throw', 'Shuffleboard']},
    {'level': 4, 'name': 'Thumb wrestling', 'options': ['Sumo', 'Powerlifting', 'Rowing', 'Pole vault', 'Bicycle polo', 'Yak polo']},
    {'level': 4, 'name': 'Alpine skiing', 'options': ['Squash', 'Powerlifting', 'Segway polo', 'Hang gliding', 'Beach tennis', 'Croquet']},
    {'level': 4, 'name': 'Fencing', 'options': ['Powerlifting', 'Paragliding', 'Paintball', 'Segway polo', 'Unicycle hockey', 'Woodball']},
    {'level': 5, 'name': 'Canoeing', 'options': ['Paintball', 'Elephant polo', 'Unicycle hockey', 'Hammer throw', 'Figure skating', 'Shot put']},
    {'level': 5, 'name': 'Croquet', 'options': ['Alpine skiing', 'Rowing', 'Canoeing', 'Cornhole', 'Roundnet', 'Kitesurfing']},
    {'level': 5, 'name': 'Softball', 'options': ['Paintball', 'Beach volleyball', 'Unicycle hockey', 'Cornhole', 'Figure skating', 'Roundnet']},
    {'level': 5, 'name': 'Bocce', 'options': ['Elephant polo', 'Thumb wrestling', 'Underwater rugby', 'Yak polo', 'Kitesurfing', 'Kung fu']},
    {'level': 5, 'name': 'Shuffleboard', 'options': ['Paintball', 'Thumb wrestling', 'Softball', 'Canoeing', 'Shot put', 'Figure skating']},
    {'level': 5, 'name': 'Bicycle polo', 'options': ['Fencing', 'Hang gliding', 'Bocce', 'Beach tennis', 'Roundnet', 'Shot put']},
    {'level': 5, 'name': 'Beach tennis', 'options': ['Segway polo', 'Elephant polo', 'Yak polo', 'Unicycle hockey', 'Kitesurfing', 'Lacrosse']},
    {'level': 5, 'name': 'Yak polo', 'options': ['Pole vault', 'Roller hockey', 'Underwater rugby', 'Bicycle polo', 'Windsurfing', 'Kitesurfing']},
    {'level': 5, 'name': 'Woodball', 'options': ['Thumb wrestling', 'Hang gliding', 'Yak polo', 'Underwater rugby', 'Kung fu', 'Lacrosse']},
    {'level': 5, 'name': 'Cornhole', 'options': ['Fencing', 'Hang gliding', 'Softball', 'Canoeing', 'Kitesurfing', 'Figure skating']},
    {'level': 5, 'name': 'Underwater rugby', 'options': ['Beach volleyball', 'Thumb wrestling', 'Scootering', 'Shuffleboard', 'Figure skating', 'Roundnet']},
    {'level': 5, 'name': 'Scootering', 'options': ['Pole vault', 'Fencing', 'Yak polo', 'Bocce', 'Racquetball', 'Kitesurfing']},
    {'level': 5, 'name': 'Hammer throw', 'options': ['Sailing', 'Roller hockey', 'Shuffleboard', 'Beach tennis', 'Windsurfing', 'Discus throw']},
    {'level': 5, 'name': 'Unicycle hockey', 'options': ['Alpine skiing', 'Elephant polo', 'Yak polo', 'Underwater rugby', 'Kitesurfing', 'Figure skating']},
    {'level': 6, 'name': 'Discus throw', 'options': ['Woodball', 'Scootering', 'Kitesurfing', 'Windsurfing', 'Ringette', 'Pickleball']},
    {'level': 6, 'name': 'Shot put', 'options': ['Shuffleboard', 'Croquet', 'Lacrosse', 'Discus throw', 'Ice cross downhill', 'Steeplechase']},
    {'level': 6, 'name': 'Lacrosse', 'options': ['Croquet', 'Canoeing', 'Racquetball', 'Discus throw', 'Hurling', 'Kite buggy']},
    {'level': 6, 'name': 'Figure skating', 'options': ['Shuffleboard', 'Softball', 'Kung fu', 'Shot put', 'Ice cross downhill', 'Pickleball']},
    {'level': 6, 'name': 'Kitesurfing', 'options': ['Softball', 'Unicycle hockey', 'Shot put', 'Kung fu', 'Steeplechase', 'Kite buggy']},
    {'level': 6, 'name': 'Kung fu', 'options': ['Canoeing', 'Hammer throw', 'Figure skating', 'Roundnet', 'Kite buggy', 'Ice cross downhill']},
    {'level': 6, 'name': 'Windsurfing', 'options': ['Shuffleboard', 'Beach tennis', 'Discus throw', 'Abseiling', 'Steeplechase', 'Curling']},
    {'level': 6, 'name': 'Racquetball', 'options': ['Shuffleboard', 'Woodball', 'Lacrosse', 'Figure skating', 'Wallyball', 'Pickleball']},
    {'level': 6, 'name': 'Abseiling', 'options': ['Underwater rugby', 'Croquet', 'Kitesurfing', 'Kung fu', 'Hurling', 'Ringette']},
    {'level': 6, 'name': 'Underwater hockey', 'options': ['Scootering', 'Cornhole', 'Kitesurfing', 'Kung fu', 'Curling', 'Pickleball']},
    {'level': 6, 'name': 'Roundnet', 'options': ['Bicycle polo', 'Unicycle hockey', 'Shot put', 'Abseiling', 'Headis', 'Broomball']},
    {'level': 7, 'name': 'Kite buggy', 'options': ['Lacrosse', 'Figure skating', 'Broomball', 'Headis', 'Shinty', 'Bandy']},
    {'level': 7, 'name': 'Steeplechase', 'options': ['Shot put', 'Underwater hockey', 'Ice cross downhill', 'Kite buggy', 'Shinty', 'Cestoball']},
    {'level': 7, 'name': 'Ringette', 'options': ['Underwater hockey', 'Racquetball', 'Kite buggy', 'Ice cross downhill', 'Frontenis', 'Kin-Ball']},
    {'level': 7, 'name': 'Curling', 'options': ['Kitesurfing', 'Racquetball', 'Headis', 'Wallyball', 'Crossminton', 'Cestoball']},
    {'level': 7, 'name': 'SlamBall', 'options': ['Lacrosse', 'Discus throw', 'Kite buggy', 'Pickleball', 'Cestoball', 'Bossaball']},
    {'level': 7, 'name': 'Hurling', 'options': ['Roundnet', 'Lacrosse', 'Pickleball', 'Broomball', 'Crossminton', 'Kin-Ball']},
    {'level': 7, 'name': 'Pickleball', 'options': ['Kung fu', 'Discus throw', 'Headis', 'Wallyball', 'Bandy', 'Crossminton']},
    {'level': 7, 'name': 'Wallyball', 'options': ['Roundnet', 'Kung fu', 'Headis', 'Curling', 'Bandy', 'Goalball']},
    {'level': 7, 'name': 'Headis', 'options': ['Lacrosse', 'Underwater hockey', 'Ringette', 'Steeplechase', 'Kin-Ball', 'Frontenis']},
    {'level': 7, 'name': 'Ice cross downhill', 'options': ['Roundnet', 'Windsurfing', 'Headis', 'Pickleball', 'Goalball', 'Stoolball']},
    {'level': 7, 'name': 'Broomball', 'options': ['Underwater hockey', 'Kitesurfing', 'SlamBall', 'Ringette', 'Luge', 'Frontenis']},
    {'level': 8, 'name': 'Stoolball', 'options': ['Hurling', 'SlamBall', 'Bandy', 'Shinty', 'Downball', 'Ringball']},
    {'level': 8, 'name': 'Frontenis', 'options': ['Kite buggy', 'Pickleball', 'Shinty', 'Goalball', 'Novuss', 'Skibobbing']},
    {'level': 8, 'name': 'Cestoball', 'options': ['Ringette', 'Kite buggy', 'Luge', 'Bossaball', 'Torball', 'Bandy']},
    {'level': 8, 'name': 'Shinty', 'options': ['Wallyball', 'Kite buggy', 'Bossaball', 'Bandy', 'Crokicurl', 'Torball']},
    {'level': 8, 'name': 'Bandy', 'options': ['Curling', 'Pickleball', 'Crossminton', 'Kin-Ball', 'Korfball', 'Downball']},
    {'level': 8, 'name': 'Luge', 'options': ['Curling', 'Ice cross downhill', 'Shinty', 'Bandy', 'Crokicurl', 'Novuss']},
    {'level': 8, 'name': 'Goalball', 'options': ['Pickleball', 'Kite buggy', 'Frontenis', 'Kin-Ball', 'Korfball', 'Elle']},
    {'level': 8, 'name': 'Bossaball', 'options': ['Ringette', 'Headis', 'Cestoball', 'Stoolball', 'Skibobbing', 'Matkot']},
    {'level': 8, 'name': 'Crossminton', 'options': ['Ice cross downhill', 'SlamBall', 'Cestoball', 'Goalball', 'Ringball', 'Korfball']},
    {'level': 8, 'name': 'Kin-Ball', 'options': ['Headis', 'Steeplechase', 'Goalball', 'Bandy', 'Ringball', 'Downball']},
    {'level': 9, 'name': 'Elle', 'options': ['Bandy', 'Frontenis', 'Matkot', 'Korfball', 'Skijouring', 'Biribol']},
    {'level': 9, 'name': 'Ringball', 'options': ['Shinty', 'Luge', 'Korfball', 'Novuss', 'Basque pelota', 'Kaatsen']},
    {'level': 9, 'name': 'Torball', 'options': ['Goalball', 'Stoolball', 'Crokicurl', 'Korfball', 'Jianzi', 'Kaatsen']},
    {'level': 9, 'name': 'Fistball', 'options': ['Bandy', 'Crossminton', 'Novuss', 'Matkot', 'Basque pelota', 'Jai alai']},
    {'level': 9, 'name': 'Downball', 'options': ['Bossaball', 'Crossminton', 'Matkot', 'Fistball', 'Jianzi', 'Bobsleigh']},
    {'level': 9, 'name': 'Novuss', 'options': ['Frontenis', 'Crossminton', 'Torball', 'Matkot', 'Fives', 'Jianzi']},
    {'level': 9, 'name': 'Skibobbing', 'options': ['Luge', 'Stoolball', 'Novuss', 'Matkot', 'Skijouring', 'Jianzi']},
    {'level': 9, 'name': 'Crokicurl', 'options': ['Crossminton', 'Luge', 'Torball', 'Fistball', 'Biribol', 'Basque pelota']},
    {'level': 9, 'name': 'Bandy', 'options': ['Cestoball', 'Luge', 'Torball', 'Downball', 'Jianzi', 'Fives']},
    {'level': 9, 'name': 'Matkot', 'options': ['Kin-Ball', 'Cestoball', 'Torball', 'Novuss', 'Skijouring', 'Biribol']},
    {'level': 9, 'name': 'Korfball', 'options': ['Bossaball', 'Stoolball', 'Fistball', 'Torball', 'Bobsleigh', 'Pesäpallo']},
    {'level': 10, 'name': 'Bobsleigh', 'options': ['Frontenis', 'Kin-Ball', 'Ringball', 'Bandy', 'Kaatsen', 'Jai alai']},
    {'level': 10, 'name': 'Basque pelota', 'options': ['Crossminton', 'Luge', 'Skibobbing', 'Downball', 'Skijouring', 'Bete-ombro']},
    {'level': 10, 'name': 'Kaatsen', 'options': ['Shinty', 'Stoolball', 'Crokicurl', 'Ringball', 'Pesäpallo', 'Jai alai']},
    {'level': 10, 'name': 'Pesäpallo', 'options': ['Frontenis', 'Shinty', 'Bandy', 'Ringball', 'Fives', 'Biribol']},
    {'level': 10, 'name': 'Whirlyball', 'options': ['Bandy', 'Shinty', 'Korfball', 'Skibobbing', 'Sepak takraw', 'Jianzi']},
    {'level': 10, 'name': 'Jianzi', 'options': ['Bossaball', 'Bandy', 'Korfball', 'Crokicurl', 'Basque pelota', 'Bobsleigh']},
    {'level': 10, 'name': 'Fives', 'options': ['Luge', 'Bandy', 'Bandy', 'Fistball', 'Bobsleigh', 'Basque pelota']},
    {'level': 10, 'name': 'Sepak takraw', 'options': ['Kin-Ball', 'Shinty', 'Bandy', 'Matkot', 'Fives', 'Jianzi']},
    {'level': 10, 'name': 'Jai alai', 'options': ['Luge', 'Goalball', 'Novuss', 'Bandy', 'Kaatsen', 'Biribol']},
    {'level': 10, 'name': 'Skijouring', 'options': ['Bandy', 'Bossaball', 'Elle', 'Bandy', 'Kaatsen', 'Fives']},
    {'level': 10, 'name': 'Bete-ombro', 'options': ['Bandy', 'Cestoball', 'Crokicurl', 'Fistball', 'Sepak takraw', 'Jianzi']},
    {'level': 10, 'name': 'Biribol', 'options': ['Bandy', 'Shinty', 'Skibobbing', 'Elle', 'Bete-ombro', 'Sepak takraw']},
]

quiz = []

for sport in sports:
    curr = {}
    curr['options'] =  fetcher.fetch('sport', sport)
