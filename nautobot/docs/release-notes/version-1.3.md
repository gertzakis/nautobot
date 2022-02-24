# Nautobot v1.3

This document describes all new features and changes in Nautobot 1.3.

If you are a user migrating from NetBox to Nautobot, please refer to the ["Migrating from NetBox"](../installation/migrating-from-netbox.md) documentation.

## Release Overview

### Added

#### GraphQL Pagination ([#1109](https://github.com/nautobot/nautobot/issues/1109))

GraphQL list queries can now be paginated by specifying the filter parameters `limit` and `offset`. Refer to the [user guide](../user-guides/graphql.md#filtering-queries) for examples.

#### Provider Network Model ([#724](https://github.com/nautobot/nautobot/issues/724))

A [data model](../models/circuits/providernetwork.md) has been added to support representing the termination of a circuit to an external provider's network.

#### Python 3.10 Support ([#1255](https://github.com/nautobot/nautobot/pull/1255))

Python 3.10 is officially supported by Nautobot now, and we are building and publishing Docker images with Python 3.10 now.

### Changed

#### Docker images now default to Python 3.7 ([#1252](https://github.com/nautobot/nautobot/pull/1252))

As Python 3.6 has reached end-of-life, the default Docker images published for this release (i.e. `1.3.0`, `stable`, `latest`) have been updated to use Python 3.7 instead.

### Fixed

### Removed

## v1.3.0a1 (2022-??-??)

### Added

- [#5](https://github.com/nautobot/nautobot/issues/5) - Added the option to perform a "dry run" of Git repository syncing.
- [#498](https://github.com/nautobot/nautobot/issues/498) - Added custom-validator support to the RelationshipAssociation model.
- [#724](https://github.com/nautobot/nautobot/issues/724) - Added Provider Network data model. (Partially based on [NetBox #5986](https://github.com/netbox-community/netbox/issues/5986).)
- [#803](https://github.com/nautobot/nautobot/issues/803) - There is now a *render_boolean* template filter in helpers, which renders computed boolean values as HTML in a consistent manner.
- [#863](https://github.com/nautobot/nautobot/issues/863) - Added the ability to hide a job in the UI by setting `hidden = True` in the Job's inner `Meta` class
- [#881](https://github.com/nautobot/nautobot/issues/881) - Improved the UX of the main Jobs by adding accordion style interface that can collapse/expand jobs provided by each module
- [#885](https://github.com/nautobot/nautobot/issues/885) - Added the ability to define a `soft_time_limit` and `time_limit` in seconds as attributes of a Job's `Meta`.
- [#1109](https://github.com/nautobot/nautobot/issues/1109) - Added pagination support for GraphQL list queries.
- [#1255](https://github.com/nautobot/nautobot/pull/1255) - Added Python 3.10 support.

### Changed

- [#368](https://github.com/nautobot/nautobot/issues/368) - All classes which inherit from all three of (nautobot.utilities.forms.BootstrapMixin, nautobot.extras.forms.CustomFieldModelForm, nautobot.extras.forms.RelationshipModelForm) now inherit from nautobot.extras.forms.NautobotModelForm as their base class. All classes which inherit from all three of (nautobot.utilities.filters.BaseFilterSet, nautobot.extras.filters.CreatedUpdatedFilterSet, nautobot.extras.filters.CustomFieldModelFilterSet) now inherit from nautobot.extras.filters.NautobotFilterSet as their base class. 
- [#443](https://github.com/nautobot/nautobot/issues/443) - The provided "Dummy Plugin" has been renamed to "Example Plugin".
- [#591](https://github.com/nautobot/nautobot/issues/591) - All uses of type() are now refactored to use isinstance() where applicable.
- [#880](https://github.com/nautobot/nautobot/issues/880) - Jobs menu items now form their own top-level menu instead of a sub-section under the Extensibility menu.
- [#909](https://github.com/nautobot/nautobot/issues/909) - Device, InventoryItem, and Rack serial numbers can now be up to 255 characters in length.
- [#916](https://github.com/nautobot/nautobot/issues/916) - A Job.Meta.description can now contain markdown-formatted multi-line text.
- [#1107](https://github.com/nautobot/nautobot/issues/1107) - Circuit Provider account numbers can now be up to 100 characters in length.
- [#1252](https://github.com/nautobot/nautobot/pull/1252) - As Python 3.6 has reached end-of-life, the default Docker images published for this release (i.e. `1.3.0`, `stable`, `latest`) have been updated to use Python 3.7 instead.
- [#1307](https://github.com/nautobot/nautobot/pull/1307) - Updated various Python package dependencies to their latest compatible versions.
- [#1314](https://github.com/nautobot/nautobot/pull/1314) - Updated various development-only Python package dependencies to their latest compatible versions.
- [#1321](https://github.com/nautobot/nautobot/pull/1321) - Updates to various browser package dependencies. This includes updating from Material Design Icons 5.x to 6.x, which has a potential impact on plugins: a [small number of icons have been removed or renamed](https://dev.materialdesignicons.com/upgrade#5.9.55-to-6.1.95) as a result of this change.

### Fixed

### Removed