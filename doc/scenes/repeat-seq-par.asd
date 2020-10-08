<asdf version="0.4">
  <par repeat="2">
    <clip id="ukulele" file="audio/ukewave.ogg" />
    <seq repeat="3">
      <transform apply-to="ukulele">
        <o pos="0 2" />
        <o pos="2 0" />
        <o pos="0 -2" />
        <o pos="-2 0" />
        <o pos="closed" />
      </transform>
      <!-- TODO: another <transform> -->
    </seq>
  </par>
</asdf>
