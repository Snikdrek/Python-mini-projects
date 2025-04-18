import PyPDF2
import os

directory = input("Enter the directory containing PDF files: ")
os.chdir(directory)
merger = PyPDF2.PdfMerger()  # Create a PdfMerger object

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)  # Add the file to the list

merger.write("merged.pdf")  # Write the merged file to disk
merger.close()  # Close the merger object