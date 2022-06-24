$net = new-object -ComObject WScript.Network
$net.MapNetworkDrive("a:", "\\srv-soft01.paulista.local\Documentos\Suporte\Homologação Argentina", $false, "paulista\fabiano.oliveira", "Express@2024")
$net.MapNetworkDrive("b:", "\\srv-soft01.paulista.local\Producao\SiTef\SiTef 5\CliSiTef - 5.0\Qualidade\Argentina\Unificada", $false, "paulista\fabiano.oliveira", "Express@2024")
#$net.MapNetworkDrive("z:", "\\192.168.50.193\c$", $false, "paulista\fabiano.oliveira", "Express@2024")




