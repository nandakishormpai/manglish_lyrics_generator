function visible(){
    var x = document.getElementById("scroller");
    x.style.display = "block";
}


function myFunction() {
    axios.get("https://manglish-lyrics-generator.herokuapp.com/").then(response => {
        console.log(response);
        visible();
        document.getElementById("demo").innerHTML = response.data.lyrics;
    })
    
}

