%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-rabbitmq
%global commit 5ac45dedd9b409c9efac654724bc74867cb9233b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

# Content of tarball for this module is puppet-rabbitmq-%{version} althoug
# module name is puppetlabs-rabbitmq so it's different for DLRN based builds
# and github tarballs based ones
%{?dlrn: %global tarsources %upstream_name}
%{!?dlrn: %global tarsources puppet-rabbitmq}


Name:           puppet-rabbitmq
Version:        5.6.0
Release:        4%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages RabbitMQ.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-rabbitmq

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Aug 24 2017 Alfredo Moralejo <amoralej@redhat.com> 5.6.0-4.5ac45degit
- Pike update 5.6.0 (5ac45dedd9b409c9efac654724bc74867cb9233b)

