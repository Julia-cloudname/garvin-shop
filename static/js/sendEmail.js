// function for sendMail service
function clearForm() {
    document.getElementById("fullname").value = '';
    document.getElementById("emailaddress").value = '';
    document.getElementById("message").value = '';
}

function sendMail(contactForm) {
    emailjs.send("service_7x3q052", "template_mp2g91d", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            document.getElementById('message-sent').style.display = 'block'; // show message sent
            clearForm();
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false; // To block from loading a new page
}

