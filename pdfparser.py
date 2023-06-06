from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise

doc = load_file("piano-syllabus-2022.pdf")
visualise(doc)
