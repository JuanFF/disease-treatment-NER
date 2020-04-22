# disease-treatment NER

Disease-Treatment NER is a Named Entity Recognition algorithm to extract named diseases and treatments from sentence-like text.

For this sentence

> Favipiravir to treat COVID-19

NER will return the following

```python
{'treatement': 'Favipiravir', 'disease': 'COVID-19'}
```

Both entities must be semantically related to be well labeled as _treatment_ and _disease_; otherwise, NER will return ```empty```. Consider the following

> Favipiravir can't treat COVID-19

The result will then be

```python
{'treatement': '<empty>', 'disease': 'COVID-19'}
```

## Installation

Clone this repository and use the package manager [pip](https://pip.pypa.io/en/stable/) to install SpaCy, an open-source library for text processing that is needed to run this NER.

```bash
pip install -r requirements.txt
```


## Usage

Use ```run_ner.py``` to call the function that receives a text string as input and returns a dict with the result of the NER analysis on your string.

If you want to test a single sentence, use ```test_sentence.py``` from the console with a string in quotation marks argument:

```
test_sentence.py "Favipiravir to treat COVID-19"
```

The output will be

~~~
Treatment: Favipiravir
Disease: COVID-19
~~~

## Performance

The precision score for _treatment_ entity recognition is **0.83** and **0.97** for _disease_. The algorithm performs differently deppending on the text source. We have used Twitter (tweets from healthcare professionals) and PubMed (research paper titles) as text sources for training and testing.

You check a [detailed report](https://datastudio.google.com/embed/u/0/reporting/17i3EjWTInDBFbFK1ruNQyvw-ijbxFXk1/page/9zcN) on precision scores, and the [test cases](https://datastudio.google.com/embed/u/0/reporting/17i3EjWTInDBFbFK1ruNQyvw-ijbxFXk1/page/iN0W) used for testing this algorithms.
