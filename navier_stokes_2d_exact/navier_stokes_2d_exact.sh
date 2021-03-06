#! /bin/bash
#
python3 navier_stokes_2d_exact.py > navier_stokes_2d_exact.txt
if [ $? -ne 0 ]; then
  echo "Run error."
  exit 1
fi
#
gnuplot < gms_commands.txt
gnuplot < lukas_commands.txt
gnuplot < poiseuille_commands.txt
gnuplot < spiral_commands.txt
gnuplot < taylor_commands.txt
gnuplot < vortex_commands.txt
#
#  Get rid of obnoxious garbage.
#
rm -f *.pyc
rm -rf __pycache__
#
echo "Normal end of execution."
