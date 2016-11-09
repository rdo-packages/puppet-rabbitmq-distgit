%{!?upstream_version: %global upstream_version %{version}}
%define upstream_name puppetlabs-rabbitmq


Name:           puppet-rabbitmq
Version:        5.6.0
Release:        1%{?dist}
Summary:        Installs, configures, and manages RabbitMQ.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-rabbitmq

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-staging
Requires:       puppet >= 2.7.0

%description
Installs, configures, and manages RabbitMQ.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
* Fri Oct 28 2016 Jon Schlueter <jschluet@redhat.com> 5.6.0-1
- Update to 5.6.0 (057a0138f9a53a1d8b7a582734968ec194c3c705)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 5.5.0-1.837d556.git
- Newton update 5.5.0 (837d556a1a817f78f4e92b80643b8d43ff437f46)


