<asdf version="0.4">
  <par>
    <clip file="audio/marimba.ogg">
      <channel id="left" />
      <channel id="right" />
    </clip>
    <transform apply-to="left">
      <o pos="-2 -2" />
      <o pos="-2 2" tension="0.5" />
      <o pos="2 2" tension="-0.5" />
      <o pos="2 -2" />
    </transform>
    <transform apply-to="right">
      <o pos="-2 -2" />
      <o pos="-2 2" bias="-1" />
      <o pos="2 2" bias="1" />
      <o pos="2 -2" />
    </transform>
  </par>
</asdf>

