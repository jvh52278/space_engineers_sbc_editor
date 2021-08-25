import random
#class functions start here
class common:
    def read_file (self,a):
        name = a + ".sbc"
        read_in = open(name,"r")
        return_v = read_in.read()
        read_in.close()
        return return_v
        
    def write_file (self,a,b): # a == the name of file ; b == the new text to over-write to the file
        name = a + ".sbc"
        read_inw = open(name,"w")
        read_inw.write(b)
        read_inw.close()
        
        
    def index_lines (self,a,b,c): #a: the text of the file to index ; b: the list to store the start indexes in ; c: the list to store the ending indexes in
    #NOTE: this puts in index OF THE NEW LINE AFTER THE END OF THE LINE as the END INDEX
        nn = [0] #index iterator
        line_end = "\n"

        while (nn[0] <= len(a) - 1):
            n = nn[0]
            if n == 0:
                b.append(n)
            if (a[n] == line_end) and (n != len(a) - 1) and (a[n+1] != line_end):
                c.append(n)
                b.append(n+1)
            if (n == len(a) - 1) and (len(b) > len(c)):
                c.append(n)
            nn[0] = nn[0] + 1
    def grep (self,a,b,c,d): #a: start index of a line ; b: end index of a line, the last character, NOT A NEW LINE; c: the target string to search for ; d: the text source
        test = ""
        s_1 = "no match"
        s_2 = "match"
        d_v = -5
        status = s_1
        for x in range (a,b):
            if (x <= b - len(c)) and (d[x] == c[0]) and (d[x + len(c) - 1] == c[len(c) - 1]):
#                print ("possible match found")  #debug
                for y in range (x, x + len(c)):
                    test = test + d[y]
            if test == c:
                return_v1 = x + len(c) - 1
                status = s_2
                return return_v1#return the index of the last character of the target search string
                test = ""
            if test != c:
                test = ""
        if status == s_1:
            return d_v
                
    def line_print (self,a,b,c,d): # a: the source text ; b: the start index ; c: the end index - NOTE: assumes that the end index is the index AFTER the last character ; d:mode - 1 == print contents, 2 == return string
        p_v = ""
        for x in range (b,c):
            p_v = p_v + a[x]
        
        if d == 1:
            print (p_v)
            
        if d == 2:
            return p_v
            
    def get_value_char_end (self,a,b,c,d): #a: source text ; b: start index ; c: the end index of the line; d: the ending character - NOTE: this is where the delimiting character is, this function will get everything from the start index to before the end index
        return_v2 = ""
        stat_v = ""
        stop = "stop"
        for x in range (b,c):
        
            if a[x] == d:
                stat_v = stop
        
            if (stat_v != stop) and (a[x] != d):
                return_v2 = return_v2 + a[x]
            
        return return_v2
        
    def insert_text (self,a,b,c,d): #a: the source text ; b: the index to break before - NOTE: this breaks the text before character, use desired index + 1 to include the character you want to break at, where index is the target character; c: the index to break after - NOTE: this does NOT include the index ; d: the text to insert in between
        half_1 = ""
        half_2 = ""
        for x in range (0,b):
            half_1 = half_1 + a[x]
        
        for y in range (c,len(a)):
            half_2 = half_2 + a[y]
            
        whole = half_1 + d + half_2
        
        return whole
# class functions end here

def regular_component_info_search (a,b,c,d): #a == start index of the line ; b == end index of the line ; c == source text ; d == mode -- 1 = return attribute value, 2 = return required quantity value, 3 = return the attribute start index, 4 = return the quantity value start index, 5 = return the critical component value start index, 6 = return the the critical component value
    #gets info for manual editing of regular component lines
    fnc = common()
    #get the attribute value
    search_1 = 'Subtype="'
    a_1 = -5 #the start point of the attribute value
    a_1 = fnc.grep(a,b,search_1,c)
    
    a_value = "" #the attribute value
    
    if a_1 > -5:
        #get the index of the corresponding '"'
        target_1 = '"'
        a_value = fnc.get_value_char_end(c,a_1 + 1,b,target_1) #attribute value
        
    #get the required quantity value
    search_2 = 'Count="'
    a_2 = -5 #the start point of the quantity value
    a_2 = fnc.grep(a,b,search_2,c)
    
    b_value = "" #the quantity value
    
    if a_2 > -5:
        b_value = fnc.get_value_char_end(c,a_2 + 1,b,target_1)
        
    #find the critical component
    c_value = "" #the critical component value
    a_3 = -5 #the start index of the critical value
    search_3 = '<CriticalComponent Subtype="'
    a_3 = fnc.grep(a,b,search_3,c)
    if a_3 > -5:
        c_value = fnc.get_value_char_end(c,a_3 + 1,b,target_1)
    
    #return the selected value
    if d == 1: #return the attribute value
        return a_value
    if d == 2: #return the quantity value
        return b_value
    if d == 3: #return the attribute start point
        return a_1
    if d == 4: #return the quantity start point
        return a_2
    if d == 5: #return the critical component value start index
        return a_3
    if d == 6: #return the critical component
        return c_value
        
    
def mass_grep (a,b,c,d,e,f,g): #a: text source ; b: list containing indexed line start indexes ; c: list containing indexed line end indexes ; d: list to store line start indexes of section starts; e: list to store line end indexes of section starts ; f: list to store start indexes of section ends ; g: list to store end indexes of section ends
    print ("indexing the entire file")
    key_1 = "SubtypeId"
    key_2 = "</Definition"
    stv = "start"
    ste = "end"
    f_stat = stv
    base_v = -5
    key_1n = [base_v]
    key_2n = [base_v]
    fc = common()
    for x in range (0,len(b) - 1):
        ############# debug 
        line = fc.line_print(a,b[x],c[x],2)
#        print ("---line----")
#        print (line)
#        print ("---line----")
        ############# debug
        k1 = key_1n[0]
        k2 = key_2n[0]
        k1 = fc.grep(b[x],c[x],key_1,a)
        if key_1n[0] > base_v: #looking for the end of a section
            k2 = fc.grep(b[x],c[x],key_2,a)
            if k2 is None:
                k2 = -5
            else:
                if (k2 > 0) and (f_stat == ste):
    #                print ("found section end") #debug
#                    print ("MSG: found end at index |",k2,"|") #debug
#                    print (line)
                    key_2n[0] = b[x]
                    f.append(b[x])
                    g.append(c[x])
                    key_1n[0] = base_v
                    key_2n[0] = base_v
                    f_stat = stv
                
        
        if k1 is None:
            k1 = -5
        else:
            if (k1 > 0) and (f_stat == stv): #looking for the start of a section
#                print ("MSG: found start at index |",k1,"|") #debug
#                print (line)
                key_1n[0] = b[x]
                d.append(b[x])
                e.append(c[x])
                f_stat = ste
                
    
def find_char (a,b,c): #a: source text ; b: start index ; c: character to look for
    i = -5
    for x in range (b,len(a)):
        if a[x] == c:
            i = x
            return i
   
    if i < 0:
        return -5
        
open_list = [] #put list of available files in here

name = "available_list.txt"

def create_list (n_list,a_list): #1: text file containing the list of available game files to edit ; 2:the list to store the file names in
    f_in = open (n_list, "r+")
    r_in = f_in.read()
    
    s_index = [] # start indexes
    e_index = [] # end indexes
    
    i = 0
    last_i = -5 #index of the last recorded index postion
    mode = 0
    while (i<len(r_in)):
#        print (r_in[i]) #debug
        s_value = "\n"
        
        if (i == 0): #intitial starting index
#            print ("intial start index") #debug
            s_index.append(i)
            mode = 1
        #
        if (i > 0) and (last_i < 0) and (r_in[i] == s_value):
 #           print ("inital end index") #debug
            e_index.append(i)
            last_i = i
            mode = 0
        #
        
        if (last_i > 0):
            if (mode == 0) and (r_in[i - 1] == s_value): #input start index
 #               print ("normal start index") #debug
                s_index.append(i)
                last_i = i
                mode = 1
            #
            if (mode == 1) and (r_in[i] == s_value): #input end index
 #               print ("normal end index") #debug
                e_index.append(i)
                last_i = i
                mode = 0
            #
            if (mode == 1) and (len(s_index) > len(e_index)) and (i == len(r_in) - 1):
 #               print ("special case: there is no new line at the end") #debug
                e_index.append(i)
        #
        i = i + 1
    #
    
    # debug
 #   print (s_index)
 #   print (e_index)
    # debug
    
    def str_copy(a,b,c): #a: starting index ; b: ending index ; c: source string
        ret = ""
        for x in range (a,b):
            ret = ret + c[x]
        #
#        print (ret) #debug
        return ret
    # 
    
    string = ""
 #   print (r_in[e_index[2]])
    for x in range (0,len(s_index)):
        s_in = s_index[x]
        e_in = e_index[x]
        if (e_in == len(r_in) - 1):
            string = str_copy(s_index[x],e_index[x] + 1,r_in)
            a_list.append(string)
        #
        else:
            string = str_copy(s_index[x],e_index[x],r_in)
            a_list.append(string)
        #
    #
    
    f_in.close()
    #
    


use_list = []
create_list (name,use_list)

u_mode = 1 ; #0 == not running, 1 == running
mode_list = [1,1,0,0] #element 0 == main loop ; element 1 == sub loop (sub modes) ; element 2 == file edit options ; element 3 == specific edit mode is active or not
while (mode_list[0] > 0):
    open_list = ["blank"] #stores the name of the file to open
    
    if (mode_list[1] == 0): #exit program
        mode_list[0] = 0
    
    while (mode_list[1] == 1): #select file/option
    
        for x in range (0,len(use_list)):
            print (use_list[x])
    
        option = input("please select a file to edit or enter 'exit' to close the program: ")
        
        e_code = "exit"
        
        if option == e_code:
            print ("exiting program")
            mode_list[1] = 0
            
        for x in range (0,len(use_list)):
            if use_list[x] == option:
                open_list[0] = option
                mode_list[1] = 2
                
    while (mode_list[1] == 2):
        print ("opening file ","'",option,"' for editing",sep="")
        edit = common()
#        edit.read_file()
        name_in = open_list[0]
        edit_file = edit.read_file(name_in)
#        print (edit_file) #debug
        print ("please select from the following editing options")
        print ("enter 'exit' to return to to the previous menu")
        edit_options_n = ["1", "2"] #index numbers match up with those in edit_options_t
        edit_options_t = ["remove non-standard components from all entries", "edit individual entries"] #index numbers match up with those in edit_options_n
        
        for x in range (0,len(edit_options_n)):
            print ("enter '",edit_options_n[x],"' to"," : ", edit_options_t[x],sep="")
        
        ed_mode = input()
        ex_code = "exit"
        
        
        if ed_mode == ex_code:
            mode_list[1] = 1
            
        for x in range (0,len(edit_options_n)):
            if ed_mode == edit_options_n[x]:
                print ("you have selected: ",edit_options_t[x],sep="")
                mode_list[2] = int(ed_mode)
                mode_list[3] = int(ed_mode)
                

        while (mode_list[2] == 2) and mode_list[3] > 0:
            print ("manual edit mode selected")
            #print ("DEBUG - this feature is under development. it is not fully functional and you will see debugging messages") #debug
            
            line_n_reg = [] #line numbers for regular component lines -- REMEMBER: clear this list when changing to a new entry
            line_n_reg_st = [] #start indexes for each regular component line -- REMEMBER: clear this list when changing to a new entry
            line_n_reg_en = [] #end indexes for each regular component line -- REMEMBER: clear this list when changing to a new entry
            reg_attributes = [] #component types for each regular component line -- REMEMBER: clear this list when changing to a new entry
            reg_attributes_st = [] #the start indexes for attribute values
            reg_values = [] #required quantities for each regular component line -- REMEMBER: clear this list when changing to a new entry
            reg_values_st = [] #the start indexes for quantity values
            
            crt_value_st = [] #the start index of the critical component value
            crt_value = [] #the critical component value
            
            section_start = [-5] #the line number of the section start
            section_end = [-5] #the line number of the section end
            
            file_st = [] #start indexes for every line in the file -- REMEMBER: clear list + re-index after every change
            file_en = [] #end indexes for every line in the file -- REMEMBER: clear list + re-index after every change
            fcc = common()
            fcc.index_lines(edit_file,file_st,file_en)
            
            #select the section to edit
            exit_code = "exit"
            
            print ("enter the name of the item you want to edit")
            print ("enter '",exit_code,"' to return to the previous menu",sep="")
            find_sec = input(":")
            
            if find_sec == exit_code:
                mode_list[3] = 0
                
            start_key_base = "<SubtypeId>"
            start_key_end = "<"
            start_key_full = start_key_base + find_sec + start_key_end #a section starts at this line
            end_key = "</Definition>" #a section ends at this line
            
            print ("searching for: ",find_sec,sep="")
            #print ("start_key_full is |",start_key_full,"|",sep="") #debug
            #find the section start line and end line
            r_mode = [1] #1 == looking for start line ; 2 == looking for end line
            lm = [0] #line number iterator
            
            while (r_mode[0] < 3) and (lm[0] < len(file_st)):
                if r_mode[0] == 1: #looking for start section
                    #print ("searching for section start") #debug
                    st_check = -5 #if this is -5, the section name does not exist in the file
                    i_num = lm[0]
                    st_check = fcc.grep(file_st[i_num],file_en[i_num],start_key_full,edit_file)
                    if st_check > -5: #the section name exists
                        print ("section start found")
                        section_start[0] = i_num
                        r_mode[0] = r_mode[0] + 1
                if r_mode[0] == 2: #looking for section end
                    #print ("seaching for section end") #debug
                    en_check = -5 #if this is -5, the section name does not exist in the file
                    i_num = lm[0]
                    en_check = fcc.grep(file_st[i_num],file_en[i_num],end_key,edit_file)
                    if en_check > -5: #the section end has been found
                        print ("found section end")
                        section_end[0] = i_num
                        r_mode[0] = r_mode[0] + 1
                lm[0] = lm[0] + 1
            #if no match is found
            if (section_start[0] < 0) or (section_end[0] < 0):
                print ("no match for |",find_sec,"| was found",sep="")
            #if a match is found
            if (section_start[0] > 0) or (section_end[0] > 0):
                print ("a match has been found for |",find_sec,"|",sep="")
                #list the relevent information
                #regular component line info gathering
                for x in range (section_start[0],section_end[0] + 1):
                    reg_l = -5
                    crt_l = -5 #trigger for the critical component value
                    reg_key = "<Component Subtype="
                    crt_key = "<CriticalComponent Subtype="
                    reg_l = fcc.grep(file_st[x],file_en[x],reg_key,edit_file)
                    crt_l = fcc.grep(file_st[x],file_en[x],crt_key,edit_file) #for the critical component value
                    if reg_l > 0: #a regular component line has been found
                        #fcc.line_print(edit_file,file_st[x],file_en[x],1) #debug
                        #log the line number
                        line_n_reg.append(x)
                        #log the start index of the line
                        num_s = file_st[x]
                        line_n_reg_st.append(num_s)
                        #log the ending index of the line
                        num_e = file_en[x]
                        line_n_reg_en.append(num_e)
                        #get the attribute and requirement values from the line
                        return_a = regular_component_info_search(file_st[x],file_en[x],edit_file,1)
                        return_b = regular_component_info_search(file_st[x],file_en[x],edit_file,2)
                        return_c = regular_component_info_search(file_st[x],file_en[x],edit_file,3)
                        return_d = regular_component_info_search(file_st[x],file_en[x],edit_file,4)
                        reg_attributes.append(return_a)
                        reg_values.append(return_b)
                        reg_attributes_st.append(return_c)
                        reg_values_st.append(return_d)
                    if crt_l > 0: #the critical component has been found
                        return_e = regular_component_info_search(file_st[x],file_en[x],edit_file,5) #the critical component start index
                        return_f = regular_component_info_search(file_st[x],file_en[x],edit_file,6) #the critical component value
                        #get the critical component value from the line
                        crt_value_st.append(return_e)
                        crt_value.append(return_f)
                #enter editing mode
                edit_loop = [1,0] #element 0 == edit loop ; element 1 == input checking
                #while the edit loop is running, edit_loop[0] = 1, otherwise 0
                #while the input is being checked, edit_loop[1] = 1, otherwise 0
                edit_exit = "exit"
                critical_edit = "critical" #trigger for modifying the critical component
                while (edit_loop[0] == 1): #edit mode activated
                     #display current values. REMEMBER: repeat these steps after every change
                    #print ("##########################") #debug
                    #print (reg_attributes) #debug
                    #print (reg_attributes_st) #debug
                    #print (reg_values) #debug
                    #print (reg_values_st) #debug
                    #print ("##########################") #debug
                
                    line_number = "line number" #line number, based on order in the attributes/values list
                    line_number_str = [] #line numbers converted to string for display purposes
                    #when displaying line number: add additional spaces to the numbers themselves to line everything up
                    attribute = "component type" #the attribute value
                    #adjust this title length based on: the longest attribute value
                    diff_blanks = "" #the additional blank spaces to add to the attributes title
                    quantity = "quantity required" #the quantity of components required -- from list reg_values
                
                    #finding the difference between the amount of characters in: the attribute title and the longest attribute name
                    #finding the longest attribute name
                    longest = [0] #the length of the longest attribute value
                    a_title = len(attribute) #the character length of the attribute title
                    for x in range (0,len(reg_attributes)):
                        length = len(reg_attributes[x])
                        if x == 0:
                            longest[0] = length
                        if x > 0:
                            if length > longest[0]:
                                longest[0] = length
                
                    a_diff = longest[0] - a_title #the difference in character count between the longest attribute value and the attribute title
                
                    #if there is a longer attribute name
                    #adjust the title length
                    if a_diff > 0:
                        #print ("DEBUG - there is a longer attribute name") #debug
                        for x in range (0,a_diff):
                            diff_blanks = diff_blanks + " "
                    #add spaces to attribute values to make everything line up
                    for x in range(0,len(reg_attributes)):
                        longest_value = [longest[0]]
                        #if there are no attribute values longer than the title
                        if a_diff <= 0:
                            longest_value[0] = a_title
                        current_a = len(reg_attributes[x])
                        diff_aa = longest_value[0] - current_a #difference in character count between the longest attribute value/title and the current attribute value
                        if diff_aa > 0: #add spaces
                            for y in range (0,diff_aa):
                                reg_attributes[x] = reg_attributes[x] + " "
                    #adjusting the line number values to be as long as the line number title
                    #convert line numbers into strings and copy them to another list
                    for x in range (0,len(reg_values)):
                        copy_v = str(x)
                        line_number_str.append(copy_v)
                    #print ("############") #Debug
                    #print (line_number_str) #debug
                    #print ("############") #Debug
                    #add blank spaces to the line number strings
                    for x in range (0,len(line_number_str)):
                        base_line = len(line_number)
                        current = len(line_number_str[x])
                        if base_line > current:
                            diff_line = base_line - current #the difference in character count between the line number title and line number values
                            if diff_line > 0:
                                for y in range(0,diff_line): #add blank spaces
                                    line_number_str[x] = line_number_str[x] + " "
                    #print ("#########") #debug
                    #print (line_number) # debug
                    #for x in range (0,len(line_number_str)): #debug
                        #print (line_number_str[x],"|",sep="") #debug
                    #print ("#########") #debug
                
                    #intial display of component requirements
                    print ("-----------------------------------------------------------")
                    print ("currently editing: ",find_sec,sep="")
                    print ("component requirements")
                    print(line_number,"|",attribute,diff_blanks,"|",quantity,sep="")
                    for x in range (0,len(line_number_str)): #there is a space between displayed element
                        print (line_number_str[x]," ",reg_attributes[x]," ",reg_values[x],sep="")
                    #display the critical component
                    #
                    if len (crt_value) > 0:
                        print ("critical component: ",crt_value[0],sep="")
                    #
                    
                    #edit mode
                    print ("---------")
                    print ("for the following input formats, '#' represents the new value or the line you want to change")
                    print ("to edit a required component line and change the component type, enter in the following format: #line_number-component-#value")
                    print ("to edit a required component line and change the required quantity, enter in the following format: #line_number-quantity-#value")
                    print ("to edit the critical component and change the critical component, enter in the following format: ",critical_edit,"-#value",sep="")
                    print ("---------")
                    print ("to return to the previous menu, enter '",edit_exit,"'",sep="")
                    test_num = [0] #the number of input validation tests that have been done, for dual entry lines
                    s_test_num = [-1] #the number of input validation tests that have been done, for single entry lines
                    e_input = input(":") #user input
                    #check if the exit option has been selected
                    if e_input == edit_exit:
                        edit_loop[0] = 0
                        
                    #check if a single entry line is being tested
                    #there is only 1 "-"
                    #the first character is not a "-"
                    #the last character is not a "-"
                    if e_input: #if the input is not blank
                        input_len = len(e_input) #the total character length of the user input
                        input_len_adj = input_len - 1 #the total character length of the input, in terms of index numbers
                        not_this = "-"
                        error_count = [0] # a running tally of input format errors
                        #test if the first character is a "-"
                        if e_input[0] == not_this:
                            error_count[0] =  error_count[0] + 1
                        #test if the last character is a "-"
                        if e_input[input_len_adj] == not_this:
                            error_count[0] = error_count[0] + 1
                        #if the first two tests pass, test if there is not exactly 1 "-"
                        if error_count[0] == 0: #no format errors should be detected, meaning that error_count[0] == 0
                            #check for the number of "-"
                            nc_count = [0] # a running count of the number of "-"
                            for x in range(0,input_len):
                                if e_input[x] == not_this: #if a "-" has been found
                                    nc_count[0] = nc_count[0] + 1
                            #there should be exactly 1 '-"
                            if nc_count[0] == 1:
                                s_test_num[0] = s_test_num[0] + 1
                    
                    #testing for a possible single entry line edit
                    if s_test_num[0] == 0:
                        #print ("DEBUG - single entry line edit is possible")
                        #check if the critical component is being modified
                        fgc = common()
                        test_first = "" #the text from the start of input to before the "-"
                        stop_here = "-"
                        test_first = fgc.get_value_char_end(e_input,0,len(e_input) - 1,stop_here)
                        if test_first == critical_edit: #if a critical component is being modified
                            print ("editing critical component")
                            s_test_num[0] = s_test_num[0] + 1
                        if test_first != critical_edit: #if there is no match for the critical component trigger
                            print ("invalid input")
                    #if the input is not the exit option AND a dual entry line is possibly being edited
                    #validate the format of the input
                    
                    #instant fail case: check if the input is blank
                    if (test_num[0] == 0) and (s_test_num[0] != 1):
                        #print ("DEBUG - test 0: checking if the input is blank") #debug
                        if e_input: #if the input is not blank
                            #print ("DEBUG - test 0 passed") #debug
                            test_num[0] = test_num[0] + 1
                        if not e_input: #if the input is blank, return to input selection
                            print ("invalid input")
                            print ("input is blank")
                    #instant fail case: check if there are not 2 "-"
                    if test_num[0] == 1: #testing there are 2 "-"
                        #print ('DEBUG - test 1: testing for 2 "-"') #debug
                        count = [0] #number of "-"
                        for x in range (0,len(e_input)):
                            find_char_o = "-"
                            if e_input[x] == find_char_o:
                                count[0] =  count[0] + 1
                        correct_num = 2
                        if count[0] == correct_num: #if this test passes, move on to the next test
                            test_num[0] = test_num[0] + 1
                            #print ("DEBUG - test 1 passed") #debug
                        if count[0] != correct_num: #if this test fails, go back to input selection
                            print ("invalid input")
                    #instant fail case: check if the first character of the input is not a number
                    if test_num[0] == 2:
                        #print ("DEBUG - test 2: checking of the first character is a number") #debug
                        first_char = (e_input[0])
                        if first_char.isnumeric(): #if the first character of the input is a number, move on to the next test
                            #print ("DEBUG - test 2 passed") #debug
                            test_num[0] =  test_num[0] + 1
                        if first_char.isnumeric() == False: #if the first character of the input is not a number, return to input selection
                            print ("invalid input")
                    #test 3: check if everything before the first "-" is a number
                    if test_num[0] == 3:
                        #print ('DEBUG - test 3: check if everything before the first "-" is a number') #debug
                        f_index = -5 #the index of the first "-"
                        find_1 = "-"
                        start_point = 0
                        f_index = find_char(e_input,start_point,find_1)
                        non_numeric = [0] #the number of non-numeric characters
                        if f_index > 0:
                            #get the number of non-numeric characters before the first "-"
                            for x in range(0,f_index):
                                test_char = e_input[x]
                                if test_char.isnumeric() == False: #if the character is not a number
                                    non_numeric[0] = non_numeric[0] + 1
                        if non_numeric[0] == 0: #if all the characters before the first "-" are numbers, move on to the next test
                            #print ("DEBUG - test 3 passed") #debug
                            test_num[0] = test_num[0] + 1
                        if non_numeric[0] > 0: #if there is at least 1 non-numeric character before the first "-"
                            print ("invalid input")
                    #test 4: check if the number before the first "-" is a valid line number
                    if test_num[0] == 4:
                        #print ('DEBUG - test 4: check if the number before the first "-" is a valid line number')
                        test_line_num = [] #stores the list of valid line numbers
                        for x in range (0,len(reg_values)): #get the line numbers into a list
                            in_v = str(x)
                            test_line_num.append(in_v)
                        #get the line inputed line number
                        first_d = "-"
                        index_d_1 = -5
                        index_d_1 = find_char(e_input,0,first_d) #the index of the first "-"
                        num_input = "" #the inputed line number
                        if index_d_1 > 0:
                            fmc = common()
                            num_input = fmc.get_value_char_end(e_input,0,len(e_input) - 1,first_d)
                        # check if the inputed line number is a match for valid line number
                        valid_status = [0] # 0 == invalid number, 1 == valid number
                        for y in range (0,len(test_line_num)):
                            if num_input == test_line_num[y]: #if the inputed line number is a match for a valid line number
                                #print ("DEBUG - the inputed line number is valid") #debug
                                #print ("DEBUG - inputed line number |",num_input,"| - matched value |",test_line_num[y],"|",sep="") #debug
                                valid_status[0] = 1
                        if valid_status[0] == 0:
                            print ("invalid input")
                        if valid_status[0] == 1:
                            #print ("DEBUG - test 4 passed") #debug
                            test_num[0] = test_num[0] + 1
                    #test 5: the last character is not a "-"
                    if test_num[0] == 5:
                        #print ('DEBUG - test 5: checking if the last character is not a "-"')
                        len_input = len(e_input) - 1
                        last_dd = "-"
                        if e_input[len_input] == last_dd: #if the last character is a "-"
                            print ("invalid input")
                        if e_input[len_input] != last_dd: #if the last character is not a "-"
                            #print ("DEBUG - test 5 passed")
                            test_num[0] = test_num[0] + 1
                    #test 6: check if the next "-" is not right next to the first "-"
                    if test_num[0] == 6: 
                        #print ('DEBUG - test 6: checking if the next "-" is not right next to the first "-"')
                        next_d = "-"
                        next_index_d = -5 #the index of the second "-"
                        next_index_d = find_char(e_input,0,next_d)
                        next_v_status = [0] #0 == the next character is a "-", 1 == the next character is not a "-"
                        if next_index_d > 0:
                            #check if the next character is a "-"
                            if e_input[next_index_d + 1] != next_d: #if the next character is not a "-"
                                next_v_status[0] = 1
                        if next_v_status[0] == 1:
                            #print ("DEBUG - test 6 passed") #debug
                            test_num[0] = test_num[0] + 1
                        if next_v_status[0] == 0:
                            print ("invalid input")
                    #test 7: the modification type between the first "-" and the second "-" is valid
                    if test_num[0] == 7:
                        #print ('DEBUG - test 7: the modification type between the first "-" and the second "-" is valid') #debug
                        mod_t_1 = "component" #valid modification type 1
                        mod_t_2 = "quantity" #valid modification type 2
                        find_ddd = "-"
                        first_p = [-5] #the index of the first "-"
                        last_p = [-5] #the index of the second "-"
                        #find the index of the first "-"
                        first_p[0] = find_char(e_input,0,find_ddd)
                        if first_p[0] > 0:
                            #find the index of last "-"
                            last_p[0] = find_char(e_input,first_p[0] + 1,find_ddd)
                        if (first_p[0] > 0) and (last_p[0] > 0):
                        # get the text in between the first "-" and the last "-"
                            fvc = common()
                            fl_between = "" #the text between the two "-"
                            fl_between = fvc.get_value_char_end(e_input,first_p[0] + 1,len(e_input) - 1,find_ddd)
                            final_status = [0] #no valid modification type = 0, valid modification type = 1
                            #check if the text is a match for a valid modification type
                            #print ("DEBUG: input |",fl_between,"|",sep="") #debug
                            if fl_between == mod_t_1: #checking if the component type value is being modified
                                #print ("DEBUG - correct argument |",mod_t_1,"|",sep="") #debug
                                #print ("DEBUG - test 7 passed: modifying component type value") #debug
                                test_num[0] = test_num[0] + 1
                                final_status[0] = 1
                            if fl_between == mod_t_2: #checking if the required quantity is being modified
                                #print ("DEBUG - correct argument |",mod_t_2,"|",sep="")
                                #print ("DEBUG - test 7 passed: modifying required quantity value") #debug
                                test_num[0] = test_num[0] + 1
                                final_status[0] = 1
                            if final_status[0] == 0: #no valid match has been found
                                print ("invalid input")
                    

                    
                    
                    #if all tests pass, replace the old value with the new value - for dual entry lines AND single entry lines
                    if (test_num[0] == 8) or (s_test_num[0] == 1): #all tests have passed
                        #print ("DEBUG - all tests passed - modifying the selected value") #debug
                        #get the value after the last "-" -> this is the replacement value
                        end_i = len(e_input) #the character length of the input
                        look_for = "-"
                        first_pos = [-5] #the index position of the first "-"
                        last_pos = [-5] #the index position of the last "-"
                        last_count = [0] #a running count of the the number of "-" found
                        replace_v_in = "" #the new input value
                        input_mode = "" #input mode, what is being edited
                        for x in range (0,end_i): #find the index of the last "-"
                            if e_input[x] == look_for: #if a "-' is found
                                #print ('DEBUG - found a "-"') #debug
                                last_count[0] = last_count[0] + 1
                            if (first_pos[0] < 0) and (last_count[0] == 1): #if the first "-" has been found
                                #print ("DEBUG - the first '-' has been found") #debug
                                first_pos[0] = x    
                            if (last_count[0] == 2) and (last_pos[0] < 0): #if the last "-" has been found
                                #print ("DEBUG - the last '-' has been found") #debug
                                last_pos[0] = x
                                #print ("DEBUG - index postion of last '-' |",last_pos[0],"|",sep="") #debug
                                #print ("DEBUG - last index of the input |",end_i - 1,"|",sep="") #debug
                        if last_pos[0] > 0: #if the last "-" has been found, and a dual entry line is being edited
                            #print ("DEBUG - editing: getting the new value") #debug
                            for x in range (last_pos[0] + 1,end_i): #get all the text from the after the last "-' to the end of the input
                                replace_v_in = replace_v_in + e_input[x]
                        if s_test_num[0] == 1: #if a single entry line is being tested
                            #print ("DEBUG - editing a single entry line, getting replacement value") #debug
                            bpp = find_char(e_input,0,look_for)
                            if bpp > 0:
                                for x in range (bpp + 1,end_i): #get the replacement value
                                    replace_v_in = replace_v_in + e_input[x]
                            #print ("DEBUG - replacement value |",replace_v_in,"|",sep="") #debug
                        #replacing the old value with the new value
                        #print ("DEBUG - new value |",replace_v_in,"|",sep="") # debug
                        mode_1 = "component" #trigger for editing component type
                        mode_2 = "quantity" #trigger for editing required quantity
                        mode_3 = critical_edit
                        start_edit_point = [-5] #break point 1
                        end_break_point = [-5] #break point 2
                        #get the edit mode:
                        #use last_pos[0] and first_pos[0] as the two points if editing a dual entry line
                        if s_test_num[0] != 1: #if editing a dual entry line
                            for x in range (first_pos[0] + 1,last_pos[0]):
                                input_mode = input_mode + e_input[x]
                        if s_test_num[0] == 1: #if editing a single entry line
                            #print ("DEBUG - getting input mode for a single entry line edit") #debug
                            bcp = find_char(e_input,0,look_for) #the position of the "-"
                            if bcp > 0:
                                for x in range (0,bcp):
                                    input_mode = input_mode + e_input[x]
                                #print ("DEBUG - input mode found |",input_mode,"|",sep="") #debug
                        #get the line number
                        line_in = "" #inputed line number
                        ln_index = [0] #running index count
                        ln_loop = [1] #1 == loop running, 0 == exit the loop
                        while ln_loop[0] == 1: #get the text before the first "-"
                            current_index = ln_index[0]
                            find_this = "-"
                            if (e_input[current_index] == find_this) or (current_index >= len(e_input) - 1): #if the first "-" is found
                                ln_loop[0] = 0
                            if (ln_loop[0] == 1) and (current_index < len(e_input) - 1):
                                line_in = line_in + e_input[current_index]
                                ln_index[0] = ln_index[0] + 1
                        if s_test_num[0] != 1: #if editing a dual entry line
                            print ("selected line number to edit |",line_in,"|",sep="")
                        #cast the line number to an int
                        line_num_int = 0
                        line_num_f = [-5]
                        if s_test_num[0] != 1: #if editing a dual entry line
                            line_num_f[0] = int(line_in)
                        if s_test_num[0] == 1: #if editing a single entry line
                            line_num_f[0] = -5
                        line_num_int = line_num_f[0]
                        #check which input mode has been selected
                        #print ("DEBUG - input mode from user input |",input_mode,"|",sep="") #debug
                        if input_mode == mode_1: #if editing a component type
                            print ("changing component type")
                            #set the first breakpoint
                            #if editing component type, use reg_attributes_st for the start point
                            start_edit_point[0] = reg_attributes_st[line_num_int]
                            #print ("DEBUG - breakpoint 1 index |",start_edit_point,"|",sep="") #debug
                            #print ("DEBUG - character at the breakpoint |",edit_file[start_edit_point[0]],"|",sep="") #debug
                        if input_mode == mode_2: #if editing a required quantity
                            print ("changing required quantity")
                            #set the first breakpoint
                            #if editing required qantity, use reg_values_st
                            start_edit_point[0] = reg_values_st[line_num_int]
                            #print ("DEBUG - breakpoint 1 index |",start_edit_point,"|",sep="") #debug
                            #print ("DEBUG - character at the breakpoint |",edit_file[start_edit_point[0]],"|",sep="") #debug
                        #
                        if input_mode == mode_3: #if editing a single entry line ; add an OR condition for other single entry line edits
                            #print ("DEBUG - setting breakpoint 1 for single entry line edit") #debug
                            start_edit_point[0] = crt_value_st[0]
                            #for other single entry lines -> loop through a list to find the specific edit mode/input mode
                            ##the use that to get the specific start point
                        #
                        #find the index of the next '"'
                        next_bp = -5 #the index of the next '"'
                        look_for_this = '"'
                        next_bp = find_char(edit_file,start_edit_point[0] + 1,look_for_this)
                        if next_bp > 0:
                            end_break_point[0] = next_bp
                            #print ('DEBUG - index of the next "'," |",end_break_point[0],"|",sep="") #debug
                        #replace old value with the new one
                        if (start_edit_point[0] > 0) and (end_break_point[0] > 0):
                            print ("inserting new value")
                            #print ("DEBUG - replacement value |",replace_v_in,"|",sep="") #Debug
                            rpc = common()
                            edit_file = rpc.insert_text(edit_file,start_edit_point[0] + 1,end_break_point[0],replace_v_in)
                        #write the changes to text file
                        fcc.write_file(name_in,edit_file)
                        #clear the following lists: line start indexes, line end indexes
                        file_st.clear()
                        file_en.clear()
                        #re-index file
                        fcc.index_lines(edit_file,file_st,file_en)
                        #clear the editable info lists
                        reg_attributes.clear()
                        reg_values.clear()
                        reg_attributes_st.clear()
                        reg_values_st.clear()
                        crt_value_st.clear()
                        crt_value.clear()
                        #re-index the editable info
                        for x in range (section_start[0],section_end[0] + 1):
                            reg_l = -5
                            crt_l = -5 #trigger for the critical component value
                            reg_key = "<Component Subtype="
                            crt_key = "<CriticalComponent Subtype="
                            reg_l = fcc.grep(file_st[x],file_en[x],reg_key,edit_file)
                            crt_l = fcc.grep(file_st[x],file_en[x],crt_key,edit_file) #for the critical component value
                            if reg_l > 0: #a regular component line has been found
                                #fcc.line_print(edit_file,file_st[x],file_en[x],1) #debug
                                #log the line number
                                line_n_reg.append(x)
                                #log the start index of the line
                                num_s = file_st[x]
                                line_n_reg_st.append(num_s)
                                #log the ending index of the line
                                num_e = file_en[x]
                                line_n_reg_en.append(num_e)
                                #get the attribute and requirement values from the line
                                return_a = regular_component_info_search(file_st[x],file_en[x],edit_file,1)
                                return_b = regular_component_info_search(file_st[x],file_en[x],edit_file,2)
                                return_c = regular_component_info_search(file_st[x],file_en[x],edit_file,3)
                                return_d = regular_component_info_search(file_st[x],file_en[x],edit_file,4)
                                reg_attributes.append(return_a)
                                reg_values.append(return_b)
                                reg_attributes_st.append(return_c)
                                reg_values_st.append(return_d)
                            if crt_l > 0: #the critical component has been found
                                return_e = regular_component_info_search(file_st[x],file_en[x],edit_file,5) #the critical component start index
                                return_f = regular_component_info_search(file_st[x],file_en[x],edit_file,6) #the critical component value
                                #get the critical component value from the line
                                crt_value_st.append(return_e)
                                crt_value.append(return_f)
        while (mode_list[2] == 1) and mode_list[3] > 0:
            print ("all entries within this file will be removed of all non standard components")
            st_index = [] #contains the start index of each line in the file
            en_index = [] #contains the ending index of each line in the file
            fn = common()
            fn.index_lines(edit_file,st_index,en_index)
            st_sec_start = [] #contains the start index of each section start
            st_sec_end = [] #contains the end index of each section end
            en_sec_start = [] #contains the start indexes of each section end
            en_sec_end = [] #contains the start indexs of each section end
            mass_grep(edit_file,st_index,en_index,st_sec_start,st_sec_end,en_sec_start,en_sec_end)
            print ("primary indexing complete")
            non_standard_list = ["MetalGrid","LargeTube","Reactor","Superconductor","SmallTube","BulletproofGlass","SolarCell","Medical","Thrust","RadioCommunication","Detector","GravityGenerator","ZoneChip"]
            x_check = "PowerCell"
            regular_component_start = '<Component Subtype="'
            critical_component_start = '<CriticalComponent Subtype="'
            
            line_count = [-1] #the last line to stop at
            run_mode = "1" # 1 == running ; 0 == not running
            
            component_list = [] #stores a running list of regular component values
            
            while (run_mode == "1"):
                #print ("loop is running") #debug
                line_count[0] = line_count[0] + 1
                ln = line_count[0]
                st_sub = [] #start indexes of each line in the file
                en_sub = [] #end indexes of each line in the file
                fn.index_lines(edit_file,st_sub,en_sub)
                #print ("line count: ",ln,sep="")
                #print ("lengh of list: ",len(st_sub) - 1,sep="")
                if ln > len(st_sub) - 1:
                    run_mode = "0"
                #print (st_sub) #debug
                #print (en_sub) #debug
                if ln <= len(st_sub) - 1:
                    line = fn.line_print(edit_file,st_sub[ln],en_sub[ln],2)
                    check_c = -5
                    check_cc = -5
                    #general function: checking for non standard components, exlcluding power cells, in regular component lines
                    
                    #check if the line is a regular component line
                    check_c = fn.grep(st_sub[ln],en_sub[ln],regular_component_start,edit_file) #possible break point 1 for regular component lines
                    #check if the line is a critical component line
                    check_cc = fn.grep(st_sub[ln],en_sub[ln],critical_component_start,edit_file) #possible break point 1 for critical component lines
                    if (check_c > 0) and (check_cc < 0): #if a regular component line is found
                        #print ("found regular component") #debug
                        #print ("current line |",line,"|",sep="") #debug
                        end_c = find_char(edit_file,check_c+1,'"') #possible break point 2
                        #get the value of the component type
                        line_1 = fn.line_print(edit_file,check_c+1,end_c,2)
                        #print ("current value |",line_1,"|",sep="") #debeug
                        component_list.append(line_1)
                        #print ("current components:") #debug
                        #print (component_list)#debug
                        #check if the value is a non-standard component OR if it is a powercell
                        if line_1 == x_check: #if a power cell is detected
                            print ("powercell detected")
                            print ("reducing required amount to 1")
                            #general function: reduce required amount to 1
                            print ("current line |",line,"|",sep="")
                            #find the first break point
                            q_line = 'Count="'
                            break_point_1 = fn.grep(st_sub[ln],en_sub[ln],q_line,edit_file) #break point 1
                            # find the second break point
                            break_point_2 = find_char(edit_file,break_point_1+1,'"') #break point 2
                            #get the current quantity required
                            p_amt = fn.line_print(edit_file,break_point_1+1,break_point_2,2)
                            print ("current required quantity of powercells |",p_amt,"|",sep="")
                            #replace the value with 1
                            replace_n = "1"
                            edit_file = fn.insert_text(edit_file,break_point_1 + 1,break_point_2,replace_n)
                            #clear the previous line indexes
                            st_sub.clear()
                            en_sub.clear()
                            #re-index the file
                            fn.index_lines(edit_file,st_sub,en_sub)
                            line = fn.line_print(edit_file,st_sub[ln],en_sub[ln],2)
                            print ("new line |",line,"|",sep="")
                        if line_1 != x_check: # check if the value is a non-standard component that is not a powercell
                            blank = "blank"
                            check_str = blank
                            for x in range (0,len(non_standard_list)):
                                if line_1 == non_standard_list[x]:
                                    check_str = line_1
                                    print ("non-standard component detected")
                            if check_str != blank:
                                print ("regular component line found")
                                #replace the value with "SteelPlate"
                                replace_v = "SteelPlate"
                                print ("replacing |",line_1,"| with |",replace_v,"|",sep="")
                                print ("current line |",line,"|",sep="")
                                print ("current component value |",line_1,"|",sep="")
                                edit_file = fn.insert_text(edit_file,check_c + 1,end_c,replace_v)
                                #re-index the file
                                st_sub.clear()
                                en_sub.clear()
                                fn.index_lines(edit_file,st_sub,en_sub)
                                line = fn.line_print(edit_file,st_sub[ln],en_sub[ln],2)
                                print ("new line |",line,"|")
                    if (check_c < 0) and (check_cc > 0): #if a critcal component line is found
                        print ("critical component line found")
                        print ("current line |",line,"|",sep="")
                        cblank = "blank"
                        check_cv = cblank
                        #get the component value
                        break_start_c = fn.grep(st_sub[ln],en_sub[ln],critical_component_start,edit_file) #possible break point 1 for critical component lines
                        break_end_c = find_char(edit_file,break_start_c+1,'"') #possible break point 2
                        critical_component_value = fn.line_print(edit_file,break_start_c+1,break_end_c,2)
                        print ("current critical component value |",critical_component_value,"|",sep="")
                        #check if the component value is a non-standard component that is not a powercell
                        for x in range (0,len(non_standard_list)):
                            if critical_component_value == non_standard_list[x]:
                                check_cv = non_standard_list[x]
                        #if the critical component is not a non-standard component
                        print ("the critical component is a powercell or a standard component")
                        print ("no action needed")
                        #if the critical component is a non-standard component
                        if check_cv != cblank:
                            print ("critical component |",check_cv,"| is a non-standard component",sep="")
                            #check the current component list for anything that is not "SteelPlate"
                            print ("current component list:")
                            print (component_list)
                            #get the list index for each item that is "SteelPlate"
                            x_check_s = "SteelPlate"
                            steel_list = [] #list of indexes that are "SteelPlate"
                            for x in range (0,len(component_list)):
                                if component_list[x] == x_check_s:
                                    steel_list.append(x)
                            #generate a random number that is:
                            #between 0 and the ending index of the current component list
                            #not the index number of a "SteelPlate"
                            #the selected random component is not a  non-standard component
                            print ("selecting a random component that is not steelplate")
                            random_run = "1" # 1 == loop is running ; 0 == loop is not running
                            random_selected = "" #this is a the randomly selected element
                            rand_list = [] #stores used random numbers
                            fail_try = [0] #how many times the tests fail
                            last_test = [1] #trigger for closing the test loop when the last random number has been tested. 3 = close the test loop
                            run_test = [0] #trigger for testing a random number. 1 = test the number
                            while (random_run == "1"):
                                print ("DEBUG: subloop start") #debug
                                sub_run = "1"
                                #generate the random number
                                test_r = random.randrange(0,len(component_list))
                                #log the random number that was generated
                                
                                if len(rand_list) < 1: #if no random numbers have been selected
                                    print ("no random numbers have been tested yet")
                                    run_test[0] = 1
                                    rand_list.append(test_r)
                                if len(rand_list) >= 1: #if at least 1 random number has been generated
                                    #check if it is a duplicate
                                    dup_count = [0] #the number of duplicates
                                    for x in range (0,len(rand_list)):
                                        if test_r == rand_list[x]: #if a duplicate is found
                                            dup_count[0] = dup_count[0] + 1
                                    #if there are no duplicates - add the random number to the list
                                    if dup_count[0] == 0:
                                        print ("random number |",test_r,"| has not been tested yet",sep="")
                                        rand_list.append(test_r)
                                        run_test[0] = 1
                                        
                                if run_test[0] == 1:
                                    print ("random number |",test_r,"| has been flagged for testing",sep="")
                                if run_test[0] == 0:
                                    print ("no random number has been flagged for testing")
                                #if the last possible random number is being tested
                                if len(rand_list) == len(component_list):
                                    print ("the last possible random number has been found")
                                    last_test[0] = 3
                                #if all possible random numbers have been tested
                                
                                if (run_test[0] == 0) and (last_test[0] == 3):
                                    print ("there are only two components: steelplate and one other non-standard component")
                                    #replace the critical component with steel plate
                                    print ("replacing critical component with steelplate")
                                    edit_file = fn.insert_text(edit_file,break_start_c + 1,break_end_c,x_check_s)
                                    #re-index the file
                                    st_sub.clear()
                                    en_sub.clear()
                                    fn.index_lines(edit_file,st_sub,en_sub)
                                    line = fn.line_print(edit_file,st_sub[ln],en_sub[ln],2)
                                    print ("new line |",line,"|",sep="")
                                    #reset last_test to 1
                                    last_test[0] = 1
                                    #close the loop
                                    random_run = "0"
                                #if a random number is being tested
                                if (last_test[0] <= 3) and (sub_run == "1") and (run_test[0] == 1):
                                    print ("testing random number |",test_r,"|",sep="")
                                    r_status = [0]
                                    count = [0]
                                    non_count = [0]
                                    #checking if the random index is steelplate
                                    print ("test 1: checking if the random index points to steelplate")
                                    if len(steel_list) > 0:
                                        for x in range(0,len(steel_list)):
                                            if test_r == steel_list[x]:
                                                count[0] = count[0] + 1
                                    if count[0] == 0:
                                        print ("random number test 1 passed")
                                        print ("random number |",test_r,"| does not point to steelplate",sep="")
                                        r_status[0] = r_status[0] + 1
                                    #check if the random number is within the index range of the list component_list
                                    print ("test 2: checking if the random number is within the index range of the component list")
                                    if (test_r >= 0) and (test_r <= len(component_list) - 1):
                                        print ("random number test 2 passed")
                                        print ("random number |",test_r,"| is within the index range of the component list",sep="")
                                        r_status[0] =  r_status[0] + 1
                                    #check that the selected component is not a non-standard component
                                    print ("test 3: checking if the selected component is not a non-standard component")
                                    test_random_select = component_list[test_r]
                                    for x in range (0,len(non_standard_list)):
                                        if test_random_select == non_standard_list[x]:
                                            non_count[0] = non_count[0] + 1
                                        
                                    if non_count[0] == 0:
                                        print ("random number test 3 passed")
                                        print ("random number |",test_r,"| is does not point to a non-standard component",sep="")
                                        r_status[0] = r_status[0] + 1
                                    #get the new critical component value from the list of components
                                    if r_status[0] == 3:
                                        print ("all tests passed")
                                        random_selected = component_list[test_r]
                                        print ("new critical component value |",random_selected,"|",sep="")
                                        #replace the component value with that random list element
                                        edit_file = fn.insert_text(edit_file,break_start_c + 1,break_end_c,random_selected)
                                        #re-index the file
                                        st_sub.clear()
                                        en_sub.clear()
                                        fn.index_lines(edit_file,st_sub,en_sub)
                                        line = fn.line_print(edit_file,st_sub[ln],en_sub[ln],2)
                                        print ("new line |",line,"|",sep="")
                                        #clear the list of used random numbers
                                        print ("clearing list of used random numbers")
                                        rand_list.clear()
                                        #reset last_test to 1
                                        last_test[0] = 1
                                        #reset the number of failed tests  to 0
                                        fail_try[0] = 0
                                        #close the loop
                                        print ("DEBUG: sub-subloop end") #debug
                                        random_run = "0"
                                        sub_run = "0"
                                    #log the number of failed attempts
                                    if r_status[0] != 3:
                                        print ("one or more tests failed")
                                        max_fail = 1
                                        fail_try[0] = fail_try[0] + 1
                                        print ("number of failed tests |",fail_try[0],"|",sep="")
                                        # if the maximum number of failed tests has been reached
                                        if fail_try[0] >= max_fail:
                                            print ("exiting the test loop")
                                            sub_run = "0" #exit the test loop
                                            print ("DEBUG: sub-subloop end") #debug
                                #reset run_test to 0
                                run_test[0] = 0
                                print ("DEBUG: subloop end") #debug    
                        #clear the current component list
                        print ("clearing component list")
                        component_list.clear()
 
            #write the changes to the file
            fn.write_file(name_in,edit_file)
            
            mode_list[3] = 0
            
           
