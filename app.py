from Bio.Alphabet import generic_dna, generic_rna
from Bio.Seq import Seq
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def web_pagina():
    """
    Haalt de ingevoerde seq op van de webpagina, en kijkt of dit DNA, RNA
    of eiwit is. En voert hier de gewenste acties op uit.
    :return: De webaplicatie
    """
    seq = request.args.get("seq", '')
    seq = seq.upper()
    # Checkt met andere funcie of het DNA is
    if check_dna(seq):
        bio_dna = Seq(seq, generic_dna)
        # Wanneer DNA, returnd hij dat het DNA is en
        # Geeft hij de bijbehoorende RNA en eiwit streng.
        return render_template("afvink4.html",
                               soort='DNA',
                               een=(bio_dna.transcribe()),
                               twee=(bio_dna.translate()))
    # Wanner het geen DNA is kijkt hij of het RNA is
    elif check_rna(seq):
        bio_rna = Seq(seq, generic_rna)
        # Wanneer RNA, returnd hij dat het RNA is en
        # Geeft hij de bijbehoorende DNA en eiwit streng.
        return render_template("Aavink4.html",
                               soort='RNA',
                               een=(bio_rna.back_transcribe()),
                               twee=(bio_rna.translate()))

    # als het zowel geen DNA als RNA is kijkt hij of het een eiwit is
    elif check_eiwit(seq):
        # Wanneer eiwit, returnd hij dat het een eiwit is en
        # geeft hij een link naar de ncbi website met ingevulde resultaat zodat
        # je de eiwit sequentie kan blasten
        return render_template("afvink4.html",
                               soort='Eiwit',
                               een="klik op de link en druk op blast",
                               twee="https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&QUERY=" + str(seq))
    # Als het zowel geen DNA, RNA of eiwit is dan returnd hij dat het
    # geen DNA, RNA of eiwit is
    else:

        return render_template("afvink4.html",
                               soort = 'Geen DNA, RNA of eiwit',
                               een='',
                               twee='')


def check_dna(seq):
    """
    :param seq: De sequentie opgehaald van de pagina
    :return: True/False of het DNA is of niet
    """
    for i in seq:
        if i not in ['A','C', 'G','T']:
            return False
    return True

def check_rna(seq):
    """
    :param seq: De sequentie opgehaald van de pagina
    :return: True/False of het RNA is of niet
    """
    for i in seq:
        if i not in ['A', 'C', 'G', 'U']:
            return False
    return True

def check_eiwit(seq):
    """
    :param seq: De sequentie opgehaald van de pagina
    :return: True/False of het eiwit is of niet
    """
    amino = ["A",
             "R",
             "N",
             "D",
             "B",
             "C",
             "E",
             "Q",
             "Z",
             "G",
             "H",
             "I",
             "L",
             "K",
             "M",
             "F",
             "P",
             "S",
             "T",
             "W",
             "Y",
             "V",
             "X"]
    for i in seq:
        if i not in amino:
            return False
    return True



if __name__ == '__main__':
    app.run()