# disease-treatment NER

Disease-Treatment NER is a Named Entity Recognition algorithm to extract named diseases and treatments from sentence-like text.

For the sentence

> Favipiravir to treat COVID-19

NER will return the following

```python
{'treatement': 'Favipiravir', 'disease': 'COVID-19'}
```

Both entities must be semantically related to be well labeled as _treatment_ and _disease_; otherwise, NER will return an ```empty``` tag.

Consider the following
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

Use ```run_ner.py``` to call the function that receives a text string as input and returns a dict with the NER analysis result on your string.

If you want to test a single sentence, use ```test_sentence.py``` from the console with a string enclosed in quotes as argument:

```
test_sentence.py "Favipiravir to treat COVID-19"
```

The output will be

~~~
Treatment: Favipiravir
Disease: COVID-19
~~~

## Performance

The precision score is 0.89. You can find [here](https://github.com/JuanFF/datasets/tree/master/performance-tests/disease-treatment%20NER) the datased used to evaluate accuracy.