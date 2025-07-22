import PyPDF2
import os

def merge_pdfs(folder_path, output_filename="merged.pdf"):
    merger = PyPDF2.PdfMerger()
    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".pdf"):
            merger.append(os.path.join(folder_path, file))
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    merge_pdfs(".")