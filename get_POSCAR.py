#!/usr/bin/env python

import sys

script, xyz_file, out_file = sys.argv 

def get_box(xyz_file):
    with open(xyz_file) as in_xyz:
        line1 = in_xyz.readlines()[1] 
        if 'Lattice="' in line1:  # Lattice="40.0 0.0 0.0 0.0 40.0 0.0 0.0 0.0 40.0"
            box =  line1.rstrip().split('"')[1].split()
            a = box[0:3]
            b = box[3:6]
            c = box[6:]
        else:
            print '''
                  OOPS, it seems that there are no box parametrs in xyz file, 
                  Do you want to type by hand or use the default vaules ( 40 x 40 x 40) ? 
                  Please enter  y or Y for tying by hand 
                  and press any other keys for using the default value.
                  '''
            check = raw_input('Please type y or Y or press other keys: >> ')
            if  check == 'y' or check == 'Y':
                a = [raw_input('please enter a direction: '), '0.0', '0.0']
                b = ['0.0', raw_input('please enter b direction: '), '0.0']
                c = ['0.0', '0.0',raw_input('please enter c direction: ') ]
            else:
                a = ['40.0', '0.0', '0.0'] 
                b = ['0.0', '40.0', '0.0'] 
                c = ['0.0', '0.0', '40.0'] 
    return a, b, c 

# get the elements list 
def get_total_ele(xyz_file):
    ele_list = []
    with open(xyz_file) as in_xyz:
        in_file = in_xyz.readlines()[2:]
        for line in in_file:
            ele_list.append(line.rstrip().split()[0])
    return list(set(ele_list))

# get the coordination for one specifix element 
def get_coordinations(ele):
    line_list = []
    with open(xyz_file) as in_xyz:
        in_file = in_xyz.readlines()[2:]
        for line in in_file:
            line_s = line.rstrip().split()[0:4]
            if ele in line_s:
                line_list.append(line_s)
    return line_list

# Get the number of each element 
def get_num_ele(ele):
    return len(get_coordinations(ele))


poscar = open(out_file, 'w')
poscar.write('Converted_POSCAR\n1.0\n')
for i in get_box(xyz_file):
    poscar.write('%s %s %s\n' %(i[0], i[1], i[2]))

# Write Elements line 
for i in get_total_ele(xyz_file):
    poscar.write(i+' ')
poscar.write('\n')

# Write elements numbers line 
for i in get_total_ele(xyz_file):
    poscar.write(str(get_num_ele(i))+' ')

# Write Cartesian line 
poscar.write('\nCartesian\n')

# Write Cooridination part 
for i in get_total_ele(xyz_file):
    for j in get_coordinations(i): 
        poscar.write('%s %s %s\n' %(j[1], j[2], j[3]))

print 'Done! the POSCAR is named as %s' %(out_file)
