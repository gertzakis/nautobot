import django_filters

from nautobot.circuits.models import Circuit
from nautobot.dcim.models import Device, Location, Rack, RackReservation, Site
from nautobot.extras.filters import NautobotFilterSet
from nautobot.ipam.models import Aggregate, IPAddress, Prefix, RouteTarget, VLAN, VRF
from nautobot.tenancy.filters.mixins import TenancyModelFilterSetMixin
from nautobot.tenancy.models import Tenant, TenantGroup
from nautobot.utilities.deprecation import class_deprecated_in_favor_of
from nautobot.utilities.filters import (
    NameSlugSearchFilterSet,
    NaturalKeyOrPKMultipleChoiceFilter,
    RelatedMembershipBooleanFilter,
    SearchFilter,
    TreeNodeMultipleChoiceFilter,
)
from nautobot.virtualization.models import Cluster, VirtualMachine


__all__ = (
    "TenancyFilterSet",
    "TenancyModelFilterSetMixin",
    "TenantFilterSet",
    "TenantGroupFilterSet",
)


class TenantGroupFilterSet(NautobotFilterSet, NameSlugSearchFilterSet):
    parent = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=TenantGroup.objects.all(),
        label="Parent tenant group (slug or ID)",
    )
    children = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=TenantGroup.objects.all(),
        label="Children (slug or ID)",
    )
    has_children = RelatedMembershipBooleanFilter(
        field_name="children",
        label="Has children",
    )
    tenants = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Tenant.objects.all(),
        label="Tenants (slug or ID)",
    )
    has_tenants = RelatedMembershipBooleanFilter(
        field_name="tenants",
        label="Has tenants",
    )

    class Meta:
        model = TenantGroup
        fields = ["id", "name", "slug", "description"]


class TenantFilterSet(NautobotFilterSet):
    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "slug": "icontains",
            "description": "icontains",
            "comments": "icontains",
        },
    )
    group = TreeNodeMultipleChoiceFilter(
        queryset=TenantGroup.objects.all(),
        field_name="group",
        label="Tenant group (slug or ID)",
    )
    aggregates = django_filters.ModelMultipleChoiceFilter(
        queryset=Aggregate.objects.all(),
        label="Aggregates (ID)",
    )
    has_aggregates = RelatedMembershipBooleanFilter(
        field_name="aggregates",
        label="Has aggregates",
    )
    circuits = django_filters.ModelMultipleChoiceFilter(
        queryset=Circuit.objects.all(),
        label="Circuits (ID)",
    )
    has_circuits = RelatedMembershipBooleanFilter(
        field_name="circuits",
        label="Has circuits",
    )
    clusters = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Cluster.objects.all(),
        to_field_name="name",
        label="Clusters (name or ID)",
    )
    has_clusters = RelatedMembershipBooleanFilter(
        field_name="clusters",
        label="Has clusters",
    )
    devices = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Device.objects.all(),
        to_field_name="name",
        label="Devices (name or ID)",
    )
    has_devices = RelatedMembershipBooleanFilter(
        field_name="devices",
        label="Has devices",
    )
    ip_addresses = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.all(),
        label="IP addresses (ID)",
    )
    has_ip_addresses = RelatedMembershipBooleanFilter(
        field_name="ip_addresses",
        label="Has IP addresses",
    )
    locations = TreeNodeMultipleChoiceFilter(
        queryset=Location.objects.all(),
        label="Locations (slugs and/or IDs)",
    )
    has_locations = RelatedMembershipBooleanFilter(
        field_name="locations",
        label="Has locations",
    )
    prefixes = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        label="Prefixes (ID)",
    )
    has_prefixes = RelatedMembershipBooleanFilter(
        field_name="prefixes",
        label="Has prefixes",
    )
    rack_reservations = django_filters.ModelMultipleChoiceFilter(
        queryset=RackReservation.objects.all(),
        field_name="rackreservations",
        label="Rack reservations (ID)",
    )
    has_rack_reservations = RelatedMembershipBooleanFilter(
        field_name="rackreservations",
        label="Has rack reservations",
    )
    racks = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=Rack.objects.all(),
        to_field_name="name",
        label="Racks (name or ID)",
    )
    has_racks = RelatedMembershipBooleanFilter(
        field_name="racks",
        label="Has racks",
    )
    route_targets = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=RouteTarget.objects.all(),
        to_field_name="name",
        label="Route targets (name or ID)",
    )
    has_route_targets = RelatedMembershipBooleanFilter(
        field_name="route_targets",
        label="Has route targets",
    )
    sites = NaturalKeyOrPKMultipleChoiceFilter(queryset=Site.objects.all(), label="Sites (slug or ID)")
    has_sites = RelatedMembershipBooleanFilter(
        field_name="sites",
        label="Has sites",
    )
    virtual_machines = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=VirtualMachine.objects.all(),
        to_field_name="name",
        label="Virtual machines (name or ID)",
    )
    has_virtual_machines = RelatedMembershipBooleanFilter(
        field_name="virtual_machines",
        label="Has virtual machines",
    )
    vlans = django_filters.ModelMultipleChoiceFilter(
        queryset=VLAN.objects.all(),
        label="VLANs (ID)",
    )
    has_vlans = RelatedMembershipBooleanFilter(
        field_name="vlans",
        label="Has VLANs",
    )
    vrfs = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=VRF.objects.all(),
        to_field_name="name",
        label="VRFs (name or ID)",
    )
    has_vrfs = RelatedMembershipBooleanFilter(
        field_name="vrfs",
        label="Has VRFs",
    )

    class Meta:
        model = Tenant
        fields = [
            "comments",
            "description",
            "id",
            "name",
            "slug",
            "tags",
        ]


# TODO: remove in 2.2
@class_deprecated_in_favor_of(TenancyModelFilterSetMixin)
class TenancyFilterSet(TenancyModelFilterSetMixin):
    pass