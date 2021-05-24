var x = "Generating...";

function visible(){
    var y = document.getElementById("scroller");
    y.style.display = "block";
}

function clearFunction(){
    var y = document.getElementById("scroller");
    y.style.display = "none";
}

function myFunction() {
    document.getElementById("demo").innerHTML = x;
    visible();
    axios.get("https://manglish-lyrics-generator.herokuapp.com/").then(response => {
        console.log(response);
        document.getElementById("demo").innerHTML = response.data.lyrics;
    })    
}
