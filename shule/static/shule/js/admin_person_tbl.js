
// Display function with emplayees
// ======================================================

$(document).on('click', '.btn-prn-dts', function() {
    $id = $(this).attr('name');
    document.getElementById("getftn").value = $id;
    document.getElementById('btnftn').style.visibility = "visible";
    document.getElementById('tbl-right').style.display = "block";
    document.getElementById('main_personnel_t').style.display = "none";

    let displayInTable = document.querySelector("#tbl-right");
    const forms = new FormData(document.getElementById("dplftn-form"));

    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/admin/edit/employee/item/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error) {
            alert(result.error);
        }

        else {
            
            let outputs = `
            <table style="width: 90%; overflow-x:auto;" id="main_personnel_t1" class="order-table table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Noms</th>
                        <th>Post-nom</th>
                        <th>Pre-nom</th>
                        <th>Salary</th>
                        <th>Activites</th>
                    </tr>
                </thead>
                <tbody>`;
            
            for(let datas in result) {
                outputs += '<tr>'
                outputs += '<td>'+result[datas].name+'</td>';
                outputs += '<td>'+result[datas].lastname+'</td>';
                outputs += '<td>'+result[datas].nickname+'</td>';
                outputs += '<td>'+result[datas].salary+'</td>';
                outputs += `<td scope='col'>
                                <a class="btn-dlt" name="${result[datas].id}">Retirer</a>   
                                <a class="btn-edt" name="${result[datas].id}">Actualiser</a>      
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
    
});


// opent delete modal  & and send delete request
// ===============================================

$(document).on("click", ".btn-dlt", function() {
    $id = $(this).attr("name");
    document.getElementById("rmv_emp").value = $id;
    document.getElementById("dlt-pop-screen").style.display = "block";
});

// remove employee function

document.querySelector("#btn-dlt-emp-form").onclick = () => {
    let displayInTable = document.querySelector("#tbl-right");
    const forms = new FormData(document.getElementById("dlt-emp-form"));

    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/admin/edit/employee/item/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error) {
            alert(result.error);
        }

        else {
            
            let outputs = `
            <table style="width: 90%; overflow-x:auto;" id="main_personnel_t1" class="order-table table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Noms</th>
                        <th>Post-nom</th>
                        <th>Pre-nom</th>
                        <th>Salary</th>
                        <th>Activites</th>
                    </tr>
                </thead>
                <tbody>`;
            
            for(let datas in result) {
                outputs += '<tr>'
                outputs += '<td>'+result[datas].name+'</td>';
                outputs += '<td>'+result[datas].lastname+'</td>';
                outputs += '<td>'+result[datas].nickname+'</td>';
                outputs += '<td>'+result[datas].salary+'</td>';
                outputs += `<td scope='col'>
                                <a class="btn-dlt" name="${result[datas].id}">Retirer</a>   
                                <a class="btn-edt" name="${result[datas].id}">Actualiser</a>      
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

// Edit employee item display first

$(document).on('click', '.btn-edt', function() {
    $id = $(this).attr('name');
    document.getElementById('edt_emp').value = $id;
    document.getElementById('edt-pop-screen').style.display = "block";

    // send form
    const forms = new FormData(document.getElementById("hidden-edt-emp-form"));

    fetch("/shule/admin/edit/employee/item/", {
        method: "POST",
        credentials:  "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error) {
            alert(result.error);
        }
        else{
            for(let datas in result){
                // display item to modal
                document.getElementById("edtname").value = result[datas].name;
                document.getElementById("edtlastname").value = result[datas].lastname;
                document.getElementById("edtnickname").value = result[datas].nickname;
                document.getElementById("edtamount").value = result[datas].salary;
                document.getElementById("get-item-id").value = result[datas].id;
            }
        }
    })
    .catch((error) => {
        console.log(error);
    })
})

// Edit item after displaying

document.querySelector("#btn-edt-emp-form").onclick = () => {
    let displayInTable = document.querySelector("#tbl-right");
    const forms = new FormData(document.getElementById("edt-emp-form"));

    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/admin/edit/employee/item/", {
        method: "POST",
        credentials: "same-origin",
        body: forms,
    }).then(response => response.json())
    .then(result => {
        if (result.error) {
            alert(result.error);
        }

        else {
            
            let outputs = `
            <table style="width: 90%; overflow-x:auto;" id="main_personnel_t1" class="order-table table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Noms</th>
                        <th>Post-nom</th>
                        <th>Pre-nom</th>
                        <th>Salary</th>
                        <th>Activites</th>
                    </tr>
                </thead>
                <tbody>`;
            
            for(let datas in result) {
                outputs += '<tr>'
                outputs += '<td>'+result[datas].name+'</td>';
                outputs += '<td>'+result[datas].lastname+'</td>';
                outputs += '<td>'+result[datas].nickname+'</td>';
                outputs += '<td>'+result[datas].salary+'</td>';
                outputs += `<td scope='col'>
                                <a class="btn-dlt" name="${result[datas].id}">Retirer</a>   
                                <a class="btn-edt" name="${result[datas].id}">Actualiser</a>      
                            </td>`;
                
                outputs +='</tr>';
                   
                }
                
            outputs +=`
                    </tbody>
                </table>`;
            displayInTable.innerHTML = outputs;
            document.getElementById('edt-pop-screen').style.display = "none";
        }
       

    }).catch((error) => {
        alert(error),
        console.error(error);
    })
}
        