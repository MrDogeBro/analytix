# Copyright (c) 2021-present, Ethan Henderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import annotations

import typing as t

from analytix import data, errors
from analytix.abc import DetailedReportType, ReportType
from analytix.features import (
    Dimensions,
    ExactlyOne,
    Filters,
    Metrics,
    OneOrMore,
    Optional,
    Required,
    SortOptions,
    ZeroOrMore,
    ZeroOrOne,
)


class BasicUserActivity(ReportType):
    def __init__(self) -> None:
        self.name = "Basic user activity"
        self.dimensions = Dimensions()
        self.filters = Filters(
            ZeroOrOne("country", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_VIDEO_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class BasicUserActivityUS(ReportType):
    def __init__(self) -> None:
        self.name = "Basic user activity (US)"
        self.dimensions = Dimensions()
        self.filters = Filters(
            Required("province"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_PROVINCE_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class TimeBasedActivity(ReportType):
    def __init__(self) -> None:
        self.name = "Time-based activity"
        self.dimensions = Dimensions(ExactlyOne("day", "month"))
        self.filters = Filters(
            ZeroOrOne("country", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_VIDEO_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class TimeBasedActivityUS(ReportType):
    def __init__(self) -> None:
        self.name = "Time-based activity (US)"
        self.dimensions = Dimensions(ExactlyOne("day", "month"))
        self.filters = Filters(
            ZeroOrOne("province"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_PROVINCE_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class GeographyBasedActivity(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based activity"
        self.dimensions = Dimensions(Required("country"))
        self.filters = Filters(
            ZeroOrOne("continent", "subContinent"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_VIDEO_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class GeographyBasedActivityUS(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based activity (US)"
        self.dimensions = Dimensions(Required("province"))
        self.filters = Filters(
            ZeroOrOne("country==US"),
            ZeroOrOne("video", "group"),
        )
        self.metrics = Metrics(*data.ALL_PROVINCE_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsSubscribedStatus(ReportType):
    def __init__(self) -> None:
        self.name = "User activity by subscribed status"
        self.dimensions = Dimensions(
            Optional("subscribedStatus"), ZeroOrOne("day", "month")
        )
        self.filters = Filters(
            ZeroOrOne("country", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            Optional("subscribedStatus"),
        )
        self.metrics = Metrics(*data.SUBSCRIPTION_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsSubscribedStatusUS(ReportType):
    def __init__(self) -> None:
        self.name = "User activity by subscribed status (US)"
        self.dimensions = Dimensions(
            Optional("subscribedStatus"), ZeroOrOne("day", "month")
        )
        self.filters = Filters(
            ZeroOrOne("video", "group"),
            ZeroOrMore("province", "subscribedStatus"),
        )
        self.metrics = Metrics(*data.LESSER_SUBSCRIPTION_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsLiveTimeBased(ReportType):
    def __init__(self) -> None:
        self.name = "Time-based playback details (live)"
        self.dimensions = Dimensions(
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
            ZeroOrOne("day", "month"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.LIVE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsViewPercentageTimeBased(ReportType):
    def __init__(self) -> None:
        self.name = "Time-based playback details (view percentage)"
        self.dimensions = Dimensions(
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
            ZeroOrOne("day", "month"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsLiveGeographyBased(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based playback details (live)"
        self.dimensions = Dimensions(
            Required("country"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.LIVE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsViewPercentageGeographyBased(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based playback details (view percentage)"
        self.dimensions = Dimensions(
            Required("country"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsLiveGeographyBasedUS(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based playback details (live, US)"
        self.dimensions = Dimensions(
            Required("province"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("country==US"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.LIVE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackDetailsViewPercentageGeographyBasedUS(ReportType):
    def __init__(self) -> None:
        self.name = "Geography-based playback details (view percentage, US)"
        self.dimensions = Dimensions(
            Required("province"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("country==US"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackLocation(ReportType):
    def __init__(self) -> None:
        self.name = "Playback locations"
        self.dimensions = Dimensions(
            Required("insightPlaybackLocationType"),
            ZeroOrMore("day", "liveOrOnDemand", "subscribedStatus"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus"),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class PlaybackLocationDetail(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Playback locations (detailed)"
        self.dimensions = Dimensions(
            Required("insightPlaybackLocationDetail"),
        )
        self.filters = Filters(
            Required("insightPlaybackLocationType==EMBEDDED"),
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus"),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(
            *data.LOCATION_AND_TRAFFIC_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 25


class TrafficSource(ReportType):
    def __init__(self) -> None:
        self.name = "Traffic sources"
        self.dimensions = Dimensions(
            Required("insightTrafficSourceType"),
            ZeroOrMore("day", "liveOrOnDemand", "subscribedStatus"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus"),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class TrafficSourceDetail(DetailedReportType):
    # TODO: Validate against supported traffic sources

    def __init__(self) -> None:
        self.name = "Traffic sources (detailed)"
        self.dimensions = Dimensions(
            Required("insightTrafficSourceDetail"),
        )
        self.filters = Filters(
            Required("insightTrafficSourceType"),
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus"),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(
            *data.LOCATION_AND_TRAFFIC_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 25


class DeviceType(ReportType):
    def __init__(self) -> None:
        self.name = "Device types"
        self.dimensions = Dimensions(
            Required("deviceType"),
            ZeroOrMore("day", "liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore(
                "operatingSystem",
                "liveOrOnDemand",
                "subscribedStatus",
                "youtubeProduct",
            ),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class OperatingSystem(ReportType):
    def __init__(self) -> None:
        self.name = "Operating systems"
        self.dimensions = Dimensions(
            Required("operatingSystem"),
            ZeroOrMore("day", "liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore(
                "deviceType",
                "liveOrOnDemand",
                "subscribedStatus",
                "youtubeProduct",
            ),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class DeviceTypeAndOperatingSystem(ReportType):
    def __init__(self) -> None:
        self.name = "Device types and operating systems"
        self.dimensions = Dimensions(
            Required("deviceType", "operatingSystem"),
            ZeroOrMore("day", "liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.LOCATION_AND_TRAFFIC_METRICS)
        self.sort_options = SortOptions(*self.metrics.values)


class ViewerDemographics(ReportType):
    def __init__(self) -> None:
        self.name = "Viewer demographics"
        self.dimensions = Dimensions(
            OneOrMore("ageGroup", "gender"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            ZeroOrMore(
                "deviceType",
                "liveOrOnDemand",
                "subscribedStatus",
                "youtubeProduct",
            ),
        )
        self.metrics = Metrics("viewerPercentage")
        self.sort_options = SortOptions(*self.metrics.values)


class EngagementAndContentSharing(ReportType):
    def __init__(self) -> None:
        self.name = "Engagement and content sharing"
        self.dimensions = Dimensions(
            Required("sharingService"),
            Optional("subscribedStatus"),
        )
        self.filters = Filters(
            ZeroOrOne("country", "continent", "subContinent"),
            ZeroOrOne("video", "group"),
            Optional("subscribedStatus"),
        )
        self.metrics = Metrics("viewerPercentage")
        self.sort_options = SortOptions(*self.metrics.values)


class AudienceRetention(ReportType):
    def __init__(self) -> None:
        self.name = "Audience retention"
        self.dimensions = Dimensions(Required("elapsedVideoTimeRatio"))
        self.filters = Filters(
            Required("video"),
            ZeroOrMore("audienceType", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics("audienceWatchRatio", "relativeRetentionPerformance")
        self.sort_options = SortOptions(*self.metrics.values)

    def validate(
        self,
        dimensions: t.Collection[str],
        filters: dict[str, str],
        metrics: t.Collection[str],
        sort_options: t.Collection[str],
        max_results: int = 0,
    ) -> None:
        super().validate(dimensions, filters, metrics, sort_options)

        if "," in filters["video"]:
            raise errors.UnsupportedFilterValue("video", filters["video"])


class TopVideosRegional(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Top videos by region"
        self.dimensions = Dimensions(Required("video"))
        self.filters = Filters(ZeroOrOne("country", "continent", "subContinent"))
        self.metrics = Metrics(*data.ALL_VIDEO_METRICS)
        self.sort_options = SortOptions(
            *data.TOP_VIDEOS_EXTRA_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 200


class TopVideosUS(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Top videos by state"
        self.dimensions = Dimensions(Required("video"))
        self.filters = Filters(Required("province"), Optional("subscribedStatus"))
        self.metrics = Metrics(*data.ALL_PROVINCE_METRICS)
        self.sort_options = SortOptions(
            *data.TOP_VIDEOS_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 200


class TopVideosSubscribed(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Top videos by subscription status"
        self.dimensions = Dimensions(Required("video"))
        self.filters = Filters(
            Optional("subscribedStatus"),
            ZeroOrOne("country", "continent", "subContinent"),
        )
        self.metrics = Metrics(*data.SUBSCRIPTION_METRICS)
        self.sort_options = SortOptions(
            *data.TOP_VIDEOS_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 200


class TopVideosYouTubeProduct(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Top videos by YouTube product"
        self.dimensions = Dimensions(Required("video"))
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrMore("subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(
            *data.TOP_VIDEOS_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 200


class TopVideosPlaybackDetail(DetailedReportType):
    def __init__(self) -> None:
        self.name = "Top videos by playback detail"
        self.dimensions = Dimensions(Required("video"))
        self.filters = Filters(
            ZeroOrOne("country", "province", "continent", "subContinent"),
            ZeroOrMore("liveOrOnDemand", "subscribedStatus", "youtubeProduct"),
        )
        self.metrics = Metrics(*data.VIEW_PERCENTAGE_PLAYBACK_DETAIL_METRICS)
        self.sort_options = SortOptions(
            *data.TOP_VIDEOS_SORT_OPTIONS, descending_only=True
        )
        self.max_results = 200


def determine(
    dimensions: t.Collection[str], filters: dict[str, str], metrics: t.Collection[str]
) -> ReportType:
    curated = filters.get("isCurated", "0") == "1"

    # if "adType" in dimensions:
    #     return AdPerformance()

    if "sharingService" in dimensions:
        return EngagementAndContentSharing()

    if "elapsedVideoTimeRatio" in dimensions:
        return AudienceRetention()

    # if "playlist" in dimensions:
    #     return TopPlaylists()

    if "insightPlaybackLocationType" in dimensions:
        # if curated:
        #     return PlaybackLocationPlaylist()
        return PlaybackLocation()

    if "insightPlaybackLocationDetail" in dimensions:
        # if curated:
        #     return PlaybackLocationDetailPlaylist()
        return PlaybackLocationDetail()

    if "insightTrafficSourceType" in dimensions:
        # if curated:
        #     return TrafficSourcePlaylist()
        return TrafficSource()

    if "insightTrafficSourceDetail" in dimensions:
        # if curated:
        #     return TrafficSourceDetailPlaylist()
        return TrafficSourceDetail()

    if "ageGroup" in dimensions or "gender" in dimensions:
        # if curated:
        #     return ViewerDemographicsPlaylist()
        return ViewerDemographics()

    if "deviceType" in dimensions:
        if "operatingSystem" in dimensions:
            # if curated:
            #     return DeviceTypeAndOperatingSystemPlaylist()
            return DeviceTypeAndOperatingSystem()
        # if curated:
        #     return DeviceTypePlaylist()
        return DeviceType()

    if "operatingSystem" in dimensions:
        # if curated:
        #     return OperatingSystemPlaylist()
        return OperatingSystem()

    # TODO: Re-do this section
    if "video" in dimensions:
        if "province" in filters:
            return TopVideosUS()
        if "subscribedStatus" not in filters:
            return TopVideosRegional()
        if "province" not in filters and "youtubeProduct" not in filters:
            return TopVideosSubscribed()
        if "averageViewPercentage" in metrics:
            return TopVideosYouTubeProduct()
        return TopVideosPlaybackDetail()

    if "country" in dimensions:
        if "liveOrOnDemand" in dimensions or "liveOrOnDemand" in filters:
            return PlaybackDetailsLiveGeographyBased()
        # if curated:
        #     return GeographyBasedActivityPlaylist()
        if (
            "subscribedStatus" in dimensions
            or "subscribedStatus" in filters
            or "youtubeProduct" in dimensions
            or "youtubeProduct" in filters
        ):
            return PlaybackDetailsViewPercentageGeographyBased()
        return GeographyBasedActivity()

    if "province" in dimensions:
        if "liveOrOnDemand" in dimensions or "liveOrOnDemand" in filters:
            return PlaybackDetailsLiveGeographyBasedUS()
        # if curated:
        #     return GeographyBasedActivityUSPlaylist()
        if (
            "subscribedStatus" in dimensions
            or "subscribedStatus" in filters
            or "youtubeProduct" in dimensions
            or "youtubeProduct" in filters
        ):
            return PlaybackDetailsViewPercentageGeographyBasedUS()
        return GeographyBasedActivityUS()

    if "youtubeProduct" in dimensions or "youtubeProduct" in filters:
        if "liveOrOnDemand" in dimensions or "liveOrOnDemand" in filters:
            return PlaybackDetailsLiveTimeBased()
        return PlaybackDetailsViewPercentageTimeBased()

    if "liveOrOnDemand" in dimensions or "liveOrOnDemand" in filters:
        return PlaybackDetailsLiveTimeBased()

    if "subscribedStatus" in dimensions:
        if "province" in filters:
            return PlaybackDetailsSubscribedStatusUS()
        return PlaybackDetailsSubscribedStatus()

    if "day" in dimensions or "month" in dimensions:
        # if curated:
        #     return TimeBasedActivityPlaylist()
        if "province" in filters:
            return TimeBasedActivityUS()
        return TimeBasedActivity()

    # if curated:
    #     return BasicUserActivityPlaylist()
    if "province" in filters:
        return BasicUserActivityUS()
    return BasicUserActivity()
