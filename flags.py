import fetcher


flags = [
    {'level': 1, 'name': 'India', 'options': ['USA', 'France', 'Ireland', 'Czech Republic', 'Niger', 'Ivory Coast']},
    {'level': 1, 'name': 'USA', 'options': ['Greece', 'Jamaica', 'Monaco', 'Australia', 'Cuba', 'Myanmar']},
    {'level': 1, 'name': 'UK', 'options': ['Pakistan', 'India', 'Serbia', 'Iceland', 'Malaysia', 'Jordan']},
    {'level': 1, 'name': 'Canada', 'options': ['Portugal', 'Croatia', 'Kuwait', 'New Zealand', 'Norway', 'Cuba']},
    {'level': 1, 'name': 'South Africa', 'options': ['Spain', 'Turkey', 'Belgium', 'Czech Republic', 'Cuba', 'Syria']},
    {'level': 1, 'name': 'South Korea', 'options': ['USA', 'UK', 'Netherlands', 'Romania', 'Ivory Coast', 'Bahrain']},
    {'level': 1, 'name': 'Japan', 'options': ['China', 'Russia', 'Serbia', 'Ireland', 'Malaysia', 'Saudi Arabia']},
    {'level': 1, 'name': 'Switzerland', 'options': ['South Africa', 'Canada', 'Poland', 'Serbia', 'Senegal', 'Ethiopia']},
    {'level': 1, 'name': 'Brazil', 'options': ['Germany', 'Russia', 'Denmark', 'Hungary', 'Cuba', 'Syria']},
    {'level': 1, 'name': 'Russia', 'options': ['Japan', 'Italy', 'Uruguay', 'Netherlands', 'Senegal', 'Bahrain']},
    {'level': 1, 'name': 'Spain', 'options': ['Argentina', 'Greece', 'Ukraine', 'Ghana', 'Cuba', 'Nigeria']},
    {'level': 1, 'name': 'Germany', 'options': ['Israel', 'Russia', 'Serbia', 'Ukraine', 'Ivory Coast', 'Cuba']},
    {'level': 1, 'name': 'Israel', 'options': ['UK', 'Jamaica', 'Kuwait', 'Bangladesh', 'Qatar', 'Norway']},
    {'level': 1, 'name': 'Turkey', 'options': ['Argentina', 'Pakistan', 'Ghana', 'Poland', 'Syria', 'Egypt']},
    {'level': 1, 'name': 'Argentina', 'options': ['USA', 'India', 'Colombia', 'Romania', 'Egypt', 'Myanmar']},
    {'level': 1, 'name': 'Italy', 'options': ['China', 'Japan', 'Morocco', 'Poland', 'Niger', 'Myanmar']},
    {'level': 1, 'name': 'Jamaica', 'options': ['Argentina', 'Switzerland', 'Mexico', 'Iran', 'Egypt', 'North Korea']},
    {'level': 1, 'name': 'France', 'options': ['Switzerland', 'Argentina', 'Monaco', 'Belgium', 'Maldives', 'Nepal']},
    {'level': 1, 'name': 'Finland', 'options': ['Switzerland', 'Russia', 'Mexico', 'Belgium', 'Syria', 'Saudi Arabia']},
    {'level': 1, 'name': 'Pakistan', 'options': ['France', 'Argentina', 'Monaco', 'Zimbabwe', 'Senegal', 'Bahrain']},
    {'level': 1, 'name': 'Greece', 'options': ['Italy', 'India', 'Morocco', 'Indonesia', 'Senegal', 'Ivory Coast']},
    {'level': 1, 'name': 'China', 'options': ['South Korea', 'Japan', 'Romania', 'Indonesia', 'Namibia', 'Senegal']},
    {'level': 1, 'name': 'Portugal', 'options': ['Brazil', 'USA', 'Iran', 'Ghana', 'Ivory Coast', 'Nigeria']},
    {'level': 1, 'name': 'Croatia', 'options': ['Argentina', 'Russia', 'Ukraine', 'Serbia', 'Saudi Arabia', 'Malaysia']},
    {'level': 2, 'name': 'Ghana', 'options': ['Canada', 'France', 'Morocco', 'Fiji', 'Jordan', 'Ethiopia']},
    {'level': 2, 'name': 'New Zealand', 'options': ['Greece', 'Turkey', 'Iraq', 'Mexico', 'Norway', 'Nepal']},
    {'level': 2, 'name': 'Hungary', 'options': ['Canada', 'USA', 'Serbia', 'Iraq', 'Namibia', 'Syria']},
    {'level': 2, 'name': 'Sri Lanka', 'options': ['Spain', 'Brazil', 'Romania', 'Hungary', 'Norway', 'Maldives']},
    {'level': 2, 'name': 'Serbia', 'options': ['Spain', 'Brazil', 'Hungary', 'Uruguay', 'Austria', 'Norway']},
    {'level': 2, 'name': 'Iceland', 'options': ['Brazil', 'Japan', 'Denmark', 'Serbia', 'Syria', 'Cuba']},
    {'level': 2, 'name': 'Colombia', 'options': ['Argentina', 'Germany', 'Iraq', 'New Zealand', 'Norway', 'Saudi Arabia']},
    {'level': 2, 'name': 'Indonesia', 'options': ['Spain', 'Finland', 'Iraq', 'Kuwait', 'Norway', 'Malaysia']},
    {'level': 2, 'name': 'Iran', 'options': ['Argentina', 'Jamaica', 'New Zealand', 'Morocco', 'Namibia', 'Senegal']},
    {'level': 2, 'name': 'Netherlands', 'options': ['Croatia', 'Italy', 'Poland', 'Colombia', 'Jordan', 'Nigeria']},
    {'level': 2, 'name': 'Zimbabwe', 'options': ['Russia', 'Spain', 'Indonesia', 'Ireland', 'Nigeria', 'Saudi Arabia']},
    {'level': 2, 'name': 'Denmark', 'options': ['Brazil', 'India', 'Morocco', 'Ukraine', 'Malaysia', 'Ethiopia']},
    {'level': 2, 'name': 'Australia', 'options': ['Portugal', 'Greece', 'Iran', 'Poland', 'Myanmar', 'Syria']},
    {'level': 2, 'name': 'Iraq', 'options': ['Greece', 'USA', 'Bangladesh', 'Netherlands', 'Senegal', 'Norway']},
    {'level': 2, 'name': 'Ireland', 'options': ['Spain', 'China', 'Bangladesh', 'Netherlands', 'Saudi Arabia', 'Cuba']},
    {'level': 2, 'name': 'Kuwait', 'options': ['Greece', 'Argentina', 'Monaco', 'Uruguay', 'Norway', 'Qatar']},
    {'level': 2, 'name': 'Belgium', 'options': ['China', 'Canada', 'Denmark', 'Bangladesh', 'Norway', 'Qatar']},
    {'level': 2, 'name': 'Mexico', 'options': ['Finland', 'South Korea', 'Ghana', 'Fiji', 'Niger', 'Saudi Arabia']},
    {'level': 2, 'name': 'Romania', 'options': ['South Africa', 'Argentina', 'Indonesia', 'Denmark', 'Cuba', 'North Korea']},
    {'level': 2, 'name': 'Monaco', 'options': ['Switzerland', 'UK', 'Belgium', 'Morocco', 'Nigeria', 'Cuba']},
    {'level': 2, 'name': 'Czech Republic', 'options': ['South Korea', 'Jamaica', 'Romania', 'Bangladesh', 'Namibia', 'Norway']},
    {'level': 2, 'name': 'Ukraine', 'options': ['USA', 'UK', 'Hungary', 'Netherlands', 'North Korea', 'Cuba']},
    {'level': 2, 'name': 'Morocco', 'options': ['Brazil', 'France', 'Uruguay', 'Serbia', 'Jordan', 'Norway']},
    {'level': 2, 'name': 'Bangladesh', 'options': ['Canada', 'India', 'Belgium', 'Ireland', 'Ivory Coast', 'Jordan']},
    {'level': 2, 'name': 'Poland', 'options': ['South Africa', 'South Korea', 'Sri Lanka', 'Iraq', 'Qatar', 'Myanmar']},
    {'level': 2, 'name': 'Fiji', 'options': ['Switzerland', 'Italy', 'Denmark', 'Iraq', 'Syria', 'North Korea']},
    {'level': 2, 'name': 'Uruguay', 'options': ['Jamaica', 'China', 'Zimbabwe', 'Serbia', 'Malaysia', 'Niger']},
    {'level': 2, 'name': 'Sweden', 'options': ['Russia', 'Jamaica', 'Denmark', 'Iceland', 'Austria', 'Nigeria']},
    {'level': 3, 'name': 'Cuba', 'options': ['Morocco', 'Czech Republic', 'Jordan', 'Ivory Coast', 'United Arab Emirates', 'Luxembourg']},
    {'level': 3, 'name': 'Qatar', 'options': ['Iran', 'Uruguay', 'Norway', 'Ethiopia', 'Oman', 'Cameroon']},
    {'level': 3, 'name': 'Jordan', 'options': ['Romania', 'Serbia', 'Cuba', 'Maldives', 'Cameroon', 'United Arab Emirates']},
    {'level': 3, 'name': 'Niger', 'options': ['Iran', 'Morocco', 'Malaysia', 'Qatar', 'Uzbekistan', 'Azerbaijan']},
    {'level': 3, 'name': 'Maldives', 'options': ['Bangladesh', 'Hungary', 'Malaysia', 'Nigeria', 'Oman', 'Philippines']},
    {'level': 3, 'name': 'Austria', 'options': ['Sweden', 'Morocco', 'Jordan', 'Niger', 'Mali', 'Bulgaria']},
    {'level': 3, 'name': 'Syria', 'options': ['Uruguay', 'Ukraine', 'Saudi Arabia', 'Niger', 'Trinidad and Tobago', 'Uzbekistan']},
    {'level': 3, 'name': 'Nigeria', 'options': ['Morocco', 'New Zealand', 'Cuba', 'Norway', 'Luxembourg', 'Oman']},
    {'level': 3, 'name': 'Malaysia', 'options': ['Zimbabwe', 'New Zealand', 'Jordan', 'Egypt', 'Liechtenstein', 'Guinea']},
    {'level': 3, 'name': 'Ivory Coast', 'options': ['Romania', 'Czech Republic', 'Myanmar', 'Saudi Arabia', 'Luxembourg', 'Trinidad and Tobago']},
    {'level': 3, 'name': 'Norway', 'options': ['Ireland', 'Romania', 'Cuba', 'Nigeria', 'Mali', 'Slovenia']},
    {'level': 3, 'name': 'Nepal', 'options': ['Colombia', 'Ireland', 'Cuba', 'Namibia', 'Barbados', 'Slovakia']},
    {'level': 3, 'name': 'Namibia', 'options': ['Belgium', 'Ireland', 'Nigeria', 'Ivory Coast', 'Sudan', 'South Sudan']},
    {'level': 3, 'name': 'Egypt', 'options': ['Iraq', 'Mexico', 'Ethiopia', 'Maldives', 'Slovenia', 'Thailand']},
    {'level': 3, 'name': 'Bahrain', 'options': ['Morocco', 'Belgium', 'Malaysia', 'Ivory Coast', 'Trinidad and Tobago', 'Thailand']},
    {'level': 3, 'name': 'North Korea', 'options': ['Zimbabwe', 'Morocco', 'Niger', 'Qatar', 'Estonia', 'Ecuador']},
    {'level': 3, 'name': 'Saudi Arabia', 'options': ['Belgium', 'Australia', 'Austria', 'Namibia', 'Philippines', 'Uzbekistan']},
    {'level': 3, 'name': 'Senegal', 'options': ['Iceland', 'Bangladesh', 'Ethiopia', 'Nepal', 'Slovenia', 'Bahamas']},
    {'level': 3, 'name': 'Myanmar', 'options': ['Australia', 'Serbia', 'Ivory Coast', 'Niger', 'Barbados', 'Liechtenstein']},
    {'level': 3, 'name': 'Ethiopia', 'options': ['Denmark', 'Bangladesh', 'Nepal', 'Ivory Coast', 'Bulgaria', 'Cameroon']},
    {'level': 4, 'name': 'Mali', 'options': ['Maldives', 'Egypt', 'Bulgaria', 'Sudan', 'Algeria', 'Guatemala']},
    {'level': 4, 'name': 'United Arab Emirates', 'options': ['Bahrain', 'Cuba', 'Liechtenstein', 'Luxembourg', 'Libya', 'Bolivia']},
    {'level': 4, 'name': 'Cameroon', 'options': ['Nepal', 'Ethiopia', 'Estonia', 'El Salvador', 'Grenada', 'Kenya']},
    {'level': 4, 'name': 'Philippines', 'options': ['Saudi Arabia', 'Qatar', 'Bahamas', 'El Salvador', 'Palestine', 'Kenya']},
    {'level': 4, 'name': 'Thailand', 'options': ['Niger', 'Qatar', 'Trinidad and Tobago', 'Azerbaijan', 'Grenada', 'Chile']},
    {'level': 4, 'name': 'Oman', 'options': ['Norway', 'Niger', 'Luxembourg', 'Trinidad and Tobago', 'Kenya', 'Rwanda']},
    {'level': 4, 'name': 'Uzbekistan', 'options': ['Qatar', 'Cuba', 'Sudan', 'Oman', 'Palestine', 'Armenia']},
    {'level': 4, 'name': 'El Salvador', 'options': ['Nepal', 'Cuba', 'Cameroon', 'Slovakia', 'Grenada', 'Armenia']},
    {'level': 4, 'name': 'Slovenia', 'options': ['Austria', 'Ivory Coast', 'United Arab Emirates', 'Azerbaijan', 'Turkmenistan', 'Tunisia']},
    {'level': 4, 'name': 'Bahamas', 'options': ['Senegal', 'North Korea', 'Philippines', 'Barbados', 'Liberia', 'Grenada']},
    {'level': 4, 'name': 'Azerbaijan', 'options': ['Syria', 'Cuba', 'Barbados', 'Trinidad and Tobago', 'Liberia', 'Armenia']},
    {'level': 4, 'name': 'Estonia', 'options': ['Malaysia', 'Syria', 'Slovenia', 'United Arab Emirates', 'Bhutan', 'Algeria']},
    {'level': 4, 'name': 'Luxembourg', 'options': ['Senegal', 'Norway', 'Estonia', 'United Arab Emirates', 'Singapore', 'Tunisia']},
    {'level': 4, 'name': 'Barbados', 'options': ['Austria', 'Ivory Coast', 'Slovenia', 'South Sudan', 'Rwanda', 'Kenya']},
    {'level': 4, 'name': 'Liechtenstein', 'options': ['Niger', 'Senegal', 'Ecuador', 'Azerbaijan', 'Libya', 'Turkmenistan']},
    {'level': 4, 'name': 'Slovakia', 'options': ['Egypt', 'Qatar', 'United Arab Emirates', 'El Salvador', 'Kenya', 'Chile']},
    {'level': 4, 'name': 'Trinidad and Tobago', 'options': ['Namibia', 'Malaysia', 'Luxembourg', 'Estonia', 'Grenada', 'Tunisia']},
    {'level': 4, 'name': 'Bulgaria', 'options': ['Nepal', 'Niger', 'United Arab Emirates', 'Cameroon', 'Costa Rica', 'Liberia']},
    {'level': 4, 'name': 'Guinea', 'options': ['North Korea', 'Bahrain', 'United Arab Emirates', 'Oman', 'Chile', 'Bolivia']},
    {'level': 4, 'name': 'South Sudan', 'options': ['Norway', 'Myanmar', 'Oman', 'Thailand', 'Libya', 'Tunisia']},
    {'level': 4, 'name': 'Ecuador', 'options': ['Nepal', 'Ethiopia', 'South Sudan', 'Oman', 'Chile', 'Tunisia']},
    {'level': 4, 'name': 'Sudan', 'options': ['Egypt', 'Nepal', 'South Sudan', 'Luxembourg', 'Grenada', 'Singapore']},
    {'level': 5, 'name': 'Libya', 'options': ['Thailand', 'Estonia', 'Cyprus', 'Bolivia', 'Botswana', 'Vietnam']},
    {'level': 5, 'name': 'Palestine', 'options': ['South Sudan', 'Luxembourg', 'Singapore', 'Armenia', 'Afghanistan', 'Vietnam']},
    {'level': 5, 'name': 'Bolivia', 'options': ['El Salvador', 'Uzbekistan', 'Tunisia', 'Grenada', 'Vietnam', 'Suriname']},
    {'level': 5, 'name': 'Algeria', 'options': ['El Salvador', 'Trinidad and Tobago', 'Bhutan', 'Costa Rica', 'Georgia', 'Dominican Republic']},
    {'level': 5, 'name': 'Tunisia', 'options': ['Ecuador', 'Slovenia', 'Singapore', 'Rwanda', 'Botswana', 'Mauritius']},
    {'level': 5, 'name': 'Cyprus', 'options': ['Bulgaria', 'Bahamas', 'Kenya', 'Palestine', 'Mauritius', 'Democratic Republic of Congo']},
    {'level': 5, 'name': 'Grenada', 'options': ['Ecuador', 'Sudan', 'Cyprus', 'Palestine', 'Suriname', 'Vietnam']},
    {'level': 5, 'name': 'Rwanda', 'options': ['Mali', 'Barbados', 'Singapore', 'Liberia', 'Kazakhstan', 'Democratic Republic of Congo']},
    {'level': 5, 'name': 'Armenia', 'options': ['Slovakia', 'Oman', 'Bhutan', 'Turkmenistan', 'Mauritius', 'Suriname']},
    {'level': 5, 'name': 'Guatemala', 'options': ['Oman', 'Mali', 'Rwanda', 'Tunisia', 'Mozambique', 'Democratic Republic of Congo']},
    {'level': 5, 'name': 'Bhutan', 'options': ['South Sudan', 'El Salvador', 'Rwanda', 'Cyprus', 'Mauritius', 'Botswana']},
    {'level': 5, 'name': 'Peru', 'options': ['Philippines', 'Barbados', 'Singapore', 'Chile', 'Andorra', 'Paraguay']},
    {'level': 5, 'name': 'Costa Rica', 'options': ['Guinea', 'Cameroon', 'Kenya', 'Peru', 'Andorra', 'Kazakhstan']},
    {'level': 5, 'name': 'Turkmenistan', 'options': ['Luxembourg', 'El Salvador', 'Liberia', 'Grenada', 'Mauritius', 'Moldova']},
    {'level': 5, 'name': 'Liberia', 'options': ['Liechtenstein', 'Slovakia', 'Rwanda', 'Tunisia', 'Georgia', 'Paraguay']},
    {'level': 5, 'name': 'Chile', 'options': ['Philippines', 'South Sudan', 'Rwanda', 'Peru', 'Gambia', 'Madagascar']},
    {'level': 5, 'name': 'Kenya', 'options': ['Bahamas', 'South Sudan', 'Palestine', 'Singapore', 'Afghanistan', 'Vietnam']},
    {'level': 5, 'name': 'Singapore', 'options': ['Azerbaijan', 'Barbados', 'Libya', 'Peru', 'Suriname', 'Andorra']},
    {'level': 6, 'name': 'Afghanistan', 'options': ['Guatemala', 'Palestine', 'Somalia', 'Mauritius', 'Latvia', 'Montenegro']},
    {'level': 6, 'name': 'Bosnia and Herzegovina', 'options': ['Liberia', 'Tunisia', 'Kazakhstan', 'Tanzania', 'Haiti', 'Micronesia']},
    {'level': 6, 'name': 'Tanzania', 'options': ['Singapore', 'Bolivia', 'Mozambique', 'Dominican Republic', 'Lebanon', 'Mauritania']},
    {'level': 6, 'name': 'Mauritius', 'options': ['Peru', 'Grenada', 'Moldova', 'Suriname', 'Dominica', 'Honduras']},
    {'level': 6, 'name': 'Kazakhstan', 'options': ['Bolivia', 'Palestine', 'Andorra', 'Afghanistan', 'Mauritania', 'Tajikistan']},
    {'level': 6, 'name': 'Belarus', 'options': ['Peru', 'Libya', 'Botswana', 'Gambia', 'Albania', 'Tajikistan']},
    {'level': 6, 'name': 'Democratic Republic of Congo', 'options': ['Tunisia', 'Liberia', 'Afghanistan', 'Belarus', 'Tuvalu', 'Chad']},
    {'level': 6, 'name': 'Madagascar', 'options': ['Chile', 'Grenada', 'Vietnam', 'Democratic Republic of Congo', 'Honduras', 'Montenegro']},
    {'level': 6, 'name': 'Gabon', 'options': ['Grenada', 'Chile', 'Andorra', 'Democratic Republic of Congo', 'Equatorial Guinea', 'Dominica']},
    {'level': 6, 'name': 'Andorra', 'options': ['Bhutan', 'Algeria', 'Afghanistan', 'Vietnam', 'Latvia', 'Micronesia']},
    {'level': 6, 'name': 'Moldova', 'options': ['Bolivia', 'Singapore', 'Gabon', 'Vietnam', 'Tuvalu', 'Montenegro']},
    {'level': 6, 'name': 'Gambia', 'options': ['Cyprus', 'Rwanda', 'Democratic Republic of Congo', 'Paraguay', 'Micronesia', 'Albania']},
    {'level': 6, 'name': 'Botswana', 'options': ['Costa Rica', 'Bolivia', 'Kazakhstan', 'Gambia', 'Dominica', 'Kiribati']},
    {'level': 6, 'name': 'Dominican Republic', 'options': ['Bhutan', 'Peru', 'Andorra', 'Bosnia and Herzegovina', 'Yemen', 'Haiti']},
    {'level': 6, 'name': 'Somalia', 'options': ['Costa Rica', 'Peru', 'Mozambique', 'Georgia', 'Mauritania', 'Haiti']},
    {'level': 6, 'name': 'Suriname', 'options': ['Kenya', 'Palestine', 'Somalia', 'Botswana', 'Angola', 'Micronesia']},
    {'level': 6, 'name': 'Paraguay', 'options': ['Peru', 'Singapore', 'Mozambique', 'Andorra', 'Tajikistan', 'Guyana']},
    {'level': 6, 'name': 'Vietnam', 'options': ['Tunisia', 'Costa Rica', 'Suriname', 'Georgia', 'Haiti', 'Micronesia']},
    {'level': 6, 'name': 'Mozambique', 'options': ['Algeria', 'Libya', 'Andorra', 'Belarus', 'Haiti', 'Albania']},
    {'level': 6, 'name': 'Georgia', 'options': ['Turkmenistan', 'Liberia', 'Mozambique', 'Gabon', 'Angola', 'Equatorial Guinea']},
    {'level': 7, 'name': 'Guyana', 'options': ['Tanzania', 'Vietnam', 'Micronesia', 'Albania', 'Cambodia', 'Seychelles']},
    {'level': 7, 'name': 'Haiti', 'options': ['Moldova', 'Georgia', 'Honduras', 'Lebanon', 'Papua New Guinea', 'Venezuela']},
    {'level': 7, 'name': 'Dominica', 'options': ['Somalia', 'Mozambique', 'Equatorial Guinea', 'Guyana', 'Guinea-Bissau', 'Malawi']},
    {'level': 7, 'name': 'Mauritania', 'options': ['Democratic Republic of Congo', 'Mozambique', 'Kiribati', 'Chad', 'Laos', 'Congo']},
    {'level': 7, 'name': 'Chad', 'options': ['Democratic Republic of Congo', 'Botswana', 'Montenegro', 'Mauritania', 'Seychelles', 'Guinea-Bissau']},
    {'level': 7, 'name': 'Honduras', 'options': ['Mauritius', 'Dominican Republic', 'Tuvalu', 'Tajikistan', 'Mongolia', 'Laos']},
    {'level': 7, 'name': 'Equatorial Guinea', 'options': ['Mozambique', 'Belarus', 'Latvia', 'Guyana', 'Malawi', 'Lithuania']},
    {'level': 7, 'name': 'Montenegro', 'options': ['Somalia', 'Gabon', 'Guyana', 'Lebanon', 'Seychelles', 'Congo']},
    {'level': 7, 'name': 'Tajikistan', 'options': ['Tanzania', 'Georgia', 'Dominica', 'Chad', 'Congo', 'Sierra Leone']},
    {'level': 7, 'name': 'Albania', 'options': ['Somalia', 'Gambia', 'Montenegro', 'Angola', 'Djibouti', 'Guinea-Bissau']},
    {'level': 7, 'name': 'Yemen', 'options': ['Gambia', 'Somalia', 'Lebanon', 'Tajikistan', 'Papua New Guinea', 'Congo']},
    {'level': 7, 'name': 'Kiribati', 'options': ['Bosnia and Herzegovina', 'Dominican Republic', 'Mauritania', 'Latvia', 'Seychelles', 'San Marino']},
    {'level': 7, 'name': 'Tuvalu', 'options': ['Mozambique', 'Paraguay', 'Mauritania', 'Micronesia', 'Lesotho', 'Cambodia']},
    {'level': 7, 'name': 'Micronesia', 'options': ['Paraguay', 'Suriname', 'Yemen', 'Equatorial Guinea', 'Benin', 'Lesotho']},
    {'level': 7, 'name': 'Latvia', 'options': ['Madagascar', 'Georgia', 'Angola', 'Kiribati', 'Benin', 'Venezuela']},
    {'level': 7, 'name': 'Angola', 'options': ['Vietnam', 'Georgia', 'Lebanon', 'Montenegro', 'San Marino', 'Sierra Leone']},
    {'level': 7, 'name': 'Lebanon', 'options': ['Moldova', 'Paraguay', 'Tajikistan', 'Haiti', 'Cambodia', 'Lesotho']},
    {'level': 8, 'name': 'Djibouti', 'options': ['Kiribati', 'Micronesia', 'Venezuela', 'Cambodia', 'Vanuatu', 'Palau']},
    {'level': 8, 'name': 'Mongolia', 'options': ['Albania', 'Latvia', 'Laos', 'Guinea-Bissau', 'Marshall Islands', 'Nauru']},
    {'level': 8, 'name': 'Papua New Guinea', 'options': ['Mauritania', 'Kiribati', 'Laos', 'San Marino', 'Tonga', 'Belize']},
    {'level': 8, 'name': 'Lithuania', 'options': ['Tuvalu', 'Lebanon', 'Congo', 'Venezuela', 'Belize', 'Uganda']},
    {'level': 8, 'name': 'Lesotho', 'options': ['Lebanon', 'Tuvalu', 'Cambodia', 'Benin', 'Saint Kitts and Nevis', 'Marshall Islands']},
    {'level': 8, 'name': 'Congo', 'options': ['Dominica', 'Albania', 'Venezuela', 'San Marino', 'Vanuatu', 'Malta']},
    {'level': 8, 'name': 'Malawi', 'options': ['Angola', 'Tajikistan', 'Papua New Guinea', 'Cambodia', 'Malta', 'Nicaragua']},
    {'level': 8, 'name': 'Laos', 'options': ['Albania', 'Micronesia', 'Papua New Guinea', 'Lesotho', 'Malta', 'Marshall Islands']},
    {'level': 8, 'name': 'Antigua and Barbuda', 'options': ['Tajikistan', 'Lebanon', 'Congo', 'Lesotho', 'Panama', 'Tonga']},
    {'level': 8, 'name': 'Guinea-Bissau', 'options': ['Tuvalu', 'Tajikistan', 'Venezuela', 'Malawi', 'Vanuatu', 'Marshall Islands']},
    {'level': 8, 'name': 'Seychelles', 'options': ['Haiti', 'Honduras', 'Cambodia', 'Sierra Leone', 'Belize', 'Saint Kitts and Nevis']},
    {'level': 8, 'name': 'Venezuela', 'options': ['Equatorial Guinea', 'Mauritania', 'Guinea-Bissau', 'San Marino', 'Belize', 'North Macedonia']},
    {'level': 8, 'name': 'Sierra Leone', 'options': ['Kiribati', 'Haiti', 'Lithuania', 'Benin', 'Marshall Islands', 'Togo']},
    {'level': 8, 'name': 'San Marino', 'options': ['Montenegro', 'Equatorial Guinea', 'Malawi', 'Guinea-Bissau', 'Belize', 'Saint Lucia']},
    {'level': 8, 'name': 'Cambodia', 'options': ['Latvia', 'Chad', 'Sierra Leone', 'Papua New Guinea', 'Malta', 'Nicaragua']},
    {'level': 8, 'name': 'Benin', 'options': ['Honduras', 'Angola', 'Papua New Guinea', 'Congo', 'Marshall Islands', 'Togo']},
    {'level': 9, 'name': 'Malta', 'options': ['Guinea-Bissau', 'Sierra Leone', 'Saint Lucia', 'Uganda', 'Eritrea', 'Burkina Faso']},
    {'level': 9, 'name': 'Uganda', 'options': ['Laos', 'Malawi', 'Malta', 'Nicaragua', 'Cabo Verde', 'Burkina Faso']},
    {'level': 9, 'name': 'Marshall Islands', 'options': ['Congo', 'Djibouti', 'Malta', 'Uganda', 'Central African Republic', 'Cabo Verde']},
    {'level': 9, 'name': 'North Macedonia', 'options': ['San Marino', 'Benin', 'Nauru', 'Nicaragua', 'St. Vincent Grenadines', 'Burundi']},
    {'level': 9, 'name': 'Nicaragua', 'options': ['Mongolia', 'Cambodia', 'Togo', 'Saint Kitts and Nevis', 'Central African Republic', 'Eritrea']},
    {'level': 9, 'name': 'Belize', 'options': ['Congo', 'Laos', 'Palau', 'Tonga', 'Timor-Leste', 'Sao Tome and Principe']},
    {'level': 9, 'name': 'Nauru', 'options': ['Cambodia', 'Benin', 'Belize', 'Vanuatu', 'Timor-Leste', 'Comoros']},
    {'level': 9, 'name': 'Tonga', 'options': ['Djibouti', 'Mongolia', 'Panama', 'Nauru', 'Burundi', 'Solomon Islands']},
    {'level': 9, 'name': 'Panama', 'options': ['Djibouti', 'Venezuela', 'Malta', 'Palau', 'Sao Tome and Principe', 'St. Vincent Grenadines']},
    {'level': 9, 'name': 'Vanuatu', 'options': ['Congo', 'Cambodia', 'Nauru', 'Belize', 'Comoros', 'Timor-Leste']},
    {'level': 9, 'name': 'Palau', 'options': ['Lithuania', 'Sierra Leone', 'Nicaragua', 'Nauru', 'Sao Tome and Principe', 'Burundi']},
    {'level': 9, 'name': 'Togo', 'options': ['Malawi', 'Congo', 'Tonga', 'Saint Lucia', 'Sao Tome and Principe', 'St. Vincent Grenadines']},
    {'level': 9, 'name': 'Saint Kitts and Nevis', 'options': ['Sierra Leone', 'Benin', 'Tonga', 'Saint Lucia', 'Eritrea', 'Samoa']},
    {'level': 9, 'name': 'Saint Lucia', 'options': ['Benin', 'Laos', 'Belize', 'Malta', 'Eritrea', 'Burkina Faso']},
    {'level': 10, 'name': 'Samoa', 'options': ['Laos', 'Malawi', 'Marshall Islands', 'Malta', 'Burkina Faso', 'Brunei']},
    {'level': 10, 'name': 'Burundi', 'options': ['Benin', 'Guinea-Bissau', 'Saint Kitts and Nevis', 'Togo', 'Cabo Verde', 'Timor-Leste']},
    {'level': 10, 'name': 'Central African Republic', 'options': ['Antigua and Barbuda', 'Malawi', 'Saint Kitts and Nevis', 'Saint Lucia', 'Eswatini', 'Burkina Faso']},
    {'level': 10, 'name': 'Kyrgyzstan', 'options': ['Antigua and Barbuda', 'Guinea-Bissau', 'Saint Kitts and Nevis', 'Marshall Islands', 'St. Vincent Grenadines', 'Brunei']},
    {'level': 10, 'name': 'Comoros', 'options': ['Antigua and Barbuda', 'Cambodia', 'Nicaragua', 'Vanuatu', 'Cabo Verde', 'Samoa']},
    {'level': 10, 'name': 'Eswatini', 'options': ['Mongolia', 'Congo', 'Saint Lucia', 'Panama', 'Central African Republic', 'Comoros']},
    {'level': 10, 'name': 'Cabo Verde', 'options': ['Papua New Guinea', 'Benin', 'Malta', 'Belize', 'Brunei', 'Eritrea']},
    {'level': 10, 'name': 'Solomon Islands', 'options': ['Venezuela', 'Guinea-Bissau', 'Nauru', 'Tonga', 'Sao Tome and Principe', 'Timor-Leste']},
    {'level': 10, 'name': 'Eritrea', 'options': ['San Marino', 'Papua New Guinea', 'Uganda', 'Nicaragua', 'Zambia', 'Comoros']},
    {'level': 10, 'name': 'St. Vincent Grenadines', 'options': ['Cambodia', 'Lesotho', 'Marshall Islands', 'Tonga', 'Cabo Verde', 'Eritrea']},
    {'level': 10, 'name': 'Zambia', 'options': ['Malawi', 'Guinea-Bissau', 'North Macedonia', 'Saint Kitts and Nevis', 'Eswatini', 'Central African Republic']},
    {'level': 10, 'name': 'Burkina Faso', 'options': ['Sierra Leone', 'Benin', 'Uganda', 'Saint Lucia', 'Burundi', 'Cabo Verde']},
    {'level': 10, 'name': 'Timor-Leste', 'options': ['Lesotho', 'Seychelles', 'Panama', 'North Macedonia', 'Central African Republic', 'Solomon Islands']},
    {'level': 10, 'name': 'Brunei', 'options': ['Antigua and Barbuda', 'Djibouti', 'Palau', 'Saint Kitts and Nevis', 'Samoa', 'Comoros']},
    {'level': 10, 'name': 'Sao Tome and Principe', 'options': ['Laos', 'Malawi', 'Togo', 'Belize', 'Solomon Islands', 'Central African Republic']}
]

quiz = []

for flag in flags:
    curr = {}
    curr['options'] =  fetcher.fetch('flag', flag)
