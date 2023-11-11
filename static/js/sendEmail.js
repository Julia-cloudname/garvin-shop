function sendMail(contactForm) {
    emailjs.send("service_7x3q052","template_mp2g91d", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            window.location.reload(); 
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}