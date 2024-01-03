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

// let tables = document.querySelectorAll("tbody");

// for(let i = 0; i < tables.length; i++){
//     let tbody = tables[i];
//     let rows = tbody.getElementsByTagName('tr');
//     if(rows.length >= 2) {
//         let secondRow = rows[1];
//         var cell = secondRow.querySelector('td');
//         if (cell.innerHTML.trim() === '') {
//             let table = tbody.parentElement;
//             let div1 = table.parentElement;
//             let finalDiv = div1.parentElement;
//             finalDiv.classList.add("Hide");
//         }
//     }

// }

let gameWrappers = document.querySelectorAll(".gameWrapper");

for (let i = 0; i < gameWrappers.length; i++) {
    let table = gameWrappers[i].querySelector("table");
    console.log(table);
    let rows = table.querySelectorAll("tr");
  
    if (rows.length <= 1) {
      gameWrappers[i].classList.add("Hide");
    }
}


let airplane = document.querySelectorAll(".airplane");

for(let i = 0; i < airplane.length; i++){
    if(airplane[i].innerText == ''){
        airplane[i].parentElement.remove();
    }
}

let carrots = document.querySelectorAll(".carrot");

for(let i = 0; i < carrots.length; i++){
    carrots[i].addEventListener('click', () => {
        carrotParent = carrots[i].parentElement;
        mainParent = carrotParent.parentElement;
        carrotChildren = mainParent.children;

        if(!carrotChildren[1].classList.contains("DrawerHide")) {
            if(carrotChildren[1].classList.contains("DrawerShow")) {
                carrotChildren[1].classList.remove('DrawerShow'); 
            }
            carrotChildren[1].classList.add("DrawerHide");
            // setTimeout( () => {
            //     hideGames(carrotChildren[1])
            // }, 350); 
        } else {
            // carrotChildren[1].classList.remove("Hide");
            carrotChildren[1].classList.add('DrawerShow'); 
            // setTimeout( () => {
            //     displayGames(carrotChildren[1])
            // }, 100);
            carrotChildren[1].classList.remove('DrawerHide'); 
        }
    })
}

function hideGames(element){
    element.classList.add('Hide');
}

function displayGames(element){
    element.classList.add('DrawerShow');
}