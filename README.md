This is a repo for the notes and demos in the June 12, 2017 Intro and Mastering Python courses...

Use the appropriate pip or pip3 to install these below.

You may need to upgrade pip before proceeding:

    pip install --upgrade pip

Windows users - you'll have to install LAPACK/BLAS binaries first:

    https://www.scipy.org/scipylib/building/windows.html
    
I ended up installing mingw-64 from win-builds:

    http://win-builds.org/doku.php/download_and_installation_from_windows

Pandas is a library that makes it easy to read/write spreadsheet-style data in a number of different formats like CSV.
XLRD reads binary Excel .xls files

NumPy has a lot of numerical methods, including statistical and probability methods.

MatPlotLib creates plots, with data formats that are produced from Pandas and NumPy

NLTK is the Natural Language Tool Kit, which has a lot of support for processing text into ways that help with sentiment analysis, semantic meaning, and other text-processing basics.

GenSim assists in the semantic meaning and structure

SciKit-Learn has a number of key machine learning algorithms

IPython is a great way to exploit all of these together. Combine it with a notebook product for a rocking web interface.

	pip install pandas
	pip install xlrd
	pip install numpy
	pip install matplotlib
	pip install nltk
    pip install gensim
    pip install scikit-learn
	pip install ipython

You can also cram them all on the same command line:

    pip install pandas xlrd numpy matplotlib nltk gensim scikit-learn ipython

Once you've done these installs, download the nltk data sets:
(This takes several gigabytes!)

    python -c "import nltk; nltk.download('all')"

Requests is an HTTP library, great for REST requests. 
http://www.python-requests.org/en/master/

Scrapy helps web page scraping
https://scrapy.org/

	pip install requests
	pip install scrapy

Pillow is a fork of the PIL - Python Imaging Library. You can parse and manipulate most graphic file formats with this library, including using the numerical data as a 2-dimensional array. Many vision-based machine learning systems will use either PIL or Pillow.
https://python-pillow.org/

	pip install pillow

Nose is a Unit Testing Framework for Python. Professional developers test their code mechanically. Amateurs don't. It's one of the clearest differentiators.

    pip install nose
    
Paramiko is an SSH/SFTP/SCP library (May need OpenSSL?)
http://www.paramiko.org/

    pip install paramiko

SymPy is a symbolic math library

    http://sympy.org

