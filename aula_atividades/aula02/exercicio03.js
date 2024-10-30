
//armazena o valor dos lados dos triangulos
let lado01 = 3
let lado02 = 4
let lado03 = 5

//armazena a quantidade de lados diferentes do triangulo
let ladosDiferentes = 0

//tipo do triangulo
let triangulo


//verifica se o triangulo é equilatero
if(lado01 == lado02 && lado01 == lado03 && lado03 == lado02){
    console.log("triangulo equilatero")
    //cheguei a essa conclusao comparando todas as combinações

}


//verifica se o triangulo é isosceles,escaleno,equilatero 
if(lado01 != lado02){
    ladosDiferentes = ladosDiferentes + 1

}if(lado01 != lado03){
    ladosDiferentes = ladosDiferentes + 1

}if(lado03 != lado02){
    ladosDiferentes = ladosDiferentes + 1
}



if(ladosDiferentes == 0){
    triangulo = "triangulo equilatero"

}else if(ladosDiferentes == 1){
    triangulo = "triangulo isosceles"

}else if(ladosDiferentes == 3){
    triangulo = "triangulo escaleno"

}else{
    triangulo = "triangulo inexistente"
}


//imprime o resultado na tela
console.log("este é um "+ triangulo +"pois possui "+ ladosDiferentes +" lados diferentes")

console.log(ladosDiferentes)