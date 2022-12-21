function removep(x) {
    const uploader = x.querySelector("td:nth-child(8)").textContent.trim()
    return uploader !== "Dohrnii"
}

Array.from(document.querySelectorAll(".lista2"))
    .filter(removep)
    .forEach(ele => ele.style.opacity = "0.35")
