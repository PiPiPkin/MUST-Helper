<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">赞</text>
			<view class="header-icons">
				<text class="icon">•••</text>
			</view>
		</view>
		
		<view class="like-list">
			<view class="like-item" v-for="(item, index) in likes" :key="index">
				<view class="like-avatar">{{item.avatar}}</view>
				<view class="like-content">
					<view class="like-user">{{item.username}}</view>
					<view class="like-action">
						<text class="like-icon">👍</text>
						<text>赞了你的{{item.type}}</text>
					</view>
					<view class="like-source">{{item.source}}</view>
					<view class="like-time">{{item.time}}</view>
				</view>
			</view>
			
			<view class="empty-tip" v-if="likes.length === 0">
				暂无点赞
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			likes: [
				{
					avatar: '👨',
					username: '租房达人',
					type: '评论',
					source: '"这个小区环境真不错，值得推荐"',
					time: '2023-11-15 16:30'
				},
				{
					avatar: '👩',
					username: '小澳同学',
					type: '分享',
					source: '"横琴租房攻略"',
					time: '2023-11-14 11:45'
				},
				{
					avatar: '👦',
					username: '横琴租客',
					type: '评价',
					source: '"华发首府"房源',
					time: '2023-11-13 18:20'
				},
				{
					avatar: '👧',
					username: '澳科新生',
					type: '问答',
					source: '"M座宿舍有独立卫浴吗？"',
					time: '2023-11-12 09:15'
				}
			]
		}
	},
	methods: {
		goBack() {
			uni.navigateBack();
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

.like-list {
	padding: 20rpx;
}

.like-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
	display: flex;
	align-items: flex-start;
}

.like-avatar {
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

.like-content {
	flex: 1;
}

.like-user {
	font-size: 30rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
}

.like-action {
	font-size: 28rpx;
	color: #666666;
	margin-bottom: 10rpx;
	display: flex;
	align-items: center;
}

.like-icon {
	color: #e74c3c;
	margin-right: 10rpx;
	font-size: 32rpx;
}

.like-source {
	font-size: 26rpx;
	color: #3498db;
	margin-bottom: 6rpx;
	padding: 6rpx 0;
}

.like-time {
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