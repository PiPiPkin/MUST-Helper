<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">隐私政策</text>
		</view>
		
		<view class="privacy-content">
			<view class="privacy-title">澳科保姆隐私政策</view>
			<view class="privacy-date">更新日期：2023年11月15日</view>
			
			<view class="privacy-intro">
				<text>本隐私政策介绍了澳科保姆如何收集、使用、存储和共享您的个人信息，以及您享有的相关权利。请您仔细阅读并了解本政策的全部内容。</text>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">1. 我们收集的信息</view>
				<view class="section-content">
					<text>1.1 您提供的信息：当您注册账号、使用我们的服务或联系我们时，您可能会提供某些个人信息，如昵称、头像等。</text>
					<text>1.2 设备信息：我们可能会收集您使用我们服务的设备信息，如设备型号、操作系统版本、设备设置、应用程序版本等。</text>
					<text>1.3 日志信息：当您使用我们的服务时，我们的服务器会自动记录某些日志信息，如访问时间、使用的功能等。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">2. 我们如何使用您的信息</view>
				<view class="section-content">
					<text>2.1 提供服务：我们使用您的信息来提供、维护和改进我们的服务。</text>
					<text>2.2 安全保障：我们使用您的信息来验证身份、防止欺诈和确保服务安全。</text>
					<text>2.3 通信联络：我们可能使用您的信息与您联系，提供与服务相关的通知和更新。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">3. 信息的共享与披露</view>
				<view class="section-content">
					<text>3.1 我们不会向第三方出售您的个人信息。</text>
					<text>3.2 在以下情况下，我们可能会共享您的个人信息：</text>
					<text>- 获得您的明确同意；</text>
					<text>- 遵守法律法规的要求；</text>
					<text>- 保护我们的合法权益。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">4. 信息的保护</view>
				<view class="section-content">
					<text>4.1 我们采取各种安全措施来保护您的个人信息不被未经授权的访问、使用或泄露。</text>
					<text>4.2 尽管我们采取了这些措施，但请理解互联网并非绝对安全的环境，我们无法保证您的个人信息绝对安全。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">5. 您的权利</view>
				<view class="section-content">
					<text>5.1 您有权访问、更正或删除您的个人信息。</text>
					<text>5.2 您有权撤回您的同意，但这不会影响我们此前基于您的同意而进行的处理。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">6. 政策更新</view>
				<view class="section-content">
					<text>6.1 我们可能会不时更新本隐私政策，更新后的政策将在应用内公布。</text>
					<text>6.2 继续使用我们的服务，即表示您同意受更新后的隐私政策的约束。</text>
				</view>
			</view>
			
			<view class="privacy-section">
				<view class="section-title">7. 联系我们</view>
				<view class="section-content">
					<text>如果您对本隐私政策有任何疑问，请通过以下方式联系我们：</text>
					<text>邮箱：privacy@mustapp.com</text>
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

.privacy-content {
	padding: 30rpx;
}

.privacy-title {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	text-align: center;
	margin-bottom: 10rpx;
}

.privacy-date {
	font-size: 24rpx;
	color: #999999;
	text-align: center;
	margin-bottom: 30rpx;
}

.privacy-intro {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.8;
	margin-bottom: 30rpx;
}

.privacy-section {
	margin-bottom: 30rpx;
}

.section-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 20rpx;
}

.section-content {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.8;
}

.section-content text {
	display: block;
	margin-bottom: 15rpx;
}
</style>