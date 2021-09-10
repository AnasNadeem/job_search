let searchJobBtn = document.getElementById('searchJobBtn');
// Checking Job Position 
let jobPosition = document.getElementById('jobTitle');
jobPosition.addEventListener('input', function checkName() {
    let jobPositionAlert = document.getElementById('jobPositionAlert');
    if ((jobPosition.value.length < 1) || (jobPosition.value.length >= 50)) {
        let msg = `Job Title shouldn't be empty.`
        let alertMsg = `<div class="alert alert-danger mt-2 mb-0" role="alert">${msg}</div>`
        jobPositionAlert.innerHTML = alertMsg
        searchJobBtn.disabled = true
    } else {
        let msg = `<strong>Success</strong>`
        let alertMsg = `<div class="alert alert-success mt-2 mb-0" role="alert">${msg}</div>`
        jobPositionAlert.innerHTML = alertMsg
        searchJobBtn.disabled = false
    }
})