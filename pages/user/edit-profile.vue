<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">编辑个人资料</text>
			<view class="save-btn" @click="saveProfile">
				<text>保存</text>
			</view>
		</view>
		
		<view class="edit-form">
			<view class="avatar-section">
				<view class="avatar-container">
					<image class="avatar" :src="userInfo.avatar" mode="aspectFill"></image>
				</view>
				<view class="avatar-hint">
					<text>头像暂不支持修改</text>
				</view>
			</view>
			
			<view class="form-item">
				<text class="form-label">昵称</text>
				<input type="text" class="form-input" v-model="userInfo.nickname" placeholder="请输入昵称" />
			</view>
			
			<view class="form-item">
				<text class="form-label">个性签名</text>
				<textarea class="form-textarea" v-model="userInfo.bio" placeholder="请输入个性签名" />
			</view>
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
				avatar: '/static/avatar.png',
				bio: ''
			}
		}
	},
	onLoad() {
		// 这里应该从全局状态或缓存中获取用户信息
		// 这里使用模拟数据
		const cachedUserInfo = {
			nickname: '澳科学子123',
			userId: 'MUST12345',
			avatar: '/static/avatar.png',
			bio: '澳科大学生，热爱生活'
		};
		
		this.userInfo = {...cachedUserInfo};
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		saveProfile() {
			// 这里应该将用户信息保存到全局状态或缓存中
			uni.showToast({
				title: '保存成功',
				icon: 'success'
			});
			
			setTimeout(() => {
				this.goBack();
			}, 1500);
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
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

.save-btn {
	color: #ffffff;
	font-size: 30rpx;
}

.edit-form {
	padding: 30rpx;
}

.avatar-section {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin-bottom: 40rpx;
}

.avatar-container {
	width: 160rpx;
	height: 160rpx;
	border-radius: 80rpx;
	overflow: hidden;
	background-color: #f0f0f0;
	margin-bottom: 20rpx;
}

.avatar {
	width: 100%;
	height: 100%;
}

.avatar-hint {
	font-size: 24rpx;
	color: #999999;
}

.form-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 20rpx;
	margin-bottom: 20rpx;
}

.form-label {
	font-size: 28rpx;
	color: #666666;
	margin-bottom: 10rpx;
	display: block;
}

.form-input {
	width: 100%;
	height: 80rpx;
	font-size: 30rpx;
	color: #333333;
}

.form-textarea {
	width: 100%;
	height: 200rpx;
	font-size: 30rpx;
	color: #333333;
}
</style>