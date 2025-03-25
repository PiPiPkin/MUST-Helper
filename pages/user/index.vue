<template>
	<view class="container">
		<view class="header">
			<text class="title">我的</text>
		</view>
		
		<view class="user-info-card">
			<template>
				<view class="avatar-container">
					<image class="avatar" :src="avatarUrl" mode="aspectFill"></image>
				</view>
			</template>
			<view class="user-details">
				<text class="username">{{userInfo.nickname}}</text>
				<text class="user-id">ID: {{userInfo.userId}}</text>
			</view>
			<view class="edit-btn" @click="editUserInfo">
				<text>编辑</text>
			</view>
		</view>
		
		<view class="menu-section">
			<view class="menu-title">
				<text>我的内容</text>
			</view>
			<view class="menu-list">
				<view class="menu-item" @click="navigateTo('/pages/user/my-reviews')">
					<view class="menu-icon">📝</view>
					<text class="menu-text">我的评价</text>
					<text class="menu-arrow">→</text>
				</view>
				<view class="menu-item" @click="navigateTo('/pages/user/my-favorites')">
					<view class="menu-icon">⭐</view>
					<text class="menu-text">我的收藏</text>
					<text class="menu-arrow">→</text>
				</view>
				<view class="menu-item" @click="navigateTo('/pages/user/my-history')">
					<view class="menu-icon">🕒</view>
					<text class="menu-text">浏览历史</text>
					<text class="menu-arrow">→</text>
				</view>
			</view>
		</view>
		
		<view class="menu-section">
			<view class="menu-title">
				<text>设置</text>
			</view>
			<view class="menu-list">
				<view class="menu-item" @click="navigateTo('/pages/user/agreement')">
					<view class="menu-icon">📄</view>
					<text class="menu-text">用户协议</text>
					<text class="menu-arrow">→</text>
				</view>
				<view class="menu-item" @click="navigateTo('/pages/user/privacy')">
					<view class="menu-icon">🔒</view>
					<text class="menu-text">隐私政策</text>
					<text class="menu-arrow">→</text>
				</view>
				<view class="menu-item" @click="navigateTo('/pages/user/about')">
					<view class="menu-icon">ℹ️</view>
					<text class="menu-text">关于我们</text>
					<text class="menu-arrow">→</text>
				</view>
			</view>
		</view>
		
		<view class="logout-btn" @click="logout">
			<text>退出登录</text>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			userInfo: {
				nickname: '',
				userId: '',
				avatar: '/static/avatar.png'
			},
			avatarUrl: getApp().globalData.userAvatar
		}
	},
	onLoad() {
		this.generateRandomUser();
		// 确保头像路径正确加载
		if (!this.avatarUrl) {
			this.avatarUrl = '/static/avatar.png'
		}
	},
	methods: {
		generateRandomUser() {
			// 澳科大相关元素
			const prefixes = ['澳科', '科大', '横琴', '氹仔', 'MUST', '澳大', '科技'];
			const suffixes = ['学子', '同学', '校友', '研究生', '博士', '教授', '学霸'];
			
			// 随机生成昵称
			const randomPrefix = prefixes[Math.floor(Math.random() * prefixes.length)];
			const randomSuffix = suffixes[Math.floor(Math.random() * suffixes.length)];
			const randomNum = Math.floor(Math.random() * 1000);
			
			this.userInfo.nickname = `${randomPrefix}${randomSuffix}${randomNum}`;
			this.userInfo.userId = `MUST${Math.floor(10000 + Math.random() * 90000)}`;
		},
		editUserInfo() {
			uni.navigateTo({
				url: '/pages/user/edit-profile'
			});
		},
		navigateTo(url) {
			if (url === '/pages/user/my-favorites' || url === '/pages/user/my-history') {
				uni.showToast({
					title: '正在快马加鞭开发中啦，请再等等哦',
					icon: 'none',
					duration: 2000
				});
				return;
			}
			uni.navigateTo({
				url: url
			});
		},
		logout() {
			uni.showModal({
				title: '提示',
				content: '确定要退出登录吗？',
				success: (res) => {
					if (res.confirm) {
						// 这里可以添加退出登录的逻辑
						uni.showToast({
							title: '已退出登录',
							icon: 'success'
						});
					}
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
	padding-bottom: 40rpx;
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

.user-info-card {
	margin: 20rpx;
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 30rpx;
	display: flex;
	align-items: center;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.avatar-container {
	width: 120rpx;
	height: 120rpx;
	border-radius: 60rpx;
	overflow: hidden;
	background-color: #f0f0f0;
	margin-right: 30rpx;
}

.avatar {
	width: 100%;
	height: 100%;
}

.user-details {
	flex: 1;
}

.username {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
	display: block;
}

.user-id {
	font-size: 24rpx;
	color: #999999;
}

.edit-btn {
	background-color: #f0f0f0;
	padding: 10rpx 30rpx;
	border-radius: 30rpx;
	font-size: 24rpx;
	color: #666666;
}

.menu-section {
	margin: 20rpx;
	background-color: #ffffff;
	border-radius: 12rpx;
	overflow: hidden;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.menu-title {
	padding: 20rpx 30rpx;
	font-size: 28rpx;
	color: #999999;
	border-bottom: 1rpx solid #f0f0f0;
}

.menu-list {
	padding: 0 20rpx;
}

.menu-item {
	display: flex;
	align-items: center;
	padding: 30rpx 10rpx;
	border-bottom: 1rpx solid #f0f0f0;
}

.menu-item:last-child {
	border-bottom: none;
}

.menu-icon {
	font-size: 36rpx;
	margin-right: 20rpx;
}

.menu-text {
	flex: 1;
	font-size: 30rpx;
	color: #333333;
}

.menu-arrow {
	font-size: 30rpx;
	color: #cccccc;
}

.logout-btn {
	margin: 40rpx 20rpx;
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 30rpx;
	text-align: center;
	font-size: 32rpx;
	color: #e74c3c;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}
</style>