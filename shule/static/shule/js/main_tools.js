// Search in main table 

(function(document) {
    'use strict';

    var LightTableFilter = (function(Arr) {

        var _input;

        function _onInputEvent(e) {
            _input = e.target;
            var tables = document.getElementsByClassName(_input.getAttribute('data-table'));
            Arr.forEach.call(tables, function(table) {
                Arr.forEach.call(table.tBodies, function(tbody) {
                    Arr.forEach.call(tbody.rows, _filter);
                });
            });
        }

        function _filter(row) {
            var text = row.textContent.toLowerCase(), val = _input.value.toLowerCase();
            row.style.display = text.indexOf(val) === -1 ? 'none' : 'table-row';
        }

        return {
            init: function() {
                var inputs = document.getElementsByClassName('search_admin_t1');
                Arr.forEach.call(inputs, function(input) {
                    input.oninput = _onInputEvent;
                });
            }
        };
    })(Array.prototype);

    document.addEventListener('readystatechange', function() {
        if (document.readyState === 'complete') {
            LightTableFilter.init();
        }
    });

})(document);


// select row in table 
function tableSelector(){
    var checkboxes = document.getElementsByName('selectTbl');
    var checkmain = document.getElementById('action-toggle');

    if(checkmain.value == 'select') {
        for (var i in checkboxes) {
            checkboxes[i].checked = 'FALSE';

        }
        checkmain.value = 'deselect'
    }else {
        for (var i in checkboxes) {
            checkboxes[i].checked = '';

        }
        checkmain.value = 'select';
    }
}