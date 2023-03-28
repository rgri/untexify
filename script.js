// matches elements of the document "document" (presumably the default instance of the Document() object instantiated by call "defer" in the script element) which have "class=myCanvas".[fn:5]
const canvas = document.querySelector('.myCanvas');
const backgroundCanvas = document.querySelector('.background')
const width = canvas.width = 72;
const height = canvas.height = 72;
const background = backgroundCanvas.getContext('2d')
const ctx = canvas.getContext('2d');

const backgroundWidth = 77;
const backgroundHeight = 77;
// background.fillStyle = 'rgb(0,0,0)';
// background.fillRect(0, 0, width, height);
ctx.fillStyle = 'rgb(0,0,0)';
ctx.strokeStyle = 'blue';
ctx.rect(0, 0, backgroundWidth, backgroundHeight);

ctx.fillRect(0, 0, width, height);

const colorPicker = document.querySelector('input[type="color"]');
const sizePicker = 4;
const output = document.querySelector('.output');
const clearBtn = document.querySelector('button');

// covert degrees to radians
function degToRad(degrees) {
  return degrees * Math.PI / 180;
};

// update sizepicker output value

// sizePicker.addEventListener('input', () => output.textContent = sizePicker.value);

// store mouse pointer coordinates, and whether the button is pressed
let curX;
let curY;
let pressed = false;

// update mouse pointer coordinates
document.addEventListener('mousemove', e => {
  curX = (window.Event) ? e.pageX : e.clientX + (document.documentElement.scrollLeft ? document.documentElement.scrollLeft : document.body.scrollLeft);
  curY = (window.Event) ? e.pageY : e.clientY + (document.documentElement.scrollTop ? document.documentElement.scrollTop : document.body.scrollTop);
});

canvas.addEventListener('mousedown', () => pressed = true);

canvas.addEventListener('mouseup', () => pressed = false);

clearBtn.addEventListener('click', () => {
  ctx.fillStyle = 'rgb(0,0,0)';
  ctx.fillRect(0, 0, width, height);
});

function draw() {
  if (pressed) {
    ctx.fillStyle = colorPicker.value;
    ctx.beginPath();
    ctx.arc(curX, curY - 85, sizePicker, degToRad(0), degToRad(360), false);
    ctx.fill();
  }

  requestAnimationFrame(draw);
}

draw();
