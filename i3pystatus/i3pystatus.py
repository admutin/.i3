from i3pystatus import Status
import sys
status = Status()

#print (str(sys.argv))
dunkel= sys.argv[1]
dunkler= "#031730"
grau= "#676E7D"
blau= "#176dad"
hell= "#affcff"

farbeSchlecht=hell
farbeGut=dunkel


status.register("clock",
    format="%X",
    )

status.register("weekcal",
  startofweek=0,
  todayhighlight=(' <span bgcolor="#176dad" color="#022234">', '</span> '),
  interval=30,
  hints={'markup': 'pango'},
)
# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week


# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)


for i in range(15):
    status.register("cpu_usage_graph",
        format="{cpu_graph}",
        cpu="usage_cpu"+str(i),
        start_color = farbeGut,
        end_color = farbeSchlecht,
        graph_width = 1,
        graph_style = "blocks",
        )






# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
# status.register("battery",
#     format="{status}/{consumption:.2f}W {bar_design} {remaining:%E%hh:%Mm}",
#     #alert=True,
#     alert_percentage=15,
#     status={
#         "DIS": "↓",
#         "CHR": "",
#         "FULL": "",
#     },)

status.register("ping",
       format = "online",
       format_down = "offline",
       color=hell,)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="enp6s0",
    format_up="E:{v4cidr}",
    format_down="E:down",)

# Note: requires both netifaces and basiciw (for essid and quality)
status.register("network",
    interface="wlp5s0",
    format_up=" {essid} {v4}",
    format_down=" :down",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format=" {avail}G",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format=" {volume}",
    format_muted="muted {volume}",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
# status.register("now_playing",
#     format="{title} ({artist}) {status}",
#     status={
#         "pause": "▷",
#         "play": "▶",
#         "stop": "◾",
#     },
#     hide_no_player=False,)

status.run()
