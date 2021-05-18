function myFunction() {
    axios.get("https://manglish-lyrics-generator.herokuapp.com/").then(response => {
        console.log(response);
        document.getElementById("demo").innerHTML = response.data.lyrics;
    })
}