#!/bin/bash

st=
echo "Seleciona o serviço que deseja verificar o Status"
echo "1 - Apache2"
echo "2 - SSH"
read service

if [ $service == 1 ]
then
	st=$(systemctl status apache2) 
	echo " $st"

else
	if [ $service == 2 ]
	then
		ts=$(systemctl status sshd )
	echo " $ts "
	fi
fi
