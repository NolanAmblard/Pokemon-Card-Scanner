import numpy as np
import imagehash
from PIL import Image, ImageOps


class EvolutionsSet:
    def __init__(self):
        self.setSize = 113  # Number of cards in Evolutions

        self.hashes = self.getHashes('hash') # Gets hashes of normal cards
        self.hashesmir = self.getHashes('hashmir') # Gets hashes of mirrored cards
        self.hashesud = self.getHashes('hashud') # Gets hashes of upside down cards
        self.hashesudmir = self.getHashes('hashudmir') # Gets hashes of mirrored upside down cards

    # Gets hashes of all cards in Evolutions set
    def getHashes(self, type):
        arr = np.empty((self.setSize, 4), dtype=object)
        for i in range(1, self.setSize + 1):
            filename = 'evolutionsCardsImages/' + str(i).rjust(3, '0') + '.png'
            img = Image.open(filename)
            match type:
                case 'hash':
                    arr[i - 1][0] = str(imagehash.average_hash(img))
                    arr[i - 1][1] = str(imagehash.whash(img))
                    arr[i - 1][2] = str(imagehash.phash(img))
                    arr[i - 1][3] = str(imagehash.dhash(img))
                case 'hashmir':
                    imgmir = ImageOps.mirror(img)
                    arr[i - 1][0] = str(imagehash.average_hash(imgmir))
                    arr[i - 1][1] = str(imagehash.whash(imgmir))
                    arr[i - 1][2] = str(imagehash.phash(imgmir))
                    arr[i - 1][3] = str(imagehash.dhash(imgmir))
                case 'hashud':
                    imgflip = ImageOps.flip(img)
                    arr[i - 1][0] = str(imagehash.average_hash(imgflip))
                    arr[i - 1][1] = str(imagehash.whash(imgflip))
                    arr[i - 1][2] = str(imagehash.phash(imgflip))
                    arr[i - 1][3] = str(imagehash.dhash(imgflip))
                case 'hashudmir':
                    imgmirflip = ImageOps.flip(ImageOps.mirror(img))
                    arr[i - 1][0] = str(imagehash.average_hash(imgmirflip))
                    arr[i - 1][1] = str(imagehash.whash(imgmirflip))
                    arr[i - 1][2] = str(imagehash.phash(imgmirflip))
                    arr[i - 1][3] = str(imagehash.dhash(imgmirflip))
        return arr
