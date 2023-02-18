var largeurImage;
var hauteurImage;

function zoom(image) {
    largeurImage = image.style.width;
    hauteurImage = image.style.height;
    image.style.width = "120%";
    image.style.height = "120%";
}
    
function dezoom(image) {
    largeurImage = image.style.width;
    hauteurImage = image.style.height;
    image.style.width = "50%";
    image.style.height = "50%";
}
