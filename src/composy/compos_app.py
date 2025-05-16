"""
Composy - Compos API python wrapper
Main interface module to the Compos Automation object
"""

__all__ = ['ComposApp']

from pathlib import Path

# import Composy components
from composy.compos_api import compos_api
from composy.error_handle import ComposError, ComposyError, ErrorCodes
from composy.compos_member import ComposMember
import composy.result_enums as result_enums


class ComposApp:
    """Compos 8.6 COM Automation Interface"""

    UtilisationFactor = result_enums.UtilisationFactor
    ResultStations = result_enums.ResultStations
    ResultProperties = result_enums.ResultProperties
    ResultActions = result_enums.ResultActions
    ResultCapacity = result_enums.ResultCapacity
    ResultNeutralAxis = result_enums.ResultNeutralAxis
    ResultDeflection = result_enums.ResultDeflection
    ResultStress = result_enums.ResultStress
    ResultStrain = result_enums.ResultStrain
    ResultVibration = result_enums.ResultVibration
    ResultStuds = result_enums.ResultStuds
    TransRebarProp = result_enums.TransRebarProp

    def __init__(self):
        self._compos_auto = compos_api.Automation()
        self._file_open: bool = False
        self._file_path: Path = Path('')
        self._num_members: int = int()
        self._member_names: list[str] = []
        self._members: list[ComposMember] = []

    def __del__(self):
        """Destructor for ComposApp class."""
        if self._file_open:
            self.close()

    @property
    def file_open(self):
        """File open?"""
        return self._file_open

    @property
    def file_path(self):
        """File path of Compos file."""
        return self._file_path

    @property
    def num_members(self):
        """Number of members in Compos file."""
        return self._num_members

    @property
    def member_names(self):
        """Name of members in Compos file."""
        return self._member_names

    @property
    def members(self):
        """Members in Compos file."""
        return self._members

    # Public methods
    def open(self, file_path: str | Path):
        """Open a COB, COA or CSV file.

        :param file_path: the name of the file to be opened, including path and extension.
        :type file_path: Union[str, Path]
        :raises ComposyError: File does not exist.
        :raises ComposError: File failed to open Compos file.
        """
        file_path = Path(file_path)
        if not file_path.exists:
            raise ComposyError(f'File does not exist: {str(file_path)}')
        ret: int = self._compos_auto.Open(str(file_path))
        if ret != 0:
            raise ComposError(ret, f'Failed to open Compos file: {str(file_path)}.')
        else:
            self._file_open = True
            self._file_path = file_path
            self.refresh_members()

    def new(self):
        """Open a new file.

        :raises ComposError: Failed to create new Compos file.
        """
        ret: int = self._compos_auto.New()
        if ret != 0:
            raise ComposError(ret, 'Failed to create new Compos file.')
        else:
            self._file_open = True

    def save(self):
        """Save the data to the default file
        (i.e. overwriting the file that was opened or last saved).

        :raises ComposError: ErrorCodes.SAVE
        """
        ret: int = self._compos_auto.Save()
        if ret != 0:
            raise ComposError(ret, ErrorCodes.SAVE[ret])

    def save_as(self, file_path: str | Path):
        """Save the data to COB, COAor CSV file.

        :param file_path: the name of the file to be saved, including path and extension.
        :type file_path: Union[str, Path]
        :raises ComposError: ErrorCodes.SAVE_AS
        """
        file_path = Path(file_path)
        ret: int = self._compos_auto.SaveAs(file_path)
        if ret != 0:
            raise ComposError(ret, ErrorCodes.SAVE_AS[ret])
        self._file_path = file_path

    def close(self):
        """Close the current file.

        :raises ComposError: No Compos file open.
        """
        ret: int = self._compos_auto.Close()
        if ret != 0:
            raise ComposError(ret, 'No Compos file open.')
        self._file_open = False
        self._file_path = Path('')
        self._clear_members()

    def refresh_members(self):
        """Reload all members within open Compos file.

        :raises ComposyError: No Compos file open.
        """
        if self._file_open:
            self._get_num_members()
            self._get_member_names()
            self._get_members()
        else:
            raise ComposyError('No Compos file open.')

    def analyse_all_members(self):
        """Analyse all members in Compos file."""
        for member in self._members:
            member.analyse_member()

    def design_all_members(self):
        """Design all members in Compos file."""
        for member in self._members:
            member.design_member()

    # Private methods
    def _get_num_members(self):
        self._num_members = self._compos_auto.NumMember()

    def _get_member_names(self):
        if not self._num_members:
            raise ComposyError('No members present in Compos file.')
        for member_index in range(0, self._num_members):
            self._member_names.append(self._compos_auto.MemberName(member_index))

    def _get_members(self):
        if not self._num_members:
            raise ComposyError('No members present in Compos file.')
        for member_index in range(0, self._num_members):
            self._members.append(ComposMember.from_index(self._compos_auto, member_index))

    def _clear_members(self):
        self._num_members = int()
        self._member_names = []
        self._members = []
