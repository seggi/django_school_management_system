// Save Level & Classes session

$(function() {
    $('#btn_save_level').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/admin/save_level/",
            type: 'POST', 
            data: $('#main_form_cachier').serialize(),
            dataType: 'json',
            success: function(data){
                if (data.error){
                   alert(data.error)
                }
                else{
                    alert(data.error);
                }
            }, 
        });
    });
});

// Save Faculty session ....


$(function() {
    $('#btn_save_faculty').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/admin/select_level_classe/",
            type: 'POST', 
            data: $('#main_form_faculty').serialize(),
            dataType: 'json',
            success: function(data){
                if (data.error){
                   alert(data.error)
                }
                else{
                    alert(data.error);
                }
            }, 
        });
    });
});

$(document).ready(function() {
    load_json_data('select_level');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = '';
        $.getJSON('/shule/admin/show_level_classe/', function(data){
            html_code += '<option value="">Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'select_level'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

                if(ids =='select_classe') {
                    
                    if(value.levels == selected){
                        html_code += '<option value="' + value.id+'">'+value.classe+'</option>';

                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#select_level', function(){

        var country_id  = $(this).val();
        if(country_id != ''){
            load_json_data('select_classe', country_id );

        }
        else{
            $('#select_classe').html('<option value="">Select classe</option>');
        }
    });
});


// This session is for showing level, classes, faculty in table 

$(function() {
    $('#btn_diplay_todo_level').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/admin/show_level_details/",
            type: 'POST', 
            data: $('#main_form_show_level_details').serialize(),
            dataType: 'json',
            success: function(data){
                if (data) {
                    $('#update_tbl1').html(data);
                    $.each(data, function(key, value) {
                        $('#main_classes_t1').prepend(
                
                        `<tr>
                            <td scope='col'>
                                <span>
                                    <input id="action-toggle" name="selectTbl" 
                                    type="checkbox" value=${value.id||""}>
                                </span>
                            </td>

                            <td>${value.level||""}</td>
                            <td>${value.classe||""}</td>
                            <td>${value.faculty||""}</td>
                            
                         </tr>
                        `
                        )
                    });  
                }
                else{
                    alert(data.msg);
                }
            }, 
        });
    });
});

$(document).ready(function() {
    load_json_data('display_level_list');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = '';
        $.getJSON('/shule/admin/show_level_classe/', function(data){
            html_code += '<option value="" selected disabled hidden>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'display_level_list'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }
});


