# dev.nix
{ pkgs, ... }: {
  # List the packages you want to have available in your workspace.
  packages = [
    pkgs.python312
    pkgs.gcc  # This package provides the missing C++ library (libstdc++)
  ];

  # Enable the following if you want to have extensions installed by default.
  # extensions = [
  #   "ms-python.python"
  #   "ms-python.vscode-pylance"
  # ];
}