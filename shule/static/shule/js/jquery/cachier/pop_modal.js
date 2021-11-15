

function openStudentSearchModal(){
    document.getElementById('small_pop_screen').style.display = 'block';
}

function closeStudentSearchModal(){
    document.getElementById('small_pop_screen').style.display = 'none';
}




function displayStudentSearch() {
    document.getElementById('small_pop_screen').style.display = 'none';
    document.getElementById('one-top-employee-main-content-right').style.display = 'block';
    document.getElementById("bottom-employee-main-content-right").style.display = 'block';
    document.getElementById('employee-left-box').style.display = 'flex';
    document.getElementById('display_form_fee_type_cachier').style.display = 'none';
    document.getElementById('bottom-employee-main-content-right1').style.display = 'none';
    document.getElementById('search_range_form').style.display = 'inline-flex';
    document.getElementById('btn_search_student1').style.display = 'block';
    document.getElementById('extend_paiement').style.display ="none";


    // close payment
    document.getElementById('one-top-employee-main-content-right1').style.display = 'none';

    // display student datails

    document.getElementById('update_connte1').innerHTML = '';
    document.getElementById('update_connte2').innerHTML = '';
    document.getElementById('update_connte3').innerHTML = '';
    document.getElementById('update_connte4').innerHTML = '';
    document.getElementById('update_connte5').innerHTML = '';
    document.getElementById('update_connte6').innerHTML = '';
    document.getElementById('update_connte7').innerHTML = '';
    document.getElementById('update_connte8').innerHTML = '';
    // document.getElementById("result_hidden1").value = '';
    // document.getElementById("update_tblstudent").innerHTML ='';
    const form = new FormData(document.getElementById('search_student_form'));

    let element = document.createElement("h2");
    let element1 = document.createElement("h2");
    let element2 = document.createElement("h2");
    let element3 = document.createElement("h2");
    let element4 = document.createElement("h2");
    let element5 = document.createElement("h2");
    let element6 = document.createElement("h2");
    let element7 = document.createElement("h2");

    required = () => {
        var inputs = document.forms['search_student_form']['searchinput1'].value;
        var inputs1 = document.forms['search_student_form']['searchinput2'].value;
        
        if(inputs == ""){
            alert("Vous avez oublie de mentionner le nom");
            return false
        }
        else if(inputs1 == ""){
            alert("Vous avez oublie de mentionner le post-nom");
            return false
        }
        

        fetch('/shule/cachier/search_student/', {
            method: 'POST',
            credentials: 'same-origin',
            body: form,

        }).then(
            response => response.json()).then(
                data => { 
                  for(let maps in data){
                    if(data[maps].faculty != null){
                        element.className = "";
                        element.textContent = data[maps].name+' '+ data[maps].lastname +' '+ data[maps].nickname;
                        element1.textContent = data[maps].classe;
                        element2.textContent = data[maps].faculty;
                        element3.textContent = data[maps].id;
                        element4.textContent = data[maps].totamount;
                        element5.textContent = data[maps].amount;
                        element6.textContent = data[maps].first;
                        element7.textContent = data[maps].second;
                    
                        document.getElementById("update_connte1").appendChild(element);
                        document.getElementById("update_connte2").appendChild(element1);
                        document.getElementById("update_connte3").appendChild(element2);
                        document.getElementById("update_connte4").appendChild(element3);
                        document.getElementById("update_connte5").appendChild(element4);
                        document.getElementById("update_connte6").appendChild(element5);
                        document.getElementById("update_connte7").appendChild(element6);
                        document.getElementById("update_connte8").appendChild(element7);
                        document.getElementById("update_connte9").value = data[maps].id;
                        document.getElementById("result_hidden1").value = data[maps].id;
                        document.getElementById("range_student_u").value = data[maps].id;
                        
                    }

                    else if(data[maps].faculty == null){
                        element.className = "";
                        element.textContent = data[maps].name+' '+ data[maps].lastname +' '+ data[maps].nickname;
                        element1.textContent = data[maps].classe;
                        element2.textContent = 'RAS';
                        element3.textContent = data[maps].id;
                        element4.textContent = data[maps].totamount;
                        element5.textContent = data[maps].amount;
                        element6.textContent = data[maps].first;
                        element7.textContent = data[maps].second;
                    
                        document.getElementById("update_connte1").appendChild(element);
                        document.getElementById("update_connte2").appendChild(element1);
                        document.getElementById("update_connte3").appendChild(element2);
                        document.getElementById("update_connte4").appendChild(element3);
                        document.getElementById("update_connte5").appendChild(element4);
                        document.getElementById("update_connte6").appendChild(element5);
                        document.getElementById("update_connte7").appendChild(element6);
                        document.getElementById("update_connte8").appendChild(element7);
                        // document.getElementById("result_hidden").value = data[maps].id;
                        document.getElementById("result_hidden1").value = data[maps].id;
                        document.getElementById("range_student_u").value = data[maps].id;
                        document.getElementById("update_connte9").value = data[maps].id;

                    }

                  }
                }
            ).catch(( error ) => {
                alert('Error from server!, pleaze check your internet connection.', error)
            });        
        
    }
   required()
}


// Display to table  student historique

document.querySelector("#btn_search_student1").onclick = () => {
    document.getElementById('bottom-employee-main-content-right2').style.display = 'none';
    document.getElementById('bottom-employee-main-content-right').style.display = 'block';
    let displayInTable = document.querySelector("#bottom-employee-main-content-right");
    let hidden_id = document.getElementById("result_hidden1").value;
    const hidden_form = new FormData(document.getElementById("hidden-form"));
    displayInTable.textContent = "Chargement des donnes...";

    fetch("/shule/cachier/search_student/", {
        method: 'POST',
        credentials: 'same-origin',
        body: hidden_form,
    }
    ).then( response => response.json()).then(
        result => {
            if (result.error){
                alert(result.error);
            }

            else {

            let output = `
            <table style="width: 60%; overflow-x:auto;" id="main_student_history_list" class="order-table table">
            <thead>
                <tr>
                    <th>Designation</th>
                    <th>Paiement</th>
                    <th>Solde</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody id="update_tblstudent">`;
            
            // document.getElementById("main_student_history_list").innerHTML = '';
            for(let data in result) {
               
                if (result[data].faculty != null ){
                    

                    output += '<tr>'+
                        '<td>'+result[data].feetype+'</td>'+
                        '<td>'+result[data].amount+'</td>'+
                        '<td>'+result[data].balance+'</td>'+
                        '<td>'+result[data].date+'</td>'+
                        '</tr>';
                    
                }
                else if (result[data].faculty == null ){
                    output += '<tr>'+
                        '<td>'+result[data].feetype+'</td>'+
                        '<td>'+result[data].amount+'</td>'+
                        '<td>'+result[data].balance+'</td>'+
                        '<td>'+result[data].date+'</td>'+
                        '</tr>';
                }
            }
            output += ` 
                        </tbody>
                    </table>`;
            
            displayInTable.innerHTML = output;
            
        }
     }
    ).catch((error) => {
        alert('Error from server!, pleaze check your internet connection.', error);
    })
}


// display fee content

function displayFeeSearch() {
    document.getElementById('one-top-employee-main-content-right').style.display = 'none';
    document.getElementById("bottom-employee-main-content-right1").style.display = 'block';
    document.getElementById('bottom-employee-main-content-right2').style.display = 'none';
    document.getElementById('employee-left-box').style.display = 'flex';
    document.getElementById('one-top-employee-main-content-right1').style.display = 'block';
    document.getElementById('display_form_fee_type_cachier').style.display = 'flex';
    document.getElementById('bottom-employee-main-content-right').style.display = 'none';
    document.getElementById('search_range_form').style.display = 'none';
    document.getElementById('btn_search_student1').style.display = 'none';
    document.getElementById('extend_paiement').style.display ="none";

}

// display btn fees

document.querySelector("#btn_diplay_fee_type_cachier").onclick = () => {
    document.getElementById('update_conntec1').innerHTML = '';
    document.getElementById('update_conntec2').innerHTML = '';
    document.getElementById('update_conntec3').innerHTML = '';
    document.getElementById('update_conntec4').innerHTML = '';

    let displayInTable = document.querySelector("#bottom-employee-main-content-right1");
    const hidden_form = new FormData(document.getElementById("display_form_fee_type_cachier"));
    displayInTable.textContent = "Chargement des donnes...";

    let element1 = document.createElement("h2");
    let element2 = document.createElement("h2");
    let element3 = document.createElement("h2");
    let element4 = document.createElement("h2");

    fetch("/shule/cachier/search_student/", {
        method: 'POST',
        credentials: 'same-origin',
        body: hidden_form,
    }
    ).then( response => response.json()).then(
        result => {
            if (result.error){
                alert(result.error);
            }

            else {

                for(let data in result){

                    if(result[data].faculty != null ){
                        element1.textContent = result[data].level;
                        element2.textContent = result[data].classe;
                        element3.textContent = result[data].faculty;
                        element4.textContent = result[data].totamount;
                        document.getElementById("update_conntec1").appendChild(element1);
                        document.getElementById("update_conntec2").appendChild(element2);
                        document.getElementById("update_conntec3").appendChild(element3);
                        document.getElementById("update_conntec4").appendChild(element4);
                    
                    }

                    else if(result[data].faculty == null ){
                        element1.textContent = result[data].level;
                        element2.textContent = result[data].classe;
                        element3.textContent = 'RAS';
                        element4.textContent = result[data].totamount;
                        document.getElementById("update_conntec1").appendChild(element1);
                        document.getElementById("update_conntec2").appendChild(element2);
                        document.getElementById("update_conntec3").appendChild(element3);
                        document.getElementById("update_conntec4").appendChild(element4);
                  
                    }

                }

            let output = `
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
            
            for(let data in result) {
               
                if (result[data].faculty != null ){
                    output += '<tr>'+
                        '<td>'+result[data].type+'</td>'+
                        '<td>'+result[data].periode+'</td>'+
                        '<td>'+result[data].tranche+'</td>'+
                        '<td>'+result[data].totamount+'</td>'+
                        '</tr>';
                    
                }
                else if (result[data].faculty == null ){
                    output += '<tr>'+
                        '<td>'+result[data].type+'</td>'+
                        '<td>'+result[data].periode+'</td>'+
                        '<td>'+result[data].tranche+'</td>'+
                        '<td>'+result[data].totamount+'</td>'+
                        '</tr>';
                }
            }
            output += ` 
                        </tbody>
                    </table>`;
            
            displayInTable.innerHTML = output;
            
        }
     }
    ).catch((error) => {
        alert('Error from server!, pleaze check your internet connection.', error);
    })
}


// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

addPagerToTables('#main_student_history_list', 4);

// Paginate all tables

function addPagerToTables(tables, rowsPerPage = 8) {

    tables = 
        typeof tables == "string"
      ? document.querySelectorAll(tables)
      : tables;

    for (let table of tables) 
        addPagerToTable(table, rowsPerPage);

}

function addPagerToTable(table, rowsPerPage = 8) {

    let tBodyRows = table.querySelectorAll('tBody tr');
    let numPages = Math.ceil(tBodyRows.length/rowsPerPage);

    let colCount = 
    [].slice.call(
        table.querySelector('tr').cells
    )
    .reduce((a,b) => a + parseInt(b.colSpan), 0);

    table
    .createTFoot()
    .insertRow()
    .innerHTML = `<td colspan=${colCount}><div class="nav"></div></td>`;

    if(numPages == 1)
        return;

    for(i = 0;i < numPages;i++) {

        let pageNum = i + 1;

        table.querySelector('.nav')
        .insertAdjacentHTML(
            'beforeend',
            `<a href="#" rel="${i}">${pageNum}</a>`        
        );

    }

    changeToPage(table, 1, rowsPerPage);

    for (let navA of table.querySelectorAll('.nav a'))
        navA.addEventListener(
            'click', 
            e => changeToPage(
                table, 
                parseInt(e.target.innerHTML), 
                rowsPerPage
            )
        );

}

function changeToPage(table, page, rowsPerPage) {

    let startItem = (page - 1) * rowsPerPage;
    let endItem = startItem + rowsPerPage;
    let navAs = table.querySelectorAll('.nav a');
    let tBodyRows = table.querySelectorAll('tBody tr');

    for (let nix = 0; nix < navAs.length; nix++) {

        if (nix == page - 1)
            navAs[nix].classList.add('active');
        else 
            navAs[nix].classList.remove('active');

        for (let trix = 0; trix < tBodyRows.length; trix++) 
            tBodyRows[trix].style.display = 
                (trix >= startItem && trix < endItem)
                ? 'table-row'
                : 'none';  

    }

}

// }












// output.appendChild(rows);
// var tds = document.createElement("TD");
// var datastxt = document.createTextNode(result[data].name);
// tds.appendChild(datastxt);
// document.getElementById("myTr").appendChild(z);

















 // fetch('/shule/cachier/search_student/', {
        //     method: 'GET',
        //     headers: {'Content-Type': 'application/json',},
        //     credentials: 'same-origin',

        // }).then(
        //     response => response.json()).then(
        //         data => { 
        //             alert(data);
        //         }
        //     ).catch(( error ) => {
        //         alert('Error', error)
        //     });