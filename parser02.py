import datetime
import sys
import os

def read_file(path_to_file):
    print('function to read file')

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    #path_to_file = os.path.join(SITE_ROOT,  "10_pathabundance _1.txt")

    myfile = open(path_to_file, encoding="latin-1")  # Reading a UTF-8 file; 'r' is omitted
    ls_lines=myfile.readlines()

    ls_lines2=[]
    for l in ls_lines:
        line=l.split('\t')
        new_line=[]
        for x in line:
            x=x.replace('\n','')
            new_line.append(x)
        ls_lines2.append(new_line)

    ls_dict_output={}
    for l in ls_lines2:
        if l[0] in ls_dict_output:
            pass
        else:
            ls_dict_output[l[0]]={}

        if len(l)==3:
            ls_dict_output[l[0]][l[1]]=l[2]


    return ls_dict_output


def formatted_dict(ls_dict):
    ls_new_dicts=[]
    for d in ls_dict:
        x_dict=ls_dict[d]
        x_dict['id']=d
        ls_new_dicts.append(x_dict)
    return ls_new_dicts


def save_dict_to_file(ls_dict, output_file):

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    path_to_file = os.path.join(SITE_ROOT,  output_file)


    ls_main_keys=[]
    for d in ls_dict:
        for k in d.keys():
            if k not in ls_main_keys:
                ls_main_keys.append(k)

    ls_main_keys.pop(ls_main_keys.index('Specie'))
    ls_main_keys.insert(0, ls_main_keys.pop(ls_main_keys.index('id')))

    with open(output_file, 'w') as f:
        st_line=''
        for e in ls_main_keys:
            st_line=st_line+e+','
        st_line=st_line+'\n'
        f.write(st_line)


        for l in ls_dict:
            st_line=''
            for k in ls_main_keys:
                if k in l:
                    e=l[k]
                else:
                    e=''
                st_line=st_line+e+','
            st_line=st_line+'\n'
            f.write(st_line)



def save_dict_to_file_old(ls_dict, output_file):

    print(' function save results to file ')

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    path_to_file = os.path.join(SITE_ROOT,  output_file)



    ls_lines_all=[]
    ls_header=['id']
    ls_main_keys=ls_dict.keys()
    for j in ls_main_keys:
        ls_new_line = [None] * 16
        ls_new_line[0]=j
        ls_keys_2=ls_dict[j].keys()
        for k in ls_keys_2:
            if k not in ls_header:
                ls_header.append(k)
            ls_new_line[ls_header.index(k)]=ls_dict[j][k]
        ls_lines_all.append(ls_new_line)


    file = open(path_to_file,'w')

    st_line=''
    for e in ls_header:
        if e is None:
            e=''
        st_line=st_line+e + '|'
    file.write(st_line)

    for l in ls_lines_all:
        st_line=''
        for e in l:
            if e is None:
                e=''
            st_line=st_line+'|'+str(e)
        st_line=st_line+'\n'
        file.write(st_line)
    file.close()







if __name__ == '__main__':
    st_now=datetime.datetime.now().strftime('%a %d %H:%M:%S')
    print('---------------------------------------------------')
    print('--------- This is the Parser of Helbert -----------')
    print('---------' , st_now , '-------------------------')
    st_input_file=sys.argv[1]
    st_output_file=sys.argv[2]

    ls_dict_output=read_file(st_input_file)

    ls_formatted_dict=formatted_dict(ls_dict_output)
    save_dict_to_file(ls_formatted_dict,st_output_file)

    print('work done, have a nice day!')


