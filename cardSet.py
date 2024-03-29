# A CardSet object contains information about a set of Pokemon cards
# This can be changed to work for any card set, but currently the values of the Evolutions set are hard coded in
class CardSet:
    def __init__(self):
        # List of the names of cards in the Evolutions Set
        self.cardnamelist = ("Venusaur EX",  # 001 Venusar EX
                             "M Venusaur EX",
                             "Caterpie",
                             "Metapod",
                             "Weedle",
                             "Kakuna",
                             "Beedrill",
                             "Tangela",
                             "Charmander",
                             "Charmeleon",
                             "Charizard",  # 011 Charizard
                             "Charizard EX",
                             "M Charizard EX",
                             "Vulpix",
                             "Ninetales",
                             "Ninetales BREAK",
                             "Growlithe",
                             "Arcanine",
                             "Ponyta",
                             "Magmar",
                             "Blastoise EX",  # 021 Blastoise
                             "M Blastoise EX",
                             "Poliwag",
                             "Poliwhirl",
                             "Poliwrath",
                             "Slowbro EX",
                             "M Slowbro EX",
                             "Seel",
                             "Dewgong",
                             "Staryu",
                             "Starmie",  # 031 Starmie
                             "Starmie BREAK",
                             "Magikarp",
                             "Gyarados",
                             "Pikachu",
                             "Raichu",
                             "Magnemite",
                             "Magneton",
                             "Voltorb",
                             "Electrode",
                             "Electabuzz",  # 041 Electabuzz
                             "Zapdos",
                             "Nidoran ♂",
                             "Nidorino",
                             "Nidoking",
                             "Nidoking BREAK",
                             "Gastly",
                             "Haunter",
                             "Drowzee",
                             "Koffing",
                             "Mewtwo",  # 051 Mewtwo
                             "Mewtwo EX",
                             "Mew",
                             "Sandshrew",
                             "Diglett",
                             "Dugtrio",
                             "Machop",
                             "Machoke",
                             "Machamp",
                             "Machamp BREAK",
                             "Onix",  # 061 Onix
                             "Hitmonchan",
                             "Clefairy",
                             "Pidgeot EX",
                             "M Pidgeot EX",
                             "Rattata",
                             "Raticate",
                             "Farfetch'd",
                             "Doduo",
                             "Chansey",
                             "Porygon",  # 071 Porygon
                             "Dragonite EX",
                             "Blastoise Spirit Link",
                             "Brock's Grit",
                             "Charizard Spirit Link",
                             "Devolution Spray",
                             "Energy Retrieval",
                             "Full Heal",
                             "Maintenance",
                             "Misty's Determination",
                             "Pidgeot Spirit Link",  # 081 Pidgeot Spirit Link
                             "Pokedex",
                             "Potion",
                             "Professor Oak's Hint",
                             "Revive",
                             "Slowbro Spirit Link",
                             "Super Potion",
                             "Switch",
                             "Venusaur Spirit Link",
                             "Double Colorless Energy",
                             "Grass Energy",  # 091 Grass Energy
                             "Fire Energy",
                             "Water Energy",
                             "Electric Energy",
                             "Psychic Energy",
                             "Fighting Energy",
                             "Dark Energy",
                             "Metal Energy",
                             "Fairy Energy",
                             "M Venusaur EX",
                             "M Charizard EX",  # 101 M Charizard EX
                             "M Blastoise EX",
                             "Mewtwo EX",
                             "Pidgeot EX",
                             "M Pidgeot EX",
                             "Dragonite EX",
                             "Brock's Grit",
                             "Misty's Determination",
                             "Exeggutor",
                             "Flying Pikachu",
                             "Surfing Pikachu",  # 111 Surfing Pikachu
                             "Imakuni?'s Doduo",
                             "Here Comes Team Rocket!")

        # List of every card's respective Pokemon. Trainer & energy cards are stored as 'NA'
        self.pokemonlist = ("Venusaur",  # 001 Venusaur EX
                            "Mega Venusaur",
                            "Caterpie",
                            "Metapod",
                            "Weedle",
                            "Kakuna",
                            "Beedrill",
                            "Tangela",
                            "Charmander",
                            "Charmeleon",
                            "Charizard",  # 011 Charizard
                            "Charizard",
                            "Mega Charizard",
                            "Vulpix",
                            "Ninetales",
                            "Ninetales",
                            "Growlithe",
                            "Arcanine",
                            "Ponyta",
                            "Magmar",
                            "Blastoise",  # 021 Blastoise EX
                            "Mega Blastoise",
                            "Poliwag",
                            "Poliwhirl",
                            "Poliwrath",
                            "Slowbro",
                            "Mega Slowbro",
                            "Seel",
                            "Dewgong",
                            "Staryu",
                            "Starmie",  # 031 Starmie
                            "Starmie",
                            "Magikarp",
                            "Gyarados",
                            "Pikachu",
                            "Raichu",
                            "Magnemite",
                            "Magneton",
                            "Voltorb",
                            "Electrode",
                            "Electabuzz",  # 041 Electabuzz
                            "Zapdos",
                            "Nidoran ♂",
                            "Nidorino",
                            "Nidoking",
                            "Nidoking",
                            "Gastly",
                            "Haunter",
                            "Drowzee",
                            "Koffing",
                            "Mewtwo",  # 051 Mewtwo
                            "Mewtwo",
                            "Mew",
                            "Sandshrew",
                            "Diglett",
                            "Dugtrio",
                            "Machop",
                            "Machoke",
                            "Machamp",
                            "Machamp",
                            "Onix",  # 061 Onix
                            "Hitmonchan",
                            "Clefairy",
                            "Pidgeot",
                            "Mega Pidgeot",
                            "Rattata",
                            "Raticate",
                            "Farfetch'd",
                            "Doduo",
                            "Chansey",
                            "Porygon",  # 071 Porygon
                            "Dragonite",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",  # 081 Pidgeot Spirit Link
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",  # 091 Grass Energy
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "NA",
                            "Mega Venusaur",
                            "Mega Charizard",  # 101 M Charizard EX
                            "Mega Blastoise",
                            "Mewtwo",
                            "Pidgeot",
                            "Mega Pidgeot",
                            "Dragonite",
                            "NA",
                            "NA",
                            "Exeggutor",
                            "Flying Pikachu",
                            "Surfing Pikachu",  # 111 Surfing Pikachu
                            "Imakuni?'s Doduo",
                            "NA")

        # List of the rarity of each card in the Evolutions set
        self.rarity = (  # Regular Pokemon
            "EX Rare",  # 001 Venusar EX
            "EX Rare",
            "Common",
            "Uncommon",
            "Common",
            "Uncommon",
            "Rare",
            "Common",
            "Common",
            "Uncommon",
            "Holo Rare",  # 011 Charizard
            "EX Rare",
            "EX Rare",
            "Common",
            "Holo Rare",
            "Break Rare",
            "Common",
            "Rare",
            "Common",
            "Uncommon",
            "EX Rare",  # 021 Blastoise EX
            "EX Rare",
            "Common",
            "Uncommon",
            "Holo Rare",
            "EX Rare",
            "EX Rare",
            "Common",
            "Rare",
            "Common",
            "Rare",  # 031 Starmie
            "Break Rare",
            "Common",
            "Holo Rare",
            "Common",
            "Holo Rare",
            "Common",
            "Rare Holo",
            "Common",
            "Rare",
            "Common",  # 041 Electabuzz
            "Holo Rare",
            "Common",
            "Uncommon",
            "Holo Rare",
            "Break Rare",
            "Common",
            "Uncommon",
            "Common",
            "Uncommon",
            "Rare",  # 051 Mewtwo
            "EX Rare",
            "Holo Rare",
            "Common",
            "Common",
            "Rare",
            "Common",
            "Uncommon",
            "Holo Rare",
            "Break Rare",
            "Common",  # 061 Onix
            "Holo Rare",
            "Holo Rare",
            "EX Rare",
            "EX Rare",
            "Common",
            "Rare",
            "Rare",
            "Common",
            "Holo Rare",
            "Uncommon",  # 071 Porygon
            "EX Rare",
            # Trainer cards
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",  # 081 Pidgeot Spirit Link
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            "Uncommon",
            # Energies
            "Common",
            "Common",  # 091 Grass Engery
            "Common",
            "Common",
            "Common",
            "Common",
            "Common",
            "Common",
            "Common",
            "Common",
            # Full arts
            "Ultra Rare",
            "Ultra Rare",  # 101 M Charizard EX
            "Ultra Rare",
            "Ultra Rare",
            "Ultra Rare",
            "Ultra Rare",
            "Ultra Rare",
            "Ultra Rare",
            "Ultra Rare",
            # Secret rares
            "Secret Rare",
            "Secret Rare",
            "Secret Rare",  # 111 Surfing Pikachu
            "Secret Rare",
            "Secret Rare")

        # List of the card type of each card in the Evolutions set
        self.cardtype = ("Pokemon",  # 001 Venusaur EX
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 011 Charizard
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 021 Blastoise EX
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 031 Starmie
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 041 Electabuzz
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 051 Mewtwo
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 061 Onix
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 071 Porygon
                         "Pokemon",
                         "Trainer Item",
                         "Trainer Supporter",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Supporter",
                         "Trainer Item",  # 081 Pidgeot Spirit Link
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Supporter",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Trainer Item",
                         "Energy",
                         "Energy",  # 091 Grass Energy
                         "Energy",
                         "Energy",
                         "Energy",
                         "Energy",
                         "Energy",
                         "Energy",
                         "Energy",
                         "Energy",
                         "Pokemon",
                         "Pokemon",  # 101 M Charizard EX
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",
                         "Trainer Supporter",
                         "Trainer Supporter",
                         "Pokemon",
                         "Pokemon",
                         "Pokemon",  # 111 Surfing Pikachu
                         "Pokemon",
                         "Trainer Supporter")

        self.numCards = len(self.cardnamelist)  # Number of cards in the Evolutions set
