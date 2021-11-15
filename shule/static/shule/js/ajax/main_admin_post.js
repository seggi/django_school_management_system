// Admin post method

// 
$(function() {
    $('#btn_save_cachier').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/jsons/",
            type: 'POST', 
            data: $('#main_form_cachier1').serialize(),
            dataType: 'json',
            success: function(data){
                if (data.error){
                    alert(data.error);
                }

                else{
                    alert(data.error);
                }
                // alert(data[0].name)
                // $('#main_fees_t1').prepend(
            
                //     `<tr>
                //     <td>${data[0].name||""}</td>
                //     <td>${data[0].last||""}</td>
                //     </tr>
                //     `
                // )
            }, 
        });

    });

});

// submit fee payment

$(function() {
    $('#btn_save_cachier1').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/jsonsp/",
            type: 'POST', 
            data: $('#main_form_cachier2').serialize(),
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
})

// submit sec fee payment

$(function() {
    $('#btn_save_cachier2').click(function(e) {
        e.preventDefault();

        $.ajax({
            url: "/shule/json_sec/",
            type: 'POST', 
            data: $('#main_form_cachier3').serialize(),
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
})


// display mat feetype
$(document).ready(function() {
    load_json_data('mat_fee');
    var defaults = "Selection _de_type_frais";
    function load_json_data(ids, fees){
        var html_code = ''
        $.getJSON('http://127.0.0.1:8000/shule/fees/', function(data) {
            html_code += '<option value="">'+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'mat_fee'){
                    if(value.title){
                        html_code += '<option value="'+value.id+'">'+value.title+'</option>';
                    }
                }
        
            });
            $('#'+ids).html(html_code);
        });
    }
})

// display prim feetype

$(document).ready(function() {
    load_json_data('prim_fee');
    
    var defaults = "Selection _de_type_frais";
    function load_json_data(ids, fees){
        var html_code = ''
        $.getJSON('http://127.0.0.1:8000/shule/fees/', function(data) {
            html_code += '<option value="">'+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'prim_fee'){
                    if(value.title){
                        html_code += '<option value="'+value.id+'">'+value.title+'</option>';
                    }
                }
        
            });
            $('#'+ids).html(html_code);
        });
    }
})

// display sec feetype

$(document).ready(function() {
    load_json_data('secon_fee');
    
    var defaults = "Selection _de_type_frais";
    function load_json_data(ids, fees){
        var html_code = ''
        $.getJSON('http://127.0.0.1:8000/shule/fees/', function(data) {
            html_code += '<option value="">'+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'secon_fee'){
                    if(value.title){
                        html_code += '<option value="'+value.id+'">'+value.title+'</option>';
                    }
                }
        
            });
            $('#'+ids).html(html_code);
        });
    }
})

// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// seach from database fees relating to level 
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$(document).ready(function() {
    loadFeeData("fee_search");
    var defaults = "selection_par_niveau";

    function loadFeeData(ids) {
        var html_code =''
        $.getJSON('http://127.0.0.1:8000/shule/search_level/', function(data) {
            html_code += '<option value="">'+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'fee_search'){
                    if(value.id){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }
            });
            $('#'+ids).html(html_code);
        })
    }
});

// display into Table 

$(function() {
    $('#display_fees').click(function(e) {
    
        e.preventDefault();
        $.ajax({
            url: "/shule/set_level/",
            type: 'POST', 
            data: $('#display_fee_tb').serialize(),
            dataType: 'json',
            success: function(data){
               if (data) {
                    $('#test').html(data);
                    $.each(data, function(key, value) {
                        
                        $('#main_fees_t1').prepend(
                
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
                            <td>${value.fee||""}</td>
                            <td>${value.amount||""}</td>
                         </tr>
                        `
                        )
                    });
                    
                }
                else{
                    alert(data.msg);
                }   
            }, 

            // complote: function(data){
            //     $('#test').html(data);
            // }
        });

    });

});


































// document.getElementById('main_form_cachier1').addEventListener('submit', postData);

// const csrfToken = getCookie('CSRF-TOKEN');

// function postData(event){
//     event.preventDefault();
//     let montant = document.getElementById('mat_montant').value;
    
//     fetch('/shule/shule_admin/', {
//         method: 'POST',
//         headers: new Headers({
//             'Content-Type': 'x-www-form-urlencoded',
//             'X-CSRF-TOKEN': getCookie('X-CSRF-TOKEN'),
//         }),
//         body: JSON.stringify({montant: montant})
//     }).then((res) => res.json())
//     .then((data) => console.log(data), alert('seggi'))
//     .catch((err)=> console.log(err))
   
// }






// const url ='/shule/shule_admin'
// const form = document.querySelector('[data-section="main_form_cachier1"]');

// form.addEventListener('submit', (e) => {
//     e.preventDefault()

//     const datas  = document.querySelector('[type=number]')
//     const formData = new FormData()
//     alert(datas)
//     for (let i = 0; i < datas.length; i++) {
//         let requestdatas = datas[i]

//         formData.append('mat_montant', requestdatas)

//     }

//     fetch(url,  {
//         method: 'POST', 
//         body:  formData, 
//     }).then((response) => {
//         console.log(response)
//     })
// })

































