function colaClick(event) {
    event.preventDefault();
    var conf = confirm("Перейти на сайт Coca-Cola?");
    if (conf == true) {
        window.open("https://www.coca-cola.com/country-selector", "_blank");
    }
}

function vkClick(event) {
    event.preventDefault();
    var conf = confirm("Перейти на сайт VK?");
    if (conf == true) {
        window.open("https://vk.com/", "_blank");
    }
}

function warnerBrosClick(event) {
    event.preventDefault();
    var conf = confirm("Перейти на сайт WarnerBros?");
    if (conf == true) {
        window.open("https://www.warnerbros.com/", "_blank");
    }
}

function yandexClick(event) {
    event.preventDefault();
    var conf = confirm("Перейти на сайт Яндекс.еда?");
    if (conf == true) {
        window.open("https://eda.yandex.ru/", "_blank");
    }
}


function onMouseOver(){
    event.target.style.cursor = "pointer";
}

function onMouseOut(){
    event.target.style.cursor = "auto";
}