import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

const routes = [];

const createRouter = () =>
  new Router({
    scrollBehavior: () => ({ y: 0 }),
    routes
  });
const router = createRouter();

export function resetRouter() {
  const newRouter = createRouter();
  router.matcher = newRouter.matcher; // reset router
}

export default router;
