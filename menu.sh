#!/bin/bash

echo " Escolha uma opcao abaixo "
echo "1 -  Verificar status de serviço"
echo "2 -  Reiniciar serviços"
#echo "3 -  
echo "3 - Sair"
read escolha

if [ $escolha == 1 ]
then
   echo " Informe qual eh a opcao desejada"
   echo "1 - Verificar status de um serviço especifico"
   echo "2 - Verificar status de todos os serviços "
   read service
fi
	if [ "$service" == 1 ]
	then
		echo " Escolha o servico que deseja verificar o status"
		echo "1 - Apache"
		echo "2 - Cron"
		echo "3 - Cups"
		read verificar

	fi
		if [ "$verificar" == 1 ]
		then
			st=$(systemctl status apache2 ) 
			echo "$st"
 			elif [ "$verificar" == 2 ]
				then
					ts=$(systemctl status cron )
					echo "$ts"
					elif [ "$verificar" == 3 ]
						then
							ho=$(systemctl status cups )
							echo "$ho"
						
		fi
			if [ "$service" == 2 ]
			then
				fh=$(systemctl status apache2 cron cups)
				echo "$fh"
			fi

	if [ "$escolha" == 2 ]
	then
		echo "Escolha o serviço que deseja reiniciar"
		echo "1 - Apache"
		echo "2 - Cron"
		echo "3 - Cups"
		read rei
	fi
	if [ "$rei" == 1 ]
		then
			fb=$(systemctl restart apache2 )
			bf=$(systemctl status apache2)
			
			    if [ "$fho" == active ]
                        then
                                echo "$fb"
                                echo -e "\n O servico foi reiniciado com sucesso\n"
                        else
                                echo -e "\n Erro ao reiniciar o serviço\n"
                        fi
		
		
	fi

	if [ "$rei" == 2 ]
		then
			fb=$(systemctl restart cron )
			bf=$(systemctl status cron)
			echo "$bf"
		
	fi

	if [ "$rei" == 3 ]
		then
			hf=$(systemctl restart cups )
			fh=$(systemctl status cups)
			oh=$(systemctl status cups | grep -i active | awk '{ print $2 }')
			if [ "$oh" == active ]
			then
				echo "$fh"
				echo -e "\n O servico foi reiniciado com sucesso\n"
			else
				echo "Erro ao reiniciar o serviço"
			fi
		
	fi
	if [ "$escolha" == 3 ]
	then
		exit
	fi
