diciplinas = {
    "Portugues": "Maria vitoria",
    "Matematica": "João Neto",
    "Ciencias": "Lucas Guilherme",
    "Informatica": "Gabriela Alves ",
    "Medicina": "Marcos Antonio",
    "Pedagogia": "Roberto Muniz",
    "Engenharia": "Laura Silva",
    "Historia": "Luan Pedro",
    "Geografia": "Adriano Pereira",
    "Quimica": "Moacir Junior"
    }
professor = list(diciplinas.keys())


while True:
    print('  Informe uma dessas materias para ver o nome do professor\n|Portugues,Matematica, Ciencias, Informatica, Medicina, Pedagogia, Engenharia, Historia, Geografia, Quimica ')
    materia = input(' materia desejada: ').capitalize()
    if materia in professor: 
        break
    else:
        print('Não foi possivel consultar essa materia tente novamente...')


print (f'O professor da materia e: {diciplinas[materia]}')