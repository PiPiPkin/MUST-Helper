// 全局混入，提供通用方法
export default {
  methods: {
    getFlowerSentData() {
      console.log('送花功能已禁用');
      return Promise.resolve({});
    }
  }
}