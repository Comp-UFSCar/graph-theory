Grafo.Algoritmos.nearestNeighbor = function() {
    console.log('K-Nearest-neighbor Search has started...');

    var nodes = Grafo.MatrizAdj.length;
    var k = 3;

    m = new Array(nodes);
    for (var i = 0; i < nodes; i++) {
        m[i] = new Array(nodes);
        for (var j = 0; j < nodes; j++) m[i][j] = 0;
    }

    for (var node = 0; node < nodes; node++) {
        neighborhood = kNearestNeighborsOf(Grafo.MatrizAdj, node, k);
        console.log(neighborhood.length);

        for (var i = 0; i < neighborhood.length; i++) {
            neighbor = neighborhood[i][0];
            cost = neighborhood[i][1];

            m[neighbor][i] = m[i][neighbor] = cost;
        }
    }

    Grafo.Algoritmos.MatrizAdj = m;
    App(true);
    return false;
}

function kNearestNeighborsOf(m, node, k) {
    var neighborhood = [];

    for (var i = 0; i < m[node].length; i++)
        neighborhood[i] = [i, m[node][i]];

    return neighborhood
        .filter(function (e) { return e[1] != 0; })
        .sort(function(left, right) { return Math.sign(left[1] - right[1]); })
        .slice(0, k);
}
