import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Element from "element-ui";
import "@/styles/index.scss"; // global css
import "./icons"; // icon
import "./styles/element-variables.scss";
import * as filters from "./filters"; // global filters
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key]);
});
Vue.use(Element, {
  size: "medium" // set element-ui default size
});
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
