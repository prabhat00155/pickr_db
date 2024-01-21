import json

import fetcher


monuments = [
    {'level': 1, 'name': 'Taj Mahal', 'options': ['Colosseum', 'Tower Bridge', 'Liberty Bell', 'Golden Gate', 'Sydney Harbour Bridge', 'Statue Of Unity']},
    {'level': 1, 'name': 'Pyramid', 'options': ['Charminar', 'Great Wall of China', 'Agra Fort', 'Lake Palace', 'Sydney Harbour Bridge', 'Meenakshi Temple']},
    {'level': 1, 'name': 'Qutub Minar', 'options': ['Great Wall of China', 'Taj Mahal', 'British Museum', 'Trafalgar Square', 'Capitol Hill', 'Khajuraho Temple']},
    {'level': 1, 'name': 'Great Wall of China', 'options': ['Stonehenge', 'Taj Mahal', 'British Museum', 'Sydney Opera House', 'Meenakshi Temple', 'Empire State Building']},
    {'level': 1, 'name': 'Eiffel Tower', 'options': ['Charminar', 'Burj Khalifa', 'One World Trade Centre', 'Lake Palace', 'Capitol Hill', 'Mahabodhi Temple']},
    {'level': 1, 'name': 'Colosseum', 'options': ['Charminar', 'Statue of Liberty', 'Trafalgar Square', 'Agra Fort', 'Meenakshi Temple', 'Sydney Harbour Bridge']},
    {'level': 1, 'name': 'Charminar', 'options': ['Burj Khalifa', 'Pyramid', 'Agra Fort', 'Atomium', 'Tower of London', 'Mahabodhi Temple']},
    {'level': 1, 'name': 'Statue of Liberty', 'options': ['Burj Khalifa', 'Tower Bridge', 'Sydney Opera House', 'Blue Domes of Oia', 'Sydney Harbour Bridge', 'Nalanda University']},
    {'level': 1, 'name': 'Burj Khalifa', 'options': ['Qutub Minar', 'Charminar', 'Petronas Towers', 'Red Fort', 'Victoria Memorial', 'Griffith Observatory']},
    {'level': 1, 'name': 'Buckingham Palace', 'options': ['Colosseum', 'Pyramid', 'Blue Domes of Oia', 'Agra Fort', 'Western Wall', 'Mysore Palace']},
    {'level': 1, 'name': 'Tower Bridge', 'options': ['Qutub Minar', 'Great Wall of China', 'Lotus Temple', 'One World Trade Centre', 'Empire State Building', 'Griffith Observatory']},
    {'level': 1, 'name': 'White House', 'options': ['Taj Mahal', 'Pyramid', 'Trafalgar Square', 'Howrah Bridge', 'Statue Of Unity', 'Mysore Palace']},
    {'level': 1, 'name': 'Big Ben', 'options': ['Qutub Minar', 'Stonehenge', 'Liberty Bell', 'One World Trade Centre', 'Notre Dame', 'Khajuraho Temple']},
    {'level': 1, 'name': 'India Gate', 'options': ['Burj Khalifa', 'Charminar', 'Trafalgar Square', 'Red Fort', 'Victoria Memorial', 'Mysore Palace']},
    {'level': 1, 'name': 'Stonehenge', 'options': ['White House', 'Buckingham Palace', 'Red Fort', 'Agra Fort', 'Khajuraho Temple', 'Mahabodhi Temple']},
    {'level': 2, 'name': 'Leaning Tower of Pisa', 'options': ['Big Ben', 'Tower Bridge', 'Lotus Temple', 'British Museum', 'Nalanda University', 'Khajuraho Temple']},
    {'level': 2, 'name': 'Gateway Of India', 'options': ['Statue of Liberty', 'Tower Bridge', 'Blue Domes of Oia', 'Liberty Bell', 'Empire State Building', 'Tower of London']},
    {'level': 2, 'name': 'Petronas Towers', 'options': ['Buckingham Palace', 'Big Ben', 'Liberty Bell', 'Gateway Of India', 'Victoria Memorial', 'Capitol Hill']},
    {'level': 2, 'name': 'Red Fort', 'options': ['White House', 'Qutub Minar', 'Golden Temple', 'Atomium', 'Great Sphinx of Giza', 'Khajuraho Temple']},
    {'level': 2, 'name': 'Lotus Temple', 'options': ['Statue of Liberty', 'Charminar', 'Trafalgar Square', 'One World Trade Centre', 'Empire State Building', 'Notre Dame']},
    {'level': 2, 'name': 'Golden Temple', 'options': ['Tower Bridge', 'Big Ben', 'Atomium', 'One World Trade Centre', 'Mysore Palace', 'Capitol Hill']},
    {'level': 2, 'name': 'Hawa Mahal', 'options': ['Stonehenge', 'Tower Bridge', 'Agra Fort', 'Petronas Towers', 'Meenakshi Temple', 'Tower of London']},
    {'level': 2, 'name': 'Howrah Bridge', 'options': ['Stonehenge', 'Colosseum', 'Lotus Temple', 'Agra Fort', 'Great Sphinx of Giza', 'Khajuraho Temple']},
    {'level': 2, 'name': 'Blue Domes of Oia', 'options': ['Qutub Minar', 'Tower Bridge', 'Atomium', 'Gateway Of India', 'Notre Dame', 'Mysore Palace']},
    {'level': 2, 'name': 'Liberty Bell', 'options': ['White House', 'Eiffel Tower', 'Hawa Mahal', 'Golden Gate', 'Notre Dame', 'Mahabodhi Temple']},
    {'level': 2, 'name': 'One World Trade Centre', 'options': ['India Gate', 'Buckingham Palace', 'Lake Palace', 'Golden Temple', 'Statue Of Unity', 'Victoria Memorial']},
    {'level': 2, 'name': 'Atomium', 'options': ['Colosseum', 'Great Wall of China', 'Gateway Of India', 'Sydney Opera House', 'Great Sphinx of Giza', 'Notre Dame']},
    {'level': 2, 'name': 'British Museum', 'options': ['Big Ben', 'Eiffel Tower', 'Agra Fort', 'Liberty Bell', 'Notre Dame', 'Western Wall']},
    {'level': 2, 'name': 'Lake Palace', 'options': ['Stonehenge', 'White House', 'Atomium', 'Sydney Opera House', 'Griffith Observatory', 'Notre Dame']},
    {'level': 2, 'name': 'Trafalgar Square', 'options': ['Pyramid', 'Charminar', 'One World Trade Centre', 'Golden Gate', 'Sydney Harbour Bridge', 'Victoria Memorial']},
    {'level': 2, 'name': 'Agra Fort', 'options': ['White House', 'Buckingham Palace', 'Liberty Bell', 'One World Trade Centre', 'Griffith Observatory', 'Empire State Building']},
    {'level': 2, 'name': 'Sydney Opera House', 'options': ['Pyramid', 'Stonehenge', 'Agra Fort', 'Lotus Temple', 'Mysore Palace', 'Empire State Building']},
    {'level': 2, 'name': 'Golden Gate', 'options': ['Statue of Liberty', 'Colosseum', 'Gateway Of India', 'Blue Domes of Oia', 'Great Sphinx of Giza', 'Notre Dame']},
    {'level': 3, 'name': 'Empire State Building', 'options': ['Agra Fort', 'Lotus Temple', 'Sydney Harbour Bridge', 'Notre Dame', "St. Peter's Basilica", 'Basilica of Bom Jesus']},
    {'level': 3, 'name': 'Statue Of Unity', 'options': ['Hawa Mahal', 'Red Fort', 'Griffith Observatory', 'Western Wall', 'Gol Gumbaz', 'Louvre Museum']},
    {'level': 3, 'name': 'Great Sphinx of Giza', 'options': ['Gateway Of India', 'Lotus Temple', 'Griffith Observatory', 'Mysore Palace', 'Palace of Versailles', 'Acropolis']},
    {'level': 3, 'name': 'Victoria Memorial', 'options': ['Agra Fort', 'Leaning Tower of Pisa', 'Empire State Building', 'Khajuraho Temple', 'The Shard', "St. Peter's Basilica"]},
    {'level': 3, 'name': 'Western Wall', 'options': ['Lotus Temple', 'Atomium', 'Mysore Palace', 'Khajuraho Temple', 'Palace of Versailles', 'Gol Gumbaz']},
    {'level': 3, 'name': 'Mysore Palace', 'options': ['Liberty Bell', 'Golden Temple', 'Victoria Memorial', 'Statue Of Unity', 'Louvre Museum', "St. Peter's Basilica"]},
    {'level': 3, 'name': 'Tower of London', 'options': ['Red Fort', 'Lotus Temple', 'Nalanda University', 'Mysore Palace', 'Gol Gumbaz', 'St Paul’s Cathedral']},
    {'level': 3, 'name': 'Sydney Harbour Bridge', 'options': ['Atomium', 'Lotus Temple', 'Mahabodhi Temple', 'Mysore Palace', 'Space Needle', "St. Peter's Basilica"]},
    {'level': 3, 'name': 'Notre Dame', 'options': ['Lake Palace', 'Lotus Temple', 'Mahabodhi Temple', 'Griffith Observatory', 'Tian Tan Buddha', 'Hoover Dam']},
    {'level': 3, 'name': 'Griffith Observatory', 'options': ['Red Fort', 'Golden Temple', 'Khajuraho Temple', 'Victoria Memorial', 'Christ the Redeemer', 'Space Needle']},
    {'level': 3, 'name': 'Meenakshi Temple', 'options': ['Golden Temple', 'Lotus Temple', 'Western Wall', 'Capitol Hill', 'Gol Gumbaz', 'Palace of Versailles']},
    {'level': 3, 'name': 'Nalanda University', 'options': ['Red Fort', 'Trafalgar Square', 'Great Sphinx of Giza', 'Western Wall', 'Christ the Redeemer', 'Space Needle']},
    {'level': 3, 'name': 'Khajuraho Temple', 'options': ['Red Fort', 'Golden Temple', 'Capitol Hill', 'Empire State Building', "St. Peter's Basilica", 'St Paul’s Cathedral']},
    {'level': 3, 'name': 'Capitol Hill', 'options': ['Lotus Temple', 'British Museum', 'Griffith Observatory', 'Mahabodhi Temple', 'Louvre Museum', 'Palace of Versailles']},
    {'level': 3, 'name': 'Mahabodhi Temple', 'options': ['Liberty Bell', 'Hawa Mahal', 'Great Sphinx of Giza', 'Griffith Observatory', 'Acropolis', 'The Shard']},
    {'level': 4, 'name': 'Gol Gumbaz', 'options': ['Khajuraho Temple', 'Mysore Palace', 'Basilica of Bom Jesus', 'Louvre Museum', 'Sistine Chapel', 'Lincoln Memorial']},
    {'level': 4, 'name': 'Christ the Redeemer', 'options': ['Western Wall', 'Empire State Building', 'Hoover Dam', 'St Paul’s Cathedral', "Saint Basil's Cathedral", 'Sistine Chapel']},
    {'level': 4, 'name': 'Space Needle', 'options': ['Empire State Building', 'Great Sphinx of Giza', 'Palace of Versailles', 'St Paul’s Cathedral', 'Mount Rushmore', 'Hagia Sophia']},
    {'level': 4, 'name': 'Louvre Museum', 'options': ['Nalanda University', 'Victoria Memorial', 'Basilica of Bom Jesus', 'Tian Tan Buddha', 'Lincoln Memorial', 'Golghar']},
    {'level': 4, 'name': 'St Paul’s Cathedral', 'options': ['Notre Dame', 'Great Sphinx of Giza', 'Acropolis', 'Hoover Dam', 'CN Tower', 'Mount Rushmore']},
    {'level': 4, 'name': "St. Peter's Basilica", 'options': ['Meenakshi Temple', 'Mysore Palace', 'Space Needle', 'The Shard', 'Pyramids Of Meroe', 'Hagia Sophia']},
    {'level': 4, 'name': 'Palace of Versailles', 'options': ['Mahabodhi Temple', 'Empire State Building', 'Basilica of Bom Jesus', 'Hoover Dam', 'CN Tower', 'Konark Sun Temple']},
    {'level': 4, 'name': 'Hoover Dam', 'options': ['Western Wall', 'Khajuraho Temple', 'St Paul’s Cathedral', 'Christ the Redeemer', 'Golghar', 'Angkor Wat']},
    {'level': 4, 'name': 'The Shard', 'options': ['Nalanda University', 'Capitol Hill', 'Tian Tan Buddha', 'Space Needle', 'Angkor Wat', 'Pyramids Of Meroe']},
    {'level': 4, 'name': 'Tian Tan Buddha', 'options': ['Statue Of Unity', 'Capitol Hill', 'Gol Gumbaz', 'Louvre Museum', 'Bibi ka maqbara', 'Angkor Wat']},
    {'level': 4, 'name': 'Acropolis', 'options': ['Khajuraho Temple', 'Griffith Observatory', 'Louvre Museum', 'Palace of Versailles', 'Golghar', 'Brandenburg Gate']},
    {'level': 4, 'name': 'Basilica of Bom Jesus', 'options': ['Khajuraho Temple', 'Mysore Palace', 'Louvre Museum', "St. Peter's Basilica", 'Arc de Triomphe', 'Hagia Sophia']},
    {'level': 5, 'name': 'Hagia Sophia', 'options': ['Louvre Museum', 'The Shard', 'Mont Saint-Michel', 'Machu Picchu', 'Edinburgh Castle', 'Trevi Fountain']},
    {'level': 5, 'name': 'Angkor Wat', 'options': ['The Shard', 'Palace of Versailles', 'Hagia Sophia', 'CN Tower', 'Itsukushima Shrine', 'Edinburgh Castle']},
    {'level': 5, 'name': 'Bibi ka maqbara', 'options': ['Basilica of Bom Jesus', 'Tian Tan Buddha', 'CN Tower', 'Machu Picchu', 'Chichen Itza', 'Parthenon']},
    {'level': 5, 'name': 'Sistine Chapel', 'options': ['Hoover Dam', 'Basilica of Bom Jesus', 'Mont Saint-Michel', 'Angkor Wat', 'Chichen Itza', 'Parthenon']},
    {'level': 5, 'name': 'Machu Picchu', 'options': ['Space Needle', 'Basilica of Bom Jesus', 'Mont Saint-Michel', 'Sistine Chapel', 'Washington Monument', 'Vivekananda Rock statue']},
    {'level': 5, 'name': 'Mount Rushmore', 'options': ['Basilica of Bom Jesus', 'Gol Gumbaz', 'Mont Saint-Michel', 'CN Tower', 'Royal Palace of Madrid', 'Itsukushima Shrine']},
    {'level': 5, 'name': 'Mont Saint-Michel', 'options': ['Space Needle', 'Palace of Versailles', 'Machu Picchu', 'Bibi ka maqbara', 'Vivekananda Rock statue', 'Royal Palace of Madrid']},
    {'level': 5, 'name': 'Arc de Triomphe', 'options': ['Gol Gumbaz', 'Palace of Versailles', "Saint Basil's Cathedral", 'Pyramids Of Meroe', 'Itsukushima Shrine', 'Windsor Castle']},
    {'level': 5, 'name': 'Brandenburg Gate', 'options': ['Christ the Redeemer', 'St Paul’s Cathedral', 'Machu Picchu', 'Lincoln Memorial', 'Parthenon', 'Washington Monument']},
    {'level': 5, 'name': 'Lincoln Memorial', 'options': ['Acropolis', 'Basilica of Bom Jesus', 'Hagia Sophia', 'Mount Rushmore', 'Itsukushima Shrine', 'Edinburgh Castle']},
    {'level': 5, 'name': 'CN Tower', 'options': ['Acropolis', 'Hoover Dam', 'Golghar', 'Konark Sun Temple', 'Royal Palace of Madrid', 'Windsor Castle']},
    {'level': 5, 'name': 'Konark Sun Temple', 'options': ['Gol Gumbaz', 'Tian Tan Buddha', 'Arc de Triomphe', 'Sistine Chapel', 'Itsukushima Shrine', 'Edinburgh Castle']},
    {'level': 5, 'name': 'Pyramids Of Meroe', 'options': ['Louvre Museum', 'Acropolis', 'Hagia Sophia', 'Brandenburg Gate', 'Parthenon', 'Washington Monument']},
    {'level': 5, 'name': 'Golghar', 'options': ['Christ the Redeemer', 'Louvre Museum', 'Machu Picchu', 'Konark Sun Temple', 'Chichen Itza', 'Windsor Castle']},
    {'level': 6, 'name': 'Vivekananda Rock statue', 'options': ['CN Tower', 'Mont Saint-Michel', 'Windsor Castle', 'Royal Palace of Madrid', 'Berlin TV Tower', 'Cologne Cathedral']},
    {'level': 6, 'name': 'Parthenon', 'options': ['Mount Rushmore', 'CN Tower', 'Taipei 101', 'Edinburgh Castle', 'Seoul Tower', 'Borobudur Temple']},
    {'level': 6, 'name': 'Royal Palace of Madrid', 'options': ["Saint Basil's Cathedral", 'Hagia Sophia', 'Windsor Castle', 'Parthenon', 'Chrysler Building', 'Temple Mount']},
    {'level': 6, 'name': 'Washington Monument', 'options': ['Brandenburg Gate', 'Bibi ka maqbara', 'Taipei 101', 'Chichen Itza', 'Seoul Tower', 'Cologne Cathedral']},
    {'level': 6, 'name': 'Trevi Fountain', 'options': ['Hagia Sophia', 'Angkor Wat', 'Chichen Itza', 'Parthenon', 'Berlin TV Tower', 'Blue Mosque']},
    {'level': 6, 'name': 'Windsor Castle', 'options': ['Mount Rushmore', 'Pyramids Of Meroe', 'Taipei 101', 'Washington Monument', 'Berlin TV Tower', 'Borobudur Temple']},
    {'level': 6, 'name': 'Taipei 101', 'options': ['Angkor Wat', 'Pyramids Of Meroe', 'Royal Palace of Madrid', 'Windsor Castle', 'Berlin TV Tower', 'Westminster Abbey']},
    {'level': 6, 'name': 'Itsukushima Shrine', 'options': ['Lincoln Memorial', 'Hagia Sophia', 'Vivekananda Rock statue', 'Chichen Itza', 'Rialto Bridge', 'Blue Mosque']},
    {'level': 6, 'name': 'Edinburgh Castle', 'options': ['Lincoln Memorial', 'Mont Saint-Michel', 'Washington Monument', 'Windsor Castle', 'Berlin TV Tower', 'Cologne Cathedral']},
    {'level': 5, 'name': "Saint Basil's Cathedral", 'options': ["St. Peter's Basilica", 'Gol Gumbaz', 'Machu Picchu', 'Brandenburg Gate', 'Edinburgh Castle', 'Vivekananda Rock statue']},
    {'level': 6, 'name': 'Chichen Itza', 'options': ['Machu Picchu', 'Golghar', 'Windsor Castle', 'Taipei 101', 'Cologne Cathedral', 'Borobudur Temple']},
    {'level': 7, 'name': 'Porcelain Tower of Nanjing', 'options': ['Taipei 101', 'Washington Monument', 'Sacré-Cœur Basilica', 'Seoul Tower', 'Bell Rock Lighthouse', 'Shwedagon Pagoda']},
    {'level': 7, 'name': 'Blue Mosque', 'options': ['Itsukushima Shrine', 'Royal Palace of Madrid', 'Sacré-Cœur Basilica', 'Porcelain Tower of Nanjing', 'La Sagrada Familia', 'Gateway Arch']},
    {'level': 7, 'name': 'Cologne Cathedral', 'options': ['Royal Palace of Madrid', 'Washington Monument', 'Berlin TV Tower', 'Chrysler Building', 'Bell Rock Lighthouse', 'Shwedagon Pagoda']},
    {'level': 7, 'name': 'Westminster Abbey', 'options': ['Chichen Itza', 'Vivekananda Rock statue', 'Seoul Tower', 'Cologne Cathedral', 'Sagrada Família', 'Moai']},
    {'level': 7, 'name': 'Berlin TV Tower', 'options': ['Windsor Castle', 'Itsukushima Shrine', 'Temple Mount', 'Borobudur Temple', 'La Sagrada Familia', 'Sagrada Família']},
    {'level': 7, 'name': 'Seoul Tower', 'options': ['Itsukushima Shrine', 'Windsor Castle', 'Rialto Bridge', 'Westminster Abbey', 'La Sagrada Familia', 'Moai']},
    {'level': 7, 'name': 'Rialto Bridge', 'options': ['Royal Palace of Madrid', 'Taipei 101', 'Berlin TV Tower', 'Westminster Abbey', 'Grand Palace', 'Petra']},
    {'level': 7, 'name': 'Chrysler Building', 'options': ['Parthenon', 'Edinburgh Castle', 'Seoul Tower', 'Sacré-Cœur Basilica', 'Saint Mark’s Basilica', 'Grand Palace']},
    {'level': 7, 'name': 'Borobudur Temple', 'options': ['Washington Monument', 'Windsor Castle', 'Porcelain Tower of Nanjing', 'Temple Mount', 'Petra', 'Grand Palace']},
    {'level': 7, 'name': 'Temple Mount', 'options': ['Itsukushima Shrine', 'Windsor Castle', 'Blue Mosque', 'Cologne Cathedral', 'Shwedagon Pagoda', 'Bell Rock Lighthouse']},
    {'level': 7, 'name': 'Sacré-Cœur Basilica', 'options': ['Chichen Itza', 'Vivekananda Rock statue', 'Blue Mosque', 'Temple Mount', 'Saint Mark’s Basilica', 'Reichstag']},
    {'level': 8, 'name': 'Gateway Arch', 'options': ['Rialto Bridge', 'Chrysler Building', 'Saint Mark’s Basilica', 'Shwedagon Pagoda', 'Tulum Ruins', 'Oriental Pearl Tower']},
    {'level': 8, 'name': 'Moai', 'options': ['Temple Mount', 'Borobudur Temple', 'Grand Palace', 'La Sagrada Familia', 'Luxor Temple', 'Auschwitz-Birkenau State Museum']},
    {'level': 8, 'name': 'La Sagrada Familia', 'options': ['Rialto Bridge', 'Seoul Tower', 'Bell Rock Lighthouse', 'Sagrada Família', 'Kronborg Slot', 'Neuschwanstein Castle']},
    {'level': 8, 'name': 'Grand Palace', 'options': ['Berlin TV Tower', 'Sacré-Cœur Basilica', 'Sagrada Família', 'La Sagrada Familia', 'Neuschwanstein Castle', 'Alhambra']},
    {'level': 8, 'name': 'Saint Mark’s Basilica', 'options': ['Seoul Tower', 'Chrysler Building', 'Sagrada Família', 'Bell Rock Lighthouse', 'Auschwitz-Birkenau State Museum', 'Kronborg Slot']},
    {'level': 8, 'name': 'Shwedagon Pagoda', 'options': ['Berlin TV Tower', 'Westminster Abbey', 'Saint Mark’s Basilica', 'Reichstag', 'Tulum Ruins', 'Neuschwanstein Castle']},
    {'level': 8, 'name': 'Reichstag', 'options': ['Chrysler Building', 'Porcelain Tower of Nanjing', 'Grand Palace', 'Moai', 'Oriental Pearl Tower', 'Neuschwanstein Castle']},
    {'level': 8, 'name': 'Petra', 'options': ['Sacré-Cœur Basilica', 'Blue Mosque', 'Shwedagon Pagoda', 'Gateway Arch', 'Guggenheim Museum Bilbao', 'Tulum Ruins']},
    {'level': 8, 'name': 'Bell Rock Lighthouse', 'options': ['Cologne Cathedral', 'Temple Mount', 'Gateway Arch', 'Petra', 'Luxor Temple', 'Oriental Pearl Tower']},
    {'level': 8, 'name': 'Sagrada Família', 'options': ['Rialto Bridge', 'Berlin TV Tower', 'Saint Mark’s Basilica', 'Reichstag', 'Neuschwanstein Castle', 'Tulum Ruins']},
    {'level': 9, 'name': 'Luxor Temple', 'options': ['Reichstag', 'Moai', 'Oriental Pearl Tower', 'Neuschwanstein Castle', 'Neuschwanstein Castle', 'Chapultepec Castle']},
    {'level': 9, 'name': 'Potala Palace', 'options': ['Grand Palace', 'Shwedagon Pagoda', 'Neuschwanstein Castle', 'Auschwitz-Birkenau State Museum', 'Schönbrunn Palace', 'Peterhof Palace']},
    {'level': 9, 'name': 'Alhambra', 'options': ['Grand Palace', 'Sagrada Família', 'Oriental Pearl Tower', 'Guggenheim Museum Bilbao', 'Mosque–Cathedral of Córdoba', 'Peterhof Palace']},
    {'level': 9, 'name': 'Topkapı Palace', 'options': ['Reichstag', 'Sagrada Família', 'Kronborg Slot', 'Alhambra', 'Wawel Castle', 'Cite du Vin']},
    {'level': 9, 'name': 'Auschwitz-Birkenau State Museum', 'options': ['Gateway Arch', 'Moai', 'Luxor Temple', 'Neuschwanstein Castle', 'Schönbrunn Palace', 'Palace on the Isle']},
    {'level': 9, 'name': 'Neuschwanstein Castle', 'options': ['Shwedagon Pagoda', 'Moai', 'Auschwitz-Birkenau State Museum', 'Luxor Temple', 'Schönbrunn Palace', 'Alcázar of Seville']},
    {'level': 9, 'name': 'Guggenheim Museum Bilbao', 'options': ['Saint Mark’s Basilica', 'Bell Rock Lighthouse', 'Luxor Temple', 'Alhambra', 'Neuschwanstein Castle', 'Palace on the Isle']},
    {'level': 9, 'name': 'Kronborg Slot', 'options': ['Reichstag', 'Bell Rock Lighthouse', 'Neuschwanstein Castle', 'Luxor Temple', 'Wawel Castle', 'The Gherkin']},
    {'level': 9, 'name': 'Oriental Pearl Tower', 'options': ['La Sagrada Familia', 'Grand Palace', 'Auschwitz-Birkenau State Museum', 'Luxor Temple', 'Palace on the Isle', 'Alcázar of Seville']},
    {'level': 9, 'name': 'Tulum Ruins', 'options': ['Petra', 'Shwedagon Pagoda', 'Oriental Pearl Tower', 'Alhambra', 'Chapultepec Castle', 'Palace on the Isle']},
    {'level': 10, 'name': 'Palace on the Isle', 'options': ['Gateway Arch', 'Petra', 'Alhambra', 'Luxor Temple', 'Peterhof Palace', 'Itaipu Dam']},
    {'level': 10, 'name': 'Neuschwanstein Castle', 'options': ['Shwedagon Pagoda', 'La Sagrada Familia', 'Kronborg Slot', 'Potala Palace', 'Wawel Castle', 'Palace on the Isle']},
    {'level': 10, 'name': 'The Gherkin', 'options': ['Shwedagon Pagoda', 'Gateway Arch', 'Kronborg Slot', 'Alhambra', 'Neuschwanstein Castle', 'Palace on the Isle']},
    {'level': 10, 'name': 'Chapultepec Castle', 'options': ['Saint Mark’s Basilica', 'Sagrada Família', 'Luxor Temple', 'Alhambra', 'Alcázar of Seville', 'Wawel Castle']},
    {'level': 10, 'name': 'Mosque–Cathedral of Córdoba', 'options': ['Reichstag', 'Bell Rock Lighthouse', 'Oriental Pearl Tower', 'Alhambra', 'Wawel Castle', 'Neuschwanstein Castle']},
    {'level': 10, 'name': 'Schönbrunn Palace', 'options': ['Reichstag', 'Sagrada Família', 'Kronborg Slot', 'Auschwitz-Birkenau State Museum', 'Neuschwanstein Castle', 'Peterhof Palace']},
    {'level': 10, 'name': 'Alcázar of Seville', 'options': ['La Sagrada Familia', 'Petra', 'Guggenheim Museum Bilbao', 'Oriental Pearl Tower', 'Cite du Vin', 'Palace on the Isle']},
    {'level': 10, 'name': 'Wawel Castle', 'options': ['Shwedagon Pagoda', 'La Sagrada Familia', 'Alhambra', 'Tulum Ruins', 'Chapultepec Castle', 'Palace on the Isle']},
    {'level': 10, 'name': 'Wilanów Palace', 'options': ['La Sagrada Familia', 'Gateway Arch', 'Topkapı Palace', 'Potala Palace', 'The Gherkin', 'Mosque–Cathedral of Córdoba']},
    {'level': 10, 'name': 'Peterhof Palace', 'options': ['Grand Palace', 'La Sagrada Familia', 'Topkapı Palace', 'Luxor Temple', 'Itaipu Dam', 'Cite du Vin']},
    {'level': 10, 'name': 'Itaipu Dam', 'options': ['Bell Rock Lighthouse', 'Gateway Arch', 'Auschwitz-Birkenau State Museum', 'Neuschwanstein Castle', 'Mosque–Cathedral of Córdoba', 'Chapultepec Castle']},
    {'level': 10, 'name': 'Cite du Vin', 'options': ['La Sagrada Familia', 'Reichstag', 'Guggenheim Museum Bilbao', 'Alhambra', 'Itaipu Dam', 'Wawel Castle']}
]

quiz = []

for monument in monuments:
    monument['urls'] = fetcher.fetch('monument', monument['name'])
    quiz.append(monument)

with open("output/monuments.json", "w") as f:
    f.write(json.dumps(quiz))
