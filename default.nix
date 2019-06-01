{ python3Packages, lib }:
python3Packages.buildPythonApplication rec {
  pname = "ikea-smartlight";
  version = "2.0.0";

  src = ./.;

  propagatedBuildInputs = with python3Packages; [
    docopt
    schema
    ansicolors
  ];

  meta = with lib; {
    description = "IKEA Trådfri command line interface.";
    license = licenses.gpl3;
    platforms = platforms.all;
  };
}
