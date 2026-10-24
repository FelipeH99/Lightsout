Add-Type -AssemblyName System.Drawing

$carpeta = Split-Path -Parent $MyInvocation.MyCommand.Path

function New-EvidenciaPng($entrada, $salida, $titulo) {
    $lineasOriginales = Get-Content -LiteralPath (Join-Path $carpeta $entrada) -Encoding UTF8
    $lineas = @()
    foreach ($linea in $lineasOriginales) {
        if ($linea.Length -le 105) { $lineas += $linea }
        else {
            for ($i = 0; $i -lt $linea.Length; $i += 105) {
                $largo = [Math]::Min(105, $linea.Length - $i)
                $lineas += $linea.Substring($i, $largo)
            }
        }
    }
    $fuente = New-Object System.Drawing.Font('Consolas', 20)
    $fuenteTitulo = New-Object System.Drawing.Font('Arial', 26, ([System.Drawing.FontStyle]::Bold))
    $ancho = 1900
    $alto = [Math]::Max(300, 115 + ($lineas.Count * 32))
    $imagen = New-Object System.Drawing.Bitmap($ancho, $alto)
    $grafico = [System.Drawing.Graphics]::FromImage($imagen)
    $grafico.Clear([System.Drawing.Color]::White)
    $grafico.DrawString($titulo, $fuenteTitulo, [System.Drawing.Brushes]::DarkBlue, 35, 25)
    $y = 75
    foreach ($linea in $lineas) {
        $grafico.DrawString($linea, $fuente, [System.Drawing.Brushes]::Black, 45, $y)
        $y += 32
    }
    $imagen.Save((Join-Path $carpeta $salida), [System.Drawing.Imaging.ImageFormat]::Png)
    $grafico.Dispose(); $imagen.Dispose(); $fuente.Dispose(); $fuenteTitulo.Dispose()
}

New-EvidenciaPng 'ejecucion_3x3.txt' 'ejecucion_3x3.png' 'Registro de ejecucion - tablero 3 x 3'
New-EvidenciaPng 'pruebas_automatizadas.txt' 'pruebas_automatizadas.png' 'Registro de pruebas automatizadas'
