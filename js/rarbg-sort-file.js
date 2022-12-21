function compareFile(a, b) {
    return a.localeCompare(b)
}

function compareListItem(a, b) {
    const afile = a.querySelector("td:nth-child(2) > a").textContent.trim()
    const bfile = b.querySelector("td:nth-child(2) > a").textContent.trim()
    return compareFile(afile, bfile)
}

function appendToTable(listItem) {
    document.querySelector(".lista2t > tbody").append(listItem)
}

Array.from(document.querySelectorAll(".lista2"))
    .sort(compareListItem)
    .forEach(appendToTable)
