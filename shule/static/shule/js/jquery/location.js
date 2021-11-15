

$(document).ready(function() {

    load_json_data('id_country');

    var defaults = 'un';

    function load_json_data(ids, locate){
        var html_code = '';
        $.getJSON('http://localhost:8000/shule/admin/country/state/city/', function(data){
            html_code += '<option value="">selectionne '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'id_country'){
                    if(value.country){
                        html_code += '<option value="'+value.id+'">'+value.country+'</option>';
                    }
                }

                if(ids =='id_state') {
                    
                    if(value.countries == locate ){
                        html_code += '<option value="' + value.id+'">'+value.state+'</option>';

                    }
                }

                if(ids == 'id_city'){
                    if(value.states == locate ){
                        html_code +='<option value="' + value.id+ '">'+value.city+'</option>';
                    }
                }
            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#id_country', function(){

        var country_id  = $(this).val();
        if(country_id != ''){
            load_json_data('id_state', country_id );

        }
        else{
            $('#id_state').html('<option value="">Select state</option>');
            $('#id_city').html('<option value="">Select city</option>');
        }
    });

    $(document).on('change', '#id_state', function(){
        var state_id = $(this).val();
        if(state_id != ''){
            load_json_data('id_city', state_id);
        }
        else{
            $('#id_city').html('<option value="">Select city</option>');
        }
    })
});




