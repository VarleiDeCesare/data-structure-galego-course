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

\*\*Sorting

- Bubble Sort - Time Complexity: O(n^2) - Space complexity: O(1)

  - Para fazer a ordenação, são usados dois ponteiros, um atrás do outro, começaria com:
    - 1 ponteiro arr[0] e 2nd ponteiro em arr[1]
    - É sempre comparado um item com o outro dos ponteiros, se o [1] for menor doq o [0] nesse caso de inicio, será swapado, e seguirá em diante para os proximos dois itens [2] [3]...
    - Complexidade é ^2 pois seria quase um loop dentro de outro loop
  - [1,2,3,4,5]....

  - QuickSort - Worst Time complexity O(n^2) Space Complexity: O(n)

    - Algoritmo de divider and conquer, basicamente deve-se escolher um pivot, e com base nele usar novamente dois ponteiros, valida-se se os valores são menores ou maiores que o valor do pivot, fazendo swap entre eles, e no final encontrando o local correto para o valor pivot. Essa regra deve-se ser feita de forma recursiva em um array, sendo chamado para cada quadrante de elementos que foi dividido pelo pivot, maiores e menores, e feito a mesma regra entre eles

  - MergeSort - Time complexity O(n log n) Space Complexity: O(n)
    - Indicado para uso em linked lists.
    - Primeiro Passo (Dividir até um nodo). Irá utilizar dois ponteiros novamnete (fast, slow). Fast precisa encontrar o ultimo elemento, para que o slow chegue no exato meio e possa quebrar a linked list em dois, esse mesmo processo será feito para os sub arrays, até que se separe todos os valores (todos os nodo separados).
    - Segundo Passo (Merge em ordem). Irá começar a juntar novamente os valores, então usando dois ponteiros, faz a comparação entre esses valores, troca a ordem e aponta o menor para o maior (direita p/esquerda). Agora compara os primeiros valores de cada subarray, o menor valor é colocado na frente, compara o valor do mesmo array que foi pego o primeiro valor, compara com o primeiro item do outro array, e ordena na nova linked list, assim fazendo a ordem.
