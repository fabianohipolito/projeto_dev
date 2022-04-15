#!/bin/bash

echo "Informe o nome do Aluno "
read nm
echo "informe a nota N1"
read n1
echo "informe a nota N2"
read n2
echo "informe a nota N3"
read n3

soma=$(($n1+$n2+$n3))
nota_final=$(($soma/3))
if [ $soma -gt 7 ]
then
	echo "O  aluno $nota_final, foi aprovado sua nota é $soma" 	
	
	elif [ $soma -le  6.5 ]
	then
		echo "O  aluno $nota_final, vai para exame, sua nota é $soma"
	elif [ $soma -lt 6.5 ]
	then
		echo " O aluno $nota_final foi reprovado, sua note eh $soma "
fi
