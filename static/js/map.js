window.onload=function(){

    var targets = document.querySelectorAll('path');
    var prompt = document.getElementById('prompt')

    targets.forEach(element => element.addEventListener('mouseover', event => {
    countryHovered = (event.target.getAttribute("data-name"));
    prompt.setAttribute('style', 'display: flex;');
    prompt.innerHTML = countryHovered;
    }));

    targets.forEach(element => element.addEventListener('mouseleave', event => {
    prompt.setAttribute('style', 'display: none;');
    }));
}