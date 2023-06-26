
document.addEventListener("DOMContentLoaded", function() {
    let domGames = document.querySelector("#domGames");
    let spans = document.querySelectorAll("span")
  
    for (var i = 0; i < spans.length; i++) {
        var span = spans[i];
  
        if (span.innerText === "Score: None") {
            let before = spans[i - 1];
            console.log(before)
            if(before){
                before.classList.add("Hide");
            }
            span.classList.add("Hide");
        }
    }

});  