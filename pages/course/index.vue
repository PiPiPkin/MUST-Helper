<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<text class="header-title">选课榜学院列表</text>
		</view>
		
		<!-- 搜索框 -->
		<view class="search-box">
			<input type="text" placeholder="搜索课程或教授..." />
			<text class="search-icon">🔍</text>
		</view>
		
		<!-- 学院介绍 -->
		<view class="college-intro">
			<text class="intro-title">澳科大学院</text>
			<text class="intro-desc">浏览学院并查看学生对课程的评价</text>
		</view>
		
		<!-- 学院列表 -->
		<view class="college-list">
			<view class="college-item" @click="goToCourseList('engineering')">
				<view class="college-icon engineering">
					<text>工程</text>
				</view>
				<view class="college-info">
					<text class="college-name">创新工程学院</text>
					<text class="college-count">45门课程 | 328条评价</text>
				</view>
				<text class="college-arrow">></text>
			</view>
			
			<view class="college-item" @click="goToCourseList('business')">
				<view class="college-icon business">
					<text>商学</text>
				</view>
				<view class="college-info">
					<text class="college-name">商学院</text>
					<text class="college-count">38门课程 | 256条评价</text>
				</view>
				<text class="college-arrow">></text>
			</view>
			
			<view class="college-item" @click="goToCourseList('arts')">
				<view class="college-icon arts">
					<text>人文</text>
				</view>
				<view class="college-info">
					<text class="college-name">人文艺术学院</text>
					<text class="college-count">42门课程 | 187条评价</text>
				</view>
				<text class="college-arrow">></text>
			</view>
			
			<view class="college-item" @click="goToCourseList('education')">
				<view class="college-icon education">
					<text>通识</text>
				</view>
				<view class="college-info">
					<text class="college-name">通识教育学院</text>
					<text class="college-count">25门课程 | 142条评价</text>
				</view>
				<text class="college-arrow">></text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			statusBarHeight: 20
		}
	},
	onLoad() {
		// 获取状态栏高度
		try {
			const systemInfo = uni.getSystemInfoSync();
			if (systemInfo && systemInfo.statusBarHeight) {
				this.statusBarHeight = systemInfo.statusBarHeight;
			}
		} catch (error) {
			console.error('获取系统信息失败:', error);
		}
	},
	methods: {
		goToCourseList(collegeId) {
			uni.navigateTo({
				url: `/pages/course/course-list?collegeId=${collegeId}`
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
	text-align: center;
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	z-index: 100;
}

.header-title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
}

.search-box {
	margin: 20rpx 30rpx;
	position: relative;
}

.search-box input {
	background-color: #ffffff;
	height: 80rpx;
	border-radius: 40rpx;
	padding: 0 80rpx 0 30rpx;
	font-size: 28rpx;
}

.search-icon {
	position: absolute;
	right: 30rpx;
	top: 50%;
	transform: translateY(-50%);
	font-size: 32rpx;
}

.college-intro {
	padding: 30rpx;
}

.intro-title {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.intro-desc {
	font-size: 28rpx;
	color: #666666;
}

.college-list {
	padding: 0 30rpx;
}

.college-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 30rpx;
	display: flex;
	align-items: center;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.college-icon {
	width: 80rpx;
	height: 80rpx;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
	color: #ffffff;
	font-size: 24rpx;
	margin-right: 20rpx;
}

.engineering {
	background-color: #3498db;
}

.business {
	background-color: #e74c3c;
}

.arts {
	background-color: #9b59b6;
}

.education {
	background-color: #f39c12;
}

.college-info {
	flex: 1;
}

.college-name {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.college-count {
	font-size: 24rpx;
	color: #999999;
}

.college-arrow {
	color: #cccccc;
	font-size: 36rpx;
}
</style>