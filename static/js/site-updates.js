const filterTopics = document.getElementById("filter-updates");

function filterToggle() {
    if (filterTopics.style.display === "none") {
            filterTopics.style.display = "block";
        } else {
            filterTopics.style.display = "none";
        }
    }
document.getElementById("filter-updates").style.display = "none";