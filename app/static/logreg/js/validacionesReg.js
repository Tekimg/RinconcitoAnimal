$(document).ready(function () {
    $("#formulario2").submit(function (event) {
        // Evitar que el formulario se envíe automáticamente
        event.preventDefault();

        // Realizar las validaciones
        var nombres = $("#nombres").val();
        var apellidos = $("#apellidos").val();
        var telefono = $("#telefono").val();
        var rut = $("#rut").val();
        var email = $("#email").val();
        var password = $("#password1").val();
        var passwordC = $("#password2").val();
        var terminosAceptados = $("#terminos").prop("checked");

        if (nombres == "") {
            alert("Ingrese un nombre.")
            return;
        }

        if (apellidos == "") {
            alert("Ingrese un apellido.")
            return;
        }

        if (rut == "") {
            alert("Ingrese un rut.")
            return;
        }

        if (telefono == "") {
            alert("Ingrese un número de telefono.")
            return;
        }

        // Email
        if (email == "") {
            alert("Ingrese un email.");
            return;
        } else if (!validateEmail(email)) {
            alert("Ingrese un email válido.")
            return;
        }

        // Contra
        if (password == "") {
            alert("Ingrese una contraseña.");
            return;
        }

        if (passwordC == "") {
            alert("Ingrese una contraseña.");
            return;
        }
        if (!terminosAceptados) {
            alert("Debe aceptar los términos y condiciones.")
            return;
        }

        function validateEmail(email) {
            var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            return re.test(email);
        }
        // Si todas las validaciones pasan, se puede enviar el formulario
        alert("¡Registro exitoso!");
        // Aquí podrías enviar el formulario utilizando AJAX o cualquier otro método
    });
});