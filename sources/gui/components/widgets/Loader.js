const loaderTemplate = `
<div class="section">
  <div class="loader-wrapper" :class="{'is-active': isActive}">
    <h1 class="loader-label">Closing feed</h1>
    <div class="loader is-loading">
    </div>
  </div>
  <slot></slot>
</div>
`;

const loaderStyle = `

`;

Vue.component('Loader', {
  template: loaderTemplate,
  style: loaderStyle,
  props: {
    isActive: {type: Boolean, default: false},
  },
  data: () => ({
    // isActive: false,
  }),
  computed: {},

  methods: {},
  mounted() {
    console.log(this.isActive);
  },
});
