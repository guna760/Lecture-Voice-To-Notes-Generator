from fpdf import FPDF

def create_pdf(notes):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, notes)

    pdf.output("outputs/notes.pdf")