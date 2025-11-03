## Anotações curso Galego - Estrutura de dados e algoritmos.

### Big O Notation.

- Fala mais sobre escalabilidade e não necessariamente performace.
  - Complexidade temporal
    - é o denominador de quanto tempo levará para a runtime terminar sua ação (percorrer todo o array, fazer contas matemáticas..)
  - Complexidade espacial
    - é o denominador de quanto espaço é necessário para finalizar a runtime, em uma busca pelo maior valor de um array por ex, é O(1), pois somente um valor é atrelado à memoria, só é trocado em caso de encontrar um valor maior.

Ex: Busca pelo maior valor de um array.
[1,6,7,2,3,5]

- Complexidade temporal é O(n), pois foi necessário percorrer todos os elementos do array, para se ter certeza que o maior valor estaria na posição 2.
- Complexidade espacial é O(1), pois o espaço em memória só alterou o seu valor, começou em 1, passou a ser 6 e por fim denominou o valor como 7, não precisou de mais memória ser alocada.

- O(1) = CONSTANTE:

  - Tempo:
    - Independente do input (array), terá sempre o mesmo tempo de execução.
      - ex: Encontrar o PRIMEIRO elemento de um array, se o array tiver tamanho 10, ou 1 milhão, sempre irá chegar apenas ao primeiro elemento e já encontrar, não importando o tamanho do input.
  - Memória:
    - Usa-se o exemplo mencionado da linha 11, independente do script rodado, o espaço de memória utilizado, inicia-se e termina-se sendo sempre o mesmo.

- O(log n) = Confome o input aumente (muito) rápido o tempo não aumenta na mesma proporção, mas sim, menos.

  - ex: O input foi dobrado de linha a linha, porém o tempo de execução aumento linearmente, não acompanhando o incremento do input:

    - O(log 10) = 3.32
    - O(log 20) = 4.32
    - O(log 40) = 5.32

  - Binary search: Necessita-se encontrar o elemento 3. (NECESSITA SEMPRE DO ARRAY ORDENADO)
    - [1,2,3,4,5,6,7,8,9,10]
      - Busca-se o meio do array ordenado (valor 5), 3 menor que o 5, logo, todos os valores a direita podem ser desconsiderados, sobrando:
      - [1,2,3,4] - Novamente se faz a validação de encontrar o meio do array, sendo ele o 2, logo todos os valores a esquerda, podem ser desconsiderados, novamente sobrando:
      - [3,4] - 3 encontrado, pois o meio é arredondado para baixo. (fim da operação)
    - Exemplificando, se o array tivesse o dobro do tamanho, apenas um passo a mais seria necessário, se tivesse 20 inputs, apenas mais um step encontraria os primeiros 10 valores, e refazendo as mesmas validações para encontrar o valor 3.

- O(n)

  - Temporal, percorrer todos os elementos de um array.
  - Busca pelo elemento 3.
    - [1,2,3,4,5,6,7,8,9,10]
  - Em n passos (3) foi encontrado o valor 3.
    - Nesse caso em específico, em apenas 3 passos encontramos o valor, mesmo tendo 10 elementos, mas em BIG O se considera sempre o PIOR dos casos.
      - Considerando esse exemplo, no pior dos casos se quissessemos encontrar o valor 10, necessitariamos fazer 10 passos, assim sendo 0(n).
      - Tendo o mesmo exemplo de dobrar o tamanho do array, dobraria o valor de n, escalando da mesma proporção.
  - Espacial:
    - Se o input tiver o dobro do tamanho, o espaço será o dobro também..

- O(n log n) - Sorting (quick sort, merge sort), Divider and conquer.

  - Pouco usado, difícil de ser exemplificado, porém é uma notação usada em merge sort por exemplo:
    - Merge sort, pegasse um array, divide-se em partes menores, e segue dividindo as partes menores até o ponto que sobre apenas um item no final de cada divisão primária, após a divisão de TODOS os elementos, é feito a ordenação dos mesmos de forma individual.

- O (n^2)
  - Loop dentro de um outro Loop.
  - para cada item dentro do array, percorre novamente outro array, ou até o mesmo array.
