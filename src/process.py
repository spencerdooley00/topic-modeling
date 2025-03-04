import en_core_web_sm
import re
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = en_core_web_sm.load()


def lemmatizer(doc):
    # This takes in a doc of tokens from the NER and lemmatizes them.
    # Pronouns (like "I" and "you" get lemmatized to '-PRON-', so I'm removing those.
    doc = [token.lemma_ for token in doc if token.lemma_ != "-PRON-"]
    doc = u" ".join(doc)
    return nlp.make_doc(doc)


def remove_stopwords(doc):
    doc = [str(token).lower() for token in doc if token.is_stop != True and token.is_punct !=
           True and token.is_digit != True and token.is_space != True]
    return doc


def lyric_tokenizer(doc):
    nlp = spacy.load('en_core_web_sm')
    stops = ["yeah", '\n', 'intro', 'hook', 'verse', 'yes', 'oh', 'chorus', 'like', 'hey', 'okay',
    'uh', 'blah', 'ooooooh', 'woah', 'la', 'aight', 'whoa', 'til', 'o', 'huh', 'ya', 'ohh', 'yea', 'oooh',
    'tryna', 'cause', 'igh', 'da', 'ha', 'woo', 'u', 'mo', 'mac', 'mmm', 'bah', 'bam', 'doo', 'dat', 'ah'
    , 'n', 'm', 'yo', 'na', 'i\'mma', 'ayy', 'uhh', 'nas', 'hmm', 'w', 'wit', 'd', 'bein', 'bout', 'ay',
     'g', 'lemme', 'i’mma', 's', 'u', 't', 'fu', 'c', 'ga', 'mm',  'ooo', 'haha', 'woo', 'p', 'hah', 'mo'
     , 'ba', 'b', 'en', 'h', 'cuz', 'dat', 'yuh', 'da', 'na', 'ooh', 'ooooh', 'l', 'bo', 'andre', 'shh'
     , 'y', 'till', 'e', 'aw']
    nlp.Defaults.stop_words.update(stops)
    nlp.add_pipe(lemmatizer, name="lemmatizer", after="ner")
    nlp.add_pipe(remove_stopwords, name="stopwords", last=True)
    return nlp(doc)
