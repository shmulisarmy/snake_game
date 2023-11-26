
// Function to set up the game
function set_up(){
    player = [[0, 0], [0, 1], [0, 2]];
    table.textContent = '';

    // Create the table
    for (var row = 1; row <= table_size; row++){
        var html_row = document.createElement('tr');
        for (var col = 1; col <= table_size; col++){
            var html_col = document.createElement('th');
            html_col.setAttribute('id', `${row} ${col}`);
            html_row.appendChild(html_col);
        } 
        table.appendChild(html_row);
    }

    // Set the initial positions of the snake
    for (const element of player) {
        table.rows[element[0]].cells[element[1]].style.backgroundColor = 'green';
    }
}

// Event listener for the 'Enter' key
window.addEventListener('keydown', key => {
    if (key.code === "Enter"){
        submit();
    }
});

// Function to move the snake
function move_snake(){
    console.log(direction);
    var mo = player.length-1;

    // Check the direction and move the snake accordingly
    if (direction == 'right' && player[mo][1] < table_size-1){
        if ([player[mo][0], player[mo][1] + 1] in player){
            window.alert('you lose');
        }
        player.push([player[mo][0], player[mo][1] + 1]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {
            table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
            player.shift();
        }
    } 
    if (direction == 'left' && player[mo][1] > 0){
        if ([player[mo][0], player[mo][1] - 1] in player){ window.alert('you lose');
        }
        player.push([player[mo][0], player[mo][1] - 1]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {
            table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
            player.shift();
        }
    } 
    if (direction == 'down' && player[mo][0] < table_size-1){
        if ([player[mo][0] + 1, player[mo][1]] in player){
            window.alert('you lose');
        }
        player.push([player[mo][0] + 1, player[mo][1]]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {
            table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
            player.shift();
        }
    } 
    if (direction == 'up' && player[mo][0] > 0){
        if ([player[mo][0] - 1, player[mo][1]] in player){
            window.alert('you lose');
        }
        player.push([player[mo][0] - 1, player[mo][1]]);
        table.rows[player[mo][0]].cells[player[mo][1]].style.backgroundColor = 'green';
        if (apple){
            apple = false;
        } else {
            table.rows[player[0][0]].cells[player[0][1]].style.backgroundColor = 'grey';
            player.shift();
        }
    }

    // Check if the snake is out of bounds
    if (!-(1 < player[mo][0] < table_size))        window.alert('you lose');
}

// Variables for the game
let table = document.getElementById('myTable');
let player;
let table_size = 20;
let direction = 'right';
let apple = false;

// Set up the game
set_up();

// Event listener for arrow key presses
window.addEventListener('keydown', key => {
    var mo = player.length-1;
    if (key.code === "ArrowRight" && direction != 'left' && player[mo][1] < table_size-1){
        direction = '';
    } 
    if (key.code === "ArrowLeft" && direction != 'right' && player[mo][1] > 0){
        direction = 'left';
    } 
    if (key.code === "ArrowDown" && direction != 'up' && player[mo][0] < table_size-1){
        direction = 'down';
    } 
    if (key.code === "ArrowUp" && direction != 'down' && player[mo][0] > 0){
        direction = 'up';
    } 
    if (key.code == 'Enter'){
        apple = true;
    }
});

// Move the snake every 180 milliseconds
setInterval(move_snake, 180);
//
//This code sets up a simple snake game. The snake starts in the top left corner of the table and moves in the direction of the arrow keys. The snake grows every time it moves, and if it hits a wall or itself, the game ends. The 'Enter' key allows the snake to eat an apple, which makes it grow even faster.