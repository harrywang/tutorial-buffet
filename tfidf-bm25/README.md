# About

tfidf and bm25 examples for document retrieval using the Cranfield dataset

"The Cranfield collection. This was the pioneering test collection in allowing precise quantitative measures of information retrieval effectiveness, but is nowadays too small for anything but the most elementary pilot experiments. Collected in the United Kingdom starting in the late 1950s, it contains 1398 abstracts of aerodynamics journal articles, a set of 225 queries, and exhaustive relevance judgments of all (query, document) pairs." -
https://nlp.stanford.edu/IR-book/html/htmledition/standard-test-collections-1.html

## Setup

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Data

The data is in `data` folder in JSON format:
- `cranfield_docs.json`: information about 1400 documents, which are abstracts from papers related to Aeronautics with information about author, bibliography, body (abstract), title:
```
  {

      "id" : 1,
      "author" : "brenckman,m.",
      "bibliography" : "j. ae. scs. 25, 1958, 324.",
      "body" : "experimental investigation of the aerodynamics of a wing in a slipstream .   an experimental study of a wing in a propeller slipstream was made in order to determine the spanwise distribution of the lift increase due to slipstream at different angles of attack of the wing and at different free stream to slipstream velocity ratios .  the results were intended in part as an evaluation basis for different theoretical treatments of this problem .   the comparative span loading curves, together with supporting evidence, showed that a substantial part of the lift increment produced by the slipstream was due to a /destalling/ or boundary-layer-control effect .  the integrated remaining lift increment, after subtracting this destalling lift, was found to agree well with a potential flow theory .   an empirical evaluation of the destalling effects was made for the specific configuration of the experiment .",
      "title" : "experimental investigation of the aerodynamics of a wing in a slipstream ."

  }
  ```
- `cranfield_queries.json`: 225 queries representing users' information need.
```
{
  "query_id": 1,
  "query": "what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft ."
}
```

- `cranfield_relevance.json`: the relevance score (1, 2, 3, 4 as 1 being the highest relevance) of each query and related documents.
```
{"query_id": "1", "r_score": 2, "doc_id": "184"},
{"query_id": "2", "r_score": 1, "doc_id": "12"},
```
  - 1 : the document is the complete answer to the query
  - 2 : the document has a high degree of relevance to the query
  - 3 : the document is useful to the query as general background information
  - 4 : the document is of minimum interest to the query



## Evaluation Metrics

Precision and Recall are used in the examples. See https://nlp.stanford.edu/IR-book/html/htmledition/information-retrieval-system-evaluation-1.html for more evaluation metrics.
