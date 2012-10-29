

function Snake(canvas_id, width, height, scale) {
  var game = this;

  // state
  var game_on = true,
      level = 1,
      score,
      snake_color = "#009DDC",
      apple_color = "#7AC143";

  // display elements
  var canvas;

  // game board width and scale (in pixels)
  width = width ? width : 38;
  height = height ? height : 22;
  scale = scale ? scale : 10;

  // directions
  var NORTH = 0, EAST = 1, SOUTH = 2, WEST = 3;

  // keys
  var UP = 38, DOWN = 40, LEFT = 37, RIGHT = 39;

  // initialize the snake in the top left
  var snake = {
    "x": 0,
    "y": 0,
    "body": [[0, 0]],
    "direction": EAST,
    "pending_direction": null
  }

  // the first apple goes in the middle
  var apple = {
    "x": (width / 2),
    "y": (2)
  }

  // keyboard handler
  function handleKeys(e) {
    var char;
    var evt = (e) ? e : window.event;

    char = (evt.charCode) ?
      evt.charCode : evt.keyCode;
    if (char > 36 && char < 41) {
      handleChar(char);
      return false;
    };
    return true;
  }

  // character specific keyboard handling
  function handleChar(char) {
    if (!game_on)
      return;

    switch (char) {
      case UP:
        if (snake.direction != SOUTH)
          snake.pending_direction = NORTH;
        break;
      case DOWN:
        if (snake.direction != NORTH)
          snake.pending_direction = SOUTH;
        break;
      case LEFT:
        if (snake.direction != EAST)
          snake.pending_direction = WEST;
        break;
      case RIGHT:
        if (snake.direction != WEST)
          snake.pending_direction = EAST;
        break;
    }
  }

  function reset() {
    snake.x = snake.y = 0;
    snake.body = [[0, 0]];
    snake.direction = EAST;
    apple.x = (width / 2);
    apple.y = (2);
    score = null;
  }
  
  // drawing routine
  function draw() {

    // if paused, keep checking every 1/10th second for unpause
    if (!game_on) { 
      t = setTimeout(function() { draw(); }, 100);
      return; 
    }

    // get reference to drawing area
    if (canvas.getContext){

      // create drawing context
      var ctx = canvas.getContext('2d');

      if (snake.pending_direction !== null) {
        snake.direction = snake.pending_direction;
        snake.pending_direction = null;
      }

      // move snake
      switch (snake.direction) {
        case NORTH:
          snake.y--;
          break;
        case EAST:
          snake.x++;
          break;
        case SOUTH:
          snake.y++;
          break;
        case WEST:
          snake.x--;
          break;
      }

      // game board color
      ctx.fillStyle = "#153152";
      ctx.fillRect(0, 0, width * scale, height * scale);

      // push new position onto stack and pop last
      var old_pos = snake.body.pop();
      snake.body.unshift([snake.x, snake.y]);

      // test to see if snake is touching itself
      for (var i = 1; i < snake.body.length; i++)
        if (snake.body[i][0] == snake.x &&
            snake.body[i][1] == snake.y)
          reset();

      // test to see if out of bounds
      if (snake.x < 0 || snake.x >= width || 
          snake.y < 0 || snake.y >= height)
        reset();

      ctx.fillStyle = snake_color;

      //draw snake
      for (var i = 0; i < snake.body.length; i++)
        ctx.fillRect (snake.body[i][0] * scale, snake.body[i][1] * scale,
                      scale, scale);

      // test if snake eats apple and if so, reset apple and make snake grow
      if (snake.x == apple.x && snake.y == apple.y) {
        snake.body.push(old_pos);
        score += parseInt(level);
        var free_space = false;
        while (!free_space) {
          free_space = true;
          apple.x = (Math.floor(Math.random() * width));
          apple.y = (Math.floor(Math.random() * height));

          // make sure apple is draw in free space, not on top of snake
          for(i = 1;i < snake.body.length; i++)
            if(snake.body[i][0] == apple.x && snake.body[i][1] == apple.y)
              free_space = false;
        }
      }

      // draw apple
      ctx.fillStyle = apple_color;
      ctx.fillRect (apple.x * scale, apple.y * scale, scale, scale);

      // display score
      //score_disp.innerHTML = score;
   
    }

    // calculate timeout using level
    t = setTimeout(function() { draw(); }, 120 - (20 * level));
  }

  this.toggle_play = function() {
    if(game_on == true) {
      game_on = false;
    } else {
      game_on = true;
    }
    return game_on;
  }

  this.change_level = function(new_level) {
    level = new_level;
  }

  this.initialize = function() {
    canvas = document.getElementById(canvas_id);
    //score_disp = document.getElementById(score_id);
    // create handlers
    document.onkeydown = function(e) { return handleKeys(e) };
    document.onkeypress = function(e) { return handleKeys(e) };

    reset();
    draw();
  }
}
