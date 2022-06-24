$net = new-object -ComObject WScript.Network
$net.MapNetworkDrive("a:", "\\srv-soft01.paulista.local\Documentos\Suporte\Homologação Argentina", $false, "dominio\login", "******")
$net.MapNetworkDrive("b:", "\\srv-soft01.paulista.local\Producao\SiTef\SiTef 5\CliSiTef - 5.0\Qualidade\Argentina\Unificada", $false, "dominio\login", "******")
#$net.MapNetworkDrive("z:", "\\192.168.50.193\c$", $false, "dominio\login", "******")




