<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">通知</text>
			<view class="header-icons">
				<text class="icon">•••</text>
			</view>
		</view>
		
		<view class="notification-list">
			<view class="notification-item" v-for="(item, index) in notifications" :key="index">
				<view class="notification-icon" :class="item.type">{{item.icon}}</view>
				<view class="notification-content">
					<view class="notification-title">{{item.title}}</view>
					<view class="notification-desc">{{item.content}}</view>
					<view class="notification-time">{{item.time}}</view>
				</view>
			</view>
			
			<view class="empty-tip" v-if="notifications.length === 0">
				暂无通知
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			notifications: [
				{
					type: 'system',
					icon: '🔔',
					title: '系统通知',
					content: '欢迎使用澳科保姆，祝您使用愉快！',
					time: '2023-11-15 10:30'
				},
				{
					type: 'activity',
					icon: '🎉',
					title: '活动通知',
					content: '新用户注册送50积分，可兑换精美礼品',
					time: '2023-11-14 15:45'
				},
				{
					type: 'update',
					icon: '🚀',
					title: '更新通知',
					content: '澳科保姆V2.0版本已发布，新增房源对比功能',
					time: '2023-11-13 09:20'
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

.notification-list {
	padding: 20rpx;
}

.notification-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
	display: flex;
	align-items: flex-start;
}

.notification-icon {
	font-size: 40rpx;
	margin-right: 20rpx;
	padding: 10rpx;
	border-radius: 50%;
}

.system {
	background-color: #3498db;
	color: #ffffff;
}

.activity {
	background-color: #f39c12;
	color: #ffffff;
}

.update {
	background-color: #2ecc71;
	color: #ffffff;
}

.notification-content {
	flex: 1;
}

.notification-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
}

.notification-desc {
	font-size: 28rpx;
	color: #666666;
	margin-bottom: 10rpx;
	line-height: 1.5;
}

.notification-time {
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
