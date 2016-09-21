%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-rabbitmq
%global commit 837d556a1a817f78f4e92b80643b8d43ff437f46
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-rabbitmq
Version:        5.5.0
Release:        1%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages RabbitMQ.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-rabbitmq

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 5.5.0-1.837d556.git
- Newton update 5.5.0 (837d556a1a817f78f4e92b80643b8d43ff437f46)


