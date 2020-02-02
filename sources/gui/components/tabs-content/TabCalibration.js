const tabCalibrationTemplate = `
<div>
  <BaseTabContent :title="title">
  
  
  </BaseTabContent>
</div>
`;

Vue.component('TabCalibration', {
  template: tabCalibrationTemplate,
  data: () => ({
    title: 'Calibration',
  }),

  methods: {},
});
