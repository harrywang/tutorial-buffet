This repo contains a set of AI and Data Science tutorials in Python curated and revised by me. I modified most of the tutorials to add more instructions and make sure they work well in configured virtual environments. Many thanks to the tutorial authors and other contributors. See the README in each tutorial folder for details.  

## Setup

Each tutorial may have different version requirements for certain packages. So, each tutorial will use a separate virtual environment. 

For some tutorials, you may need to set API keys. You need to add a `.env` file and include the API keys as follows (see my blog post on [Manage Environment Variables in Python Projects](https://harrywang.me/env)):

```
OPENAI_API_KEY=sk-proj-xxxx
LANGCHAIN_API_KEY=ls__69650xxxx
REPLICATE_API_TOKEN=r8_W0V3rJxxx
```

To run each tutorial, you need to do the following at the root of this project - I use `document_clustering` tutorial as an example:

```
cd document_clustering
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, you can use VSCode `code .` to open the notebooks.
