var x = "Generating...";
// function readkeyWord(){
//     var keyword = document.getElementById("key");
//     console.log(keyword);
// }
var keyword;

function readkeyWord() {
    var keyword = document.getElementById("myForm")
    // document.getElementById("myForm").submit();
    console.log(keyword);
}

function visible(){
    var y = document.getElementById("scroller");
    y.style.display = "block";
}

function clearFunction(){
    var y = document.getElementById("scroller");
    y.style.display = "none";
}


function myFunction() {

    var elements = document.getElementById("myForm").elements;
    if (elements[0].value != "" )
        {
        document.getElementById("demo").innerHTML = x;
        visible();
        keyword = elements[0].value;
        console.log(keyword)
        axios.post("https://manglish-lyrics-generator.herokuapp.com/", json = {"keyword": keyword} ).then(response => {
            console.log(response);
            var failed = "Keyword not found";
            if(response.data.lyrics.includes(failed)){
                document.getElementById("myForm").reset();
                clearFunction();
                alert(response.data.lyrics);
            }
            else{
                document.getElementById("demo").innerHTML = response.data.lyrics;
            }

        })
    }
    else
    {
        alert("Enter a keyword !");
    }
}
