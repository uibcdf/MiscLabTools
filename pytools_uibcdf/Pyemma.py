import pyemma

#def most_weighted_node_in_basin(basin,pcca):
#    jj=pcca.stationary_probability[pcca.metastable_sets[basin]].argmax()
#    jj=pcca.metastable_sets[basin][jj]
#    return jj

#def most_weighted_node(nodes,pcca):
#    jj=pcca.stationary_probability[nodes].argmax()
#    jj=nodes[jj]
#    return jj

def translate_tptsets2originalnodes(list_sets,tpt_sets):
    aux_list=[]
    for ii in list_sets:
        aux_list+=list(tpt_sets[ii])
    return aux_list

def most_weighted_node(nodes=None,metastable_states=None,msm=None,pcca=None):

    aux_stationary_probability=None
    if msm is not None:
        aux_stationary_probability=msm.stationary_distribution
    elif pcca is not None:
        aux_stationary_probability=pcca.stationary_probability

    aux_list_nodes=[]
    if nodes is not None:
        aux_list_nodes=nodes
    elif metastable_states is not None:
        if type(metastable_states) == int:
            metastable_states = [metastable_states]
        for ii in metastable_states:
            aux_list_nodes+=pcca.metastable_sets[ii].tolist()


    jj=aux_stationary_probability[aux_list_nodes].argmax()
    jj=aux_list_nodes[jj]
    return jj
