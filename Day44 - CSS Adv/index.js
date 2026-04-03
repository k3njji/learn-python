function validate(){
    const username = document.getElementById("username").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const repassword = document.getElementById("repassword").value
    const agreement = document.getElementById("agreement")
    const selectedCountry = document.getElementById("countrypick").value;
    console.log(username)
    console.log(email)
    console.log(password)
    console.log(repassword)
    console.log(selectedCountry)



    if(username.length < 3){
        alert("Username Length Must Consist of 3 Letters")
    }
    else if((!email.endsWith(".com")) || (!email.includes("@"))){
        alert("Please Enter A Valid Email")
    }
    else if( (checkPass(password) == false) || (password.length < 6)){
        alert("Password Must Consist A Number and Minimum 6 Characters Long")
    }
    else if( password !== repassword ){
        alert("Please Make Sure the Password You Re-Input is Correct")
    }
    else if( selectedCountry === "select" ){
        alert("Please Pick a Country")
    }
    else if(!agreement.checked){
        alert("You Have To Agree To our Terms and Conditon")
    }
    else{
        
    }
}

function checkPass(password){
    var isAlpha = false
    var isNum = false

    for(let i = 0; i < password.length; i++){
        if(isNaN(password[i])){
            isAlpha = true
        }else{
            isNum = true
        }
    }

    if(isAlpha == false || isNum == false){
        return false
    }
    return true
}

hamburger = document.querySelector(".theline")
hamburger.onclick = function(){
    navBar = document.querySelector(".middle2");
    navBar.classList.toggle("active");
}