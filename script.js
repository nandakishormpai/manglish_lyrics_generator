var x = "Generating...";
var keyword;

function visible() {
    var y = document.getElementById("scroller");
    y.style.display = "block";
}

function clearFunction() {
    document.getElementById("myForm").reset();
    var y = document.getElementById("scroller");
    y.style.display = "none";
}


function myFunction() {
    var elements = document.getElementById("myForm").elements;
    if (elements[0].value == "") {
        alert("Enter one or More Manglish words !");
    } else if (elements[0].value.includes("(") ||
        elements[0].value.includes(")")) {
        alert("Enter only Manglish keywords !");
        clearFunction();
    } else {
        document.getElementById("demo").innerHTML = x;
        visible();
        keyword = elements[0].value;
        console.log(keyword)
        axios.post("https://manglish-lyrics-generator.herokuapp.com/", json = { "keyword": keyword }).then(response => {
            console.log(response);
            var failed = "Keyword not found";
            if (response.data.lyrics.includes(failed)) {
                clearFunction();
                alert(response.data.lyrics);
            } else {
                document.getElementById("demo").innerHTML = response.data.lyrics;
            }

        })
    }

}