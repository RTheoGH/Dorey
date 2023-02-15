var largeurImage;
var hauteurImage;

function zoom(image) {
    largeurImage = image.style.width;
    hauteurImage = image.style.height;
    image.style.width = "10em";
    image.style.height = "10em";
}
    
function dezoom(image) {
    largeurImage = image.style.width;
    hauteurImage = image.style.height;
    image.style.width = "5em";
    image.style.height = "5em";
}
