
$(function() {
    var urls = "/shule/admin/fee_type/";
     // submit fee type
    $('#btn_save_fee_type').click(function(e){
        e.preventDefault();
        $.ajax({
            url: urls, 
            type: 'POST',
            data:  $('#main_form_fee_type').serialize(),
            dataType: 'json',
            success: function(data) {
                if (data.error){
                    alert(data.error);
                }
                else {
                    alert(data.error);
                }
            }
        });
    });

    // submit payment by class main_form_cachier
    $('#btn_save_fixe_payment').click(function(e){
        e.preventDefault();
        $.ajax({
            url: urls, 
            type: 'POST',
            data:  $('#main_form_payment').serialize(),
            dataType: 'json',
            success: function(data) {
                if (data.error){
                    alert(data.error);
                }
                else {
                    alert(data.error);
                }
            }
        });
    });

});

 // add payment periode 
 $('#btn_save_periode').click(function(e){
    e.preventDefault();
    $.ajax({
        url: '/shule/admin/fee_type/', 
        type: 'POST',
        data:  $('#main_form_periode').serialize(),
        dataType: 'json',
        success: function(data) {
            if (data.error){
                alert(data.error);
            }
            else {
                alert(data.error);
            }
        }
    });
});

// =============================================


$(document).ready(function() {
    load_json_data('select_level1');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = '';
       
        $.getJSON('/shule/admin/show_level_classe/', function(data){
            html_code += '<option value="" selected disabled>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'select_level1'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

                if(ids =='select_classe1') {
                    if(value.levels == selected){
                        html_code += '<option value="' + value.id+'">'+value.classe+'</option>';
                    }
                }

                if(ids =='select_facutly1') {
                    if(value.classes == selected){
                        html_code += '<option value="' + value.id+'">'+value.faculty+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#select_level1', function(){
        var level_id  = $(this).val();
        if(level_id != ''){
            load_json_data('select_classe1', level_id );
        }
        else{
            $('#select_classe1').html('<option value="">Select classe</option>');
            $('#select_facutly1').html('<option value="">Select faculty</option>');
        }
    });

    $(document).on('change', '#select_classe1', function(){
        var classes_id  = $(this).val();
        if(classes_id != ''){
            load_json_data('select_facutly1', classes_id );

        }
        else{
            $('#select_facutly1').html('<option value="">Select facutly</option>');
        }
    });
});



// display levels

$(document).ready(function() {
    load_json_data('display_level_list1');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = '';
        $.getJSON('/shule/admin/show_level_classe/', function(data){
            html_code += '<option value="" selected disabled hidden>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'display_level_list1'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }
});


// This session is for showing payment fixed by level, classe.......

$(function() {
    $('#btn_diplay_todo_payment1').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/shule/admin/fee_type/',
            type: 'POST', 
            data: $('#main_form_show_payment_details1').serialize(),
            dataType: 'json',
            success: function(data){
                if (data) {
                    $('#update_tbl2').html(data);
                    $.each(data, function(key, value) {
                        if (value.faculty == null){
                            $('#main_fees_t1').prepend(
                    
                            `<tr>
                                <td scope='col'>
                                    <span>
                                        <input id="action-toggle" name="selectTbl" 
                                        type="checkbox" value=${value.id||""}>
                                    </span>
                                </td>

                                <td>${value.classe||""}</td>
                                <td>${"RAS"}</td>
                                <td>${value.type||""}</td>
                                <td>${value.periode||""}</td>
                                <td>${value.tranche||""}</td>
                                <td>${value.totamount||""}</td>
                                
                            </tr>
                            `
                            )
                        }
                        else{
                            
                            $('#main_fees_t1').prepend(
                    
                            `<tr>
                                <td scope='col'>
                                    <span>
                                        <input id="action-toggle" name="selectTbl" 
                                        type="checkbox" value=${value.id||""}>
                                    </span>
                                </td>

                                <td>${value.classe||""}</td>
                                <td>${value.faculty||""}</td>
                                <td>${value.type||""}</td>
                                <td>${value.periode||""}</td>
                                <td>${value.tranche||""}</td>
                                <td>${value.totamount||""}</td>
                                
                            </tr>
                            `
                            )
                            
                        }
                    });  
                }
                else{
                    alert(data.msg);
                }
            }, 
        });
    });
});



// Save personnel  title ......................


$('#btn_save_personnel').click(function(e){
    e.preventDefault();
    $.ajax({
        url: '/shule/admin/fee_type/', 
        type: 'POST',
        data:  $('#main_form_personnel').serialize(),
        dataType: 'json',
        success: function(data) {
            if (data.error){
                alert(data.error);
            }
            else {
                alert(data.error);
            }
        }
    });
});