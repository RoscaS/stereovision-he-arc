const sectionHeaderTemplate = `
<section class="section-header section-mixin debug-section-mixin debug-header">
<!--  <p class="debug-container-title">HEADER</p>-->
  <main-title/>
  <Navbar/>
</section>
`;

Vue.component('SectionHeader', {
  template: sectionHeaderTemplate,
  data: () => ({}),

  methods: {},
});
