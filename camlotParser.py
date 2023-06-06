import camelot

tables = camelot.read_pdf("piano-syllabus-2022.pdf", pages="all")

for table in tables:
  if table.parsing_report["accuracy"] > 90:
    print(table.df)