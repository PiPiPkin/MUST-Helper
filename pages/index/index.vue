<template>
	<view class="container">
		<view class="header">
			<text class="title">澳科保姆</text>
		</view>
		
		<view class="content">
			<view class="nav-card" @click="navigateTo('course')">
				<text class="card-title">选课榜</text>
				<text class="card-desc">课程评价与选课推荐</text>
			</view>
			
			<view class="nav-card" @click="navigateTo('canteen')">
				<text class="card-title">美食榜</text>
				<text class="card-desc">校园美食与餐厅点评</text>
			</view>
			
			<view class="nav-card" @click="navigateTo('housing')">
				<text class="card-title">租房榜</text>
				<text class="card-desc">周边房源与租房攻略</text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			
		}
	},
	onLoad() {
		// 页面加载时自动跳转到选课榜页面
		setTimeout(() => {
			uni.switchTab({
				url: '/pages/course/index'
			});
		}, 100);
	},
	methods: {
		navigateTo(page) {
			uni.switchTab({
				url: `/pages/${page}/index`
			});
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
	padding: 30rpx;
}

.header {
	padding: 40rpx 0;
	text-align: center;
}

.title {
	font-size: 48rpx;
	font-weight: bold;
	color: #3498db;
}

.content {
	margin-top: 60rpx;
}

.nav-card {
	background-color: #ffffff;
	padding: 30rpx;
	border-radius: 12rpx;
	margin-bottom: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.card-title {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.card-desc {
	font-size: 28rpx;
	color: #666666;
}
</style>
