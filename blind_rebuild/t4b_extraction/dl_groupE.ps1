$ErrorActionPreference = "Continue"
$items = @(
  @("ragozzine2012_a1758", "1111.4983"),
  @("groupE_jee2014_a520", "1401.3356"),
  @("clowe2012_a520", "1209.2143"),
  @("rau2014_macs1149", "1402.7321"),
  @("wittman2018", "1701.05877"),
  @("harvey2015", "1503.07675")
)
foreach ($it in $items) {
  $dir = Join-Path "d:\Blind_Rebuild\data\papers" $it[0]
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  foreach ($kind in @("eprint","pdf")) {
    if ($kind -eq "eprint") { $url = "https://arxiv.org/e-print/" + $it[1]; $f = Join-Path $dir ($it[1] + "_eprint.gz") }
    else { $url = "https://arxiv.org/pdf/" + $it[1]; $f = Join-Path $dir ($it[1] + ".pdf") }
    try {
      Invoke-WebRequest -Uri $url -OutFile $f -UserAgent "Mozilla/5.0 (research extraction)" -ErrorAction Stop
      $t = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
      $h = (Get-FileHash $f -Algorithm SHA256).Hash
      Add-Content -Path "d:\Blind_Rebuild\t4b_extraction\downloads_E.tsv" -Value ("{0}`t{1}`t{2}`t{3}" -f $f, $url, $t, $h)
      Write-Output "OK $f"
    } catch { Write-Output "FAIL $url $_" }
    Start-Sleep -Seconds 2
  }
}
