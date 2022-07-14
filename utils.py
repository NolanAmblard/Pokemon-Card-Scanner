import cv2
import numpy as np
import math
from PIL import Image
import imagehash
import cardData


# Returns the corners & area of the biggest contour
def biggestContour(contours):
    biggest = np.array([])
    maxArea = 0
    for i in contours:  # Loop through contours
        area = cv2.contourArea(i)  # Get area of contour
        if area > 5000:
            peri = cv2.arcLength(i, True)  # Get perimeter of contour
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)  # Gets number of sides of contour
            if area > maxArea and len(approx) == 4:  # If area of contour is > than current max & contour is a rectangle
                biggest = approx
                maxArea = area
    return biggest, maxArea


# Returns corners in order [topleft, topright, bottomleft, bottomright]
# This is meant to return a vertical image no matter the card orientation, but the result may be upside-down or mirrored
def reorderCorners(corners):
    # Copy corner values into xvals and yvals
    xvals = [corners[0][0], corners[1][0], corners[2][0], corners[3][0]]
    yvals = [corners[0][1], corners[1][1], corners[2][1], corners[3][1]]

    # Sort yvals and get indexes of original values in sorted array
    yvals, idxs = sortVals(yvals)

    # Change xvals to same order as yvals
    temp = xvals.copy()
    for i in range(len(idxs)):
        xvals[i] = temp[idxs[i]]

    # Check if card is horizontal or vertical and make sure [0, 0] is point closest to top left of image (smallest x)
    if yvals[0] == yvals[1]:
        if xvals[1] < xvals[0]:
            # yvals are same so only swap xvals
            tempx = xvals[0]
            xvals[0] = xvals[1]
            xvals[1] = tempx

    # Find distance from corner with min y to corners
    dist1 = math.sqrt((xvals[1] - xvals[0]) ** 2 + (yvals[1] - yvals[0]) ** 2)
    dist2 = math.sqrt((xvals[2] - xvals[0]) ** 2 + (yvals[2] - yvals[0]) ** 2)
    dist3 = math.sqrt((xvals[3] - xvals[0]) ** 2 + (yvals[3] - yvals[0]) ** 2)
    dists = [dist1, dist2, dist3]

    # Sort distances and get indexes of original values in sorted array
    distSorted, idxsDist = sortVals(dists.copy())

    # Reformat index array to be 4 values, not necessary but makes code easier to read
    idxsDist.insert(0, 0)
    idxsDist[1] += 1
    idxsDist[2] += 1
    idxsDist[3] += 1

    # Check if card is vertical/horizontal
    if yvals[0] == yvals[1]:
        if dists[0] == distSorted[0]:  # If card is vertical; corner [0, 0] is top left of card
            topleft = [xvals[idxsDist[0]], yvals[idxsDist[0]]]  # Same as [xvals[0], yvals[0]]
            topright = [xvals[idxsDist[1]], yvals[idxsDist[1]]]
            bottomright = [xvals[idxsDist[3]], yvals[idxsDist[3]]]
            bottomleft = [xvals[idxsDist[2]], yvals[idxsDist[2]]]
        else:  # If card is horizontal; corner [0, 0] is top right of card
            topleft = [xvals[idxsDist[1]], yvals[idxsDist[1]]]
            topright = [xvals[idxsDist[0]], yvals[idxsDist[0]]]
            bottomright = [xvals[idxsDist[2]], yvals[idxsDist[2]]]
            bottomleft = [xvals[idxsDist[3]], yvals[idxsDist[3]]]
    else:  # Else card is tilted in some other orientation
        if xvals[idxsDist[1]] == min(xvals):  # Left-most point is the closest to the point with the smallest y value
            # Left-most point is top left corner
            topleft = [xvals[idxsDist[1]], yvals[idxsDist[1]]]
            topright = [xvals[idxsDist[0]], yvals[idxsDist[0]]]
            bottomright = [xvals[idxsDist[2]], yvals[idxsDist[2]]]
            bottomleft = [xvals[idxsDist[3]], yvals[idxsDist[3]]]
        else:  # Corner [0, 0] is the top left corner
            topleft = [xvals[idxsDist[0]], yvals[idxsDist[0]]]
            topright = [xvals[idxsDist[1]], yvals[idxsDist[1]]]
            bottomright = [xvals[idxsDist[3]], yvals[idxsDist[3]]]
            bottomleft = [xvals[idxsDist[2]], yvals[idxsDist[2]]]

    return [[topleft], [topright], [bottomleft], [bottomright]]


# Returns sorted array and array of indexes of locations of original values
# Selection sort is used as efficieny won't matter as much for n = 3 or 4
def sortVals(vals):
    indexes = list(range(len(vals)))
    for i in range(len(vals)):
        index = i
        minval = vals[i]
        for j in range(i, len(vals)):
            if vals[j] < minval:
                minval = vals[j]
                index = j
        swap(vals, i, index)
        swap(indexes, i, index)
    return vals, indexes


# Swaps the values of at two indexes in the given array
def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


# Compares the average hash of the current frame with the average has of every card in evolutions
# Returns True if a matching card is found and False if not
def findCard(imgWarpColor):
    # Converts image format from OpenCV format to PIL format
    # Converts from Blue Green Red to Red Green Blue image format
    convertedImgWarpColor = cv2.cvtColor(imgWarpColor, cv2.COLOR_BGR2RGB)

    # Gets the average hash value from the frame
    hashes = np.empty(4, dtype=object)
    scannedCard = Image.fromarray(convertedImgWarpColor)
    hashes[0] = imagehash.average_hash(scannedCard)
    hashes[1] = imagehash.whash(scannedCard)
    hashes[2] = imagehash.phash(scannedCard)
    hashes[3] = imagehash.dhash(scannedCard)

    # Compares this hash to a database of hash values for all cards in the Evolutions set
    cardinfo = cardData.compareCards(hashes)

    # If a matching card was found, print its information and return True
    if cardinfo is not None:
        print("Card info: \n-------------------------------")
        print(f"Card Name:          {cardinfo['Card Name']}" )
        print(f"Card Number:        {cardinfo['Card Number']}")
        print(f"Card Rarity:        {cardinfo['Rarity']}")
        print(f"Card Type:          {cardinfo['Card Type']}\n\n")
        print("Pokemon info: \n-------------------------------")
        print(f"Pokemon:            {cardinfo['Pokemon']}")
        print(f"Pokedex Number:     {cardinfo['Pokedex Number']}")
        print(f"Pokemon Card Type:  {cardinfo['Pokemon Type']}")
        print(f"Pokemon Stage:      {cardinfo['Pokemon Stage']}")
        print(f"Pokemon Height (m): {cardinfo['Pokemon Height']}")
        return True
    return False  # If no matching card was found, return False
