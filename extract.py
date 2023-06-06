from py_pdf_parser.loaders import load_file
from py_pdf_parser.visualise import visualise

doc = load_file("piano-syllabus-2022.pdf")


def getScales():  
  scales = doc.elements.filter_by_text_equal("Four-octave")
  return scales

def getThirds():
  thirds = doc.elements.filter_by_text_equal("Separated by a 3rd")
  return thirds

def getSixths():
  sixths = doc.elements.filter_by_text_equal("Separated by  a 6th")
  return sixths

def getOctaves(): 
  octaves = doc.elements.filter_by_text_contains("In Octaves")
  return octaves

def getChromaticOctaves():
  chromaticOctaves = doc.elements.filter_by_text_equal("Chromatic in Octaves")
  return chromaticOctaves

def  getTonic4NoteChords():
  chords = 

def getText(element):
    texts = doc.elements.to_the_right_of(element)
    return [text.text() for text in texts]

for s in getOctaves():
    print(getText(s))
