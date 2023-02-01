<asdf version="0.4">
  <par>
    <clip id="ukulele" file="audio/ukewave.ogg" pos="-2 -2" />
    <transform id="horizontal-movement" apply-to="ukulele" repeat="10">
      <o pos="2 4" />
      <o pos="0 2" />
      <o pos="2 0" />
      <o pos="4 2" />
      <o pos="closed" />
    </transform>
    <transform apply-to="horizontal-movement">
      <o rot="0" />
      <o rot="0 0 90" />
      <o rot="0 0 180" />
    </transform>
  </par>
</asdf>
