<template>
	<view class="container">
		<view class="top-header">
			<text class="page-title">消息中心</text>
			<view class="header-icons">
				<text class="icon">•••</text>
				<text class="icon">⦿</text>
			</view>
		</view>
		
		<view class="message-cards">
			<view class="message-card" @click="navigateTo('notification')">
				<view class="card-icon notification-icon">📢</view>
				<view class="card-content">
					<view class="card-title">通知</view>
					<view class="card-desc">系统通知和重要提醒</view>
				</view>
				<view class="card-badge" v-if="notificationCount > 0">{{notificationCount}}</view>
				<text class="card-arrow">→</text>
			</view>
			
			<view class="message-card" @click="navigateTo('comment')">
				<view class="card-icon comment-icon">💬</view>
				<view class="card-content">
					<view class="card-title">评论</view>
					<view class="card-desc">收到的评论和回复</view>
				</view>
				<view class="card-badge" v-if="commentCount > 0">{{commentCount}}</view>
				<text class="card-arrow">→</text>
			</view>
			
			<view class="message-card" @click="navigateTo('like')">
				<view class="card-icon like-icon">👍</view>
				<view class="card-content">
					<view class="card-title">赞</view>
					<view class="card-desc">收到的点赞和喜欢</view>
				</view>
				<view class="card-badge" v-if="likeCount > 0">{{likeCount}}</view>
				<text class="card-arrow">→</text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			notificationCount: 3,
			commentCount: 5,
			likeCount: 12
		}
	},
	methods: {
		navigateTo(type) {
			uni.navigateTo({
				url: `/pages/message/${type}`,
				success: function() {
					console.log(`跳转到${type}页面成功`);
				},
				fail: function(err) {
					console.error(`跳转到${type}页面失败`, err);
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
	padding-bottom: 30rpx;
}

.top-header {
	background-color: #3498db;
	padding: 20rpx 30rpx;
	display: flex;
	justify-content: space-between;
	align-items: center;
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

.message-cards {
	padding: 20rpx;
}

.message-card {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
	display: flex;
	align-items: center;
	position: relative;
}

.card-icon {
	font-size: 48rpx;
	margin-right: 20rpx;
}

.notification-icon {
	color: #3498db;
}

.comment-icon {
	color: #2ecc71;
}

.like-icon {
	color: #e74c3c;
}

.card-content {
	flex: 1;
}

.card-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 6rpx;
}

.card-desc {
	font-size: 24rpx;
	color: #999999;
}

.card-badge {
	background-color: #e74c3c;
	color: #ffffff;
	font-size: 24rpx;
	height: 40rpx;
	min-width: 40rpx;
	border-radius: 20rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	padding: 0 10rpx;
	margin-right: 20rpx;
}

.card-arrow {
	font-size: 36rpx;
	color: #999999;
}
</style>