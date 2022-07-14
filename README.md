Pokémon Card Scanner
=========================
This repository contains Python code for a Pokémon card scanner and identifier for any card in the [Evolutions Pokémon set](https://bulbapedia.bulbagarden.net/wiki/Evolutions_%28TCG%29).  

The code first starts by defining whether the input is a live video or a saved image. If live video is chosen, the computer's second webcam is used which can be connected to a smart phone using the `Iriun Webcam` app.  

Using the `OpenCV` library, we can get a normalized scan (think PDF scanner apps) of the Pokémon card in the feed by doing the following:
 1. Taking in a single image or video feed
 2. Finding edges in the image/frame
 3. Finding the biggest contour that is a rectangle
 4. Finding the corners of the biggest contour
 5. Identifying which corner is which (i.e. reordering the corners to ensure that they are in the order: topLeft, topRight, bottomLeft, bottomRight)
 6. Creating a transformation matrix based on the original corners to transform the image / frame of the card into a vertical rectangle   
   
It then gets the hashes (average hash, whash, phash, dhash) of the scanned card using the `ImageHash` library and compares these hashes to their counterparts for each card in the Evolutions set by finding the distance between these hashes. By using four different hashing methods, we can reduce the margin of error that only using one may introduce.  A smaller distance is indicative of more cards being more similar. A cutoff value is defined so as if a hash distance is smaller than it, we can assume the images are similar. 

These hashes are stored in the `EvolutionsCards` table of the `pokemoncarddatabase` MySQL database, which is created through the `cardData.createDatabase()` and `cardData.initializeDatabase()` function calls.  
  
This database stores information in three tables: **Pokemon**, **EvolutionsCards**, and **EvolutionsSet**. These tables hold the following data:  

**Pokémon**:
|  dexnumber | pokemon | type | stage | height |
|--|--|--|--|--|

**EvolutionsSet**:
|  cardnumber| cardname| pokemon| rarity| cardtype|
|--|--|--|--|--|

**EvolutionsCards**:
|  cardnumber| avghashes| avghashesmir| avghashesud| avghashesmirud| whashes | whashesmir | whashesud | whashesmirud | phashes | phashesmir | phashesud | phashesmirud | dhashes | dhashesmir | dhashesud | dhashesmirud |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|  

*Note: The **EvolutionsCards** table has four hashes saved for each hashing method, representing different orientations the card may be in (normal, mirrored, upside down, mirrored & upside down) to ensure that a card can be scanned no matter its orientation.*
  
If a similar card is found, information on said card is printed to the console. If the code was using a live feed, it is aborted.
