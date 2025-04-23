from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.aggregated_metrics_response_body import AggregatedMetricsResponseBody
from ...models.aggregation_mode import AggregationMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    jobid: str,
    vertexid: str,
    *,
    get: Union[Unset, str] = UNSET,
    agg: Union[Unset, AggregationMode] = UNSET,
    subtasks: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["get"] = get

    json_agg: Union[Unset, str] = UNSET
    if not isinstance(agg, Unset):
        json_agg = agg.value

    params["agg"] = json_agg

    params["subtasks"] = subtasks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/jobs/{jobid}/vertices/{vertexid}/subtasks/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AggregatedMetricsResponseBody]:
    if response.status_code == 200:
        response_200 = AggregatedMetricsResponseBody.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AggregatedMetricsResponseBody]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    jobid: str,
    vertexid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    get: Union[Unset, str] = UNSET,
    agg: Union[Unset, AggregationMode] = UNSET,
    subtasks: Union[Unset, str] = UNSET,
) -> Response[AggregatedMetricsResponseBody]:
    """Provides access to aggregated subtask metrics.

    Args:
        jobid (str):
        vertexid (str):
        get (Union[Unset, str]):
        agg (Union[Unset, AggregationMode]):
        subtasks (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedMetricsResponseBody]
    """

    kwargs = _get_kwargs(
        jobid=jobid,
        vertexid=vertexid,
        get=get,
        agg=agg,
        subtasks=subtasks,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    jobid: str,
    vertexid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    get: Union[Unset, str] = UNSET,
    agg: Union[Unset, AggregationMode] = UNSET,
    subtasks: Union[Unset, str] = UNSET,
) -> Optional[AggregatedMetricsResponseBody]:
    """Provides access to aggregated subtask metrics.

    Args:
        jobid (str):
        vertexid (str):
        get (Union[Unset, str]):
        agg (Union[Unset, AggregationMode]):
        subtasks (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedMetricsResponseBody
    """

    return sync_detailed(
        jobid=jobid,
        vertexid=vertexid,
        client=client,
        get=get,
        agg=agg,
        subtasks=subtasks,
    ).parsed


async def asyncio_detailed(
    jobid: str,
    vertexid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    get: Union[Unset, str] = UNSET,
    agg: Union[Unset, AggregationMode] = UNSET,
    subtasks: Union[Unset, str] = UNSET,
) -> Response[AggregatedMetricsResponseBody]:
    """Provides access to aggregated subtask metrics.

    Args:
        jobid (str):
        vertexid (str):
        get (Union[Unset, str]):
        agg (Union[Unset, AggregationMode]):
        subtasks (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AggregatedMetricsResponseBody]
    """

    kwargs = _get_kwargs(
        jobid=jobid,
        vertexid=vertexid,
        get=get,
        agg=agg,
        subtasks=subtasks,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    jobid: str,
    vertexid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    get: Union[Unset, str] = UNSET,
    agg: Union[Unset, AggregationMode] = UNSET,
    subtasks: Union[Unset, str] = UNSET,
) -> Optional[AggregatedMetricsResponseBody]:
    """Provides access to aggregated subtask metrics.

    Args:
        jobid (str):
        vertexid (str):
        get (Union[Unset, str]):
        agg (Union[Unset, AggregationMode]):
        subtasks (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AggregatedMetricsResponseBody
    """

    return (
        await asyncio_detailed(
            jobid=jobid,
            vertexid=vertexid,
            client=client,
            get=get,
            agg=agg,
            subtasks=subtasks,
        )
    ).parsed
