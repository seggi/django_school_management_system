// Get logged pk primary key 

// Get admin logged in primary key ...
$(document).ready(function() {
    load_json_data('id_admin');
    function load_json_data(ids, fees){
        var html_code = ''
        $.getJSON('/shule/admin/request_admin_pk/', function(data) {
            $.each(data, function(key, value){
                if(ids == 'id_admin'){
                    if(value){
                       $('#idhidden').val(value);
                    }
                }
        
            });
            $('#'+ids).html(html_code);
        });
    }
})

// Get admin logged in primary key ...
$(document).ready(function() {
    load_json_data('id_admin');
    function load_json_data(ids, fees){
        var html_code = ''
        $.getJSON('/shule/admin/request_admin_pk/', function(data) {
            $.each(data, function(key, value){
                if(ids == 'id_admin'){
                    if(value){
                       $('#idhidden1').val(value);
                    }
                }
        
            });
            $('#'+ids).html(html_code);
        });
    }
})


// --------------------------------------
// Submit cachier informations to models

$(function() {
    $('#btn_save_cachier').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/admin/register_staff/",
            type: 'POST', 
            data: $('#admin_save_cachier').serialize(),
            dataType: 'json',
            success: function(data){
                if (data.error){
                    alert(data.error);
                }

                else{
                    alert(data.error);
                }
                
            }, 
        });
    });
});

// --------------------------------------------
// Submit secretary informations to models

$(function() {
    $('#btn_save_secretary').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/admin/register_sec/",
            type: 'POST',
            data: $('#admin_save_secretary').serialize(),
            dataType: 'json',
            success: function(data) {
                if (data.error){
                    alert(data.error);
                }
                else{
                    alert(data.error);
                }
            }
        });
    });
});
