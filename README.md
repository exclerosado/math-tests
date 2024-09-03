# Repositório dedicado a testes de matemática

## `rsa.py`
### Conceito básico do algoritmo RSA
#### Esse código visa demonstrar a complexidade de um problema simples envolvendo números primos 

O código demonstra a dificuldade de descobrirmos quais os dois números primos que geraram o resultado final. 
- Entre com um valor que será o intervalo de números primos presentes no mesmo;
- Tente adivinhar quais o dois números que geraram o número gerado pelo algoritmo;
- Quanto maior a lista, mais complexo fica.  

## `pi.py`
### Estimando o valor de Pi
#### Equação recém descoberta acidentalmente para estimar o valor de Pi

O algoritmo foi construído com base no estudo disponível no link https://mindyourdecisions.com/blog/2024/06/30/scientists-just-discovered-a-new-formula-for-pi-accidentally/

## `perfect_number.py`
### Validando se um número é perfeito ou não
#### Um número é considerado perfeito quando a soma de seus divisores inteiros é igual ao próprio número

Para saber mais, acesse o link https://pt.wikipedia.org/wiki/N%C3%BAmero_perfeito

## `fibonnaci.c`
### Encontrando o n termo da sequência Fibonnaci
#### Um clássico exercício de programação

A sequência fibonacci é composta por 2 termos iniciais, 0 e 1. Os próximos termos serão a soma do termo atual e do termo anterior. Mais informações no link https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci.
O código foi escrito em linguagem C propositalmente pelo fato do processamento se tornar extensivo quando aumentamos o número de entrada.

## `collatz.py`
### Gerando a sequência de Collatz
#### Famoso problema 3x + 1

A sequência de Collatz tem como princípio o seguinte:
- escolha um número natural inteiro;
- se for par, divida-o por 2;
- se for ímpar, multiplique por 3 e some 1.

Será gerada uma sequência que sempre terminará em 4 → 2 → 1, não importa qual o tamanho do número inicial.  
Mais informações no link https://en.wikipedia.org/wiki/Collatz_conjecture.
