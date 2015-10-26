function App(args) {
    Grafo.Grafico.displayLoadingMessage();

    if(!args) {
        lnConsole.start();
        Grafo.loadFromFile();
    }
    else {
        Grafo
            .Init(args)
            .Grafico.Init(args);
    }

    return false;
}

$(document).ready(function() {
    $('#bt-console').popover({
        'html': true,
        'placement': 'bottom',
        'content': '<ul id="graph-console"></ul>'
    }).popover('show');

    $('#bt-atualiza-grafo').click(function() {
        return App();
    })
    $('#algoritmo-kruskal').click(function() {
        Grafo.Algoritmos.Kruskal();
        return false;
    })
    $('#algoritmo-prim').click(function() {
        Grafo.Algoritmos.Prim();
        return false;
    })
    $('#algoritmo-dijkstra').click(function() {
        Grafo.Algoritmos.Dijkstra();
        return false;
    })
	$('#algoritmo-profundidade').click(function() {
        Grafo.Algoritmos.Profundidade();
        return false;
    })
	$('#algoritmo-largura').click(function() {
        Grafo.Algoritmos.Largura();
        return false;
    })
    $('#algoritmo-nearest').click(function() {
        Grafo.Algoritmos.nearestNeighbor();
        return false;
    })
    $('#algoritmo-coloracao').click(function() {
        return Grafo.Algoritmos.Coloracao();
        return false;
    });

    $(document).on('keyup', function(event){
        AppKeys.EntrarTecla(event);
    });

    App();
});
