import axios from "axios";
import router from "@/router/index";
import { getToken, removeToken, saveToken } from "@/lib/util";
import { Message } from "element-ui";

axios.defaults.timeout = 20000;
axios.defaults.baseURL =
  process.env.NODE_ENV === "production"
    ? process.env["VUE_APP_BASE_API "]
    : "/api";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded;charset=UTF-8";
axios.defaults.headers["X-Requested-With"] = "XMLHttpRequest"; //让后台知道这是ajax请求
Message({
  duration: 5
});
let loading = null;
const queue = {}; //使用队列解决多个请求加载问题
/*
 *请求前拦截
 *用于处理需要请求前的操作
 */
axios.interceptors.request.use(
  config => {
    // console.log(config.baseURL + config.url)
    queue[config.baseURL + config.url] = true;
    if (getToken()) {
      config.headers.Authorization = getToken(); //请求头携带JWT
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);
/*
 *请求响应拦截
 *用于处理数据返回后的操作
 */
axios.interceptors.response.use(
  response => {
    return new Promise((resolve, reject) => {
      if (response && response.headers && response.headers.authorization) {
        saveToken(response.headers.authorization); //JWT失效后，存新的JWT
      }
      //请求成功后关闭加载菊花
      // console.log(response.config);
      if (response && response.config && response.config.url) {
        delete queue[response.config.url];
      }
      if (!Object.keys(queue).length) {
        loading = this.$loading({
          lock: true,
          text: "Loading",
          spinner: "el-icon-loading",
          background: "rgba(0, 0, 0, 0.7)"
        });
      }
      // console.log(queue);
      //文件下载
      if (
        response &&
        response.config &&
        response.config.responseType === "blob"
      ) {
        resolve(response.data);
        return;
      }
      if (response.data.status === true) {
        resolve(response.data.data);
        Message.success(response.data.message);
      } else {
        reject(response.data);
        Message.error(response.data.message || "服务器维护中");
      }
    });
  },
  error => {
    if (error.response && error.response.config && error.response.config.url) {
      delete queue[error.response.config.url];
    }
    if (!Object.keys(queue).length) {
      loading.close();
    }
    //断网处理或者请求超时
    if (!error.response) {
      for (const key in queue) {
        if (queue.hasOwnProperty(key)) {
          delete queue[key];
        }
      }
      loading.close();
      //请求超时
      if (error.message.includes("timeout")) {
        Message.error("请求超时,请检查互联网连接后重试");
      } else {
        Message.error("未知错误");
      }
      return Promise.reject(error);
    }
    /**
     * 后台返回的errors对象，从中间取一个提示出来
     */
    if (error.response && error.response.data && error.response.data.errors) {
      const keys = Object.keys(error.response.data.errors);
      Message.error(error.response.data.errors[keys[0]]);
    }
    const status = error.response.status;
    switch (status) {
      case 500:
        Message.error("服务器错误");
        break;
      case 404:
        Message.error("未找到远程服务器");
        break;
      case 401:
        router.replace({
          path: "/"
        });
        Message.warning("当前登录已失效，请重新登陆");
        removeToken();
        break;
      case 400:
        Message.error("数据异常");
        break;
      default:
        Message.error(error.response.data.message);
    }
    return Promise.reject(error);
  }
);

/*
 *get方法，对应get请求
 *@param {String} url [请求的url地址]
 *@param {Object} params [请求时候携带的参数]
 */
export function get(url, params) {
  return new Promise((resolve, reject) => {
    axios
      .get(url, {
        params
      })
      .then(res => {
        resolve(res);
      })
      .catch(err => {
        reject(err);
      });
  });
}

/*
 *post方法，对应post请求
 *@param {String} url [请求的url地址]
 *@param {Object} params [请求时候携带的参数]
 */
export function post(url, params) {
  return new Promise((resolve, reject) => {
    axios
      .post(url, params)
      .then(res => {
        resolve(res);
      })
      .catch(err => {
        reject(err);
      });
  });
}

//上传图片的方法
export function upload(url, data) {
  return new Promise((resolve, reject) => {
    axios
      .post(url, data.formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      .then(res => {
        resolve(res);
      })
      .catch(err => {
        reject(err);
      });
  });
}

//下载excel的方法
export function download(url, { params }) {
  return new Promise((resolve, reject) => {
    axios
      .get(url, {
        params: params,
        headers: {
          "Content-Type": "application/json;charset=utf-8"
        },
        responseType: "blob"
      })
      .then(res => {
        resolve(res);
      })
      .catch(err => {
        reject(err);
      });
  });
}
