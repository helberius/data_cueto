import os


def read_file():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    path_to_file = os.path.join(SITE_ROOT,  "10_pathabundance _1.txt")

    myfile = open(path_to_file, encoding="latin-1")  # Reading a UTF-8 file; 'r' is omitted
    ls_lines=myfile.readlines()

    return ls_lines

def process_lines(ls_lines):
    ls_lines2=[]
    for l in ls_lines:
        ls_lines2.append(l.split('\t'))
    return ls_lines2

def get_unique_column_specie(ls_lines):
    ls_specie=[]
    ls_not_valid_species=['Specie']
    for l in ls_lines:
        if len(l)==3:
            st_potential_specie=l[1].strip()
            if st_potential_specie not in ls_specie and st_potential_specie not in ls_not_valid_species:
                ls_specie.append(l[1])
    return ls_specie

def transform_lines_to_dict(ls_lines):

    old_id=''
    dict_group = {}
    ls_groups=[]
    for l in ls_lines:
        id=l[0]

        if (old_id!=id):
            """ we have a new group """
            ls_groups.append(dict_group)
            dict_group = {}
            dict_group['id']=id
            old_id=id


        if len(l)==3:
            try:
                key=l[1].strip()
                dict_group[key]=float(l[2].replace('\n',''))
            except Exception as err:
                print(id,key,err)
    return ls_groups

def create_new_ls_lines(ls_info_as_dict, ls_specie):
    header_line=['id']
    ls_lines=[]
    for s in ls_specie:
        header_line.append(s)
    ls_lines.append(header_line)

    for d in ls_info_as_dict:
        new_line=[None]*(len(ls_specie)+1)
        ls_keys=d.keys()
        for k in ls_keys:
            new_line[header_line.index(k)]= d[k]
        ls_lines.append(new_line)
    return ls_lines

def save_list_to_file(ls_lines, path_output):
    file = open(path_output,'w')


    for l in ls_lines:
        st_line=''
        for e in l:
            if e is None:
                e=''
            st_line=st_line+'|'+str(e)
        st_line=st_line+'\n'
        file.write(st_line)
    file.close()



if __name__ == '__main__':
    ls_lines=read_file()

    ls_lines_updated=process_lines(ls_lines)

    ls_specie=get_unique_column_specie(ls_lines_updated)

    ls_info_as_dict=transform_lines_to_dict(ls_lines_updated)

    ls_formatted_lines=create_new_ls_lines(ls_info_as_dict, ls_specie)

    path_output='/home/helbert/PycharmProjects/cueto/output.csv'
    save_list_to_file(ls_formatted_lines, path_output)

