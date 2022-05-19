const username = document.getElementById("username");
const text = document.getElementById("text");
const main = document.getElementById("main");
const content = document.getElementById("content");

function addUsername() {
        const name = document.createElement("p");
        name.innerText = "Welcome " + text.value + " !";
        name.className = "login";
        content.appendChild(name);
        const input = "name " + localStorage.length;
        localStorage.setItem(input, text.value);
    }

function display() {
    for (let i= 0; i < localStorage.length; i++) {
        const value = localStorage.getItem("name " + i);
        const name = document.createElement("p");
        name.innerText = "Welcome back " + value + " !";
        name.className= "login";
        content.appendChild(name);
    }
}



username.addEventListener("click", addUsername);
display();