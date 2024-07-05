from Bio import SeqIO
import constantes as constante_aminoacidos

class Sequencia:
    def __init__(self, nome, sequencia):
        self.nome = nome
        self.sequencia = sequencia

def ler_fasta(arquivo_fasta):
    sequencias = []
    with open(arquivo_fasta, 'r') as f:
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


def traducao_cada_sequencia(cada_sequencia):
    orf = ""
    
    #if(to_stop is True):
        # SUA TRADUCAO DEVE PARA NO STOP CODON
        #return True
    for base in (0, cada_sequencia, 3):
        orf += base
        print(orf)

    #return orf

def teste(arquivo_fasta):
    lista_sequencias = []

    for record in SeqIO.parse(arquivo_fasta, "fasta"):
        #print(record.id)
        #print(record.description)
        #print("O tamanho da sequencia é ", len(record.seq))
        #print("SEQUENCIA => ", record.seq)
        lista_sequencias.append(record.seq)
        # FAZER FUNCAO DE TRADUCAO
        #traducao_cada_sequencia(record.seq)
        
        #print()
    
    return lista_sequencias
    

arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
sequencias = ler_fasta(arquivo_fasta)

lista_de_sequencias = teste(arquivo_fasta)
#print(lista_de_sequencias)
#print(lista_de_sequencias.pop(1))
#traducao_cada_sequencia(lista_de_sequencias.pop(1))


#for i in len(constante_aminoacidos.DNA_PARA_AMINOACIDO):
    #print(amino["DNA_PARA_AMINOACIDO"])
    #print(constante_aminoacidos.DNA_PARA_AMINOACIDO[i][0])
    #print()

#print(constante_aminoacidos.DNA_PARA_AMINOACIDO)
#print(len(constante_aminoacidos.DNA_PARA_AMINOACIDO))

traducao_cada_sequencia(lista_de_sequencias)
 
 
 print()

