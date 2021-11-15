// Depense 

$(document).on('click', '.btn-watch', function () {
    $id = $(this).attr('name');

    document.getElementById('details-modals').style.display = "block";
    document.getElementById('employee-detail').value = $id;

    let forms = new FormData(document.getElementById('employee-detail-form'));

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error){
            document.getElementById('details-modals').style.display = "none";
            alert(result.error);
        }

        else {
            for(let datas in result){
               
                document.getElementById('name').textContent = result[datas].name;
                document.getElementById('lastname').textContent = result[datas].lastname;
                document.getElementById('nickname').textContent = result[datas].nickname;
                document.getElementById('function').textContent = result[datas].title;
                document.getElementById('salary').textContent = result[datas].salary;
                document.getElementById('histo-employee').value = result[datas].id;
            }
        }

    })
    .catch((error) => {
        console.log(error)
    })

})

// Save amount 
// =========================================================

$(document).on('click', '.btn-save-amount', function () {
    $id = $(this).attr('name');
    document.getElementById('modal1-window').style.display = "block";
    document.getElementById('employee_id_avance').value = $id;

})


// display student payment 

$(document).on('click', '.btnstdpay', function () {
    $id = $(this).attr('name');
    document.getElementById('stdpaiements').value = $id;

    let displayInTable = document.querySelector("#bottom-employee-main-content-right6");
    let forms = new FormData(document.getElementById("form-levelHisto"));
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/repport/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
            document.getElementById("repport-right-content").style.display = "none";
        }
        else {
            for (let datas in result[1]) {
                document.getElementById('getvalue').textContent = '$ '+ result[1][datas].sum;
                document.getElementById('getvalueContent').textContent = result[1][datas].content;

                document.getElementById('getCredit').style.display ="none";
                document.getElementById('getDebit').style.display = "none";
            }


            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Montant</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].lbl+'</td>';
                outputs += '<td>'+result[0][datas].amount+'</td>';
                outputs += '<td>'+result[0][datas].date+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById("repport-right-content").style.display = "block";
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })

})

// display Mixed Repport  (all content in one)

document.querySelector("#btn-rapport-mixed").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right6");
    const froms = new FormData(document.getElementById("form-mixHisto"));
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/repport/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
            document.getElementById("repport-right-content").style.display = "none";
        }
        else {
            for (let datas in result[1]) {
                document.getElementById('getvalueContent').textContent = result[1][datas].content;
                document.getElementById('getDebit').textContent ='Debit $ '+ result[1][datas].debit;
                document.getElementById('getCredit').textContent ='Credit $ ' + result[1][datas].credit;
                document.getElementById('getvalue').textContent = result[1][datas].debit - result[1][datas].credit;

                document.getElementById('getCredit').style.display ="block";
                document.getElementById('getDebit').style.display = "block";
            }


            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Debit</th>
                    <th>Credit</th>
                    <th>Balance</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].lbl+'</td>';
                outputs += '<td>'+result[0][datas].debit+'</td>';
                outputs += '<td>'+result[0][datas].credit+'</td>';
                outputs += '<td>'+result[0][datas].balance+'</td>';
                outputs += '<td>'+result[0][datas].dates+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById("repport-right-content").style.display = "block";
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

// display sold product from db 
// ==========================================

document.querySelector("#btn-repport-sold").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right6");
    const froms = new FormData(document.getElementById("form-soldproduct"));
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/repport/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
            document.getElementById("repport-right-content").style.display = "none";
        }
        else {
            for (let datas in result[1]) {
                document.getElementById('getvalueContent').textContent = result[1][datas].content;
                document.getElementById('getvalue').textContent ='$ ' + result[1][datas].debit ;

                document.getElementById('getCredit').style.display ="none";
                document.getElementById('getDebit').style.display = "none";
            }

            let outputs = `
            <table style="width: 97%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Produit</th>
                    <th>Designation</th>
                    <th>Vente</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].product+'</td>';
                outputs += '<td>'+result[0][datas].lbl+'</td>';
                outputs += '<td>'+result[0][datas].amount+'</td>';
                outputs += '<td>'+result[0][datas].date+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById("repport-right-content").style.display = "block";
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

// Autres depenses
// ========================================

document.querySelector("#btn-amount-dps").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right4");
    const froms = new FormData(document.getElementById("form-save-amount-dps"));
   
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
            document.getElementById("dps-right-content").style.display = "none";
        }

        

        else {
            for (let datas in result[1]) {
                document.getElementById('getdpsContent').textContent = result[1][datas].sum;
                document.getElementById('getvaluedp').textContent ='$ ' + result[1][datas].credit ;

            }

            let outputs = `
            <table style="width: 97%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Credit</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].designation+'</td>';
                outputs += '<td>'+result[0][datas].credit+'</td>';
                outputs += '<td>'+result[0][datas].date+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById("dps-right-content").style.display = "block";
        }
      
        
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}


// Display historic payment 
// ======================================

document.querySelector("#btn-dps-histo").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right4");
    const froms = new FormData(document.getElementById("dps-histo-form"));
   
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
            document.getElementById("dps-right-content").style.display = "none";
        }

        

        else {
            for (let datas in result[1]) {
                document.getElementById('getdpsContent').textContent = result[1][datas].sum;
                document.getElementById('getvaluedp').textContent ='$ ' + result[1][datas].credit ;

            }

            let outputs = `
            <table style="width: 97%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Credit</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].designation+'</td>';
                outputs += '<td>'+result[0][datas].credit+'</td>';
                outputs += '<td>'+result[0][datas].date+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById("dps-right-content").style.display = "block";
        }
      
        
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

