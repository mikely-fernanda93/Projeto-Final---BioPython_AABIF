from Bio import SeqIO, Seq

class Sequencia:
    def __init__(self, nome, sequencia):
        self.nome = nome
        self.sequencia = sequencia

    def calcular_percentual(self, bases):
        total_bases = len(self.sequencia)
        base_counts = {base: self.sequencia.count(base) for base in bases}
        percentuais = {base: (count / total_bases) * 100 for base, count in base_counts.items()}
        return percentuais

def ler_fasta(arquivo):
    sequencias = []
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        nome, sequencia = None, ''
        for linha in linhas:
            if linha.startswith('>'):
                if nome and sequencia:
                    sequencias.append(Sequencia(nome, sequencia))
                nome = linha.strip()[1:]
                sequencia = ''
            else:
                sequencia += linha.strip()
        if nome and sequencia:
            sequencias.append(Sequencia(nome, sequencia))
    return sequencias

# Exemplo de uso
arquivo_fasta = '\arquivos\Flaviviridae-genomes.fasta'
#arquivo_fasta = 'Flaviviridae-genomes.fasta'

bases_nucleotideos = ['A', 'T', 'C', 'G']

sequencias = ler_fasta(arquivo_fasta)
for seq in sequencias:
    percentuais = seq.calcular_percentual(bases_nucleotideos)
    print(f"Sequência: {seq.nome}")
    for base, percentual in percentuais.items():
        print(f"{base}: {percentual:.2f}%")
    gc_content = percentuais['G'] + percentuais['C']
    print(f"Conteúdo GC: {gc_content:.2f}%")
    print()
