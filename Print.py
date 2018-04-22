import pprint
import natsort

def __print_branch(branch,d=0,depth=None,values=True,indentstr="\t",lines=None,arrow=None):

    if lines:
        indentspace="\t" * (d-1) + lines*(d>0)
    else:
        indentspace="\t" * d

    if (branch == None or len(branch) == 0):
        print (indentspace, "-")
    else:
        for key, val in natsort.humansorted(branch.items()):
            if (isinstance(val, dict)):
                print (indentspace, key)
                __print_branch(val, d+1, depth=depth,values=values,indentstr=indentstr,lines=lines,arrow=arrow)
            else:
                if values:
                    postval=val
                    if type(val)==str and len(val)>33:
                        postval=val[:7]+'...'+val[-27:]
                    if arrow is None:
                        print(indentspace, key, str('(') + postval + str(')'))
                    else:
                        print(indentspace, key, arrow, postval)
                else:
                    print(indentspace, key)

def dict_as_tree(dictionary=None,depth=None,values=True
                 ,indentstr="\t",lines=" "*4+u"\u2517"+u"\u2501"*4,arrow=u"\u2501"*2+u"\u25B6"):

    __print_branch(dictionary,depth=depth,values=values,indentstr=indentstr,lines=lines,arrow=arrow)

    pass
