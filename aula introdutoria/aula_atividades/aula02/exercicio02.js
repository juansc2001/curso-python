
//armazena as notas do aluno
let nota01 = 7
let nota02 = 5

//calcula a media do aluno
media = (nota01 + nota02)/2

//verifica se o aluno esta aprovado,reprovado,recuperação
if(media >= 6){
    console.log("aluno aprovado")

}else if(media <= 5.9 && media >= 4){
    console.log("aluno de recuperação")

}else if(media < 4){
    console.log("aluno reprovado")

}else{
    console.log("error no calculo de media")
}

console.log("a media do aluno é " + media)