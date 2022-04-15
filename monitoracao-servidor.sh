#!/bin/bash

resposta_http=$(curl --write-out %{http_code} --silent --output /dev/null http://192.168.1.113)
if [ $resposta_http -ne 200 ]
then
mail -s "Problema no Servidor" faabianohipolito@gmail.com<<del
Houve um problema no servidor e os usuarios pararam deter acesso ao conteudi web.
del
	systemctl restart apache2
fi

