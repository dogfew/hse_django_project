let helloButton = document.getElementById("helloButton");
let byeButton = document.getElementById("byeButton");
let askButton = document.getElementById("askButton");
let gayButton = document.getElementById("gayButton");
let clearButton = document.getElementById("clearButton");

helloButton.onclick = function() {
    let name = prompt('Tell me your name!');
    document.getElementById("script").innerHTML +=
        "<br>" + (`${name}, you are welcome!`);
}

byeButton.onclick = function() {
    let name = prompt('You dare!');
    document.getElementById("script").innerHTML +=
        "<br>" + (`${name}, get out of here!`);
}

askButton.onclick = function() {
    document.getElementById("script").innerHTML +=
        "<br>" + "This was created by Vladimir Perepelkin";
}

gayButton.onclick = function() {
    document.getElementById("script").innerHTML +=
        "<br>" + "Yes. I hope, you like it.";
}

clearButton.onclick = function() {
    document.getElementById("script").innerHTML =
        "This page does not have any meaning, but it is created for educational purposes and may contain educational and entertaining content. Welcome!" +
        "\n"
}