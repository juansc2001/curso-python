/* capturar dados do formulario */
document.getElementById("loginForm").addEventListener("submit",function(event){


    /*aqui paramos o formulario */
    event.preventDefault();

    /*guardar o usuario e a senha */
    var usuario = document.getElementById("user").value;
    var senha = document.getElementById("password").value;

    /*exibe no console do navegador as informações capturadas no formulario */
    console.log("seu usuario é:"+ usuario + "sua senha é:" + senha);
})