def is_depend_on(a, b):
    """ Determine whether `a` depends on `b`
    return Bool
    """
    if a.graph is not b.graph:
        return False
    gd = a.graph.as_graph_def()
    gd_sub = tf.graph_util.extract_sub_graph(gd, [a.op.name])
    return b.op.name in {n.name for n in gd_sub.node}
    
def get_all_parents(a):
    """ Return a list of names where a depends on all these variables.
    """
    gd = a.graph.as_graph_def()
    gd_sub = tf.graph_util.extract_sub_graph(gd, [a.op.name])
    return [n.name for n in gd_sub.node]
    
def get_all_variables(scope):
    """ Return all variables that belong to this scope.
    """
    return tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope= scope)
