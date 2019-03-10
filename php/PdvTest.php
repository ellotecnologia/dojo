<?php
declare(strict_types=1);

require("./pdv.php");

use PHPUnit\Framework\TestCase;

final class PdvTest extends TestCase
{

    public function testValorDaCompraIgualOValorPago(): void
    {
        $esperado = "Sem troco";
        $obtido = calculaTroco(10.00, 10.00);
        $this->assertEquals($esperado, $obtido);
    }

    public function testValorDaCompraSendoCincoReaisEValorPagoSendoDezReais(): void
    {
        $esperado = "\n5 moeda(s) de $1.00";
        $obtido = calculaTroco(5.00, 10.00);
        $this->assertEquals($esperado, $obtido);
    }

    public function testValorDaCompraSendoCincoReaisEValorPagoSendoDezReaisEQuinzeCentavos(): void
    {
        $esperado = "\n5 moeda(s) de $1.00\n3 moeda(s) de $0.05";
        $obtido = calculaTroco(5.00, 10.15);
        $this->assertEquals($esperado, $obtido);
    }

    public function testValorDaCompraSendoCincoReaisEValorPagoSendoDezReaisESetentaETresCentavos(): void
    {
        $esperado = "\n5 moeda(s) de $1.00\n2 moeda(s) de $0.25\n4 moeda(s) de $0.05\n3 moeda(s) de $0.01";
        $obtido = calculaTroco(5.00, 10.73);
        $this->assertEquals($esperado, $obtido);
    }

    public function testValorDaCompraEValorPagoNegativos(): void
    {
        $esperado = "Sem troco";
        $obtido = calculaTroco(-5.00, -7.00);
        $this->assertEquals($esperado, $obtido);
    }

}

