const additem = document.getElementById("additem");
const text = document.getElementById("text");
const main = document.getElementById("main");
const content = document.getElementById("content");

function addingitem() {
    const item = document.createElement("p");
    item.innerText = text.value;
    item.className = "beautiful";
    content.appendChild(item);
    const input = "item " + localStorage.length;
    localStorage.setItem(input, text.value);
}

function display() {
    for (let i= 0; i < localStorage.length; i++) {
        const value = localStorage.getItem("item " + i);
        const item = document.createElement("p");
        item.innerText = value;
        item.className= "beautiful";
        content.appendChild(item);
    }
}

additem.addEventListener("Click", addingitem);
display();