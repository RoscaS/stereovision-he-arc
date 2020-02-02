const sectionFooterTemplate = `
<section class="section-footer section-mixin debug-section-mixin debug-footer">
    <small>
      Design & code:
      <a href="mailto:sol.rosca@gmail.com">
        Sol Rosca
      </a>
      <br />
      Prototype réalisé dans le cadre du projet d'automne 2020 pour l'<b>He-Arc</b>
  </small>
</section>
`;

Vue.component('SectionFooter', {
  template: sectionFooterTemplate,
  data: () => ({}),

  methods: {},
});
