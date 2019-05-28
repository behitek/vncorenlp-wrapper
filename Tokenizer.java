
package vn;

import vn.pipeline.Annotation;
import vn.pipeline.VnCoreNLP;

import java.io.IOException;

public class Tokenizer {
    private String[] annotators;
    private VnCoreNLP pipeline;

    public Tokenizer(String annotators) {
        this.annotators = annotators.split("\\s+");
        try {
            this.pipeline = new VnCoreNLP(this.annotators);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String tokenize(String str) {
        Annotation annotation = new Annotation(str);
        try {
            pipeline.annotate(annotation);
            return annotation.toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return str;
    }

    public static void main(String[] args) {
        Tokenizer tokenizer = new Tokenizer("wseg pos ner parse");
        System.out.println(tokenizer.tokenize("ba mươi sáu đến bốn mươi năm bốn mươi sáu đến năm mươi năm và năm mươi năm tuổi trở lên"));
    }
}
