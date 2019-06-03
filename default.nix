{ buildPythonApplication, lib, docopt, schema, ansicolors, libcoap }:
buildPythonApplication rec {
  pname = "traadfri";
  version = "2.1.0";

  src = ./.;

  propagatedBuildInputs = [
    docopt
    schema
    ansicolors
    libcoap
  ];

  meta = with lib; {
    description = "IKEA Trådfri command line interface.";
    license = licenses.gpl3;
    platforms = platforms.all;
  };
}
