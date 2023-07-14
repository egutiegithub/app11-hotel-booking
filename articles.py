import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id":str})

class BuyArticle():
    def __init__(self, article_id):
        self.article_id = article_id
        self.article = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def print_receip(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")

        print(f"""
        Receip nr. {self.article_id}
        Article: {self.article}
        Price: {self.price}
        """)

print(df)
article_id = input("Choose an article to buy: ")
buy_article = BuyArticle(article_id)
buy_article.print_receip()
