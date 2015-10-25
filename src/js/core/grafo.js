(function() {
    var Grafo = {
        MatrizAdj: [], // Matriz de adjacencia

        Direcionado: false,
		VertInicial: 0,
        MediaDeGraus: 0,

        Algoritmos: {},

        Arquivo: 'data/lemis.json',

        Grafico: {
            FisicaAtiva: true,
            Parente: '#graph',
            width: 0.98 *document.body.clientWidth,
            height: 820,

            NodeRadius: 15,
            MovimentacaoVertices: -300,

            TamArestas: 150
        }
    }

    var Init = function(pAlg) {
        var tmpMatrizAdj = pAlg && pAlg !== 'coloracao' ? Grafo.Algoritmos.MatrizAdj : Grafo.MatrizAdj,
            i, j

        // ENCONTRA GRAU DE CADA VERTICE
        Grafo.Grau = new Array(tmpMatrizAdj.length); // vetor que armazena grau de cada vertice

        for(i = 0; i < Grafo.Grau.length; i++)
            Grafo.Grau[i] = 0;

        for(i = 0; i < Grafo.Grau.length; i++) {
            if(tmpMatrizAdj[i][i] > 0)
                Grafo.Grau[i] += 2; // soma 2 no grau caso o elemento [i][i] tenha um loop

            // percore a matriz e verifica se existe uma aresta que liga os vertices i e j
            for(j = i +1; j < Grafo.Grau.length; j++)
                if(tmpMatrizAdj[i][j] > 0) { // existe uma aresta entre i e j
                    Grafo.Grau[i]++;             // vertice origem tem seu grau incrementado
                    Grafo.Grau[j]++;
                }
        }

        // ENCONTRA O GRAU MEDIO NO GRAFO
        // este valor sera utilizado para exibir os vertices em escala
        Grafo.MediaDeGraus = 0;
        for(i = 0; i < Grafo.Grau.length; i++)
            Grafo.MediaDeGraus += Grafo.Grau[i];

        Grafo.MediaDeGraus /= Grafo.Grau.length; // media = somatorio(Grau[] / tamanho de Grau)

        return Grafo;
    }

    var loadFromFile = function() {
        console.log('Tentando carregar grafo do arquivo...')

        if(!Grafo.Arquivo) {
            console.log('Erro! Arquivo invalido. Carregando matriz de adjacencia padrao.')
            Grafo.MatrizAdj = [
                [0, 10, 0,  30, 24,  0],
                [10, 0, 12,  3,  0, 99],
                [0, 12, 0,  0, 33,  0 ],
                [30, 3, 0,  0,  0,  4 ],
                [24, 0, 33, 0,  0, 200],
                [0, 99, 0, 4,  200,  0]];

            Grafo.Init()
                .Grafico.Init();
        }

        else d3.json(Grafo.Arquivo, function(graph, error) {
            console.log('Arquivo carregado com sucesso! Criando matriz de adjac�ncia...')

            for (var i = 0; i < graph.nodes.length; i++) {
                Grafo.MatrizAdj[i] = []
                for (var j = 0; j < graph.nodes.length; j++)
                    Grafo.MatrizAdj[i][j] = 0
            }

            for(var i = 0; i < graph.links.length; i++) {
                var arestAtual = graph.links[i]

                Grafo.MatrizAdj[arestAtual.source][arestAtual.target] = arestAtual.value
                if (!Grafo.Direcionado)
                    Grafo.MatrizAdj[arestAtual.target][arestAtual.source] = arestAtual.value
            }

            console.log('Matriz de adjac�ncia criada com sucesso.')

            Grafo.Init().Grafico.Init()
        })

        return this
    }

    /*
     * ALGORITMOS DE MANIPULACAO DE GRAFO:
     * Arquivos dentro da pasta /js/modelos
     */

    Grafo.Init = Init;
    Grafo.loadFromFile = loadFromFile;
    window.Grafo = Grafo; //  retorna objeto publico
}());
