from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .._generated_types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.linear_issue_assignee_is_the_minimal_assignee_shape_returned_on_linear_issues import (
        LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues,
    )
    from ..models.linear_project_is_a_linear_project_for_a_team import LinearProjectIsALinearProjectForATeam
    from ..models.linear_team_is_a_linear_team_returned_by_the_team_picker_api import (
        LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI,
    )
    from ..models.linear_workflow_state_is_a_linear_workflow_state_for_a_team import (
        LinearWorkflowStateIsALinearWorkflowStateForATeam,
    )


T = TypeVar("T", bound="LinearIssueIsAnIssueReturnedByTheTypedLinearConnectorAPI")


@_attrs_define
class LinearIssueIsAnIssueReturnedByTheTypedLinearConnectorAPI:
    """
    Attributes:
        assignee (LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues | Unset):
        created_at (str | Unset):
        description (str | Unset):
        id (str | Unset):
        identifier (str | Unset):
        priority (int | Unset):
        project (LinearProjectIsALinearProjectForATeam | Unset):
        state (LinearWorkflowStateIsALinearWorkflowStateForATeam | Unset):
        team (LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI | Unset):
        title (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    assignee: LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues | Unset = UNSET
    created_at: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    identifier: str | Unset = UNSET
    priority: int | Unset = UNSET
    project: LinearProjectIsALinearProjectForATeam | Unset = UNSET
    state: LinearWorkflowStateIsALinearWorkflowStateForATeam | Unset = UNSET
    team: LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI | Unset = UNSET
    title: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        created_at = self.created_at

        description = self.description

        id = self.id

        identifier = self.identifier

        priority = self.priority

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        team: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        title = self.title

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if priority is not UNSET:
            field_dict["priority"] = priority
        if project is not UNSET:
            field_dict["project"] = project
        if state is not UNSET:
            field_dict["state"] = state
        if team is not UNSET:
            field_dict["team"] = team
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.linear_issue_assignee_is_the_minimal_assignee_shape_returned_on_linear_issues import (
            LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues,
        )
        from ..models.linear_project_is_a_linear_project_for_a_team import LinearProjectIsALinearProjectForATeam
        from ..models.linear_team_is_a_linear_team_returned_by_the_team_picker_api import (
            LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI,
        )
        from ..models.linear_workflow_state_is_a_linear_workflow_state_for_a_team import (
            LinearWorkflowStateIsALinearWorkflowStateForATeam,
        )

        d = dict(src_dict)
        _assignee = d.pop("assignee", UNSET)
        assignee: LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues | Unset
        if isinstance(_assignee, Unset) or _assignee is None:
            assignee = UNSET
        else:
            assignee = LinearIssueAssigneeIsTheMinimalAssigneeShapeReturnedOnLinearIssues.from_dict(_assignee)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        priority = d.pop("priority", UNSET)

        _project = d.pop("project", UNSET)
        project: LinearProjectIsALinearProjectForATeam | Unset
        if isinstance(_project, Unset) or _project is None:
            project = UNSET
        else:
            project = LinearProjectIsALinearProjectForATeam.from_dict(_project)

        _state = d.pop("state", UNSET)
        state: LinearWorkflowStateIsALinearWorkflowStateForATeam | Unset
        if isinstance(_state, Unset) or _state is None:
            state = UNSET
        else:
            state = LinearWorkflowStateIsALinearWorkflowStateForATeam.from_dict(_state)

        _team = d.pop("team", UNSET)
        team: LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI | Unset
        if isinstance(_team, Unset) or _team is None:
            team = UNSET
        else:
            team = LinearTeamIsALinearTeamReturnedByTheTeamPickerAPI.from_dict(_team)

        title = d.pop("title", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        linear_issue_is_an_issue_returned_by_the_typed_linear_connector_api = cls(
            assignee=assignee,
            created_at=created_at,
            description=description,
            id=id,
            identifier=identifier,
            priority=priority,
            project=project,
            state=state,
            team=team,
            title=title,
            updated_at=updated_at,
            url=url,
        )

        linear_issue_is_an_issue_returned_by_the_typed_linear_connector_api.additional_properties = d
        return linear_issue_is_an_issue_returned_by_the_typed_linear_connector_api

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
