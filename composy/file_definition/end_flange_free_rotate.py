"""
Composy - Compos API python wrapper
Compos file definition - End Flange Free Rotate
"""
__all__ = ['EndFlangeFreeRotate']

class EndFlangeFreeRotate():
    _is_free_to_rotate = {True: 'FREE_TO_ROTATE',
                          False: 'NOT_FREE_TO_ROTATE'}

    def __init__(self,
                 member_name,
                 is_free: bool,
                 ):
        self.member_name = member_name
        self.value = self._is_free_to_rotate[is_free]

    def __repr__(self) -> str:
        return f"END_FLANGE_FREE_ROTATE({self.value})"

    def __str__(self) -> str:
        return f"END_FLANGE_FREE_ROTATE,{self.member_name},{self.value}"
