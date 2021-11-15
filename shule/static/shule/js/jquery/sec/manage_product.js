$(function() {
    $('#btn_save_product').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/secretary/save_product/",
            type: 'POST', 
            data: $('#main_form_save_product').serialize(),
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

$(function() {
    $('#btn_display_product1').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/shule/secretary/save_product/',
            type: 'POST', 
            data: $('#main_form_display_products').serialize(),
            dataType: 'json',
            success: function(data){
                if (data) {
                    $('#update_tbl3').html(data);
                    $.each(data, function(key, value) {
                        if (value){
                            $('#main_product_t1').prepend(
                    
                            `<tr>
                                <td scope='col'>
                                    <span>
                                        <input id="action-toggle" name="selectTbl" 
                                        type="checkbox" value=${value.id||""}>
                                    </span>
                                </td>
                                <td>${value.article||""}</td>
                                <td>${value.unit_amount||""}</td>
                                <td>${value.quantity||""}</td>
                                <td>${value.tot_amount||""}</td>
                                <td>${value.remaing||""}</td>
                                <td>${value.date||""}</td>
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