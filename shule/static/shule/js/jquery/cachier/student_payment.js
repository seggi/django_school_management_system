




// $(function() {
//     $('#btn_search_student').click(function(e) {
//         e.preventDefault();
//         $.ajax({
//             url: '/shule/cachier/search_student/',
//             type: 'POST', 
//             data: $('#search_student_form').serialize(),
//             dataType: 'json',
//             success: function(data){
//                 if (data) {
//                         $('#update_connte1').html(data);
//                         $('#update_connte2').html(data);
//                         $('#update_connte3').html(data);
//                         $('#update_connte4').html(data);
//                         $('#update_connte5').html(data);
//                         $('#update_connte6').html(data);
//                         $('#update_connte7').html(data);
//                         $('#update_connte8').html(data);
//                         $('#update_tbl7').html(data);
//                         $('#update_tbl8').html(data);
//                         // $("input[id=update_connte9]")
//                         $.each(data, function(key, value) {
//                             alert(value.name)
                           
//                             if (value.faculty != null){  
//                                 $('#update_connte1').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.name+' '+value.lastname+' '+ value.nickname+"</h2>"));
//                                 $('#update_connte2').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.classe+"</h2>"));
//                                 $('#update_connte3').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.faculty+"</h2>"));
//                                 $('#update_connte4').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.id+"</h2>"));
//                                 $('#update_connte5').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.totamount+"</h2>"));
//                                 $('#update_connte6').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.amount+"</h2>"));
//                                 $('#update_connte7').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.first+"</h2>"));
//                                 $('#update_connte8').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.second+"</h2>"));
//                                 $("input[id=update_connte9]").val(value.id)
                               
//                             }

//                             else if(value.faculty == null){
                                
//                                 $('#update_connte1').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.name+' '+value.lastname+' '+ value.nickname+"</h2>"));
//                                 $('#update_connte2').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.classe+"</h2>"));
//                                 $('#update_connte3').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.faculty+"</h2>"));
//                                 $('#update_connte4').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.id+"</h2>"));
//                                 $('#update_connte5').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.totamount+"</h2>"));
//                                 $('#update_connte6').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.amount+"</h2>"));
//                                 $('#update_connte7').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.first+"</h2>"));
//                                 $('#update_connte8').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.second+"</h2>"));
//                                 $("input[id=update_connte9]").val(value.id)
                                
//                             }
//                             // else{
                                
//                             //     $('#main_fees_t1').prepend(
                        
//                             //     `<tr>
//                             //         <td scope='col'>
//                             //             <span>
//                             //                 <input id="action-toggle" name="selectTbl" 
//                             //                 type="checkbox" value=${value.id||""}>
//                             //             </span>
//                             //         </td>
                    
//                             //         <td>${value.classe||""}</td>
//                             //         <td>${value.faculty||""}</td>
//                             //         <td>${value.type||""}</td>
//                             //         <td>${value.periode||""}</td>
//                             //         <td>${value.tranche||""}</td>
//                             //         <td>${value.totamount||""}</td>
                                    
//                             //     </tr>
//                             //     `
//                             //     )
                                
//                             // }
//                         });  
//                     }
//                 else{
//                     alert(data.msg);
//                 }
//             }, 
//         });
//     });
// });




$(function() {
    var urls = "/shule/cachier/search_student/";
    $('#btn_save_amount_student').click(function(e){
        e.preventDefault();
        $.ajax({
            url: urls, 
            type: 'POST',
            data:  $('#save_student_payment_form').serialize(),
            dataType: 'json',
            success: function(data) {
                alert(data)
                if (data){
                    $('#update_tbl8').html(data);
                    $.each(data, function(key, value) {
                        $('#main_student_history_list').prepend(
                            
                            `<tr>
                                <td>${value.feetype||""}</td>
                                <td>${value.amount}</td>
                                <td>${value.balance}</td>
                                <td>${value.date||""}</td>
                                
                            </tr>
                            `
                            )
                        });
                   }
                else {
                    alert(data.error);
                }
            }
        });
    });
});













$(document).ready(function() {
    load_json_data('student_level');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = ''; 
        
        $.getJSON('/shule/cachier/student_show_level_classe/', function(data){
            html_code += '<option value="" selected disabled>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'student_level'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

                if(ids =='student_classe') {
                    if(value.levels == selected){
                        html_code += '<option value="' + value.id+'">'+value.classe+'</option>';
                    }
                }

                if(ids =='student_facutly') {
                    if(value.classes == selected){
                        html_code += '<option value="' + value.id+'">'+value.faculty+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#student_level', function(){
        var level_id  = $(this).val();
        if(level_id != ''){
            load_json_data('student_classe', level_id );
        }
        else{
            $('#student_classe').html('<option value="">Select classe</option>');
            $('#student_facutly').html('<option value="">Select faculty</option>');
        }
    });

    $(document).on('change', '#student_classe', function(){
        var classes_id  = $(this).val();
        if(classes_id != ''){
            load_json_data('student_facutly', classes_id );

        }
        else{
            $('#student_facutly').html('<option value="">Select facutly</option>');
        }
    });
});

// display fee ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

$(document).ready(function() {
    load_json_data('student_level1');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = ''; 
        
        $.getJSON('/shule/cachier/student_show_level_classe/', function(data){
            html_code += '<option value="" selected disabled>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'student_level1'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#student_level1', function(){
        var level_id  = $(this).val();
        if(level_id != ''){
            load_json_data('student_classe1', level_id );
        }
        else{
            $('#student_classe1').html('<option value="">Select classe</option>');
            $('#student_facutly').html('<option value="">Select faculty</option>');
        }
    });
});









// if (data) {
//     $('#update_connte1').html(data);
//     $('#update_connte2').html(data);
//     $('#update_connte3').html(data);
//     $('#update_connte4').html(data);
//     $('#update_connte5').html(data);
//     $('#update_connte6').html(data);
//     $('#update_connte7').html(data);
//     $('#update_connte8').html(data);
//     $.each(data, function(key, value) {
//         alert(value.name)
//         // var newHeader = $("<h2>"+value.name+"</h2>");
//         // <h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>
//         if (value.faculty != null){  
//             $('#update_connte1').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.name+' '+value.lastname+' '+ value.nickname+"</h2>"));
//             $('#update_connte2').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.classe+"</h2>"));
//             $('#update_connte3').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.faculty+"</h2>"));
//             $('#update_connte4').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.id+"</h2>"));
//             $('#update_connte5').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.totamount+"</h2>"));
//             $('#update_connte6').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.amount+"</h2>"));
//             $('#update_connte7').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.date+"</h2>"));
//             $('#update_connte8').append($("<h2 style='margin-left: 30px; font-weight: 300; font-size: 16px;'>"+value.date+"</h2>"));
            
//         }
//         // else{
            
//         //     $('#main_fees_t1').prepend(
    
//         //     `<tr>
//         //         <td scope='col'>
//         //             <span>
//         //                 <input id="action-toggle" name="selectTbl" 
//         //                 type="checkbox" value=${value.id||""}>
//         //             </span>
//         //         </td>

//         //         <td>${value.classe||""}</td>
//         //         <td>${value.faculty||""}</td>
//         //         <td>${value.type||""}</td>
//         //         <td>${value.periode||""}</td>
//         //         <td>${value.tranche||""}</td>
//         //         <td>${value.totamount||""}</td>
                
//         //     </tr>
//         //     `
//         //     )
            
//         // }
//     });  
// }