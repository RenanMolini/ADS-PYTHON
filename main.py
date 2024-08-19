import pandas as pd

# Compreendi que aqui devemos puxar o documento pra dentro do código
# e que posso escolher o nome do arquivo que irá ser gerado

input_file = 'renan.xlsx'
output_file = 'resultado.xlsx'

# Devo sempre colocar o comando df para realizar a leitura do excel
# O excel agora está dentro da variável input_file
df = pd.read_excel(input_file)

# Aqui especifiquei cada coluna dentro de uma variável, mudando o nome para padronizar
column_e = 'E'
column_f = 'F'
colour_column = 'Colour_G'

# Utilizei a condicional if para verificar se estavam nos locais corretos, se não geraria um erro
if column_e in df.columns and column_f in df.columns and colour_column in df.columns:
    # Aqui está a proposta do trabalho, identificar se o estoque é maior ou menor que o mínimo
    # Além disso, o código deve verificar aqueles que estão em vermelho, itens prioritários
    filtered_df = df[(df[column_e] < df[column_f]) & (df[colour_column].str.contains('vermelho', case=False, na=False))]

    # O código abaixo é uma condicional para verificar se há espaços vazios
    if not filtered_df.empty:
        filtered_df.to_excel(output_file, index=False)
        print(f"Filtered data written to {output_file}")
    else:
        print("No entries found where column E is less than column F and Colour_G contains 'red'.")
else:
    print(f"Columns {column_e}, {column_f}, and {colour_column} are not present in the spreadsheet.")
