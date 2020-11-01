from fpdf import FPDF
import os


class PDF(FPDF):


    # def chapter_title(self, num, label):
    #     # Arial 12
    #     self.set_font('Arial', '', 12)
    #     # Background color
    #     self.set_fill_color(200, 220, 255)
    #     # Title
    #     self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
    #     # Line break
    #     self.ln(4)

    def chapter_body(self):
        # Read text file
        with open('text/assignment1.txt', 'rb') as fh:
            txt = fh.read().decode('latin-1')
        # Times 12
        self.set_font('khand', '', 12)
        self.set_text_color(0,0,150)
        # self.set_font
        # Output justified text
        self.multi_cell(0, 5, txt)
        # Line break
        self.ln()
        # Mention in italics
        # self.set_font('khand', 12)
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self):
        self.add_page()
        # self.chapter_title(num, title)
        self.chapter_body()

def handwriter():

    pdf = PDF()
    # pdf.set_title(title)
    pdf.add_font('khand', '', 'khand.ttf',uni=True)
    # pdf.add_font
    # pdf.set_author('UK')
    pdf.print_chapter()
    # pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
    pdf.output('handwritten.pdf', 'F')
