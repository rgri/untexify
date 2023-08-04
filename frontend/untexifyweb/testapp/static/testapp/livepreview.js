import "./script"
let previewCopy = /** @type{HTMLCanvasElement} */(document.getElementById("canvas"));
const preview = previewCopy.getContext("2d");



function draw() {
  preview = ctx;
  requestAnimationFrame(draw);
}
document.addEventListener("mouseup", draw);
