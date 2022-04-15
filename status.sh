#!/bin/bash

#echo "Informe o nome do serviço"
#read service


st=$(sudo systemctl status apache2 | grep -i Active: | awk   '{ print $2 }')
if [ $st == active ] 
	echo "Serviço esta ativo"
then
	stats=$(sudo systemctl start apache2)
	echo "$stats"
fi
