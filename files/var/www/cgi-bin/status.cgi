#!/usr/bin/haserl
content-type: text/html

<%
interfaces=$(/sbin/ifconfig | grep '^\w' | awk {'print $1'})
ipaddr=$(printenv | grep HTTP_HOST | cut -d= -f2 | cut -d: -f1)
hostname="Hostname: openipc-$(ipctool --chip_id)-$(ipctool --sensor_id | awk -F '_' '{print $1}')"
openipc_version=$(cat /etc/os-release | grep "OPENIPC_VERSION" | cut -d= -f2 2>&1)
[ ! -z "$openipc_version" ] && openipc_version="<br>Version: ${openipc_version}"
soc=$(ipcinfo --chip_id 2>&1)
[ ! -z "$soc" ] && soc="<br>SoC: ${soc}"
sensor=$(ipcinfo --long_sensor 2>&1)
[ ! -z "$sensor" ] && sensor="<br>Sensor: ${sensor}"
soc_temp=$(ipcinfo --temp 2>&1)
[ ! -z "$soc_temp" ] && soc_temp="<br>Temp.: $soc_temp°C"
%>
<%in _header.cgi %>
<h2>Device Status</h2>

<div class="row">
  <div class="col mb-3">
    <div class="card h-100">
      <div class="card-header">Device Info</div>
      <div class="card-body">
        <b># ipcinfo</b>
        <pre><%= $hostname %><% echo -n "$openipc_version" %><% echo -n "$soc" %><% echo -n "$sensor" %><% echo -n "$soc_temp" %></pre>
      </div>
    </div>
  </div>

  <div class="col mb-3">
    <div class="card h-100">
      <div class="card-header">System Info</div>
      <div class="card-body">
        <b># uptime</b>
        <pre><% /usr/bin/uptime %></pre>
        <b># cat /proc/meminfo | grep Mem</b>
        <pre><% cat /proc/meminfo | grep Mem %></pre>
      </div>
    </div>
  </div>
</div>

<div class="row">
  <div class="col">
    <div class="card mb-3">
      <div class="card-header">Top 20 Processes</div>
      <div class="card-body">
        <pre><%= "$(ps aux | sort -nrk 3,3 | head -n 20)" %></pre>
      </div>
    </div>
  </div>
</div>

<%in _footer.cgi %>