frase = input('Digite uma frase para gravar no arquivo:')
# O parâmetro 'a' (de append) passado para a função open
# cria ou abre um arquivo e o habilita para escrita no final.
arquivo = open('frase.txt',  'a')
arquivo.write(frase + '\n')  # Escreve a frase no arquivo.
# Fecha o arquivo logo ao terminar a escrita para evitar 
# corrupção de dados.
arquivo.close()
print('Feito! Verifique o conteúdo do arquivo.')