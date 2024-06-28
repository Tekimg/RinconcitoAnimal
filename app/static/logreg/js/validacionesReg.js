$(function(){
    $("#formulario2").validate({
        rules:{
            rut: "required",
            nombre: "required",
            apellidos: "required",
            celular: "required",
            email: "required",
            pass1: "required",
            pass2: "required"
        },
        messages:{
            rut:{
                required: 'Ingrese su rut...',
            },
            nombres:{
                required: 'Ingrese su nombre...',
            },
            apellidos:{
                required: 'Ingrese su apellido...',
            },
            celular:{
                required: 'Ingrese su celular...',
            },
            email:{
                required: 'Ingrese su email...',
            },
            pass1:{
                required: 'Ingrese una contraseña...',
            },
            pass2:{
                required: 'Ingrese su contraseña nuevamente...',
            },
        },

    })
})