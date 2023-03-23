function generateRandom() {
  number = Math.floor(Math.random() * 100) + 1;
  document.getElementById("random").innerHTML = (`${number}`);
}


function calc() {
  let input = document.getElementById("field").value;
  let result = eval(input.replaceAll("log", "Math.log")
      .replaceAll("pi", "Math.PI").replaceAll("e", "Math.E")
      .replaceAll("sin", "Math.sin").replaceAll("cos", "Math.cos")
      .replaceAll("min", "Math.min").replaceAll("max", "Math.max")
      .replaceAll("abs", "Math.abs").replaceAll("round", "Math.round")
      .replaceAll("sqrt", "Math.sqrt").replaceAll("random", "Math.random")
      .replaceAll("^", "**").replaceAll("_", "").replaceAll("$", ""));
  if (Math.abs(result) < 1e-12){
    result=0;
  }
  document.getElementById("res").innerHTML
      += "&nbsp;&nbsp;&nbsp;&nbsp;" + input + "  --->  " + result + "<br>";
  document.getElementById("field").value = '';
  document.getElementById("field").focus();
}

function clearField(){
  document.getElementById("res").innerHTML = "";
}
