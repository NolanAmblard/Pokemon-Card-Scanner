import numpy as np
import imagehash
from PIL import Image, ImageOps


# Gets the average hash, whash, phash, & dhash for each card in the set in each orientation for a total of 16 hashes
# Four different hash methods are used to reduce potential for error in using only one hashing method
class EvolutionsSet:
    def __init__(self):
        self.setSize = 113  # Number of cards in Evolutions

        self.hashes = self.getHashes('hash')  # Gets hashes of normally oriented cards
        self.hashesmir = self.getHashes('hashmir')  # Gets hashes of mirrored cards
        self.hashesud = self.getHashes('hashud')  # Gets hashes of upside down cards
        self.hashesudmir = self.getHashes('hashudmir')  # Gets hashes of mirrored upside down cards

    # Gets hashes of all cards in Evolutions set
    def getHashes(self, type):
        # Create an array with self.setSize rows and 4 columns. Each column represents a different hashing method
        arr = np.empty((self.setSize, 4), dtype=object)
        # Loop through each card image
        for i in range(1, self.setSize + 1):
            filename = 'evolutionsCardsImages/' + str(i).rjust(3, '0') + '.png'
            img = Image.open(filename)
            match type:
                # For each case, find the average hash, whash, phash, & dhash of the image & convert it to a string
                case 'hash':  # Normally oriented card
                    arr[i - 1][0] = str(imagehash.average_hash(img))
                    arr[i - 1][1] = str(imagehash.whash(img))
                    arr[i - 1][2] = str(imagehash.phash(img))
                    arr[i - 1][3] = str(imagehash.dhash(img))
                case 'hashmir':  # Mirrored card
                    imgmir = ImageOps.mirror(img)
                    arr[i - 1][0] = str(imagehash.average_hash(imgmir))
                    arr[i - 1][1] = str(imagehash.whash(imgmir))
                    arr[i - 1][2] = str(imagehash.phash(imgmir))
                    arr[i - 1][3] = str(imagehash.dhash(imgmir))
                case 'hashud':  # Upside down card
                    imgflip = ImageOps.flip(img)
                    arr[i - 1][0] = str(imagehash.average_hash(imgflip))
                    arr[i - 1][1] = str(imagehash.whash(imgflip))
                    arr[i - 1][2] = str(imagehash.phash(imgflip))
                    arr[i - 1][3] = str(imagehash.dhash(imgflip))
                case 'hashudmir':  # Upside down & mirrored card
                    imgmirflip = ImageOps.flip(ImageOps.mirror(img))
                    arr[i - 1][0] = str(imagehash.average_hash(imgmirflip))
                    arr[i - 1][1] = str(imagehash.whash(imgmirflip))
                    arr[i - 1][2] = str(imagehash.phash(imgmirflip))
                    arr[i - 1][3] = str(imagehash.dhash(imgmirflip))
        return arr  # Return self.setSize x 4 array of image hashes for selected orientation
