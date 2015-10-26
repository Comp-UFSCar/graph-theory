(function() {
    window.lnConsole = {

        MAXIMUM_ELEMENTS_DISPLAYED: 32,

        inserted: 0,
        start: function() {
            this.inserted = 0;
            $('#graph-console').empty();
        },

        message: function(message, additionalParameters, styleClass, graphObject) {
            if (!message || message == undefined) return false;

            this.inserted++;

            if (additionalParameters == undefined) additionalParameters = false;
            if (styleClass == undefined) styleClass = '';

            // Prevent message repetiton in the console.
            var $consoleElement = $('#graph-console');

            $consoleElement.children().each(function() {
                if (this.dataset.msg == message) $(this).remove();
            });

            // Constraint maximum number of message.
            if ($consoleElement.children().length >= this.MAXIMUM_ELEMENTS_DISPLAYED)
                $consoleElement.children().last().remove();

            var $messageElement = $('<li />')
                .attr('data-msg', message)
                .addClass('console-item')
                .on('click', function() { return false; })
                .html('<span class="' + styleClass + '">' + message +'</span>');

            if (graphObject && graphObject != undefined) {
                if (styleClass == 'console-message-edge') {
                    $messageElement.children().eq(0)
                        .on('mouseover', function() { Grafo.Grafico.selectEdge(graphObject.__data__, 0, 0, true); })
                        .on('mouseout', function() { Grafo.Grafico.unselectEdge(graphObject.__data__); });
                }
                if (styleClass == 'console-message-node') {
                    $messageElement.children().eq(0)
                        .on('mouseover', function() { Grafo.Grafico.selectNode(graphObject.__data__, 0, 0, true); })
                        .on('mouseout', function() { Grafo.Grafico.unselectNode(graphObject.__data__); });
                }
            }

            if (additionalParameters)
                $messageElement.children().eq(0).tooltip({
                    'title': additionalParameters,
                    'placement': 'right',
                    'html': true
                });

            $consoleElement.prepend($messageElement);
            return true;
        }
    };
}());
