from Bio import Entrez
Entrez.email = "ekalak.thang@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
records = handle.read()
print(records)