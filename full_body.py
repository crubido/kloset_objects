from article import Article


class Fullbody (Article):
    def __init__(self, product_number, product_name, product_description, color, texture, material, sex, brand, style, pattern):
        Article.__init__(self, product_number, product_name, product_description,
                         color, texture, material, sex, brand, style, pattern)
