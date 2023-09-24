# Este programa realiza tabuadas de Multiplicação , Soma , Divisão e Subtração 
# Desenvolvido com funções cada Função realiza uma tarefa 

# importando as funções de cada tabuada 
from multiplicacao import *
from soma import *
from divisao import *
from subtracao import *

print ("""
       Este programa resolve seus problemas matematicos !
       digite qual  opção que voce deseja 
       1)multiplicação 
       2)soma
       3)divisão
       4)subtração
       0)sair 

   """)


opcao = int(input('digite a opção desejada: de acordo com sua nescidade: '))
while True: # para realizar um looping de tarefas para escolha do usuario
    
    if opcao == 1:
        multiplicacao() # chamando a função de multiplicação
        
        print ('deseja realizar outra outra atividade ? 1) sim 2) não : ')
        opcao = int (input('digite a opção desejada '))
        
        if opcao == 1 :
            opcao = int(input('digite a opção desejada: de acordo com sua nescidade. '))
        elif opcao == 2 :
            print ('programa finalizado: ')
            break
        else:
            print('opção invalida , digite a opção correta !')
    
    elif opcao  == 2 :
        soma() # chamando a função de Soma
        
        print ('deseja realizar outra outra atividade ? 1) sim 2) não : ')
        opcao = int (input('digite a opção desejada '))
        
        if opcao == 1 :
            opcao = int(input('digite a opção desejada: de acordo com sua nescidade. '))
        elif opcao == 2 :
            print ('programa finalizado: ')
            break
        else:
            print('opção invalida , digite a opção correta !')
    
    elif opcao == 3 : # Chamnado a função de Divisão
        divisao()
        print ('deseja realizar outra outra atividade ? 1) sim 2) não : ')
        opcao = int (input('digite a opção desejada '))
        
        if opcao == 1 :
            opcao = int(input('digite a opção desejada: de acordo com sua nescidade. '))
        elif opcao == 2 :
            print ('programa finalizado: ')
            break
        else:
            print('opção invalida , digite a opção correta !')
    
    elif opcao == 4 :
        subtracao() # chamando a função de Subtração
        print ('deseja realizar outra outra atividade ? 1) sim 2) não : ')
        opcao = int (input('digite a opção desejada '))
        
        if opcao == 1 :
            opcao = int(input('digite a opção desejada: de acordo com sua nescidade. '))
        elif opcao == 2 :
            print ('programa finalizado: ')
            break
        else:
            print('opção invalida , digite a opção correta !')
          
    elif opcao == 0 :
        break