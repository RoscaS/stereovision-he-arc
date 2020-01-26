const tabDepthTemplate = `
<div>
  <BaseTabContent :title="title">
  
  
  </BaseTabContent>
</div>
`;

Vue.component('TabDepth', {
  template: tabDepthTemplate,
  data: () => ({
    title: 'Depth'
  }),

  methods: {

  },
});
