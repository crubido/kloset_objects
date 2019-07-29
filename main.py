from article import Article
from tops import Tops
from bottons import Bottons
from accesories import Accessories
from full_body import Fullbody
from shoewear import Shoewear
from outfit import Outfit


def main():
    tShirt = Tops("637387222", "Tretch Muscle Fit Polo", "A comfortable, cotton-blend polo made with stretch, featuring an icon at left chest. Designed in a muscle-defining, super slim fit through the chest, waist and arms. Muscle Fit. Imported",
                  "White", "Flat", "Cotton", "Male", "Hollister", "Classic", "N/A")
    short = Bottons("001987623", "Minimal pink short", "Minimalistic and moder short great for the summer",
                    "Pink", "Flat", "Cotton", "Male", "Hollister", "Modern", "N/A")
    toms = Shoewear("908876789", "Ericsons", "Gret comfort toms ideal for hot climates",
                    "White", "Flat", "Polyester", "Unisex", "Toms", "Modern", "N/A")

    acc = Accessories("099897789", "Leo Dimond ring", "2k white gold luxury ring",
                      "Silver", "N/A", "N/A", "Male", "Leo Dimond", "Classic", "N/A")

    suit = Fullbody("N/A", "N/A", "N/A", "N/a", "N/A",
                    "N/A", "N/A", "N/A", "N/A", "N/A")

    firstOutfit = Outfit(tShirt, short, toms, acc, suit)

    def getItemInList():
        topDict = {}
        topDict["Product Number"] = tShirt.getProductNumber()
        topDict["Product Name"] = tShirt.getProductName()
        topDict["Product Description"] = tShirt.getProductDescription()
        topDict["Color"] = tShirt.getColor()
        topDict["Texture"] = tShirt.getTexture()
        topDict["Material"] = tShirt.getMaterial()
        topDict["Sex"] = tShirt.getSex()
        topDict["Brand"] = tShirt.getBrand()
        topDict["Style"] = tShirt.getStyle()
        topDict["Pattern"] = tShirt.getPattern()

        bottomDict = {}
        bottomDict["Product Number"] = short.getProductNumber()
        bottomDict["Product Name"] = short.getProductName()
        bottomDict["Product Description"] = short.getProductDescription()
        bottomDict["Color"] = short.getColor()
        bottomDict["Texture"] = short.getTexture()
        bottomDict["Material"] = short.getMaterial()
        bottomDict["Sex"] = short.getSex()
        bottomDict["Brand"] = short.getBrand()
        bottomDict["Style"] = short.getStyle()
        bottomDict["Pattern"] = short.getPattern()

        print(topDict)
        print(bottomDict)

    getItemInList()
    print(firstOutfit.getTop())


if __name__ == "__main__":
    main()
