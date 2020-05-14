// getting the username of the user and storing it in local storage
/*document.addEventListener("DOMContentLoaded", () =>{
    document.querySelector('#form').onsubmit = () =>{
        // getting the user name from the form
        const username = document.querySelector("#username").value;
        alert(username);
        // storing the username in local storage
        localStorage.setItem("username",username);
        // setting the h1 tag in layout to welcome the user
        h1 = document.createElement("h1");
        h1.idAttribute("welcome_user");
        h1.innerHTML =  `Welcome ${username}`;


    }
    }
);

*/

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('#form').onsubmit = () => {
        // getting the user name from the form
        request = new XMLHttpRequest();
        request.open("POST", "/user");
    };
});


