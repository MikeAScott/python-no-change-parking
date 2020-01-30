#!/bin/bash
usage () {
  echo -e "Usage $0 COMMAND" \
    '\n Builds, tests, and packages the app' \
    '\ncommands:' \
    '\n  build       Build app virtual environment' \
    '\n  test        Start test server' \
    '\n  package     Create distributable package' \
    '\n  clean       Clean up build and test environments' \
    '\n  --help      Print usage'    
}

build () {
  echo 'Building venv environment'
  pip3 install virtualenv
  virtualenv venv
  pip3 install -r requirements.txt
  echo -e '\nTo use the environment:\nsource venv/bin/activate\n...\ndeactivate\n'
}

test () {
  echo 'Running test environment'
  source venv/bin/activate
  export FLASK_APP=app
  flask run
  rm -rf __pycache__
  deactivate
  echo -e '\nStopped\n'
}

package () {
  echo 'Building distributable package'
  virtualenv package_venv
  source package_venv/bin/activate
  python3 setup.py bdist_wheel

  deactivate
  rm -rf package_venv
  rm -rf build
  rm -rf sampleapp.egg-info

  echo -e '\nWheel package created in dist:'
  ls dist
  echo -e '\nInstall with pip eg:\npip install dist/no_change_parking-0.0.0.1.py3-none-any.whl\n'
}

clean() {
  echo -e 'Cleaning venv environment'
  rm -rf venv
}

if [ $# -eq 0 ]
  then usage
fi

for var in "$@"
do
  case $var in
    build|test|package|clean)
      $var
      ;;
    -h|--help|help)
      usage
      ;;
    *)
      usage
      ;;
  esac
done
