function set_up(){
    player = [[0, 0], [0, 1], [0, 2]];
    table.textContent = '';

    for (var row = 1; row <= table_size; row++){
        var html_row = document.createElement('tr');
    for (var col = 1; col <= table_size; col++){
        var html_col = document.createElement('th');
        html_col.setAttribute('id', `${row} ${col}`);
        html_row.appendChild(html_col);
} 
table.appendChild(html_row);
}
for (const element of player) {
    table.rows[element[0]].cells[element[1]].style.backgroundColor = 'green';
}};
window.addEventListener('keydown', key => {
    if (key.code === "Enter"){
        submit();
}})

function move_snake(){
    console.log(direction);
    var mo = player.length-1;
    if (direction == 'right' && player[mo][1] < table_size-1){
        // player[-1][1]++;
        player.push([player[mo][0], player[mo][1] + 1]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
        player.shift();}
    }  if (direction == 'left' && player[mo][1] > 0){
        // player[-1][1]--;
        player.push([player[mo][0], player[mo][1] - 1]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
        player.shift();}
    }  if (direction == 'down' && player[mo][0] < table_size-1){
        // player[-1][0]++;
        player.push([player[mo][0] + 1, player[mo][1]]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
        player.shift();}
    }  if (direction == 'up' && player[mo][0] > 0){
        // player[-1][0]--;
        player.push([player[mo][0] - 1, player[mo][1]]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
        player.shift();}
    }
    // for (const element of player) {
    //     table.rows[element[0]].cells[element[1]].style.backgroundColor = 'green';
    };//};
    


let table = document.getElementById('myTable');
let player;
let table_size = 20;
let direction = 'right';
let apple = false;
set_up();

window.addEventListener('keydown', key => {
    var mo = player.length-1;
    if (key.code === "ArrowRight" && direction != 'left' && player[mo][1] < table_size-1){
        direction = 'right';
        // player[1]++;
    }  if (key.code === "ArrowLeft" && direction != 'right' && player[mo][1] > 0){
        direction = 'left';
        // player[1]--;
    }  if (key.code === "ArrowDown" && direction != 'up' && player[mo][0] < table_size-1){
        direction = 'down';
        // player[0]++;
    }  if (key.code === "ArrowUp" && direction != 'down' && player[mo][0] > 0){
        direction = 'up';
        // player[0]--;
    } if (key.code == 'Enter'){
        apple = true;
    }
})


setInterval(move_snake, 180);
