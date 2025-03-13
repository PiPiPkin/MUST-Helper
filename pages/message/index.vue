<template>
	<view class="container">
		<view class="header">
			<text class="title">消息</text>
		</view>
		
		<view class="content">
			<!-- 临时内容 -->
			<text>消息页面开发中...</text>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
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
	text-align: center;
}

.title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
}

.content {
	padding: 30rpx;
	text-align: center;
}
</style>