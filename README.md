# HuMaIN (Human- and Machine-Intelligent Network)

### Scripts developed for the paper titled "*Cooperative Human-Machine Data Extraction from Biological Collections*":
  - [damerauCmpDir.py](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/damerauCmpDir.py) : It compares the files in two folders, returning the normalized Damerau-Levenshtein distance for each common file. The Damerau-Levenshtein used is the developed by Geoffrey Fairchild and available at [https://github.com/gfairchild/pyxDamerauLevenshtein](https://github.com/gfairchild/pyxDamerauLevenshtein).
  - [jaroCmpDir.py](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/jaroCmpDir.py) : It compares the files in two folders, returning the normalized Jaro-Winkler distance for each common file. The Jaro-Winkler implementation is the available at [https://pypi.python.org/pypi/jellyfish](https://pypi.python.org/pypi/jellyfish).
  - [eqCmpDir.py](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/eqCmpDir.py) : It compares the files in two folders, returning the percentage of words in file 1 which are also present in file 2.
  - [img2txt.py](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/img2txt.py) : Script which executes the OCRopy OCR process (Binarization, Segmentation, and Recognition). Please configure dirOcropy variable to indicate the OCRopus path.
  - [ocrFolder.py](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/ocrFolder.py) : Script which executes the img2txt (OCR) script to each jpg file available at the input folder.

### License
Apache 2.0 ([read License](https://github.com/acislab/HuMaIN_Collaborative_Data_Extraction/blob/master/LICENSE))

Icaro Alzuru  (August - 2016)
