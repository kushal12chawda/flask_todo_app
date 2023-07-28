// function showModal(){
//     document.querySelector('.add-new-task').classList.add('show-add-new-task');
// }
// function closeModal(){
//     document.querySelector('.add-new-task').classList.remove('show-add-new-task');
// }
// function checked(){
//     document.querySelectorAll(".blue").checked = true
// }

// var addnew=document.querySelector(".success")
// addnew.addEventListener("click", showModal)

// var close=document.querySelector(".close")
// close.addEventListener('click', closeModal)

// var blue=document.querySelectorAll(".blue")
// blue.addEventListener("click", checked)
// console.log(blue)

function update_task_js(task_id, task_status){
    // console.log(x)
    console.log("task_id" + task_id)
    let status = task_status.toLowerCase()=="true"
    fetch("/update_task/" + task_id, {method: 'POST', })
}

function edit_name_js(x){
    console.log(x)
    if (document.querySelector('.retry').innerText.toLowerCase() == "edit"){
        document.querySelector('.edit_todo_name').removeAttribute("readonly")
        document.querySelector('.edit_todo_name').focus()
        document.querySelector('.retry').innerText = "Save"
        // console.log(x)
    }
    else{
        document.querySelector('.edit_todo_name').setAttribute("readonly", "readonly")
        document.querySelector('.retry').innerText = "Edit"
        // console.log(x)
        // console.log(x)
    }
    let y = document.querySelector('.edit_todo_name').value
    console.log(y)
    console.log(x)
    fetch('/edit_name/' + x + '/' + y, {method: 'POST'})
}

let popup = document.getElementById("full-desc")

function openPopup(x){
    popup.classList.add("open-popup", x)
}
function closePopup(){
    popup.classList.remove("open-popup")
}

let noOfCharac = 50;
let contents = document.querySelectorAll(".read")
console.log(contents)
contents.forEach(content => {
    if (content.textContent.length < noOfCharac){
        content.nextElementSibling.style.display = "none"
    }
    else{
        let displayText = content.textContent.slice(0, noOfCharac)
        let moreText = content.textContent.slice(noOfCharac)
        console.log(moreText)
        content.outerHTML = `${displayText}<span class="dots">...</span><span class="hide more">${moreText}</span>`
        console.log(content.outerHTML)
    }
})

function readMore(btn){
    let post = btn.parentElement
    console.log(btn.parentElement)
    post.querySelector(".dots").classList.toggle("hide")
    post.querySelector(".more").classList.toggle("hide")
    btn.textContent == "Read More" ? btn.textContent = "Read Less" : btn.textContent = "Read More"
}