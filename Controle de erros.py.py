# exercício:Sistema de monitoramento de erros

semana = ['Segunda','Terça','Quarta','Quinta','Sexta']

while True:
    dia = int(input('''
[1] Responder todos os dias 
[0] Sair                    

:'''))
    
    total_erros = 0

    if dia == 1:
        for dia_semana in semana:
            erros = int(input(f'Quantos erros teve na {dia_semana} ?:'))
            total_erros += erros
        break 

    elif dia == 0:
        break

    else:
        print('FIM')
        

print(f'Total de erros registrados: {total_erros}')

media = input('Quer calcular a media ? (S/N) : ').upper()

if media =='S':
    media = total_erros / len(semana)
    print(f'Média de erros: {media:.2f}')

    if media <= 20:
        print('Sistema: Estavel')
    
    elif media <= 30:
        print('Sistema: Precisa de atenção')
    else:
        print('Sistema: Instavel')
else:
    print('FIM')