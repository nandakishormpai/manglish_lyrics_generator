var x = "Generating...";

// Globally calling so that We get a Lyrics ready for the user
axios.get("https://manglish-lyrics-generator.herokuapp.com/").then(response => {
        console.log("first");
        x = response.data.lyrics;
})

function visible(){
    var y = document.getElementById("scroller");
    y.style.display = "block";
}

function clearFunction(){
    var y = document.getElementById("scroller");
    y.style.display = "none";
}

function myFunction() {
    var prev_lyrics;
    document.getElementById("demo").innerHTML = x;
    visible();
    axios.get("https://manglish-lyrics-generator.herokuapp.com/").then(response => {
        document.getElementById("demo").innerHTML = x;
        prev_lyrics = x;
        console.log("second");
        x = response.data.lyrics;
        if(prev_lyrics.localeCompare("Generating...")==0){
            document.getElementById("demo").innerHTML = x;
        }
    })    
}
