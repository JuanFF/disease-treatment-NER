# disease-treatment NER

Disease-Treatment NER is a Named Entity Recognition algorithm to extract named diseases and treatments from sentence-like text.

For example, in a sentence like

> Favipiravir to treat COVID-19

You will get the following output 

```python
{'treatement': 'Favipiravir', 'disease': 'COVID-19'}
```



## Installation

Clone this repository and use the package manager [pip](https://pip.pypa.io/en/stable/) to install SpaCy, an open-source library for text processing that is needed to run this NER.

```bash
pip install -r requirements.txt
```


## Usage

Use ```run_ner.py``` to call the function that receives a text string as input and returns a dict with the result of the NER analysis on your string.

If you want to test a single sentence, use ```test_sentence.py``` from the console with a string in quotes as argument:

```
test_sentence.py "Favipiravir to treat COVID-19"
```

The output will be

~~~
Treatment: Favipiravir
Disease: COVID-19
~~~

## Performance

The precision score for treatment mention retrieval is **0.83** and **0.97** for disease mentions. The algorithm performs differently deppending on the text source or style. We have used Twitter and PubMed as text sources for training and testing it. You check a [detailed report](https://datastudio.google.com/embed/u/0/reporting/17i3EjWTInDBFbFK1ruNQyvw-ijbxFXk1/page/9zcN) on precision scores, and the [test cases](https://datastudio.google.com/embed/u/0/reporting/17i3EjWTInDBFbFK1ruNQyvw-ijbxFXk1/page/iN0W) we have used.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
