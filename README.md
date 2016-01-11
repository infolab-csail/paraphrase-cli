# paraphrase-cli

A command-line wrapper to query textual entailment and paraphrasing systems. Currently wraps the EXCITEMENT Open Platform [web demo](http://hlt-services4.fbk.eu/eop/).

> Given two text fragments called 'Text' and 'Hypothesis', Textual Entailment Recognition is the task of determining whether the meaning of the Hypothesis is entailed (can be inferred) from the Text.

## Installing

To install, run:

    python setup.py install
    
If pip fails to install lxml, you might need to run `sudo apt-get install libxml2-dev libxslt1-dev`.

## Usage

Usage summary:

    usage: excitement [-h] [-m model] [-o out_file] test_file
    
Specify your test set as a comma-separated file of text, hypothesis.

    John is in love with Mary,John likes Mary
    John is in the park,John is not in his house
    John is tall,John is a man

The output format is a comma-separated file of text, hypothesis, entailment relationship, and confidence score. If an output file is not specified, `excitement` will print to the console.

    John is in love with Mary,John likes Mary,Entailment,0.9813405993
    John is in the park,John is not in his house,Entailment,0.240675551189
    John is tall,John is a man,Entailment,0.994980828692

You can specify one of these models using the `--model` flag:

Code | Model
-----|------
edit-distance | ALG:EditDistance COMP:FixedWeightLemma
edit-distance-wordnet | ALG:EditDistance COMP:FixedWeightLemma RES: WordNet
maxent-verbocean | ALG:MaxEntClassification COMP:TreeSkeleton RES:VerbOcean,TreePattern
maxent-wordnet | ALG:MaxEntClassification COMP:TreeSkeleton RES:WordNet,TreePattern
maxent-all | ALG:MaxEntClassification COMP:TreeSkeleton RES:WordNet,VerbOcean,TreePattern
biutee | ALG:BIUTEE RES:WordNet,CatVar,BAP
pieda | ALG:P1EDA RES:Paraphrase Table

The default model is maxent-all.
