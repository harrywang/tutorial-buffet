# Intro
This is a program to do some data transformation.

The key challenge is converting the following "list-like" string into a real list:

```
"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]"
```

`ast.literal_eval` does the trick: https://docs.python.org/2/library/ast.html

Another useful trick is converting a list of list:

```
[[862, 16], [862, 35], [862, 10751], [8844, 12]]
```
into a csv file:

```
862,16
862,35
862,10751
8844,12
```
pandas makes it easy:
```
my_df = pd.DataFrame(my_list)
my_df.to_csv('my_csv.csv', index=False, header=False)
```

# Run

Python 2.x

- create virtual environment: `$virtualenv venv`
- activate virtual env: `$source venv/bin/activate`
- install required packages: `pip install -r requirements.txt`
