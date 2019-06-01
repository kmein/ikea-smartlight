{ python3Packages, lib }:
python3Packages.buildPythonApplication rec {
  pname = "ikea-smartlight";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = [
    python3Packages.docopt
    python3Packages.schema
    python3Packages.ansicolors
  ];

  meta = with lib; {};
}
