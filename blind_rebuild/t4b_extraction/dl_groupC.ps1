$ErrorActionPreference = "Stop"
$items = @(
  @{name="jee2014_a520"; id="1401.3356"},
  @{name="okabe_umetsu2008"; id="astro-ph/0702649"},
  @{name="jee2015_ciza2242"; id="1410.2898"},
  @{name="dawson2012_musketball"; id="1110.4391"}
)
$tsv = "d:\Blind_Rebuild\t4b_extraction\downloads_C.tsv"
if (-not (Test-Path $tsv)) { "file_path`turl`tutc_time`tsha256" | Out-File -FilePath $tsv -Encoding utf8 }
foreach ($it in $items) {
  $dir = "d:\Blind_Rebuild\data\papers\" + $it.name
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  foreach ($kind in @("e-print","pdf")) {
    $url = "https://arxiv.org/$kind/" + $it.id
    $ext = if ($kind -eq "pdf") { ".pdf" } else { ".eprint.gz" }
    $out = Join-Path $dir ($it.name + $ext)
    Invoke-WebRequest -Uri $url -OutFile $out -UserAgent "Mozilla/5.0 (BlindRebuild extraction)"
    $t = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
    $h = (Get-FileHash -Algorithm SHA256 $out).Hash
    "$out`t$url`t$t`t$h" | Out-File -FilePath $tsv -Append -Encoding utf8
    Start-Sleep -Seconds 3
  }
}
Get-Content $tsv
