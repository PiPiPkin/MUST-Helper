<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<text class="header-title">校园点评助手</text>
		</view>
		
		<!-- 简单提示信息 -->
		<view class="welcome-message">
			<text>欢迎使用澳科保姆</text>
			<text class="sub-message">校园生活好帮手</text>
		</view>
		
		<!-- 功能导航 -->
		<view class="nav-grid">
			<view class="nav-item" v-for="(item, index) in navItems" :key="index" @click="navigateTo(item.url)">
				<view class="nav-icon" :style="{ backgroundColor: item.color }">
					<text class="icon-text">{{item.name.substr(0,1)}}</text>
				</view>
				<text>{{item.name}}</text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			statusBarHeight: 20, // 默认值
			navItems: [
				{
					name: '选课榜',
					color: '#3498db',
					url: '/pages/course/index'
				},
				{
					name: '美食榜',
					color: '#e74c3c',
					url: '/pages/canteen/index'
				},
				{
					name: '租房榜',
					color: '#2ecc71',
					url: '/pages/housing/index'
				}
			]
		}
	},
	onLoad() {
		// 安全地获取状态栏高度
		try {
			const systemInfo = uni.getSystemInfoSync();
			if (systemInfo && systemInfo.statusBarHeight) {
				this.statusBarHeight = systemInfo.statusBarHeight;
			}
			console.log('状态栏高度:', this.statusBarHeight);
		} catch (error) {
			console.error('获取系统信息失败:', error);
		}
	},
	methods: {
		navigateTo(url) {
			console.log('导航到:', url);
			uni.switchTab({
				url: url,
				success: function() {
					console.log('导航成功');
				},
				fail: function(err) {
					console.error('导航失败:', err);
					uni.showToast({
						title: '页面跳转失败',
						icon: 'none'
					});
				}
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

.welcome-message {
	margin: 50rpx 30rpx;
	text-align: center;
	background-color: #ffffff;
	padding: 40rpx;
	border-radius: 20rpx;
	box-shadow: 0 4rpx 12rpx rgba(0,0,0,0.1);
}

.welcome-message text {
	font-size: 40rpx;
	font-weight: bold;
	color: #333333;
	display: block;
}

.sub-message {
	font-size: 28rpx !important;
	color: #666666 !important;
	font-weight: normal !important;
	margin-top: 20rpx;
}

.nav-grid {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	gap: 20rpx;
	padding: 30rpx;
	background-color: #ffffff;
	margin: 30rpx;
	border-radius: 20rpx;
	box-shadow: 0 4rpx 12rpx rgba(0,0,0,0.1);
}

.nav-item {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 10rpx;
	padding: 20rpx 0;
}

.nav-icon {
	width: 100rpx;
	height: 100rpx;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.icon-text {
	color: #ffffff;
	font-size: 40rpx;
	font-weight: bold;
}

.nav-item text {
	font-size: 28rpx;
	color: #333333;
	margin-top: 10rpx;
}
</style>
