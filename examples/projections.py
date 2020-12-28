#***************************************************#
# This file is part of PFNET.                       #
#                                                   #
# Copyright (c) 2015, Tomas Tinoco De Rubira.       #
#                                                   #
# PFNET is released under the BSD 2-clause license. #
#***************************************************#

# Power Networks - Projections

import sys
import pfnet
import numpy as np

def main(args=None):
    
    if args is None:
        args = sys.argv[1:]
        
    net = pfnet.Parser(args[0]).parse(args[0])

    net.set_flags('bus',
                  'variable',
                  'any',
                  ['voltage magnitude','voltage angle'])
    
    print(net.num_vars, 2*net.num_buses)
    
    P1 = net.get_var_projection('bus', 'any', 'voltage magnitude')
    P2 = net.get_var_projection('bus', 'any', 'voltage angle')
    
    print(type(P1))
    
    x = net.get_var_values()
    v_mags = P1*x
    v_angs = P2*x
    
    print(v_mags)
    print(v_angs)
    
    print(np.linalg.norm(x - (P1.T*v_mags+P2.T*v_angs)))

if __name__ == "__main__":
    main()
