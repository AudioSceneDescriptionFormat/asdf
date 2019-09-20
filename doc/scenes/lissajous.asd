<asdf version="0.4">
  <par>
    <clip id="ukulele" file="audio/ukewave.ogg" />
    <par repeat="2">
      <transform apply-to="ukulele">
        <o pos="-2 0" speed="0" />
        <o pos="2 0" time="15" speed="0" />
        <o pos="closed" time="30" />
      </transform>
      <seq repeat="3">
        <transform apply-to="ukulele">
          <o pos="0 0" />
          <o pos="0 2" time="2.5" speed="0" />
          <o pos="0 -2" time="7.5" speed="0" />
          <o pos="closed" time="10" />
        </transform>
      </seq>
    </par>
  </par>
</asdf>
