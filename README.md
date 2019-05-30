# VnCoreNLP wrapper Python

VnCoreNLP: [https://github.com/vncorenlp/VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP)

## Setup
> $ pip install py4j \
\
Copy `VnCoreNLP.jar`, `vncorenlp.py` and `models` to your project in the same directory

## Example
See [example.py](example.py)
```python
from vncorenlp import VnCoreNLP

txt = 'học sinh học sinh học'

# Init & load model
vncore_nlp = VnCoreNLP(annotators="wseg pos ner parse")

# Use tokenize only
print(vncore_nlp.tokenize(txt, str=True))
print()
print(vncore_nlp.tokenize(txt, str=False))
print()
print(vncore_nlp.extract(txt))

```

> Output:

```text
học_sinh học_sinh học

['học_sinh', 'học_sinh', 'học']

[
    ['học_sinh', 'N', 'O', '3', 'sub'], 
    ['học_sinh', 'N', 'O', '1', 'nmod'], 
    ['học', 'V', 'O', '0', 'root']
]
```

## Update new VnCoreNLP version

1. Clone or Download [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP)
```bash
$ git clone https://github.com/vncorenlp/VnCoreNLP
```

2. Build VnCoreNLP.jar from VnCoreNLP project

- Copy Tokenizer.java to VnCoreNLP project
```bash
$ cp Tokenizer.java /path/VnCoreNLP/src/main/java/vn/
```
- Build jar for `Tokenizer.java` main class

3. Copy ./models dir and new .jar file to this repository



