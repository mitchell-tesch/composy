# Comosy - Compos API python wrapper
# Compos Automation object
__all__ = ['ComposApp']

from pathlib import Path

# import Composy components
from composy.compos_api import *
from composy.error_handle import *
from composy.member import *
from composy.result_enums import *


class ComposApp():
    """Compos 8.6 COM Automation Interface"""
    eUtilisationFactor = eUtilisationFactor
    eResultStations = eResultStations
    eResultProperties = eResultProperties
    eResultActions = eResultActions
    eResultCapacity = eResultCapacity
    eResultNeutralAxis = eResultNeutralAxis
    
    def __init__(self):
        self._compos_api = compos.Automation()
        self._file_open : bool = False
        self._file_path : Path = Path("")
        self._num_members : int = int()
        self._member_names : list[str] = []
        self._members : list[Member] = []

    @property
    def file_open(self):
        return self._file_open

    @property
    def file_path(self):
        return self._file_path

    @property
    def num_members(self):
        return self._num_members
    
    @property
    def members_names(self):
        return self._member_names
    
    @property
    def members(self):
        return self._members


    def open(self, file_path: str | Path) -> None:
        """Open a COB, COA or CSV file.

        :param file_path: the name of the file to be opened, including path and extension.
        :type file_path: Union[str, Path]
        :raises ComposyError: File does not exist.
        :raises ComposError: File failed to open Compos file.
        """
        file_path = Path(file_path)
        if not file_path.exists:
            raise ComposyError(f"File does not exist: {str(file_path)}")
        iErr = self._compos_api.Open(str(file_path))
        if iErr != 0:
            raise ComposError(iErr, f"Failed to open Compos file: {str(file_path)}.")
        else:
            self._file_open = True
            self._file_path = file_path
            self.refresh_members()

    def new(self) -> None:
        """Open a new file.

        :raises ComposError: Failed to create new Compos file.
        """
        iErr : int = self._compos_api.New()
        if iErr != 0:
            raise ComposError(iErr, "Failed to create new Compos file.")
        else:
            self._file_open = True

    def save(self) -> None:
        """Save the data to the default file (i.e. overwriting the file that was opened or last saved).

        :raises ComposError: ErrorCodes.SAVE
        """
        iErr : int = self._compos_api.Save()
        if iErr != 0:
            raise ComposError(iErr, ErrorCodes.SAVE[iErr])

    def save_as(self, file_path: str | Path) -> None:
        """Save the data to COB, COAor CSV file.

        :param file_path: the name of the file to be saved, including path and extension.
        :type file_path: Union[str, Path]
        :raises ComposError: ErrorCodes.SAVE_AS
        """
        file_path = Path(file_path)
        iErr : int = self._compos_api.SaveAs(file_path)
        if iErr != 0:
            raise ComposError(iErr, ErrorCodes.SAVE_AS[iErr])
        self._file_path = file_path

    def close(self) -> None:
        """Close the current file.

        :raises ComposError: No Compos file open.
        """
        iErr : int = self._compos_api.Close()
        if iErr != 0:
            raise ComposError(iErr, "No Compos file open.")

    def refresh_members(self) -> None:
        """Reload all members within open Compos file.

        :raises ComposyError: No Compos file open.
        """
        if self._file_open:
            self._get_num_members()
            self._get_member_names()
            self._get_members()
        else:
            raise ComposyError(f"No Compos file open.")

    def analyse_all_members(self) -> None:
        for member in self._members:
            member.analyse_member()

    def design_all_members(self) -> None:
        for member in self._members:
            member.design_member()


    def _get_num_members(self) -> int:
        self._num_members = self._compos_api.NumMember()

    def _get_member_names(self) -> list[str]:
        if not self._num_members:
            raise ComposyError("No members present in Compos file.")
        for member_index in range(0, self._num_members):
            self._member_names.append(self._compos_api.MemberName(member_index))

    def _get_members(self) -> list[Member]:
        if not self._num_members:
            raise ComposyError("No members present in Compos file.")
        for member_index in range(0, self._num_members):
            self._members.append(Member(self._compos_api, member_index))
        return self._members