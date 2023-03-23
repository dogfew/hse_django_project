function addFormula() {
  let input = document.getElementById("formula").value;
  if (input.replace(" ", "") === ""){
    return 0;
  }
  MathJax.typeset();
  document.getElementById("script").innerHTML
      += MathJax.tex2chtml(input, {display: true}).outerHTML;
  document.getElementById("formula").value = '';
  document.getElementById("formula").focus();
  MathJax.typeset();
}
