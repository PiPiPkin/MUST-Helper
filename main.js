import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

// 全局错误处理
Vue.config.errorHandler = function(err, vm, info) {
  console.error('Vue错误:', err);
  console.info('错误信息:', info);
}

App.mpType = 'app'

const app = new Vue({
  ...App
})
app.$mount()