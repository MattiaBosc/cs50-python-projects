from fpdf import FPDF, Align

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_auto_page_break(False)
pdf.set_margins(left=20, top=20, right=20)
pdf.set_font("Courier", "B", 40)
pdf.cell(h=30, text="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", x=Align.C, y=70, w=pdf.epw)
pdf.ln(110)
pdf.set_text_color(255, 255, 255)
pdf.set_font("Helvetica", size=20)
pdf.cell(text=f"{name} took CS50", center=True)
pdf.output("shirtificate.pdf")

