{ python3Packages, lib, libcoap }:
python3Packages.buildPythonApplication rec {
  pname = "ikea-smartlight";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = [ python3Packages.tqdm libcoap ];

  meta = with lib; {};
}
