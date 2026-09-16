// Función para calcular el factorial de un número
function factorial(numero) {

    // Validar que sea un número entero y no negativo
    if (numero < 0 || !Number.isInteger(numero)) {
        return "Error: ingrese un número entero positivo";
    }

    let resultado = 1;

    // Calcular factorial
    for (let i = 1; i <= numero; i++) {
        resultado = resultado * i;
    }

    return resultado;
}
