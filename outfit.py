class Outfit (object):
    nextOutfitIdNum = 0

    def __init__(self, top, bottom, shoeware, accesory, fullbody):
        self.__top = top
        self.__bottom = bottom
        self.__shoeware = shoeware
        self.__accesory = accesory
        self.__fullbody = fullbody
        self.idNum = Outfit.nextOutfitIdNum
        Outfit.nextOutfitIdNum += 1

    # Get methods:
    def getTop(self):
        return [self.__top.getProductNumber(), self.__top.getProductName(), self.__top.getProductDescription(), self.__top.getColor(), self.__top.getTexture(), self.__top.getMaterial(), self.__top.getSex(), self.__top.getBrand(), self.__top.getStyle(), self.__top.getPattern()]

    def getBottom(self):
        return self.__bottom

    def getShoeware(self):
        return self.__shoeware

    def getAccesory(self):
        return self.__accesory

    def getFullbody(self):
        return self.__fullbody

    # Set methods

    def getIdNum(self):
        return self.idNum
