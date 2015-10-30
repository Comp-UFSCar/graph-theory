T2: Random walks (Caminhadas aleatórias em grafos)
==================================================
O programa deve ler o(s) grafo(s) G = (V, E) especificados abaixo e executar diversas caminhadas aleatórias com tamanhos diferentes iniciando de vértices quaisquer. 

###GRUPO
--------

* Thales Eduardo Adair Menato   

* Daniel Nobusada               

* Jorge Augusto Bernardo    


###METODOLOGIA
--------------

A seguir são apresentadas 3 maneiras de computar a distribuição estacionária de uma CMH (Cadeia de Markov Homogênea que representa o processo não-determinístico conhecido como caminhada aleatória)

1. Primeiramente, compute a distribuição estacionária teórica (steady state) do grafo em questão conforme visto em sala: w(i) = d(vi) / 2|E| (basta dividir o grau de cada vértice por 2 vezes o número de arestas do grafo). Armazene a distribuição num vetor de n elementos chamado w_real

2. Em seguida, execute o Power Method com N=5 e depois com N=100. Armazene as distribuições obtidas nos vetores w_power5 e w_power100.  

3. Por fim, escolha 2 vértices iniciais distintos (de preferência bem longe um do outro) e realize 2 caminhadas aleatórias de tamanho N=100. O programa desenvolvido deve contar o número de visitas que cada vértice do grafo teve ao longo da caminhada. De posse desses valores as probabilidades de cada vértice são obtidas dividindo o número de visitas pelo tamanho total da caminhada, N (dessa forma estamos computando aproximadamente a fração do tempo que passamos em cada vértice do grafo). Armazene as distribuições obtidas nos vetores w_random100a e w_random100b. Refaça as 2 caminhadas mas agora utilizando N=10000, armazenando as distribuições obtidas nos vetores w_random10000a e w_random10000b.


###QUESTIONAMENTOS
------------------

De posse de tais distribuições estacionárias (que representam as probabilidades de se chegar em cada vértice do conjunto), liste quais são os 10 vértices mais importantes do conjunto como sendo aqueles que possuem as maiores probabilidades w(i). Faça uma listagem dos 10 mais importantes em ordem decrescente de probabilidade. Esse processo modela de forma bastante simplificada e aproximada a ideia adotada pelo Google para organizar a internet rankeando websites de acordo com a sua importância no conjunto (Pagerank).


###PERGUNTAS
-------------

a) Compare os vetores w_power5 e w_power100 com a distribuição estacionária teórica (steady state) w_real. O que você percebe? 

b) Compare os vetores w_random100a e w_random100b. O que você pode perceber nas 2 caminhadas quando N=100 e utilizamos diferentes vértices iniciais? 

c) Compare os vetores w_random10000a e w_random10000b. O que você pode perceber nas 2 caminhadas quando N=10000 e utilizamos diferentes vértices iniciais? Ela se aproxima mais de w_real? Porque?

d)  Crie um ranking com os 10 vértices mais importantes do conjunto de acordo com as seguintes distribuições estacionárias obtidas:

  > i) w_random100a
  
  > ii) w_random10000a
  
  > iii) w_power100
  
  > iv) w_real

Os rankings são todos iguais? Qual o mais próximo de w_real?


###DADOS PARA EXECUÇÃO DOS PROJETOS
-----------------------------------
[Zachary's Karate Club](http://networkdata.ics.uci.edu/data/karate/karate.zip): grafo com 34 vértices

<img src="http://ifisc.uib-csic.es/jramasco/fig/zach_layout3.jpg" alt="Zachary's Karate Club" width=666 height=478 />