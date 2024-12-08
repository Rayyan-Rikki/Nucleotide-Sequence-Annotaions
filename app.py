from flask import Flask, request, render_template

app = Flask(__name__)

# Utility functions
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence.strip().upper()))

def dna_to_mrna(sequence):
    return sequence.strip().upper().replace('T', 'U')

def calculate_gc_content(sequence):
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0

def mrna_to_protein(sequence):
    codon_table = {
        'AUG': 'M', 'UGG': 'W', 'UAA': '*', 'UAG': '*', 'UGA': '*',
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'GUU': 'V',
        'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UCU': 'S',
        'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S',
        'AGC': 'S', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q', 'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K', 'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'UGU': 'C', 'UGC': 'C',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    sequence = sequence.strip().replace('T', 'U').upper()
    protein = []
    codon_map = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in codon_table:
            amino_acid = codon_table[codon]
            codon_map.append((codon, amino_acid))
            if amino_acid == '*':
                break
            protein.append(amino_acid)
    return ''.join(protein), codon_map

def mutation_identification(sequence):
    ref_sequence = "ATGCATGCATGC"  # Example reference sequence
    sequence = sequence.strip().upper()
    mutations = []
    for i, base in enumerate(sequence):
        if i < len(ref_sequence) and base != ref_sequence[i]:
            mutations.append((i + 1, ref_sequence[i], base))
    return mutations

def transcription_efficiency(sequence):
    sequence = sequence.strip().upper()
    # Mock transcription factor binding site
    if "TATA" in sequence:
        return "High transcription efficiency due to TATA box."
    return "Low transcription efficiency."

def reverse_transcriptase(sequence):
    return sequence.strip().upper().replace('U', 'T')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    analysis_type = None
    if request.method == 'POST':
        sequence = request.form['sequence']
        analysis_type = request.form['analysis']
        try:
            if analysis_type == 'reverse_complement':
                result = reverse_complement(sequence)
            elif analysis_type == 'dna_to_mrna':
                result = dna_to_mrna(sequence)
            elif analysis_type == 'gc_content':
                gc_content = calculate_gc_content(sequence)
                result = f"GC Content: {gc_content:.2f}%"
            elif analysis_type == 'protein_translation':
                protein, codon_map = mrna_to_protein(sequence)
                result = {"protein": protein, "codon_map": codon_map}
            elif analysis_type == 'mutation_identification':
                mutations = mutation_identification(sequence)
                result = mutations
            elif analysis_type == 'transcription_efficiency':
                result = transcription_efficiency(sequence)
            elif analysis_type == 'reverse_transcriptase':
                result = reverse_transcriptase(sequence)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('index.html', result=result, analysis_type=analysis_type)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)