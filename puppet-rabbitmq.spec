%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppet-rabbitmq

Name:           puppet-rabbitmq
Version:        10.1.2
Release:        1%{?dist}
Summary:        Installs, configures, and manages RabbitMQ.
License:        ASL 2.0

URL:            https://github.com/voxpupuli/puppet-rabbitmq

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/v%{version}.tar.gz
BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-archive
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages RabbitMQ.

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/rabbitmq/



%files
%{_datadir}/openstack-puppet/modules/rabbitmq/


%changelog
* Mon Mar 22 2021 RDO <dev@lists.rdoproject.org> 10.1.2-1
- Update to 10.1.2

* Mon May 04 2020 RDO <dev@lists.rdoproject.org> 10.0.2-0.1.0rc0.eafe833git
- Update to post 10.0.2-rc0 (eafe8330240c98321b4bd52ce04061b8a47509d6)

