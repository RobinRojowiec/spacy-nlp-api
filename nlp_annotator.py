import spacy


class Annotator:
    def __init__(self):
        self.models = {}

        en_model = spacy.load("en");
        self.models["en"] = en_model;

    def get_model(self, lang):
        if lang in self.models:
            return self.models[lang]

    def analyze(self, text, lang):
        doc = self.get_model(lang)(text);

        result = []
        for sent in doc.sents:
            annotation = {"type": "Sentence"};
            annotation["text"] = sent.text;
            annotation["begin"] = sent.start
            annotation["end"] = sent.end
            annotation["tokens"] = []
            result.append(annotation)

            for token in sent:
                tokenAnno = {"type": "Token"}
                tokenAnno["text"] = token.text;
                tokenAnno["lemma"] = token.lemma_;
                tokenAnno["pos_tag"] = token.pos_;
                tokenAnno["detailed_pos_tag"] = token.tag_;
                tokenAnno["dependency_tag"] = token.dep_;
                tokenAnno["stopword"] = token.is_stop;
                tokenAnno["sentiment"] = token.sentiment;

                annotation["tokens"].append(tokenAnno)

        for ent in doc.ents:
            annotation = {"type": "NamedEntity"};
            annotation["label"] = ent.label;
            annotation["text"] = ent.text;
            annotation["begin"] = ent.start
            annotation["end"] = ent.end
            result.append(annotation)

        return result
