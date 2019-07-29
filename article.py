from abc import ABC, abstractmethod


class Article(ABC):

    def __init__(self, product_number, product_name, product_description, color, texture, material, sex, brand, style, pattern):
        self.product_number = product_number
        self.product_name = product_name
        self.product_description = product_description
        self.color = color
        self.texture = texture
        self.material = material
        self.sex = sex
        self.brand = brand
        self.style = style
        self.pattern = pattern
        super().__init__()

    # Get methods:

    def getProductNumber(self):
        return self.product_number

    def getProductName(self):
        return self.product_name

    def getProductDescription(self):
        return self.product_description

    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture

    def getMaterial(self):
        return self.material

    def getSex(self):
        return self.sex

    def getBrand(self):
        return self.brand

    def getStyle(self):
        return self.style

    def getPattern(self):
        return self.pattern

    # Set Methods:
    def setProductNumber(self, product_number):
        self.product_number = product_number

    def setProductName(self, product_name):
        self.product_name = product_name

    def setProductDescription(self, product_description):
        self.product_description = product_description

    def setColor(self, color):
        self.color = color

    def setTexture(self, texture):
        self.texture = texture

    def setMaterial(self, material):
        self.material = material

    def setSex(self, sex):
        self.sex = sex

    def setBrand(self, brand):
        self.brand = brand

    def setStyle(self, style):
        self.style = style

    def setPattern(self, pattern):
        self.pattern = pattern
