# rsa-python
Algoritimo de Criptografia RSA desenvolvido em Pyhton.
Entrada com um caracter ASCII, saída com mensagem cifrada e chave pública e privada.

# Lógia
## Escolha dois valores primos diferentes:
P = 3
Q = 7
## Equação N
N = P * Q = 3 * 7 = 21
## Equação PHI(Toteliente) -> Núcleo do RSA
PHI(N) = (P - 1) * (Q - 1) = (3 - 1) * (7 - 1) = 2 * 6 = 12
## Agora escolhemos o valor E, sendo que o mesmo tem que ser um valor primo e co-primo,
podemos fazer isso de duas formas, sendo:
MDC(E, PHI(N)) = 1
Ou:
1 mod (PHI(N))
##Esta segunda regra é mais na mão, porém mais simples de entender:
###Obj:
- Valor não pode ser primo
- Valor tem que ser fatorado
- Se a fatoração der mais de dois valores, junte a vontade os valores até somente
existem dois valores multiplicantes, isso funciona porque é simples matemática de
multiplicação.
1 mod (12)
1+ 12 = 13
1 + (2 * 12) = 25
1 + (3 * 12) = 37
1 + (4 * 12) = 49
Podemos utilizar o 25 pois ele é o valor que é fatorado de 5 * 5 e não é primo, sendo que
desta forma temos o valor E e D de uma vez, sendo que o D é o valor inversamente
multiplicável de E.
E = 5
D = 5
## Agora vamos criptografar um valor, Ex: oi -> [14, 9]
## Equação para criptografar: C = M ^ E mod (N), sendo:
C = valor a encontrar -> Valor RSA
M = Valor do caractere atual
E = Valor descoberto acima
C = 14 ^ 5 mod (21) = 537824 mod (21) = 537824 % 21 = 14
C = 9 ^ 5 mod (21) = 59049 mod (21) = 59049 % 21 = 18
OI de [14, 9] foi convertido para [14, 18]-> Valores não variam muito por que os valores
utilizados na equação foram muito baixos
## Descriptografar
M = C ^ D mod (N)
M = Valor resultante do descriptografar
C = Valor RSA
D = Valor obtido acima
M = 14 ^ 5 mod (21) = 537824 mod (21) = 537824 % 21 = 14
C = 18 ^ 5 mod (21) = 1889568 mod (21) = 1889568 % 21 = 9
Chave pública (21,5) -> (N, E)
Chave privada (21,5) -> (N, D)
