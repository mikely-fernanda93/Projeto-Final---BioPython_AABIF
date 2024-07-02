from Bio import SeqIO, Seq

import importlib.util
import os
import sys

# Caminho para o arquivo que contém a função
caminho_ler_fasta = os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio/ler_fasta.py'))

# Adiciona a pasta bio ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio')))

# Agora você pode importar usando importlib
spec = importlib.util.spec_from_file_location("ler_fasta", caminho_ler_fasta)
ler_fasta_modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ler_fasta_modulo)

arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'

# Usar a função importada
ler_fasta_modulo.ler_fasta(arquivo_fasta) 

print("OI") 
 


