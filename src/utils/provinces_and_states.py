# Canadian provinces with cities in descending order of population
canadian_provinces = {
    "ON": {"name": "Ontario", "cities": ["Toronto", "Ottawa", "Mississauga", "Brampton", "Hamilton", "London", "Markham", "Vaughan", "Kitchener", "Windsor", "Richmond Hill", "Oakville", "Burlington", "Greater Sudbury", "Oshawa"]},
    "QC": {"name": "Quebec", "cities": ["Montreal", "Quebec City", "Laval", "Gatineau", "Longueuil", "Sherbrooke", "Saguenay", "Levis", "Trois-Rivieres", "Terrebonne", "Saint-Jean-sur-Richelieu", "Repentigny", "Drummondville", "Saint-Jerome", "Granby"]},
    "BC": {"name": "British Columbia", "cities": ["Vancouver", "Surrey", "Burnaby", "Richmond", "Abbotsford", "Coquitlam", "Kelowna", "Langley", "Saanich", "Delta", "Kamloops", "Nanaimo", "Victoria", "Chilliwack", "Maple Ridge"]},
    "AB": {"name": "Alberta", "cities": ["Calgary", "Edmonton", "Red Deer", "Lethbridge", "St. Albert", "Medicine Hat", "Grande Prairie", "Airdrie", "Spruce Grove", "Leduc", "Fort Saskatchewan", "Chestermere", "Lloydminster", "Camrose", "Beaumont"]},
    "MB": {"name": "Manitoba", "cities": ["Winnipeg", "Brandon", "Steinbach", "Thompson", "Portage la Prairie", "Winkler", "Selkirk", "Morden", "Dauphin", "Flin Flon", "The Pas", "Stonewall", "Niverville", "Altona", "Swan River"]},
    "SK": {"name": "Saskatchewan", "cities": ["Saskatoon", "Regina", "Prince Albert", "Moose Jaw", "Swift Current", "Yorkton", "North Battleford", "Estevan", "Weyburn", "Martensville", "Meadow Lake", "Melfort", "Humboldt", "Kindersley", "Melville"]},
    "NS": {"name": "Nova Scotia", "cities": ["Halifax", "Sydney", "Truro", "New Glasgow", "Glace Bay", "Kentville", "Amherst", "Bridgewater", "Yarmouth", "Greenwood", "Antigonish", "Windsor", "Wolfville", "Shelburne", "Digby"]},
    "NB": {"name": "New Brunswick", "cities": ["Moncton", "Saint John", "Fredericton", "Dieppe", "Miramichi", "Edmundston", "Bathurst", "Campbellton", "Oromocto", "Sackville", "Grand Falls", "Riverview", "Quispamsis", "Rothesay", "Sussex"]},
    "NL": {"name": "Newfoundland and Labrador", "cities": ["St. John's", "Mount Pearl", "Corner Brook", "Conception Bay South", "Paradise", "Grand Falls-Windsor", "Gander", "Happy Valley-Goose Bay", "Labrador City", "Bay Roberts", "Stephenville", "Carbonear", "Deer Lake", "Marystown", "Bonavista"]},
    "PE": {"name": "Prince Edward Island", "cities": ["Charlottetown", "Summerside", "Stratford", "Cornwall", "Montague", "Kensington", "Souris", "Alberton", "Tignish", "Georgetown", "Borden-Carleton", "North Rustico", "O'Leary", "Murray River", "Morell"]}
}

# American states with cities in descending order of population
us_states = {
    "CA": {"name": "California", "cities": ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno", "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim", "Santa Ana", "Riverside", "Stockton", "Chula Vista", "Irvine"]},
    "TX": {"name": "Texas", "cities": ["Houston", "San Antonio", "Dallas", "Austin", "Fort Worth", "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo", "Lubbock", "Garland", "Irving", "Amarillo", "Grand Prairie"]},
    "FL": {"name": "Florida", "cities": ["Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg", "Hialeah", "Port St. Lucie", "Tallahassee", "Cape Coral", "Fort Lauderdale", "Pembroke Pines", "Hollywood", "Miramar", "Gainesville", "Coral Springs"]},
    "NY": {"name": "New York", "cities": ["New York City", "Buffalo", "Rochester", "Yonkers", "Syracuse", "Albany", "New Rochelle", "Mount Vernon", "Schenectady", "Utica", "White Plains", "Troy", "Niagara Falls", "Binghamton", "Rome"]},
    "IL": {"name": "Illinois", "cities": ["Chicago", "Aurora", "Naperville", "Joliet", "Rockford", "Springfield", "Elgin", "Peoria", "Champaign", "Waukegan", "Cicero", "Bloomington", "Arlington Heights", "Evanston", "Decatur"]},
    "PA": {"name": "Pennsylvania", "cities": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster", "Harrisburg", "York", "Altoona", "Wilkes-Barre", "State College", "Chester", "Easton"]},
    "OH": {"name": "Ohio", "cities": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton", "Parma", "Canton", "Youngstown", "Lorain", "Hamilton", "Springfield", "Kettering", "Elyria", "Lakewood"]},
    "GA": {"name": "Georgia", "cities": ["Atlanta", "Augusta", "Columbus", "Macon", "Savannah", "Athens", "Sandy Springs", "Roswell", "Johns Creek", "Albany", "Warner Robins", "Alpharetta", "Marietta", "Valdosta", "Smyrna"]},
    "NC": {"name": "North Carolina", "cities": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem", "Fayetteville", "Cary", "Wilmington", "High Point", "Concord", "Greenville", "Asheville", "Gastonia", "Jacksonville", "Chapel Hill"]},
    "MI": {"name": "Michigan", "cities": ["Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Ann Arbor", "Lansing", "Flint", "Dearborn", "Livonia", "Westland", "Troy", "Farmington Hills", "Kalamazoo", "Wyoming", "Southfield"]}
}

accepted_regions = {
    "ON": {"name": "Ontario", "cities": ["Toronto", "Ottawa", "Mississauga", "Brampton", "Hamilton", "London", "Markham", "Vaughan", "Kitchener", "Windsor", "Richmond Hill", "Oakville", "Burlington", "Greater Sudbury", "Oshawa"]},
    "AB": {"name": "Alberta", "cities": ["Calgary", "Edmonton", "Red Deer", "Lethbridge", "St. Albert", "Medicine Hat", "Grande Prairie", "Airdrie", "Spruce Grove", "Leduc", "Fort Saskatchewan", "Chestermere", "Lloydminster", "Camrose", "Beaumont"]},
    "MB": {"name": "Manitoba", "cities": ["Winnipeg", "Brandon", "Steinbach", "Thompson", "Portage la Prairie", "Winkler", "Selkirk", "Morden", "Dauphin", "Flin Flon", "The Pas", "Stonewall", "Niverville", "Altona", "Swan River"]},
    "NS": {"name": "Nova Scotia", "cities": ["Halifax", "Sydney", "Truro", "New Glasgow", "Glace Bay", "Kentville", "Amherst", "Bridgewater", "Yarmouth", "Greenwood", "Antigonish", "Windsor", "Wolfville", "Shelburne", "Digby"]},
    "NB": {"name": "New Brunswick", "cities": ["Moncton", "Saint John", "Fredericton", "Dieppe", "Miramichi", "Edmundston", "Bathurst", "Campbellton", "Oromocto", "Sackville", "Grand Falls", "Riverview", "Quispamsis", "Rothesay", "Sussex"]},
    "PE": {"name": "Prince Edward Island", "cities": ["Charlottetown", "Summerside", "Stratford", "Cornwall", "Montague", "Kensington", "Souris", "Alberton", "Tignish", "Georgetown", "Borden-Carleton", "North Rustico", "O'Leary", "Murray River", "Morell"]}
}