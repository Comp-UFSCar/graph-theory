(function() {
    Grafo.Grafico.Init = function(args) {
        // caso esta funcao seja chamada com o parametro @args como verdadeiro, isso
        // significa que algum algoritmo foi aplicado sobre o grafo. Logo devemos desenhar
        // o grafo contido em Grafo.Algoritmos.MatrizAdj, exceto se tal algoritmo for o de
        // coloracao, onde a matriz de saida ee a original
        var adjacencyMatrix = args ? Grafo.Algoritmos.MatrizAdj : Grafo.MatrizAdj

        var i, j, tmpID = 0,
            $parente = $(Grafo.Grafico.Parente),
            nodes = new Array(), links = new Array()

        // DEFINE VERTICES
        for (i = 0; i < adjacencyMatrix.length; i++) {
            nodes.push({
                name: '',
                cor: 0
            })

            if (args == 'coloracao') nodes[i].cor = adjacencyMatrix[i][i]
        }

        // DEFINE AS ARESTAS
        for (i = 0; i < adjacencyMatrix.length; i++) { // para todos os vertices
            for (j = Grafo.Direcionado ? 0 : i; j < adjacencyMatrix.length; j++) {

                if( i == j && args == 'coloracao' )
                    continue // impede criacao de loops quando o algoritmo de coloracao foi aplicado, levando em consideracao
                             // que na pos. [i][i] da matriz de adjacencia esta representada a cor do vertice, e nao uma conexao

                if (adjacencyMatrix[i][j] != 0)    // atraves da matriz de adjacencia, busca
                    links.push({             // quais vertices sao ligadas por quais arestas
                        id: tmpID++,
                        source: i,
                        target: j,
                        weight: adjacencyMatrix[i][j] // peso da aresta
                    })
            }
        }

        // se um grafo ja esta sendo mostrado, o remove.
        $parente.empty()

        var color = d3.scale.category20();
        var force = d3.layout.force()
            .size([Grafo.Grafico.width, Grafo.Grafico.height])
            .charge(Grafo.Grafico.MovimentacaoVertices)
            .linkDistance(Grafo.Grafico.TamArestas);

        var svg = d3.select(Grafo.Grafico.Parente).append('svg')
            .attr('width', Grafo.Grafico.width)
            .attr('height', Grafo.Grafico.height)
            .style({
                'margin': 0,
                'top': 0,
                'left': 0
            });

        force.nodes(nodes)
                .links(links)
                .start();

        var link = svg.selectAll('.link')
            .data(force.links())
            .enter().append('line')
                .attr('class', 'link')
                .style("stroke-width", function(d) { return Math.sqrt(d.value); })
                .on('mouseover', selectEdge)
                .on('mouseout', unselectEdge);

        var node = svg.selectAll('.node')
            .data(force.nodes())
            .enter()
            .append('g')
                .attr('class', 'node')
                .on('mouseover', selectNode)
                .on('mouseout', unselectNode)
                .append('circle')
                    .attr('r', Grafo.Grafico.NodeRadius)
                    .call(force.drag);

        force.on('tick', function () {
            link.attr('x1', function(d) { return d.source.x })
                .attr('y1', function(d) { return d.source.y })
                .attr('x2', function(d) { return d.target.x })
                .attr('y2', function(d) { return d.target.y });

             node.attr('cx', function(d) { return d.x })
    			 .attr('cy', function(d) { return d.y });
        });

        // colore grafo, caso o algoritmo de coloracao tenha sido aplicado.
        if (args == 'coloracao') node.style("fill", function(d) { return color(d.cor); })

        // definindo raio dos vertices proporcionalmente a seus graus
        var $vertices = $('.node'), $arestas = $('.link')

        $vertices.each(function(index, el) {
            $(el).attr('id', index) // adiciona IDs aos vertices
            var $circle = $(el).children().eq(0)   // seleciona o circulo dentro de vertice

            var tmpRaio = Grafo.Grafico.NodeRadius

            // verifica se media de graus = 0. Se sim, a conta abaixo nao ee executada
            // (ela retornaria 'infinity'). tmpRaio continua valendo 25 (valor minimo)
            if (Grafo.MediaDeGraus)
                tmpRaio = Grafo.Grau[index] *Grafo.Grafico.NodeRadius / Grafo.MediaDeGraus
            tmpRaio = parseInt(tmpRaio)

            if (tmpRaio < Grafo.Grafico.NodeRadius)
                tmpRaio = Grafo.Grafico.NodeRadius
            if (tmpRaio > Grafo.Grafico.NodeRadius *3)
                tmpRaio = Grafo.Grafico.NodeRadius *3

            $circle.attr('r', tmpRaio)
        })

        // atribuindo IDs as arestas, a fim de manipula-las com a jQuery
        $arestas.each(function(index, el){
            $(el).attr('id', index);
        })

        // EXIBINDO A MATRIZ DE ADJACENCIA NA TABELA DA PAGINA
        $('#matrix-modal .modal-body').children().remove();

        var $matriz = $('<table />', {
            'id': 'tabela-m-adj',
            'class': 'table table-condensed'
        });

        $matriz.html($('<thead />'));
        $matriz.children().html('<tr />');

        $matriz.append($('<tbody />'));

        for (i = 0; i < adjacencyMatrix.length; i++) {
            $matriz.children().eq(0).children().append('<th>V'+i+'</th>')
            var $linha = $('<tr />')

            for (j = 0; j < adjacencyMatrix.length; j++) {
                var $el = $('<td />')
                $el.html(adjacencyMatrix[i][j])
                $linha.append($el)     // insere a coluna

            }
            $matriz.children().eq(1).append($linha) // insere a linha em
        }

        $('#matrix-modal .modal-body').append($matriz);
        $('#matrix-modal .modal-body').append('<p><strong>mean(degree):</strong> ' + Grafo.MediaDeGraus + '</p>');

        lnConsole.message('Rendering complete.', $('.node').length + ' nodes and ' + $('.link').length + ' edges');
        return false
    }

    Grafo.Grafico.displayLoadingMessage = function() {
        var $parente = $(Grafo.Grafico.Parente);

        $parente.empty()
        $parente.append('<center><br /><div style="margin-top:50px; height:60%; min-height:100px">' +
        '<h1><img src="img/loader.gif" /> <small>Loading...</small></h1></div></center>');

        return false
    }

    function selectNode(d, el, key, inibeConsole) {
        var obj = $('#' +d.index +'.node')[0],
            D3Circle = d3.select(obj).select('circle'), i, tmpDesc = '<ul>'

        // se existe um link em que o source ou target sao iguais a d.index,
        // exibe a outra ponta dele (o outro vertice)
        $('.link').each(function(){
            if (this.__data__.source.index == d.index)
                tmpDesc += '<li>' +(this.__data__.target.index +1)  +'</li>'

            if (this.__data__.target.index == d.index)
                tmpDesc += '<li>' +(this.__data__.source.index +1)  +'</li>'
        })
        tmpDesc += '</ul>'

        D3Circle.transition()
        .duration(300)
        .attr({
			'r': function() { return D3Circle.attr('r') *0.9 },
		})

		d3.select(obj).attr('class', 'nodeSelected')

        if (!inibeConsole || inibeConsole === 'undefined')
            lnConsole.message('Node ' +(d.index +1) + (d.name ? ': ' + d.name : ''), 'Degree: ' + Grafo.Grau[d.index]
                     + '<br />' +'Adjacent nodes: ' +tmpDesc, 'console-message-node', obj)
    }
    function unselectNode(v) {
        var obj = $('#' +v.index +'.nodeSelected')[0],
            tmpRaio = Grafo.Grafico.NodeRadius

        // verifica se media de graus = 0. Se sim, a conta abaixo nao ee executada
        // (ela retornaria 'infinity'). tmpRaio continua valendo 25 (valor minimo)
        if (Grafo.MediaDeGraus)
            tmpRaio = Grafo.Grau[v.index] *Grafo.Grafico.NodeRadius / Grafo.MediaDeGraus
        tmpRaio = parseInt(tmpRaio)

        if (tmpRaio < Grafo.Grafico.NodeRadius)
            tmpRaio = Grafo.Grafico.NodeRadius
        if (tmpRaio > Grafo.Grafico.NodeRadius *3)
            tmpRaio = Grafo.Grafico.NodeRadius *3

        d3.select(obj).select('circle')
        .transition()
        .delay(500)
        .duration(300)
        .attr({
			'r': tmpRaio
		})

		d3.select(obj).attr('class', 'node')
    }
    function selectEdge(d, key, el, inibeConsole) {
        var obj = $('#' +d.id +'.link')[0]

        d3.select(obj)
        .attr('class', 'linkSelected')

        if (!inibeConsole)
            lnConsole.message('Edge ' +(d.id +1), 'Weight: ' +d.weight +'<br />Connecting '
                             +(d.source.index +1) + '-' +(d.target.index +1), 'console-message-edge', obj)
    }
    function unselectEdge(d) {
        var obj = $('#' +d.id +'.linkSelected')[0]
        d3.select(obj).attr('class', 'link')
    }

    Grafo.Grafico.selectNode = selectNode;
    Grafo.Grafico.unselectNode = unselectNode;
    Grafo.Grafico.selectEdge = selectEdge;
    Grafo.Grafico.unselectEdge = unselectEdge;

    return Grafo
}());
