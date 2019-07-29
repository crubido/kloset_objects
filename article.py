from abc import ABC, abstractmethod


class Article(ABC):

    def __init__(self, product_number, product_name, product_description, color, texture, material, sex, brand, style, pattern):
        self.__product_number = product_number
        self.__product_name = product_name
        self.__product_description = product_description
        self.__color = color
        self.__texture = texture
        self.__material = material
        self.__sex = sex
        self.__brand = brand
        self.__style = style
        self.__pattern = pattern

    # Get methods:
    def getProductNumber(self):
        return self.__product_number

    def getProductName(self):
        return self.__product_name

    def getProductDescription(self):
        return self.__product_description

    def getColor(self):
        return self.__color

    def getTexture(self):
        return self.__texture

    def getMaterial(self):
        return self.__material

    def getSex(self):
        return self.__sex

    def getBrand(self):
        return self.__brand

    def getStyle(self):
        return self.__style

    def getPattern(self):
        return self.__pattern

    # Set Methods:
    def setProductNumber(self, product_number):
        self.__product_number = product_number

    def setProductName(self, product_name):
        self.__product_name = product_name

    def setProductDescription(self, product_description):
        self.__product_description = product_description

    def setColor(self, color):
        self.__color = color

    def setTexture(self, texture):
        self.__texture = texture

    def setMaterial(self, material):
        self.__material = material

    def setSex(self, sex):
        self.__sex = sex

    def setBrand(self, brand):
        self.__brand = brand

    def setStyle(self, style):
        self.__style = style

    def setPattern(self, pattern):
        self.__pattern = pattern


class Tops(Article):

    def __init__(self, product_number, product_name, product_description, color, texture, material, sex, brand, style, pattern):
        Article.__init__(self, product_number, product_name, product_description,
                         color, texture, material, sex, brand, style, pattern)
