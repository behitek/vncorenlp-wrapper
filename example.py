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
