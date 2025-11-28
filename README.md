# dicionarios-prova-A1

📚  Projeto: Consulta de Professor por Matéria

Este documento oferece uma visão geral e a documentação completa do projeto, que é um script simples em Python para consultar o nome do professor responsável por uma determinada matéria em uma lista pré-definida.

📝 Descrição do Projeto

O objetivo principal deste script é simular um sistema de consulta rápida onde o usuário pode inserir o nome de uma matéria e receber o nome do professor correspondente. O código utiliza um dicionário Python para armazenar a relação matéria: professor e um loop de repetição para garantir que a entrada do usuário seja válida antes de exibir o resultado.

✨ Funcionalidades

Mapeamento de Dados: Utiliza um dicionário (diciplinas) para mapear matérias (chaves) aos seus respectivos professores (valores).

Validação de Entrada: Emprega um loop while para solicitar a matéria ao usuário e garantir que a matéria inserida exista na lista de matérias disponíveis.

Normalização de Entrada: O método .capitalize() é usado na entrada do usuário para garantir que a primeira letra seja maiúscula, correspondendo ao formato das chaves no dicionário.

Exibição do Resultado: Informa o professor da matéria desejada em um formato amigável.

⚙️ Detalhes da Implementação

1. Estrutura de Dados
   
O projeto utiliza a seguinte estrutura de dados:

Dicionário (diciplinas): Armazena os pares Matéria : Professor.

Lista (professor): Contém todas as chaves (matérias) do dicionário, usada para a validação de entrada.

2. Lógica do Programa (Algoritmo)
   
O fluxo do programa é estruturado para solicitar a entrada, validar e, em seguida, fornecer a saída.

2.1. Pseudocódigo

O algoritmo do programa pode ser representado pelo seguinte Pseudocódigo:

INÍCIO

    DEFINIR dicionário diciplinas
    DEFINIR lista professor como as chaves de diciplinas

    REPETIR
        IMPRIMIR "Informe uma dessas matérias..."
        LER materia_desejada
        CONVERTER materia_desejada para formato 'Capitalize'

        SE materia_desejada PERTENCE a professor ENTÃO
            SAIR DO REPETIR
        SENÃO
            IMPRIMIR "Não foi possível consultar essa materia, tente novamente..."
        FIM SE
    FIM REPETIR

    IMPRIMIR "O professor da matéria e: " + diciplinas[materia_desejada]
    FIM
    
🚀 Como Executar o Projeto

Requisito: É necessário ter o Python 3 instalado no seu sistema.

Copiar o Código: Copie o código Python fornecido.

Salvar: Salve o código em um arquivo com a extensão .py (ex: consulta_professor.py).

Executar: Abra o terminal ou prompt de comando, navegue até o diretório onde o arquivo foi salvo e execute o comando:

🤝 Contribuições

Este é um projeto simples, mas sinta-se à vontade para expandi-lo com as seguintes funcionalidades:

Adicionar mais matérias e professores.

Implementar busca case-insensitive (ignorando maiúsculas/minúsculas).

Criar uma função para adicionar novos professores e matérias durante a execução.
