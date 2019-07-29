from tops import Tops
from bottons import Bottons
from shoewear import Shoewear
from accesories import Accessories
from full_body import Fullbody


class Outfit (Tops, Bottons, Shoewear, Accessories):
    nextOutfitIdNum = 0

    def __init__(self, product_number, product_name, product_description, color, texture, material, sex, brand, style, pattern):
        Tops.__init__(self, product_number, product_name, product_description,
                      color, texture, material, sex, brand, style, pattern)
        Bottons.__init__(self, product_number, product_name, product_description,
                         color, texture, material, sex, brand, style, pattern)
        Shoewear.__init__(self, product_number, product_name, product_description,
                          color, texture, material, sex, brand, style, pattern)
        Accessories.__init__(self, product_number, product_name, product_description,
                             color, texture, material, sex, brand, style, pattern)
        Fullbody.__init__(self, product_number, product_name, product_description,
                          color, texture, material, sex, brand, style, pattern)
        self.idNum = Outfit.nextOutfitIdNum

    # Get the idNum of an outfit:
    def getIdNum(self):
        return self.idNum
