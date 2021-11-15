// btn_register_student


$(function() {
    $('#btn_register_student1').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/secretary/register_student/",
            type: 'POST', 
            data: $('#main_form_register_student').serialize(),
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

// ++++++++++ Display Student List in table ++++++++++

$(function() {
    $('#btn_display_student_registered').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/secretary/register_student/",
            type: 'POST', 
            data: $('#main_form_display_students_registered').serialize(),
            dataType: 'json',
            success: function(data){
                if (data) {
                    $('#update_tbl5').html(data);
                    $.each(data, function(key, value) {
                        if (value.faculty == null ){
                            $('#main_student_list').prepend(
                    
                            `<tr>
                                <td scope='col'>
                                    <span>
                                        <input id="action-toggle" name="selectTbl" 
                                        type="checkbox" value=${value.id||""}>
                                    </span>
                                </td>
                                <td>${value.name||""} ${value.lastname||""} ${value.nickname||""}</td>
                                <td>${value.sex||""}</td>
                                <td>${value.age||""}</td>
                                <td>${value.classe||""}</td>
                                <td>${"RAS"}</td>
                                <td>${value.parent_name||""} ${value.parent_last||""}</td>
                                <td>${value.address||""}</td>
                                <td>${value.phone||""}</td>
                            </tr>
                            `
                            )
                        }
                        else{
                            $('#main_student_list').prepend(
                    
                                `<tr>
                                    <td scope='col'>
                                        <span>
                                            <input id="action-toggle" name="selectTbl" 
                                            type="checkbox" value=${value.id||""}>
                                        </span>
                                    </td>
                                    <td>${value.name||""} ${value.lastname||""} ${value.nickname||""}</td>
                                    <td>${value.sex||""}</td>
                                    <td>${value.age||""}</td>
                                    <td>${value.classe||""}</td>
                                    <td>${value.faculty||""}</td>
                                    <td>${value.parent_name||""} ${value.parent_last||""}</td>
                                    <td>${value.address||""}</td>
                                    <td>${value.phone||""}</td>
                                </tr>
                                `
                                )
                        }

                    });  
                }
                
                else{
                    alert(data.error);
                }
            }, 
        });
    });
});

// +++++++++++++++++++++++++++++++++++++++++++++++++++

$(document).ready(function() {
    load_json_data('select_level1');
    var defaults = '';
    function load_json_data(ids, selected){
        var html_code = '';
       
        $.getJSON('/shule/secretary/show_level_classe/', function(data){
            html_code += '<option value="" selected disabled>Fait une selection '+defaults+'</option>';
            $.each(data, function(key, value){
                if(ids == 'select_level1'){
                    if(value.level){
                        html_code += '<option value="'+value.id+'">'+value.level+'</option>';
                    }
                }

                if(ids =='select_classe1') {
                    if(value.levels == selected){
                        html_code += '<option value="' + value.id+'">'+value.classe+'</option>';
                    }
                }

                if(ids =='select_facutly1') {
                    if(value.classes == selected){
                        html_code += '<option value="' + value.id+'">'+value.faculty+'</option>';
                    }
                }

            });
            $('#'+ids).html(html_code);

        });
    }

    $(document).on('change', '#select_level1', function(){
        var level_id  = $(this).val();
        if(level_id != ''){
            load_json_data('select_classe1', level_id );
        }
        else{
            $('#select_classe1').html('<option value="">Select classe</option>');
            $('#select_facutly1').html('<option value="">Select faculty</option>');
        }
    });

    $(document).on('change', '#select_classe1', function(){
        var classes_id  = $(this).val();
        if(classes_id != ''){
            load_json_data('select_facutly1', classes_id );

        }
        else{
            $('#select_facutly1').html('<option value="">Select facutly</option>');
        }
    });
});


// Register employee session.......................

$(function() {
    $('#btn_register_employee1').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/secretary/register_employee/",
            type: 'POST', 
            data: $('#main_form_register_employee').serialize(),
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

// ++++++++++ Display employee List in table ++++++++++

$(function() {
    $('#btn_display_employee_registered').click(function(e) {
        e.preventDefault();
        $.ajax({
            url: "/shule/secretary/display_employee/",
            type: 'POST', 
            data: $('#main_form_employees_registered').serialize(),
            dataType: 'json',
            success: function(data){
                if (data) {
                    $('#update_tbl6').html(data);
                    
                    $.each(data, function(key, value) {
                        if (value){
                            $('#main_employee_list').prepend(
                    
                            `<tr>
                                <td scope='col'>
                                    <span>
                                        <input id="action-toggle" name="selectTbl" 
                                        type="checkbox" value=${value.id||""}>
                                    </span>
                                </td>
                                <td>${value.name||""} ${value.lastname||""} ${value.nickname||""}</td>
                                <td>${value.sex||""}</td>
                                <td>${value.age||""}</td>
                                <td>${value.email||""}</td>
                                <td>${value.phone||""} </td>
                                <td>${value.function||""}</td>
                            </tr>
                            `
                            )
                        }

                    });  
                }
                
                else{
                    alert(data.error);
                }
            }, 
        });
    });
});




















addPagerToTables('#main_student_list', 2);

function addPagerToTables(tables, rowsPerPage = 10) {
    tables = 
        typeof tables == "string"
      ? document.querySelectorAll(tables)
      : tables;

    for (let table of tables) 
        addPagerToTable(table, rowsPerPage);

}

function addPagerToTable(table, rowsPerPage = 10) {

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


