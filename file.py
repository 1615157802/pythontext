import os
import tkinter
import tkinter as tk
from logging import root

import fitz
from PIL import Image,ImageTk


class PDFViewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.pdf_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.pdf')])

        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.page_num = 1
        self.label = tk.Label(self.frame, text='Page 1')
        self.label.pack()

        self.canvas = tk.Canvas(self.frame, width=700, height=900)
        self.canvas.pack()
        self.prev_button = tk.Button(self.frame, text='Previous Page', command=self.prev_page)
        self.prev_button.pack(side='left')

        self.next_button = tk.Button(self.frame, text='Next Page', command=self.next_page)
        self.next_button.pack(side='right')

        self.load_pdf()

        self.root.mainloop()

    def load_pdf(self):
        # pdf_path = os.path.join(self.folder_path, self.pdf_files[self.page_num-1])
            #with open(pdf_path, 'rb') as f:
            #pdf_reader = PyPDF2.PdfReader(f)
            #page = pdf_reader.pages[0]
            #text = page.extract_text()

            #self.textbox = tk.Text(self.frame)
            #self.textbox.insert('end', text)
            #self.textbox.pack()
        pdf_folder = "C:\\Users\\sunson\\AppData\\Local\\Temp\\music21"
        for file in os.listdir(pdf_folder):
            if file.endswith(".pdf"):
                pdf_files = os.path.join(pdf_folder, file)
                pdf_doc = fitz.open(pdf_files)
                print(pdf_doc)
                for pg in range(0,pdf_doc.page_count):
                   print(pg)
                   #page = pdf_doc[page_index]
                   #pix = page.get_pixmap()
                   #img = tkinter.Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                   #img.show()
                   page = pdf_doc[pg]
                   print(page)
                   pix= page.get_pixmap()
                   print(pix)
                   img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                   print(img)
                   #img.show()
                   imgtk= ImageTk.PhotoImage(image=img)
                   print(repr(imgtk))
                   self.canvas.imgtk = imgtk
                   self.canvas.create_image(0, 0, anchor='nw', image=imgtk)
    def prev_page(self):
        if self.page_num > 1:
            self.page_num -= 1
            self.label.configure(text='Page {}'.format(self.page_num))
            self.load_pdf()

    def next_page(self):
        if self.page_num < len(self.pdf_files):
            self.page_num += 1
            self.label.configure(text='Page {}'.format(self.page_num))
            self.load_pdf()

if __name__ == '__main__':
    viewer = PDFViewer('C:\\Users\\sunson\\AppData\\Local\\Temp\\music21')
