# xyz2POSCAR
This script converts the xyz format files into POSCAR for VASP calculation

Download it and move it to the bin file 

chmod u+x ~/bin/get_POSCAR.py

To use it: 

get_POSCAR.py XXX.xyz POSCAR 

Note: 
1 The script read the second line to get the box parameters of the structure

2 If there are no parameters, it will ask you to type by hand 

3 if you do not want to type by hand, press anykey and it will use the default values of 40 x 40 x 40


