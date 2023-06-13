let domGames = document.querySelector("#domGames");
let spans = document.querySelectorAll("span")


for (spans in domGames){
    if(spans.innertext = "None")
        spans.classList.add("Hide");
}