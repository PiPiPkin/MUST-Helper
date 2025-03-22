<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">评论</text>
			<view class="header-icons">
				<text class="icon">•••</text>
			</view>
		</view>
		
		<view class="comment-list">
			<view class="comment-item" v-for="(item, index) in comments" :key="index">
				<view class="comment-avatar">{{item.avatar}}</view>
				<view class="comment-content">
					<view class="comment-user">{{item.username}}</view>
					<view class="comment-text">{{item.content}}</view>
					<view class="comment-source">来自 {{item.source}}</view>
					<view class="comment-time">{{item.time}}</view>
				</view>
			</view>
			
			<view class="empty-tip" v-if="comments.length === 0">
				暂无评论
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			comments: [
				{
					avatar: '👨',
					username: '租房达人',
					content: '这个房源真不错，价格合理，环境也好',
					source: '皇朝广场房源',
					time: '2023-11-15 14:30'
				},
				{
					avatar: '👩',
					username: '小澳同学',
					content: '请问这个宿舍有独立卫浴吗？',
					source: 'M座宿舍',
					time: '2023-11-14 09:45'
				},
				{
					avatar: '👦',
					username: '横琴租客',
					content: '感谢分享，这个信息对我很有帮助',
					source: '横琴租房攻略',
					time: '2023-11-13 16:20'
				}
			]
		}
	},
	methods: {
		goBack() {
			uni.navigateBack({
				fail: function() {
					uni.switchTab({
						url: '/pages/index/index'
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
	padding-bottom: 30rpx;
}

.top-header {
	background-color: #3498db;
	padding: 20rpx 30rpx;
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.back-btn {
	color: #ffffff;
	font-size: 36rpx;
}

.page-title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	flex: 1;
	text-align: center;
}

.header-icons {
	display: flex;
	gap: 20rpx;
}

.icon {
	color: #ffffff;
	font-size: 32rpx;
}

.comment-list {
	padding: 20rpx;
}

.comment-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
	display: flex;
	align-items: flex-start;
}

.comment-avatar {
	font-size: 40rpx;
	margin-right: 20rpx;
	background-color: #f0f0f0;
	width: 80rpx;
	height: 80rpx;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.comment-content {
	flex: 1;
}

.comment-user {
	font-size: 30rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
}

.comment-text {
	font-size: 28rpx;
	color: #666666;
	margin-bottom: 10rpx;
	line-height: 1.5;
}

.comment-source {
	font-size: 24rpx;
	color: #3498db;
	margin-bottom: 6rpx;
}

.comment-time {
	font-size: 24rpx;
	color: #999999;
}

.empty-tip {
	text-align: center;
	padding: 40rpx;
	color: #999999;
	font-size: 28rpx;
}
</style>