TOKENIZE_JAR = "VnCoreNLP.jar"

from py4j.java_gateway import JavaGateway


def get_vncorenlp(jar_file, annotators):
    gateway = JavaGateway.launch_gateway(classpath=jar_file)
    vncorenlp = gateway.jvm.vn.Tokenizer(annotators)
    return vncorenlp


class VnCoreNLP:
    def __init__(self, jar_file=TOKENIZE_JAR, annotators="wseg pos ner parse"):
        try:
            self.__model = get_vncorenlp(jar_file, annotators)
        except:
            raise RuntimeError("Can not init model. Check log file!")

    def extract(self, txt):
        res = self.__model.tokenize(txt)
        result = []
        for line in res.split("\n"):
            line = line.strip()
            if line == '':
                continue
            result.append(line.split("\t"))
        return result

    def tokenize(self, txt, str=True):
        result = []
        for respond in self.extract(txt):
            result.append(respond[0])
        return ' '.join(result) if str else result


if __name__ == '__main__':
    vncorenlp = VnCoreNLP(annotators="wseg")
    print(vncorenlp.extract('học sinh học sinh học'))
