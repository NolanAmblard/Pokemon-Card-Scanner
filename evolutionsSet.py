import numpy as np
import imagehash
from PIL import Image, ImageOps


class EvolutionsSet:
    def __init__(self):
        self.setSize = 113  # Number of cards in Evolutions

        self.hashes = self.getHashes(self, 'hash') # Gets hashes of normal cards
        self.hashesmir = self.getHashes(self, 'hashmir') # Gets hashes of mirrored cards
        self.hashesud = self.getHashes(self, 'hashud') # Gets hashes of upside down cards
        self.hashesudmir = self.getHashes(self, 'hashudmir') # Gets hashes of mirrored upside down cards

    # Gets hashes of all cards in Evolutions set
    def getHashes(self, type):
        arr = np.empty(self.setSize, dtype=object)
        for i in range(1, self.setSize + 1):
            filename = 'evolutionsCardsImages/' + str(i).rjust(3, '0') + '.png'
            match type:
                case 'hash':
                    arr[i - 1] = imagehash.average_hash(Image.open(filename))
                case 'hashmir':
                    arr[i - 1] = imagehash.average_hash(ImageOps.mirror(Image.open(filename)))
                case 'hashud':
                    arr[i - 1] = imagehash.average_hash(ImageOps.flip(Image.open(filename)))
                case 'hashudmir':
                    arr[i - 1] = imagehash.average_hash(ImageOps.flip(ImageOps.mirror(Image.open(filename))))
        return arr
