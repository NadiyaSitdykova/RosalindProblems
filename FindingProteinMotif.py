import requests
import regex as re

def get_seq(fasta):
    return "".join(fasta.split('\n')[1:])

def finding_protein_motif(pattern, uniprot_ids):
    matches = []
    for uniprot_id in uniprot_ids:
        params = {"query": uniprot_id, "format": "fasta", "allow_redirects": True}
        response = requests.get("http://www.uniprot.org/uniprot/", params)
        seq = get_seq(response.text)
        if pattern.search(seq):
            matches.append((uniprot_id, \
                            list(map(lambda x: str(x.start()+1), list(pattern.finditer(seq, overlapped=True))))))
    return matches

#looking for N-glycosylation motif
pattern = re.compile('N[^P][ST][^P]')
uniprot_ids = []

with open("input.txt", 'r') as file:
    for uniprot_id in file.readlines():
        uniprot_ids.append(uniprot_id.strip())

matches = finding_protein_motif(pattern, uniprot_ids)
print(matches)

with open("output.txt", 'w') as out:
    for (uniprot_id, positions) in matches:
        out.write(uniprot_id + "\n")
        out.write(" ".join(positions) + "\n")