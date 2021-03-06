/*
 * DIJKSTRA.JS
 *
 * DATA CRIACAO: 29/11/2012
 *
 * DESCRICAO: declaracao da funcao de Dijkstra, algoritmo que
 * tem como objetivo obter a arvore de caminhos minimos.
 *
 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 * LISTA DE MODIFICACOES
 *
 * 29/11/2012: criacao do arquivo, +Dijkstra()
 *
 * +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 */

(function() {
    Grafo.Algoritmos.Dijkstra = function() {
        if (Grafo.Direcionado) {
            console.log('Directed graphs are not supported.');
            return 0;
        }

        console.log('Dijkstra\'s algorithm has started...');

        //  Q: vetor de vertices a serem analizados
        //  matAcm: matriz de adjacencia de uma arvore de caminhos minimos
        var Q = [], i, j, VertMenor, PosMenor, matAcm,
        numVertices = Grafo.MatrizAdj.length;

        var acm = [];  // armazena os vertices pertencentes a arvore de caminhos minimos

        for (i = 0; i < Grafo.MatrizAdj.length; i++)
            Q.push({index: i, pred: -1, custo: -1});

        Q[Grafo.VertInicial].custo = 0;
        Q[Grafo.VertInicial].pred = 0;

        while(Q.length > 0) {
            PosMenor = 0;

            //  encontra o vertice de menor custo
            for(i = 1; i < Q.length; i++)
                if(Q[PosMenor].custo == -1 || (Q[i].custo < Q[PosMenor].custo && Q[i].custo != -1))
                    PosMenor = i;

            console.log('Edge ' + Q[PosMenor].index +' with cost ' +Q[PosMenor].custo + ' was chosen.');

            VertMenor = Q.splice(PosMenor, 1)[0];
            acm.push(VertMenor);

            for(i = 0; i < Q.length; i++) {
                if(Grafo.MatrizAdj[VertMenor.index][Q[i].index] > 0)  //  para todos os vertices adjacentes
                    if(Q[i].custo == -1 || Q[i].custo > VertMenor.custo +Grafo.MatrizAdj[VertMenor.index][Q[i].index]) {  //  relaxa aresta
                        Q[i].custo = VertMenor.custo +Grafo.MatrizAdj[VertMenor.index][Q[i].index];
                        Q[i].pred = VertMenor.index;
                    }
            }
        }

        matAcm = [];
        for (i = 0; i < numVertices; i++) {
            matAcm[i] = [];
            for(j = 0; j < numVertices; j++)
                matAcm[i][j] = 0;
        }

        for(i = 0; i < numVertices; i++) {
            //console.log(Grafo.MatrizAdj[acm[i].index][acm[i].pred]);
            matAcm[acm[i].index][acm[i].pred] = Grafo.MatrizAdj[acm[i].index][acm[i].pred];
            matAcm[acm[i].pred][acm[i].index] = Grafo.MatrizAdj[acm[i].pred][acm[i].index];
        }

        Grafo.Algoritmos.MatrizAdj = matAcm;

        App(true);
        return false;
    }
}());
