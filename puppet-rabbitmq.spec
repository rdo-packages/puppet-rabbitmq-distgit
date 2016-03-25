%define upstream_name puppetlabs-rabbitmq

Name:           puppet-rabbitmq
Version:        XXX
Release:        XXX
Summary:        Installs, configures, and manages RabbitMQ.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-rabbitmq

Source0:        https://github.com/puppetlabs/puppetlabs-rabbitmq/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
#Requires:       puppet-apt
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

