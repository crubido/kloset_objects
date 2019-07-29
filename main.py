from article import Article
from tops import Tops
from bottons import Bottons
from accesories import Accessories
from full_body import Fullbody
from shoewear import Shoewear


def main():
    tShirt = Tops("637387222", "Tretch Muscle Fit Polo", "A comfortable, cotton-blend polo made with stretch, featuring an icon at left chest. Designed in a muscle-defining, super slim fit through the chest, waist and arms. Muscle Fit. Imported",
                  "White", "Flat", "Cotton", "Male", "Hollister", "Classic", "N/A")

    def getItemInList():
        ItemDict = {}
        ItemDict["Product Number"] = tShirt.getProductNumber()
        ItemDict["Product Name"] = tShirt.getProductName()
        ItemDict["Product Description"] = tShirt.getProductDescription()
        ItemDict["Color"] = tShirt.getColor()
        ItemDict["Texture"] = tShirt.getTexture()
        ItemDict["Material"] = tShirt.getMaterial()
        ItemDict["Sex"] = tShirt.getSex()
        ItemDict["Brand"] = tShirt.getBrand()
        ItemDict["Style"] = tShirt.getStyle()
        ItemDict["Pattern"] = tShirt.getPattern()

        print(ItemDict)

    getItemInList()


if __name__ == "__main__":
    main()
