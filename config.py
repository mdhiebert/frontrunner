from typing import NamedTuple
    
class Deployment_Vars(NamedTuple):
    path: str
    search_diagonally: bool
    flat_size: int

DEPLOYMENT_VARS = Deployment_Vars(
    path = "/Users/imiller/Desktop/projects/frontrunner",
    search_diagonally = True,
    flat_size = 22,

)

