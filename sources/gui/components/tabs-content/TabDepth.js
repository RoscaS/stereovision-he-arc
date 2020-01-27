const tabDepthTemplate = `
<div>
  <BaseTabContent :title="title">  

    </BaseTabContent>
    <depth-radio-input/>
    
</div>
`;

Vue.component('TabDepth', {
  template: tabDepthTemplate,
  data: () => ({
    title: 'Depth',
    playerState: $Stores.player.state,
  }),
});
