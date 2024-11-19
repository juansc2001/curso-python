
//armazena o valor dos lados dos triangulos
let lado01 = 10
let lado02 = 7
let lado03 = 10

//armazena a quantidade de lados diferentes e lados iguais do triangulo
let ladosDiferentes = 0
let ladosIguais

//tipo do triangulo
let triangulo



//conta quantos lados diferentes tem o triangulo
if(lado01 != lado02){
    ladosDiferentes = ladosDiferentes + 1

}if(lado01 != lado03){
    ladosDiferentes = ladosDiferentes + 1

}if(lado03 != lado02){
    ladosDiferentes = ladosDiferentes + 1
}


//guarda o resultado do triangulo dentro da variavel
if(ladosDiferentes == 0){
    triangulo = "triangulo equilatero"

}else if(ladosDiferentes == 1){
    triangulo = "triangulo isosceles"

}else if(ladosDiferentes == 3){
    triangulo = "triangulo escaleno"

}else{
    triangulo = "triangulo inexistente"
}

ladosIguais = 3 - ladosDiferentes

//imprime o resultado na tela
console.log("este é um "+ triangulo +"pois possui "+ ladosIguais +" lados iguais")