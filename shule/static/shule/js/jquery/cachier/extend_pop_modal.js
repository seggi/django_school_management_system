// search range date++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

document.querySelector("#btn_search_range").onclick  = () => {
    document.getElementById('bottom-employee-main-content-right').style.display = 'none';
    document.getElementById('bottom-employee-main-content-right2').style.display = 'block';

    let displayInTable = document.querySelector("#bottom-employee-main-content-right2");
    const forms =  new FormData(document.getElementById("search_range_form"));
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/search_student/", {
        method: "POST",
        credentials: 'same-origin',
        body: forms,

    }
    ).then(response => response.json())
     .then(result => {
        if(result.error){
            alert(result.error);
        }
        else{
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Categories</th>
                    <th>Period</th>
                    <th>Par tranche</th>
                    <th>Montant tot</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            for(let datas in result){
                outputs += '<tr>'+
                    '<td>'+result[datas].type+'</td>'+
                    '<td>'+result[datas].amount+'</td>'+
                    '<td>'+result[datas].totfee+'</td>'+
                    '<td>'+result[datas].date+'</td>'+
                    '</tr>';
            }
            outputs += `
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
     })
     .catch((error) => {
         alert(error),
         console.error(error);
     })

}

function openExtendPaiement() {
    document.getElementById('extend_paiement').style.display ="block";
    document.getElementById("bottom-employee-main-content-right1").style.display = 'none';
    document.getElementById('one-top-employee-main-content-right1').style.display = 'none';
    document.getElementById('display_form_fee_type_cachier').style.display = 'none';
    document.getElementById('employee-left-box').style.display = 'none';
    document.getElementById('one-top-employee-main-content-right').style.display = 'none';
    document.getElementById('one-top-employee-main-content-right2').style.display = 'none';
    document.getElementById('one-top-employee-main-content-right3').style.display = 'none';


    document.getElementById('employee-left-box').style.display = 'none'; 

}


document.querySelector("#btn_search_range_recouvre").onclick  = () => {
    document.getElementById('pop_recorver_small_screen').style.display ="none";
    document.getElementById('bottom-employee-main-content-right').style.display = 'none';
    document.getElementById('bottom-employee-main-content-right2').style.display = 'none';
    document.getElementById('bottom-employee-main-content-right3').style.display = 'block';

    document.getElementById('update_recovery_content1').innerHTML = '';
    document.getElementById('update_recovery_content2').innerHTML = '';
    document.getElementById('update_recovery_content3').innerHTML = '';
    document.getElementById('update_recovery_content4').innerHTML = '';
    // document.getElementById('update_recovery_content5').innerHTML = '';
    // document.getElementById('update_recovery_content6').innerHTML = '';
    // document.getElementById('update_recovery_content7').innerHTML = '';
    // document.getElementById('update_recovery_content8').innerHTML = '';

    let element = document.createElement("h2");
    let element1 = document.createElement("h2");
    let element2 = document.createElement("h2");
    let element3 = document.createElement("h2");
    let element4 = document.createElement("h2");
    let element5 = document.createElement("h2");
    let element6 = document.createElement("h2");
    let element7 = document.createElement("h2");
    

    let displayInTable = document.querySelector("#bottom-employee-main-content-right3");
    const forms_recover =  new FormData(document.getElementById("search_range_form_recouvre"));
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/search_student/", {
        method: "POST",
        credentials: 'same-origin',
        body: forms_recover,
    }
    ).then(response => response.json())
     .then(result => {
        if(result.error){
            alert(result.error);
        }
        else{

            // SURMARY ON LEVEL AND CLASS OR FACULTY

            for(let sum in result[1]){
                element.textContent = result[1][sum].level;
                element1.textContent = result[1][sum].classe;
                element2.textContent = result[1][sum].faculty;
                
                document.getElementById("update_recovery_content1").appendChild(element);
                document.getElementById("update_recovery_content2").appendChild(element1);
                document.getElementById("update_recovery_content3").appendChild(element2);
                document.getElementById("update_recovery_content4").appendChild(element3);

            }


            for(let sum in result[2]){
                element4.textContent = result[2][sum].student;
                
                document.getElementById("update_recovery_content4").appendChild(element4);

            }



            // STUDENT DATAILS RECOVERY
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Noms</th>
                    <th>Montant paye</th>
                    <th>Montant restant</th>
                    <th>Solde a realiser</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            for(let datas in result[0]){
                outputs += '<tr>'+
                    '<td>'+result[0][datas].name+' '+result[0][datas].lastname+' '+result[0][datas].nickname+'</td>'+
                    '<td>'+result[0][datas].totamount+'</td>'+
                    '<td>'+result[0][datas].remaining+'</td>'+
                    '<td>'+result[0][datas].balance+'</td>'+
                    '</tr>';
            }
            outputs += `
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
     })
     .catch((error) => {
         alert(error),
         console.error(error);
     })
}

// recover select level, classe, faculty

$(document).ready(function() {
    load_json_data('student_level2');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = ''; 
        
        $.getJSON('/shule/cachier/student_show_level_classe/', function(data){
            html_code += '<option value="" selected disabled>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'student_level2'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

                if(ids =='student_classe2') {
                    if(value.levels == selected){
                        html_code += '<option value="' + value.id+'">'+value.classe+'</option>';
                    }
                }

                if(ids =='student_facutly2') {
                    if(value.classes == selected){
                        html_code += '<option value="' + value.id+'">'+value.faculty+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#student_level2', function(){
        var level_id  = $(this).val();
        if(level_id != ''){
            load_json_data('student_classe2', level_id );
        }
        else{
            $('#student_classe2').html('<option value="">Select classe</option>');
            $('#student_facutly2').html('<option value="">Select faculty</option>');
        }
    });

    $(document).on('change', '#student_classe2', function(){
        var classes_id  = $(this).val();
        if(classes_id != ''){
            load_json_data('student_facutly2', classes_id );

        }
        else{
            $('#student_facutly2').html('<option value="">Select facutly</option>');
        }
    });
});
