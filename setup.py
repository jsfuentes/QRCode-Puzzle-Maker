from distutils.core import setup
setup(
    name = "qrcode_puzzle_maker",
    packages = ["qrcode_puzzle_maker"],
    version = "1.0",
    description = "Takes a qrcode and generates the words to make a puzzle",
    author = "Jorge Fuentes",
    author_email = "jsjfuentes@ucla.edu",
    install_requires = [
        "pillow",
    ],
    download_url = "https://github.com/jsfuentes/QRCode-Puzzle-Maker",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 4 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ])
