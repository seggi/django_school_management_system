
$(function() {
    $('#display_staff').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/admin/get_staff/",
            type: 'POST', 
            data: $('#display_staff_tb').serialize(),
            dataType: 'json',
            success: function(data){
                
                if (data) {
                    $('#update_tbl').html(data);
                    $.each(data, function(key, value) {
                        $('#main_staff_tbl').prepend(
                
                        `<tr>
                            <td scope='col'>
                                <span>
                                    <input id="action-toggle" name="selectTbl" 
                                    type="checkbox" value=${value.id||""}>
                                </span>
                            </td>

                            <td>${value.name||""}</td>
                            <td>${value.last_name||""}</td>
                            <td>${value.gender||""}</td>
                            <td>${value.email||""}</td>
                            <td>${value.phone||""}</td>
                            <td>${value.address||""}</td>
                            <td>${value.username||""}</td>
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




