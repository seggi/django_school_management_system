
displaysDropdown = () => {
    document.getElementById("contentDropDown").classList.toggle("displayed");
    
}

window.onclick = (event) => {
    if (!event.target.matches('.dropdownbtn')){
        var  dropdowns = document.getElementsByClassName("box-content");
        var i;
        for(i=0; i < dropdowns.length; i++){
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('displayed')) {
                openDropdown.classList.remove('displayed');
            }
        }
    }
}


displaySelect = () =>{
    document.getElementById('pop_recorver_small_screen').style.display ="block";
}

closeSelect = () => {
    document.getElementById('pop_recorver_small_screen').style.display ="none";
}

displaysDropdownbtn = () => {
    document.getElementById('contentDropDown1').classList.toggle("displayed2");
}

window.onclick = (event) => {
    if (!event.target.matches('.btn_search_student_recouvre')){
        var  dropdowns = document.getElementsByClassName("box-content2");
        var i;
        for(i=0; i < dropdowns.length; i++){
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('displayed2')) {
                openDropdown.classList.remove('displayed2');
            }
        }
    }
}