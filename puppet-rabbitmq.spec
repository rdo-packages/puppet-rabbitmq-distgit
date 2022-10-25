%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-rabbitmq
%global commit 138a977c21b9acb5a007f3c53a7f4a2623101f9e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-rabbitmq
Version:        12.0.3
Release:        0.2%{?milestone}%{?alphatag}%{?dist}
Summary:        Installs, configures, and manages RabbitMQ.
License:        ASL 2.0

URL:            https://github.com/voxpupuli/puppet-rabbitmq

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz
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
* Tue Oct 25 2022 Joel Capitao <jcapitao@redhat.com> 12.0.3-0.2.0rc0.138a977git
- Set the right commit

* Mon Oct 03 2022 RDO <dev@lists.rdoproject.org> 12.0.3-0.1.0rc0.138a977git
- Update to post 12.0.3 (138a977c21b9acb5a007f3c53a7f4a2623101f9e)



