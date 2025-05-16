# encoding: utf-8
# module Compos_8_6
# from Compos_8_6, Version=8.6.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes


class IAutomation:
    # no doc
    def Analyse(self, csMemName):
        """Analyse(self: IAutomation, csMemName: str) -> Int16"""
        pass

    def BeamSectDesc(self, csMemName):
        """BeamSectDesc(self: IAutomation, csMemName: str) -> str"""
        pass

    def Close(self):
        """Close(self: IAutomation) -> Int16"""
        pass

    def CodeSatisfied(self, csMemName):
        """CodeSatisfied(self: IAutomation, csMemName: str) -> Int16"""
        pass

    def Design(self, csMemName):
        """Design(self: IAutomation, csMemName: str) -> Int16"""
        pass

    def MaxResult(self, csMemName, sOption, iPos):
        """MaxResult(self: IAutomation, csMemName: str, sOption: str) -> (Single, Int16)"""
        pass

    def MemberName(self, index):
        """MemberName(self: IAutomation, index: int) -> str"""
        pass

    def MinResult(self, csMemName, sOption, iPos):
        """MinResult(self: IAutomation, csMemName: str, sOption: str) -> (Single, Int16)"""
        pass

    def New(self):
        """New(self: IAutomation) -> Int16"""
        pass

    def NumIntermediatePos(self, csMemName):
        """NumIntermediatePos(self: IAutomation, csMemName: str) -> Int16"""
        pass

    def NumMember(self):
        """NumMember(self: IAutomation) -> Int16"""
        pass

    def NumTranRebar(self, csMemName):
        """NumTranRebar(self: IAutomation, csMemName: str) -> Int16"""
        pass

    def Open(self, csPathName):
        """Open(self: IAutomation, csPathName: str) -> Int16"""
        pass

    def Result(self, csMemName, sOption, iPos):
        """Result(self: IAutomation, csMemName: str, sOption: str, iPos: Int16) -> Single"""
        pass

    def Save(self):
        """Save(self: IAutomation) -> Int16"""
        pass

    def SaveAs(self, sPathName):
        """SaveAs(self: IAutomation, sPathName: str) -> Int16"""
        pass

    def TranRebarProp(self, csMemName, sOption, iRebar):
        """TranRebarProp(self: IAutomation, csMemName: str, sOption: str, iRebar: Int16) -> Single"""
        pass

    def UtilisationFactor(self, sMemName, sCheckItem):
        """UtilisationFactor(self: IAutomation, sMemName: str, sCheckItem: str) -> Single"""
        pass

    def __init__(self, *args):  # cannot find CLR method
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        pass


class Automation(IAutomation):
    # no doc
    def __init__(self, *args):  # cannot find CLR method
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        pass


class AutomationClass(__ComObject, IAutomation, Automation):
    """AutomationClass()"""

    def Analyse(self, csMemName):
        """Analyse(self: AutomationClass, csMemName: str) -> Int16"""
        pass

    def BeamSectDesc(self, csMemName):
        """BeamSectDesc(self: AutomationClass, csMemName: str) -> str"""
        pass

    def Close(self):
        """Close(self: AutomationClass) -> Int16"""
        pass

    def CodeSatisfied(self, csMemName):
        """CodeSatisfied(self: AutomationClass, csMemName: str) -> Int16"""
        pass

    def Design(self, csMemName):
        """Design(self: AutomationClass, csMemName: str) -> Int16"""
        pass

    def MaxResult(self, csMemName, sOption, iPos):
        """MaxResult(self: AutomationClass, csMemName: str, sOption: str) -> (Single, Int16)"""
        pass

    def MemberName(self, index):
        """MemberName(self: AutomationClass, index: int) -> str"""
        pass

    def MemberwiseClone(self, *args):  # cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject



            Creates a shallow copy of the current System.MarshalByRefObject object.



            cloneIdentity: lse to delete the current System.MarshalByRefObject object's identity, which will cause the object to be assigned a new identity when it is

             marshaled across a remoting boundary. A value of lse is usually appropriate. ue to copy the current System.MarshalByRefObject object's identity to

             its clone, which will cause remoting client calls to be routed to the remote server object.



            Returns: A shallow copy of the current System.MarshalByRefObject object.

        MemberwiseClone(self: object) -> object



            Creates a shallow copy of the current System.Object.

            Returns: A shallow copy of the current System.Object.
        """
        pass

    def MinResult(self, csMemName, sOption, iPos):
        """MinResult(self: AutomationClass, csMemName: str, sOption: str) -> (Single, Int16)"""
        pass

    def New(self):
        """New(self: AutomationClass) -> Int16"""
        pass

    def NumIntermediatePos(self, csMemName):
        """NumIntermediatePos(self: AutomationClass, csMemName: str) -> Int16"""
        pass

    def NumMember(self):
        """NumMember(self: AutomationClass) -> Int16"""
        pass

    def NumTranRebar(self, csMemName):
        """NumTranRebar(self: AutomationClass, csMemName: str) -> Int16"""
        pass

    def Open(self, csPathName):
        """Open(self: AutomationClass, csPathName: str) -> Int16"""
        pass

    def Result(self, csMemName, sOption, iPos):
        """Result(self: AutomationClass, csMemName: str, sOption: str, iPos: Int16) -> Single"""
        pass

    def Save(self):
        """Save(self: AutomationClass) -> Int16"""
        pass

    def SaveAs(self, sPathName):
        """SaveAs(self: AutomationClass, sPathName: str) -> Int16"""
        pass

    def TranRebarProp(self, csMemName, sOption, iRebar):
        """TranRebarProp(self: AutomationClass, csMemName: str, sOption: str, iRebar: Int16) -> Single"""
        pass

    def UtilisationFactor(self, sMemName, sCheckItem):
        """UtilisationFactor(self: AutomationClass, sMemName: str, sCheckItem: str) -> Single"""
        pass

    def __init__(self, *args):  # cannot find CLR method
        """x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature"""
        pass

    def __str__(self, *args):  # cannot find CLR method
        pass
