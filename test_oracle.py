from oracle import *
from conllu import *
import pytest


def test_is_projective():
    """Test case for a projective sentence (should return True)."""

    #English
    sent = [
        Token('<ROOT>', upos='ROOT', head=0),
        Token('It', upos='PRON', head=2, deprel='nsubj'),
        Token("'s", upos='AUX', head=0, deprel='root'),
        Token('hers', upos='PRON', head=2, deprel='xcomp'),
        Token('.', upos='PUNCT', head=2, deprel='punct')
    ]

    #Korean
    sent = [
        Token('<ROOT>', upos='ROOT'),
        Token('제일', lemma='제일', upos='ADV', feat='_', head=2, deprel='advmod'),
        Token('가까운', lemma='가깝+ㄴ', upos='ADJ', feat='_', head=3, deprel='amod'),
        Token('스타벅스가', lemma='스타벅스+가', upos='NOUN', feat='_', head=5, deprel='nsubj'),
        Token('어디', lemma='어디', upos='ADV', feat='_', head=5, deprel='advmod'),
        Token('있지', lemma='있+지', upos='ADJ', feat='_', head=0, deprel='root'),
    ]

    #Yakut
    sent = [
        Token('<ROOT>', upos='ROOT'),
        Token('Биһиги', lemma='биһиги', upos='PRON', feat='Case=Nom|Number=Plur|Person=1|PronType=Prs', head=3,
              deprel='nsubj'),
        Token('манна', lemma='манна', upos='ADV', feat='_', head=3, deprel='advmod'),
        Token('баарбыт', lemma='баар', upos='AUX', feat='Number=Plur|Person=1|Tense=Pres', head=0, deprel='root'),
    ]
    assert is_projective(sent) == True


def test_non_projective():
    """Test case for a non-projective sentence (should return False)."""

    #English
    sent = [
        Token('<ROOT>', upos='ROOT', head='_', deprel='root'),
        Token('John', upos='NOUN', head=2, deprel='nsubj'),
        Token('saw', upos='VERB', head=0, deprel='root'),
        Token('Mary', upos='NOUN', head=2, deprel='obj'),
        Token('yesterday', upos='ADV', head=2, deprel='advmod'),
        Token('walking', upos='VERB', head=3, deprel='acl'),
        Token('in', upos='ADP', head=7, deprel='case'),
        Token('the', upos='DET', head=8, deprel='det'),
        Token('park', upos='NOUN', head=5, deprel='obl'),
        Token('.', upos='PUNCT', head=2, deprel='punct')
    ]

    #Spanish
    sent = [
        Token('<ROOT>', upos='ROOT'),
        Token('Con', lemma='con', upos='ADP', feat='_', head=3, deprel='case'),
        Token('la', lemma='el', upos='DET', feat='Definite=Def|Gender=Fem|Number=Sing|PronType=Art', head=3,
              deprel='det'),
        Token('llegada', lemma='llegada', upos='NOUN', feat='Gender=Fem|Number=Sing', head=19, deprel='nmod'),
        Token('de', lemma='de', upos='ADP', feat='_', head=5, deprel='case'),
        Token('maquinaria', lemma='maquinaria', upos='NOUN', feat='Gender=Fem|Number=Sing', head=3, deprel='nmod'),
        Token('(', lemma='(', upos='PUNCT', feat='PunctSide=Ini|PunctType=Brck', head=7, deprel='punct'),
        Token('martillos', lemma='martillo', upos='NOUN', feat='Gender=Masc|Number=Plur', head=5, deprel='appos'),
        Token('hidráulicos', lemma='hidráulico', upos='ADJ', feat='Gender=Masc|Number=Plur', head=7, deprel='amod'),
        Token('y', lemma='y', upos='CCONJ', feat='_', head=10, deprel='cc'),
        Token('compresores', lemma='compresor', upos='NOUN', feat='Gender=Masc|Number=Plur', head=7, deprel='conj'),
        Token(')', lemma=')', upos='PUNCT', feat='PunctSide=Fin|PunctType=Brck', head=7, deprel='punct'),
        Token(',', lemma=',', upos='PUNCT', feat='PunctType=Comm', head=3, deprel='punct'),
        Token('la', lemma='el', upos='DET', feat='Definite=Def|Gender=Fem|Number=Sing|PronType=Art', head=14,
              deprel='det'),
        Token('perforación', lemma='perforación', upos='NOUN', feat='Gender=Fem|Number=Sing', head=16, deprel='nsubj'),
        Token('manual', lemma='manual', upos='ADJ', feat='Number=Sing', head=14, deprel='amod'),
        Token('dejó', lemma='dejar', upos='VERB', feat='Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin', head=0,
              deprel='root'),
        Token('de', lemma='de', upos='ADP', feat='_', head=19, deprel='mark'),
        Token('ser', lemma='ser', upos='AUX', feat='VerbForm=Inf', head=19, deprel='cop'),
        Token('necesaria', lemma='necesario', upos='ADJ', feat='Gender=Fem|Number=Sing', head=16, deprel='xcomp'),
        Token('en', lemma='en', upos='ADP', feat='_', head=22, deprel='case'),
        Token('las', lemma='el', upos='DET', feat='Definite=Def|Gender=Fem|Number=Plur|PronType=Art', head=22,
              deprel='det'),
        Token('canteras', lemma='cantera', upos='NOUN', feat='Gender=Fem|Number=Plur', head=19, deprel='nmod'),
        Token('y', lemma='y', upos='CCONJ', feat='_', head=24, deprel='cc'),
        Token('minas', lemma='mina', upos='NOUN', feat='Gender=Fem|Number=Plur', head=22, deprel='conj'),
        Token('.', lemma='.', upos='PUNCT', feat='PunctType=Peri', head=16, deprel='punct'),
    ]

    #French
    sent = [
        Token('<ROOT>', upos='ROOT', head='_', deprel='root'),
        Token('Lors', upos='ADV', head=16, deprel='advmod'),
        Token('de', upos='ADP', head=5, deprel='case'),
        Token('le', upos='DET', head=5, deprel='det'),
        Token('dernier', upos='ADJ', head=5, deprel='amod'),
        Token('rapport', upos='NOUN', head=1, deprel='obj'),
        Token('publié', upos='VERB', head=5, deprel='acl'),
        Token('par', upos='ADP', head=9, deprel='case'),
        Token('le', upos='DET', head=9, deprel='det'),
        Token('ministère', upos='NOUN', head=6, deprel='obl:agent'),
        Token('de', upos='ADP', head=12, deprel='case'),
        Token("l'", upos='DET', head=12, deprel='det'),
        Token('écologie', upos='NOUN', head=9, deprel='nmod'),
        Token(',', upos='PUNCT', head=1, deprel='punct'),
        Token('il', upos='PRON', head=16, deprel='expl:subj'),
        Token("s'", upos='PRON', head=16, deprel='expl:pv'),
        Token('avère', upos='VERB', head=0, deprel='root'),
        Token('que', upos='SCONJ', head=29, deprel='mark'),
        Token("l'", upos='DET', head=19, deprel='det'),
        Token('état', upos='NOUN', head=29, deprel='nsubj'),
        Token('de', upos='ADP', head=22, deprel='case'),
        Token('nos', upos='DET', head=22, deprel='det'),
        Token('cours', upos='NOUN', head=19, deprel='nmod'),
        Token("d'", upos='ADP', head=24, deprel='case'),
        Token('eau', upos='NOUN', head=22, deprel='nmod'),
        Token('ne', upos='ADV', head=29, deprel='advmod'),
        Token('soit', upos='AUX', head=29, deprel='cop'),
        Token('pas', upos='ADV', head=28, deprel='advmod'),
        Token('si', upos='ADV', head=29, deprel='advmod'),
        Token('brillant', upos='ADJ', head=16, deprel='csubj'),
        Token('que', upos='SCONJ', head=31, deprel='case'),
        Token('ça', upos='PRON', head=28, deprel='obj'),
        Token('.', upos='PUNCT', head=16, deprel='punct')
    ]
    assert is_projective(sent) == False

def test_single_word():
    """Test case for a single-word sentence (should return True)."""
    sent = [
        Token('<ROOT>', upos='ROOT', head=0),
        Token('Hello', upos='INTJ', head=0, deprel='root')
    ]
    assert is_projective(sent) == True  # No dependencies to cross

def test_root_only():
    """Test case for an empty sentence (only root, should return True)."""
    sent = [Token('<ROOT>', upos='ROOT', head=0)]
    assert is_projective(sent) == True  # No dependencies exist

#Test get_features() using German conllu
def test_get_features():
    sent = [
        Token('<ROOT>', upos='ROOT'),  # Artificial root token
        Token('Absolut', lemma='absolut', upos='ADJ', feat='Degree=Pos', head=2, deprel='advmod'),
        Token('empfehlenswert', lemma='empfehlenswert', upos='ADJ', feat='Degree=Pos', head=0, deprel='root'),
        Token('ist', lemma='sein', upos='AUX', feat='Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin', head=2,
              deprel='cop'),
        Token('auch', lemma='auch', upos='ADV', feat='_', head=2, deprel='advmod'),
        Token('der', lemma='der', upos='DET', feat='Case=Nom|Definite=Def|Gender=Masc|Number=Sing|PronType=Art', head=6,
              deprel='det'),
        Token('Service', lemma='Service', upos='NOUN', feat='Case=Nom|Gender=Masc|Number=Sing', head=2, deprel='nsubj'),
        Token('.', lemma='.', upos='PUNCT', feat='_', head=2, deprel='punct')
    ]
    features, actions = get_features(sent)
    assert features[0:2] == [['ROOT', 'ADJ'],['ADJ', 'ADJ']]
    assert actions[0:2] == ['shift', 'left-arc(advmod)']

#Test get_features() using english conllu
def test_get_features2():
    sent = [
        Token('<ROOT>', upos='ROOT'),
        Token(form='We', lemma='we', upos='PRON', head=2, deprel='nsubj'),
        Token(form='love', lemma='love', upos='VERB', head=0, deprel='root'),
        Token(form='parsing', lemma='parse', upos='NOUN', head=2, deprel='obj')
    ]

    features, actions = get_features(sent)
    assert features == [['ROOT', 'PRON'],['PRON', 'VERB'], ['ROOT', 'VERB'], ['VERB', 'NOUN'], ['ROOT', 'VERB']]
    assert actions == ['shift', 'left-arc(nsubj)', 'shift', 'right-arc(obj)', 'right-arc(root)']

#Test get_features() using japanese conllu
def test_get_features3():
    sent = [
        Token(form='<ROOT>', upos='ROOT', head=0, deprel='root'),
        Token(form='先生', lemma='先生', upos='NOUN', head=3, deprel='nmod'),
        Token(form='の', lemma='の', upos='ADP', head=1, deprel='case'),
        Token(form='理想', lemma='理想', upos='NOUN', head=6, deprel='nsubj'),
        Token(form='は', lemma='は', upos='ADP', head=3, deprel='case'),
        Token(form='限りなく', lemma='限り無い', upos='ADJ', head=6, deprel='advcl'),
        Token(form='高い', lemma='高い', upos='ADJ', head=0, deprel='root'),
        Token(form='。', lemma='。', upos='PUNCT', head=6, deprel='punct')
    ]

    features, actions = get_features(sent)
    assert features[0:7] == [['ROOT', 'NOUN'], ['NOUN', 'ADP'], ['NOUN', 'NOUN'], ['ROOT', 'NOUN'],
    ['NOUN', 'ADP'], ['NOUN', 'ADJ'], ['ADJ', 'ADJ']]
    assert actions[0:5] ==['shift', 'right-arc(case)', 'left-arc(nmod)', 'shift', 'right-arc(case)']

#Test get_features() using spanish conllu
def test_get_features4():
    sent = [
        Token(form='<ROOT>', upos='ROOT', head=0, deprel='root'),
        Token(form='De', upos='ADP', head=2, deprel='case'),
        Token(form='allí', upos='ADV', head=3, deprel='advmod'),
        Token(form='procedía', upos='VERB', head=0, deprel='root'),
        Token(form='la', upos='DET', head=5, deprel='det'),
        Token(form='familia', upos='NOUN', head=3, deprel='nsubj'),
        Token(form='el', upos='DET', head=7, deprel='det'),
        Token(form='escritor', upos='NOUN', head=5, deprel='nmod'),
        Token(form='vallisoletano', upos='ADJ', head=7, deprel='amod'),
        Token(form='Blas', upos='PROPN', head=7, deprel='appos'),
        Token(form='Pajarero', upos='PROPN', head=9, deprel='flat'),
        Token(form=',', upos='PUNCT', head=15, deprel='punct'),
        Token(form='cuya', upos='DET', head=13, deprel='det'),
        Token(form='casa', upos='NOUN', head=15, deprel='nsubj'),
        Token(form='se', upos='PRON', head=15, deprel='expl:pv'),
        Token(form='encuentra', upos='VERB', head=9, deprel='acl:relcl'),
        Token(form='en', upos='ADP', head=18, deprel='case'),
        Token(form='la', upos='DET', head=18, deprel='det'),
        Token(form='Plaza', upos='PROPN', head=15, deprel='obl'),
        Token(form='San', upos='PROPN', head=20, deprel='amod'),
        Token(form='Pedro', upos='PROPN', head=18, deprel='nmod'),
        Token(form=';', upos='PUNCT', head=3, deprel='punct')
    ]

    features, actions = get_features(sent)
    assert features[0:5] == [['ROOT', 'ADP'],['ADP', 'ADV'],['ROOT', 'ADV'],['ADV', 'VERB'],['ROOT', 'VERB']]
    assert actions[0:5] == ['shift','left-arc(case)','shift','left-arc(advmod)','shift']



