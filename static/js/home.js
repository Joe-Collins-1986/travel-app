
// This script is used to flash the arrow on home
$('.blink').each(function() {
var elem = $(this);
elem.fadeOut(1000)
    .fadeIn(1000)
    .fadeOut(1000)
    .fadeIn(1000)
    .fadeOut(1000)
    .fadeIn(1000);
});
