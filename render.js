function request_game_state(game_id, player_id)
{
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://localhost:8888/game_state/" + game_id + "/" + player_id, false);
    console.log("GET", "http://localhost:8888/game_state/" + game_id + "/" + player_id)
    xhttp.send(null)
    console.log(xhttp.response)
    return xhttp.response;
}

console.log("BEGIN")
document.getElementById("map_txt").innerHTML = request_game_state(123456, 4200042);

window.setInterval(function () {
    document.getElementById("map_txt").innerHTML = request_game_state(123456, 4200042);    
}, 100 );