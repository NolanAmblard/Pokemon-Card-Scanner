import mysql.connector
import cardSet
import pokedex
import evolutionsSet

username = "########"  # Your mysql username
password = "########"  # Your mysql password
databasename = "pokemoncards"  # name of database we want to create


def createDatabase():
    db = mysql.connector.connect(
        host="localhost",
        user=username,
        passwd=password
    )

    mycursor = db.cursor()

    mycursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'pokemoncards'")
    if mycursor.fetchone() is None:
        mycursor.execute("CREATE DATABASE pokemoncards")

    initializeDatabase()


def initializeDatabase():
    db = mysql.connector.connect(
        host="local",
        user=username,
        passwd=password,
        database="pokemoncards"
    )

    mycursor = db.cursor()

    evolutionsSet = cardSet.CardSet()

    mycursor.execute("CREATE TABLE EvolutionsSet (cardnumber smallint PRIMARY KEY AUTO_INCREMENT, \
        cardname VARCHAR(50), pokemon VARCHAR(11), rarity VARCHAR(13), cardtype VARCHAR(17))")

    mycursor.execute("CREATE TABLE EvolutionsCards (cardnumber smallint PRIMARY KEY, FOREIGN KEY(cardnumber) REFERENCES EvolutionsSet(cardnumber), \
        hash VARCHAR(20), hashmir VARCHAR(20), hashud VARCHAR(20), hashudmir VARCHAR(20))")

    mycursor.execute("CREATE TABLE EvolutionsPokemon (id smallint PRIMARY KEY AUTO_INCREMENT, pokemon VARCHAR, \
        FOREIGN KEY(pokemon) REFERENCES EvolutionsSet(pokemon), \
        type VARCHAR(10), height smallint UNSIGNED, weight smallint UNSIGNED, stage VARCHAR(5))")

    mycursor.executemany("INSERT INTO EvolutionsSet (cardname, pokemon, rarity) VALUES(%s, %s, %s, %s)", \
                         evolutionsSet.cardnamelist, evolutionsSet.pokemonlist, evolutionsSet.rarity,
                         evolutionsSet.cardtype)

    db.commit()
