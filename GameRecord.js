let selectGame = document.querySelector("#gameSelect");

selectGame.addEventListener('change', () => {
    let val = selectGame.value;
    console.log(val);
    let games = document.querySelectorAll(".gameWrapper");

    
    if(val !== "allGames"){
        for(let i = 0; i < games.length; i++){
            console.log("removing")
            console.log(val);
            console.log(games[i].id)
            if(val !== games[i].id) {
                console.log("Removed")
                games[i].classList.add("Hide");
            } else {
                console.log("wtf")
                games[i].classList.remove("Hide");
            }
        }
    } else {
        console.log("whaha  ")
        for(let i = 0; i < games.length; i++){
            console.log(games[i])
            games[i].classList.remove("Hide");
        }
    }



})

let tables = document.querySelectorAll("tbody");

for(let i = 0; i < tables.length; i++){
    let tbody = tables[i];
    let rows = tbody.getElementsByTagName('tr');
    if(rows.length >= 2) {
        let secondRow = rows[1];
        var cell = secondRow.querySelector('td');
        if (cell.innerHTML.trim() === '') {
            let table = tbody.parentElement;
            let div1 = table.parentElement;
            let finalDiv = div1.parentElement;
            finalDiv.classList.add("Hide");
        }
    }

}