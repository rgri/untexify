var blank = true;
let canvas = /**  @type{HTMLCanvasElement} */(document.getElementById("canvas"));
const width = canvas.width = 72
const height = canvas.height = 72
const ctx = canvas.getContext('2d');
const formInput = document.getElementById("id_drawingLink")

ctx.fillStyle = 'rgb(255,255,255)';
ctx.fillRect(0, 0, width, height);

const colorPicker = 'rgb(0,0,0)';
const sizePicker = 2;
const output = document.querySelector('.output');
const clearBtn = document.querySelector('.clearButton');

// covert degrees to radians
function degToRad(degrees) {
  return degrees * Math.PI / 180;
};

// update sizepicker output value


// store mouse pointer coordinates, and whether the button is pressed
let curX;
let curY;
let pressed = false;

// update mouse pointer coordinates
document.addEventListener('mousemove', e => {
  curX = e.pageX - canvas.getBoundingClientRect().x - window.scrollX
  if (curX > width) {
    pressed = false
  }
  curX = curX % width
  curY = e.pageY - canvas.getBoundingClientRect().y - window.scrollY
  if (curY > width) {
    pressed = false
  }
  curY = curY % height
  if (blank == false) {
    const currentURL = canvas.toDataURL("image/png");
    formInput.setAttribute("value", currentURL);
  }

});

canvas.addEventListener('mousedown', () => pressed = true);

canvas.addEventListener('mouseup', () => pressed = false);
clearBtn.addEventListener('click', () => {
  ctx.fillStyle = 'rgb(255,255,255)';
  ctx.fillRect(0, 0, width, height);
  blank = true;
});

function draw() {
  if (pressed) {
    ctx.fillStyle = colorPicker;
    ctx.beginPath();
    ctx.arc(curX, curY, sizePicker, degToRad(0), degToRad(360), false);
    ctx.fill();
    blank = false;
  }

  requestAnimationFrame(draw);
}

draw();
