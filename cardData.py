import mysql.connector
import cardSet
import pokedex
import evolutionsSet

username = "########"  # Your mysql username
password = "########"  # Your mysql password
databasename = "pokemonDatabase"  # name of database we want to create


# Creates a database of pokemon
def createDatabase():
    # Connects to the localhost
    db = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password
    )

    # Creates a cursor so that we can create and databases
    mycursor = db.cursor()

    # Check if database has already been created; if not, create it
    mycursor.execute(
        "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(databasename))
    if mycursor.fetchone() is None:
        mycursor.execute("CREATE DATABASE {}".format(databasename))

    # Add tables and values to database
    initializeDatabase()


# Initializes database with inital values for cards and pokemon
def initializeDatabase():
    # Connects to the database that already existed or was created in createDatabase()
    db = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password,
        database=databasename
    )

    # Creates a cursor so that we can edit the database
    mycursor = db.cursor()

    # Creates a Pokedex object that holds information on the first 151 (Kanto) Pokemon and some of their mega evolutions
    # Information includes pokedex number, pokemon names, type, stage, and height
    poke = pokedex.Pokedex()

    # Creates a CardSet object that has information on the cards in Evolutions
    # Information includes card numbers, pokemon names, card names, card rarity, and card type
    evoSet = cardSet.CardSet()

    # Creates a EvolutionsSet object that stores the hashes for the images of the Pokemon cards
    # Has hashes for the following orientations of the card: normal, mirrored, upside-down, upside down mirrored
    evoCards = evolutionsSet.EvolutionsSet()

    # Creates a new table Pokemon that will hold the values in the poke Pokedex object
    mycursor.execute("CREATE TABLE Pokemon (dexNumber SMALLINT, pokemon VARCHAR(20) PRIMARY KEY, \
            poketype VARCHAR(10), height DOUBLE UNSIGNED, stage VARCHAR(5))")

    # Populates the Pokemon table
    for x in range(poke.numpoke):
        mycursor.execute("INSERT INTO Pokemon (dexNumber, pokemon, poketype, stage, height) VALUES(%s, %s, %s, %s, %s)",
                         (poke.dexnumber[x], poke.pokemon[x], poke.type[x], poke.stage[x], poke.height[x]))

    # Creates a new table EvolutionsSet that will hold the values in the evoSet CardSet object
    mycursor.execute("CREATE TABLE EvolutionsSet (cardnumber TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, \
            cardname VARCHAR(50), pokemon VARCHAR(20), rarity VARCHAR(13), cardtype VARCHAR(17))")

    # Populates the EvolutionsSet table
    for x in range(evoSet.numCards):
        mycursor.execute("INSERT INTO EvolutionsSet (cardname, pokemon, rarity, cardtype) VALUES(%s, %s, %s, %s)",
                         (evoSet.cardnamelist[x], evoSet.pokemonlist[x], evoSet.rarity[x], evoSet.cardtype[x]))

    # Creates a new table EvolutionsCards that will hold the values in the evoCards EvolutionsSet object
    mycursor.execute("CREATE TABLE EvolutionsCards (cardnumber TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT, \
            FOREIGN KEY(cardnumber) REFERENCES EvolutionsSet(cardnumber), \
            hashes VARCHAR(20), hashesmir VARCHAR(20), hashesud VARCHAR(20), hashesudmir VARCHAR(20))")

    # Populates the EvolutionsCards table
    for x in range(evoCards.setSize):
        mycursor.execute(
            "INSERT INTO EvolutionsCards (hashes, hashesmir, hashesud, hashesudmir) VALUES(%s, %s, %s, %s)",
            (evoCards.hashes[x], evoCards.hashesmir[x], evoCards.hashesud[x], evoCards.hashesudmir[x]))

    # Commits changes to the database
    db.commit()
