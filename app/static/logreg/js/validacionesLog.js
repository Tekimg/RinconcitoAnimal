$(document).ready(function(){
    $("#formulario").submit(function(event){
        // Evitar que el formulario se envíe automáticamente
        event.preventDefault();


        // Realizar las validaciones
        var email = $("#email").val();
        var password =$("#password").val();


        // Email
        if(email=="" ){
            alert("Ingrese un email.");
            return;
        } else if (!validateEmail(email)){
            alert("Ingrese un email válido.")
            return;
        }

        // Contra
        if(password==""){
            alert("Ingrese una contraseña.");
            return;
        }

        function validateEmail(email) {
            var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            return re.test(email);
        }
        // Si todas las validaciones pasan, se puede enviar el formulario
        alert("¡Acceso exitoso!");
        // Aquí podrías enviar el formulario utilizando AJAX o cualquier otro método
    });
});