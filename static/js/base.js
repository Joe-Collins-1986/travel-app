//time for alert dismissal
let bootstrap;

setTimeout(function () {
    let messages = document.getElementById('msg-alert');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);