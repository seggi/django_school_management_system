// display employee 

document.querySelector("#btn_display_employee").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right4");
    const froms = new FormData(document.getElementById("hidden_form_employee_display"));
   
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
        }
        else {
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
                <thead>
                    <tr>
                        <th>Nom</th>
                        <th>Post-nom</th>
                        <th>Pres-nom</th>
                        <th>Activites</th>
                    </tr>
                </thead>
                <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result){
                outputs +='<tr>'
                outputs += '<td>'+result[datas].name+'</td>';
                outputs += '<td>'+result[datas].lastname+'</td>';
                outputs += '<td>'+result[datas].nickname+'</td>';
                outputs += `<td scope='col'>
                                <a class="btn-watch" name="${result[datas].id}">Details</a>   
                                <a class="btn-save-amount" name="${result[datas].id}">Montant</a>      
                            </td>`;
                
                outputs +='</tr>';
                   
                }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

// show details 

test = (name) => {alert(name);}

employDetails = () => {
    let gethidden = document.getElementById("emplaydetails");
    alert(gethidden)
    const forms1 = new FormData(document.getElementById("showEmployeeDetails"));
    fetch("/shule/cachier/outlay/",{
        method: 'POST',
        credentials: 'same-origin',       
        body: forms1,
        
        
    }).then(response => response.json())
    .then(result => {
        for(let datas in result){
            
        }
    })
}

// document.querySelector("#EmployDetails1").onclick = () => {
//     const forms1 = new FormData(document.getElementById("showEmployeeDetails"));
//     fetch("/shule/cachier/outlay/",{
//         method: 'POST',
//         credentials: 'same-origin',
//         body: forms1,
//     }).then(response => response.json())
//     .then(result => {
//         for(let datas in result){
//             alert('seggi')
//         }
//     })
// }


// outputs += '<tr>'+
// '<td>'+result[datas].name+'</td>'+
// '<td>'+result[datas].lastname+'</td>'+
// '<td>'+result[datas].nickname+'</td>'+
// '<td>'+'Voir'+addEventListener("click", () => { alert(result[datas].id)})+'</td>'+
// '</tr>';



// display employee salary history
// ==============================

document.querySelector("#btn-histo").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right4");
    const froms = new FormData(document.getElementById("histo-form"));
   
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
        }
        else {
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Montant</th>
                    <th>Solde</th>
                    <th>Date de payment</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result){
                outputs +='<tr>'
                outputs += '<td>'+result[datas].designation+'</td>';
                outputs += '<td>'+result[datas].amount+'</td>';
                outputs += '<td>'+result[datas].tot_payment+'</td>';
                outputs += '<td>'+result[datas].date+'</td>';
                
                outputs +='</tr>';
                   
                }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

// Save employee amount 

// ==================================

document.querySelector("#btn-amount-employee").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right4");
    const froms = new FormData(document.getElementById("form-save-amount-employee"));
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
        }
        else {
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Montant</th>
                    <th>Solde</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result){
                outputs +='<tr>'
                outputs += '<td>'+result[datas].designation+'</td>';
                outputs += '<td>'+result[datas].amount+'</td>';
                outputs += '<td>'+result[datas].tot_payment+'</td>';
                outputs += '<td>'+result[datas].date+'</td>';
                // outputs += `<td scope='col'>
                //                 <a class="btn-watch" name="${result[datas].id}">Details</a>   
                //                 <a class="btn-save-amount" name="${result[datas].id}">Montant</a>      
                //             </td>`;
                outputs +='</tr>';
                   
                }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}


// Selling products 
// ==============================

document.querySelector("#btn_display_article").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right5");
    const froms = new FormData(document.getElementById("hidden_form_article_display"));
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/sell/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
        }
        else {

            for (let datas in result[1]) {
                document.getElementById('productname').textContent = result[1][datas].article;
                document.getElementById('totsell').textContent = 'Total vente $'+ result[1][datas].totself;
            }
            
            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Article</th>
                    <th>Prix unitaire</th>
                    <th>Vente</th>
                    <th>Reste dans le stock</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].article+'</td>';
                outputs += '<td>'+result[0][datas].unit_amount+'</td>';
                outputs += '<td>'+result[0][datas].sold_amount+'</td>';
                outputs += '<td>'+result[0][datas].remaing+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}

// Save amount to db 
// ====================================

document.querySelector("#btn-article-amount").onclick = () => {
    let displayInTable = document.querySelector("#bottom-employee-main-content-right5");
    const froms = new FormData(document.getElementById("form-save-amount-article"));
    
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/outlay/sell/", {
        method: "POST",
        credentials: "same-origin",
        body: froms,
    }).then(response => response.json())
    .then(result => {
        
        if (result.error){
            alert(result.error);
        }
        else {
            for (let datas in result[1]) {
                document.getElementById('productname').textContent = result[1][datas].article;
                document.getElementById('totsell').textContent = 'Total vente $'+ result[1][datas].totself;
            }


            let outputs = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Article</th>
                    <th>Prix unitaire</th>
                    <th>Vente</th>
                    <th>Reste dans le stock</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            let name ='{% csrf_token %}';

            for(let datas in result[0]){
                outputs +='<tr>'
                outputs += '<td>'+result[0][datas].article+'</td>';
                outputs += '<td>'+result[0][datas].unit_amount+'</td>';
                outputs += '<td>'+result[0][datas].sold_amount+'</td>';
                outputs += '<td>'+result[0][datas].remaing+'</td>';
                outputs +='</tr>';

            }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
        }
    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}