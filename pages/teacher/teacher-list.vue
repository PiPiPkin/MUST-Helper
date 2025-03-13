<template>
	<view class="container">
		<view class="header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">教师列表</text>
		</view>
		
		<view class="content">
			<text>教师列表页面</text>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			
		}
	},
	methods: {
		goBack() {
			uni.navigateBack({
				fail: function() {
					uni.switchTab({
						url: '/pages/course/index'
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
}

.header {
	background-color: #3498db;
	padding: 20rpx;
	display: flex;
	align-items: center;
}

.back-btn {
	color: #ffffff;
	font-size: 36rpx;
	padding: 0 20rpx;
}

.header-title {
	flex: 1;
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	text-align: center;
}

.content {
	padding: 30rpx;
	text-align: center;
	margin-top: 100rpx;
}
</style>