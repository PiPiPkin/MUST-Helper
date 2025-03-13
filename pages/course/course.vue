// 在学院列表页面的点击事件中应该有类似这样的代码
navigateToDepartment(deptId) {
  uni.navigateTo({
    url: `/pages/course/course-list?deptId=${deptId}`
  });
}