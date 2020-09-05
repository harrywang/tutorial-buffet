This repo contains a set of data analysis tutorials in Python curated by me. I modified most of the tutorials to add more instructions and make sure they work well in configured virtual environments. Many thanks to the tutorial authors and other contributors. See the README in each tutorial folder for details.  

## Setup

Each tutorial may have different version requirements for certain packages. So, each tutorial will use a separate virtual environment. 

To run each tutorial, you need to do the following at the root of this project - I use `document_clustering` tutorial as an example:

```
cd document_clustering
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, you can use `jupyter notebook` or use VSCode `code .` to open the notebooks.
