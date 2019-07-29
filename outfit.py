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
        return [self.__bottom.getProductNumber(), self.__bottom.getProductName(), self.__bottom.getProductDescription(), self.__bottom.getColor(), self.__bottom.getTexture(), self.__bottom.getMaterial(), self.__bottom.getSex(), self.__bottom.getBrand(), self.__bottom.getStyle(), self.__bottom.getPattern()]

    def getShoeware(self):
        return [self.__shoeware.getProductNumber(), self.__shoeware.getProductName(), self.__shoeware.getProductDescription(), self.__shoeware.getColor(), self.__shoeware.getTexture(), self.__shoeware.getMaterial(), self.__shoeware.getSex(), self.__shoeware.getBrand(), self.__shoeware.getStyle(), self.__shoeware.getPattern()]

    def getAccesory(self):
        return [self.__accesory.getProductNumber(), self.__accesory.getProductName(), self.__accesory.getProductDescription(), self.__accesory.getColor(), self.__accesory.getTexture(), self.__accesory.getMaterial(), self.__accesory.getSex(), self.__accesory.getBrand(), self.__accesory.getStyle(), self.__accesory.getPattern()]

    def getFullbody(self):
        return [self.__fullbody.getProductNumber(), self.__fullbody.getProductName(), self.__fullbody.getProductDescription(), self.__fullbody.getColor(), self.__fullbody.getTexture(), self.__fullbody.getMaterial(), self.__fullbody.getSex(), self.__fullbody.getBrand(), self.__fullbody.getStyle(), self.__fullbody.getPattern()]

    def getIdNum(self):
        return self.idNum

    def getOutfit(self):
        return {"Outfit ID": self.getIdNum(), "Top": self.getTop(), "Bottom": self.getBottom(), "Shoeware": self.getShoeware(), "Accesory": self.getAccesory(), "Full Body": self.getFullbody()}
    # Set methods
