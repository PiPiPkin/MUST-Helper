<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{collegeTitle}}课程</text>
		</view>
		
		<!-- 课程列表 -->
		<view class="course-list">
			<view class="course-item" v-for="(item, index) in courseList" :key="index" @click="goToCourseDetail(item)">
				<view class="course-info">
					<text class="course-name">{{item.name}}</text>
					<text class="course-code">{{item.code}}</text>
					<view class="course-rating">
						<text class="rating-value">{{item.rating}}</text>
						<view class="rating-stars">
							<text v-for="n in 5" :key="n" :class="['star', n <= Math.floor(item.rating) ? 'active' : '']">★</text>
						</view>
						<text class="review-count">{{item.reviewCount}}条评价</text>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			statusBarHeight: 20,
			collegeId: '',
			collegeTitle: '',
			courseList: []
		}
	},
	onLoad(options) {
		// 获取状态栏高度 - 使用新的API
		try {
			uni.getSystemInfo({
				success: (res) => {
					this.statusBarHeight = res.statusBarHeight;
					console.log('获取系统信息成功:', res);
				},
				fail: (err) => {
					console.error('获取系统信息失败:', err);
					this.statusBarHeight = 20;
				}
			});
		} catch (error) {
			console.error('获取系统信息异常:', error);
			this.statusBarHeight = 20;
		}
		
		// 获取学院ID - 修改为接收deptId参数
		if (options.deptId) {
			// 将数字ID转换为字符串ID
			const deptId = parseInt(options.deptId);
			console.log('接收到的学院ID:', deptId);
			
			switch(deptId) {
				case 1: this.collegeId = 'engineering'; break;
				case 2: this.collegeId = 'business'; break;
				case 3: this.collegeId = 'arts'; break;
				case 4: this.collegeId = 'education'; break;
				default: this.collegeId = 'engineering';
			}
			
			console.log('转换后的学院ID:', this.collegeId);
			this.loadCoursesByCollege(this.collegeId);
		} else {
			console.error('未接收到学院ID参数');
			uni.showToast({
				title: '加载失败，缺少学院信息',
				icon: 'none'
			});
		}
	},
	methods: {
		goBack() {
			// 修改返回逻辑，添加错误处理
			uni.navigateBack({
				delta: 1,
				success: function() {
					console.log('返回成功');
				},
				fail: function(err) {
					console.error('返回失败:', err);
					// 如果返回失败，尝试直接跳转到学院列表页
					uni.navigateTo({
						url: '/pages/course/index',
						fail: function(navErr) {
							console.error('跳转到学院列表失败:', navErr);
							// 最后尝试重新加载页面
							uni.reLaunch({
								url: '/pages/course/index'
							});
						}
					});
				}
			});
		},
		loadCoursesByCollege(collegeId) {
			// 根据学院ID加载不同的课程列表
			switch(collegeId) {
				case 'engineering':
					this.collegeTitle = '创新工程学院';
					this.courseList = [
						{
							name: '计算机视觉',
							code: 'CS460',
							rating: 4.8,
							reviewCount: 56,
							credits: 3
						},
						{
							name: '机器学习',
							code: 'CS462',
							rating: 4.9,
							reviewCount: 78,
							credits: 3
						},
						{
							name: '深度学习',
							code: 'CS463',
							rating: 4.7,
							reviewCount: 42,
							credits: 3
						}
					];
					break;
				case 'business':
					this.collegeTitle = '商学院';
					this.courseList = [
						{
							name: '市场营销',
							code: 'BUS201',
							rating: 4.5,
							reviewCount: 63,
							credits: 3
						},
						{
							name: '财务管理',
							code: 'BUS302',
							rating: 4.3,
							reviewCount: 45,
							credits: 3
						}
					];
					break;
				case 'arts':
					this.collegeTitle = '人文艺术学院';
					this.courseList = [
						{
							name: '中国文学',
							code: 'ART101',
							rating: 4.6,
							reviewCount: 38,
							credits: 3
						},
						{
							name: '西方哲学',
							code: 'ART202',
							rating: 4.4,
							reviewCount: 29,
							credits: 3
						}
					];
					break;
				case 'education':
					this.collegeTitle = '通识教育学院';
					this.courseList = [
						{
							name: '大学英语',
							code: 'GEN101',
							rating: 4.2,
							reviewCount: 85,
							credits: 3
						},
						{
							name: '批判性思维',
							code: 'GEN202',
							rating: 4.7,
							reviewCount: 57,
							credits: 3
						}
					];
					break;
				default:
					this.collegeTitle = '课程';
					this.courseList = [];
			}
		},
		goToCourseDetail(course) {
			uni.navigateTo({
				url: `/pages/course/course-detail?code=${course.code}&name=${encodeURIComponent(course.name)}`
			});
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
	padding-top: 120rpx;
}

.header {
	background-color: #3498db;
	padding: 20rpx;
	display: flex;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	z-index: 100;
}

.back-btn {
	color: #ffffff;
	font-size: 36rpx;
	padding: 0 20rpx;
}

.header-title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	flex: 1;
	text-align: center;
}

.course-list {
	padding: 20rpx;
}

.course-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.course-name {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.course-code {
	font-size: 28rpx;
	color: #666666;
	display: block;
	margin-bottom: 20rpx;
}

.course-rating {
	display: flex;
	align-items: center;
}

.rating-value {
	font-size: 40rpx;
	font-weight: bold;
	color: #f39c12;
	margin-right: 20rpx;
}

.rating-stars {
	display: flex;
	margin-right: 20rpx;
}

.star {
	color: #dddddd;
	font-size: 32rpx;
}

.star.active {
	color: #f39c12;
}

.review-count {
	font-size: 24rpx;
	color: #999999;
}
</style>