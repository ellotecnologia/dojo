<?php declare (strict_types = 1);

//PHP7.2

/*
 * Calcula quantidade de moedas de diversos valores para troco
 *
 * @param float $valorTotal
 * @param float $valorPago
 * @return string
 */
function calculaTroco(float $valorTotal, float $valorPago)
{
    $troco          = $valorPago - $valorTotal;
    if ($troco <= 0) return "Sem troco";

    $moedas     = ['1.00' => 0, '0.25' => 0, '0.05' => 0, '0.01' => 0];
    $resultado  = '';
    foreach ($moedas as $moeda => &$qtde) {
        while ($troco >= $moeda) {
            $qtde++;
            $troco -= $moeda;
        }
        if ($qtde > 0) {
            $resultado .= "\n{$qtde} moeda(s) de \${$moeda}";
        }
    }
    return $resultado;
}
fscanf(STDIN, "%f%f", $valorTotal, $valorPago);
printf("%s\n", calculaTroco($valorTotal, $valorPago));
