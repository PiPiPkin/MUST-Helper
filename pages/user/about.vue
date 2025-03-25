<template>
	<view class="container">
		<view class="top-header">
			<text class="back-btn" @click="goBack">←</text>
			<text class="page-title">关于我们</text>
		</view>
		
		<view class="about-content">
			<view class="logo-section">
				<text class="app-name">MUST-Helper 科大保姆</text>
				<text class="app-subtitle">由科大学生，为科大学生</text>
			</view>
			
			<view class="card mission">
				<view class="card-title">我们的目标</view>
				<view class="card-content">
					<text class="highlight-text">「让每一次校园选择，都有真实经验可循」</text>
					<text class="description-text">我们致力于为澳门科技大学学生打造一个专属的校园生活决策平台，通过汇聚校友的真实评分与经验，解决课程选择、食堂探索、租房避坑中的信息不对称问题。从课堂到餐桌，从宿舍到社区，我们愿做你校园生活的"贴心指南针"。</text>
				</view>
			</view>
			
			<view class="card contact">
				<view class="card-title">联系我们</view>
				<view class="card-content">
					<text class="sub-title">遇到问题或建议？我们随时倾听！</text>
					<view class="contact-item" @click="sendEmail">
						<text class="item-label">• 反馈邮箱：</text>
						<text class="item-value">pi7631140@gmail.com</text>
					</view>
					<text class="service-promise">• 服务承诺：所有问题将在 48小时内 回复，重大功能需求优先纳入迭代计划。</text>
				</view>
			</view>
			
			<view class="card join-us">
				<view class="card-title">加入我们</view>
				<view class="card-content">
					<text>如果你也热爱用技术优化校园生活，欢迎提交你的创意或加入开发团队（邮件标题请注明【加入科大保姆】）。</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {}
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		sendEmail() {
			// 在支持的平台上打开邮件客户端
			uni.setClipboardData({
				data: 'pi7631140@gmail.com',
				success: () => {
					uni.showToast({
						title: '邮箱已复制到剪贴板',
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

.about-content {
	padding: 30rpx;
}

.logo-section {
	text-align: center;
	margin-bottom: 40rpx;
}

.app-name {
	font-size: 40rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.app-subtitle {
	font-size: 28rpx;
	color: #666666;
	display: block;
}

.card {
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 30rpx;
	margin-bottom: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.card-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #3498db;
	margin-bottom: 20rpx;
}

.card-content {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.6;
}

.highlight-text {
	display: block;
	font-size: 32rpx;
	color: #333333;
	font-weight: bold;
	margin-bottom: 20rpx;
}

.description-text {
	display: block;
	margin-top: 10rpx;
}

.sub-title {
	display: block;
	margin-bottom: 20rpx;
	color: #333333;
}

.contact-item {
	display: flex;
	align-items: center;
	margin-bottom: 10rpx;
}

.item-label {
	color: #333333;
}

.item-value {
	color: #3498db;
}

.service-promise {
	display: block;
	margin-top: 10rpx;
}
</style>