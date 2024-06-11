'''
O rei da Nlogônia ordenou que todos os documentos importantes sejam "cifrados", para que apenas quem tem conhecimento da cifra possa lê-los (cifrar um documento significa alterar o original modificando as letras de acordo com algum algoritmo de cifra).

O rei decretou que o seguinte algotimo deve ser usado para cifrar os documentos:

Cada consoante deve ser substituída por exatamente três letras, na seguinte ordem:
a própria consoante (vamos chamar de consoante original);
a vogal mais próxima da consoante original no alfabeto, com a regra adicional de que se a consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do alfabeto é usada. Por exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois esta é a vogal mais próxima; se a consoante original é c, a vogal que deve ser utilizada é a, porque c está à mesma distância de a e e, e a é mais próxima do início do alfabeto.
a consoante que segue a consoante original, na ordem do início ao fim do alfabeto. Por exemplo, se a consoante original é d, a consoante a ser utilizada é f. No caso de a consoante original ser z, deve ser utilizada a própria letra z.
As vogais não são modificadas.
Nesta tarefa, o alfabeto é
a b c d e f g h i j k l m n o p q r s t u v x z
e as vogais são
a e i o u
Por exemplo, a cifra da palavra "ter" é "tuveros" (tuv-e-ros) e a cifra da palavra "paz" é "poqazuz" (poq-a-zuz).

O rei da Nlogônia procura por alguém que saiba escrever um programa que produza a cifra de uma palavra dada. Você pode ajudá-lo?
'''

P = str(input())

alfabeto = [
    'a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'x' ,'z'
    ]

vogais = ['a', 'e', 'i', 'o', 'u']

vogais_mais_prox = [
    'a','a','a','e','e','e','e','i','i','i','i','i','o','o','o','o','o','o','u','u','u','u','u','u'
]

def cifra (palavra ,alfabeto , vogais,vogaisprox):
    palavra_cifrada = ''
    for letra in palavra:
        cache = ''
        # Consoante
        if letra not in vogais and letra in alfabeto:
            # Primeira Cifra
            cache += letra
            # Segunda Cifra
            c2 = alfabeto.index(letra)
            cache += vogaisprox[c2]
            # Terceira cifra
            c3 = alfabeto.index(letra)
            if alfabeto[c3] == 'z':
                cache += 'z'
            else :
                c3 += 1
                if alfabeto[c3] in vogais:
                    c3 += 1
                cache += alfabeto[c3]
        else:
            cache += letra
        palavra_cifrada += cache
    return palavra_cifrada

print(cifra(P,alfabeto,vogais,vogais_mais_prox))
