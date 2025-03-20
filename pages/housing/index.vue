<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn">
				<text>←</text>
			</view>
			<text class="page-title">澳科大学生租房</text>
			<view class="header-icons">
				<text class="icon">•••</text>
				<text class="icon">⦿</text>
			</view>
		</view>
		
		<view class="search-box">
			<input type="text" placeholder="搜索房源..." />
			<text class="search-icon">🔍</text>
		</view>
		
		<view class="header">
			<text class="title">澳科大租房</text>
			<text class="subtitle">浏览各区域学生对房源的真实评价</text>
		</view>
		
		<view class="area-list">
			<view class="area-item" @click="navigateToArea('macau')">
				<view class="area-icon-box macau">
					<text>澳门</text>
				</view>
				<view class="area-detail">
					<text class="area-name">澳门</text>
					<text class="area-count">12门房源 | 328条评价</text>
				</view>
				<text class="arrow">></text>
			</view>
			
			<view class="area-item" @click="navigateToArea('hengqin')">
				<view class="area-icon-box hengqin">
					<text>横琴</text>
				</view>
				<view class="area-detail">
					<text class="area-name">横琴</text>
					<text class="area-count">18门房源 | 256条评价</text>
				</view>
				<text class="arrow">></text>
			</view>
			
			<view class="area-item" @click="navigateToArea('campus')">
				<view class="area-icon-box campus">
					<text>校内</text>
				</view>
				<view class="area-detail">
					<text class="area-name">校内宿舍</text>
					<text class="area-count">8门房源 | 187条评价</text>
				</view>
				<text class="arrow">></text>
			</view>
			
			<view class="area-item" @click="navigateToArea('zhuhai')">
				<view class="area-icon-box zhuhai">
					<text>珠海</text>
				</view>
				<view class="area-detail">
					<text class="area-name">珠海</text>
					<text class="area-count">15门房源 | 142条评价</text>
				</view>
				<text class="arrow">></text>
			</view>
			
			<view class="area-item" @click="navigateToArea('campus-dorm')">
				<view class="area-icon-box dorm">
					<text>校区</text>
				</view>
				<view class="area-detail">
					<text class="area-name">校区宿舍</text>
					<text class="area-count">5门房源 | 98条评价</text>
				</view>
				<text class="arrow">></text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
    data() {
        return {
            areas: [
                { id: 'macau', name: '澳门', count: 12, reviews: 328, color: '#3498db' },
                { id: 'hengqin', name: '横琴', count: 18, reviews: 256, color: '#e74c3c' },
                { id: 'campus', name: '校内宿舍', count: 8, reviews: 187, color: '#9b59b6' },
                { id: 'zhuhai', name: '珠海', count: 15, reviews: 142, color: '#f39c12' },
                { id: 'campus-dorm', name: '校区宿舍', count: 5, reviews: 98, color: '#2ecc71' }
            ]
        }
    },
    methods: {
        navigateToArea(areaId) {
            uni.navigateTo({
                url: `/pages/housing/area-detail?id=${areaId}`
            });
        }
    }
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
	padding-bottom: 0;
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
	padding: 0 20rpx;
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

.search-box {
	position: relative;
	padding: 15rpx 20rpx;
	background-color: #3498db;
}

.search-box input {
	width: 100%;
	height: 70rpx;
	background-color: #ffffff;
	border-radius: 35rpx;
	padding: 0 80rpx 0 30rpx;
	font-size: 28rpx;
}

.search-icon {
	position: absolute;
	right: 40rpx;
	top: 30rpx;
	font-size: 32rpx;
	color: #3498db;
}

.header {
	padding: 20rpx;
	background-color: #f5f5f5;
}

.title {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 5rpx;
}

.subtitle {
	font-size: 26rpx;
	color: #666666;
}

.area-list {
	padding: 0 15rpx;
}

.area-item {
	display: flex;
	align-items: center;
	padding: 25rpx 20rpx;
	margin-bottom: 15rpx;
	background-color: #ffffff;
	border-radius: 8rpx;
	box-shadow: 0 1rpx 4rpx rgba(0, 0, 0, 0.05);
}

.area-icon-box {
	width: 90rpx;
	height: 90rpx;
	border-radius: 50%;
	display: flex;
	align-items: center;
	justify-content: center;
	margin-right: 20rpx;
	color: #ffffff;
	font-size: 28rpx;
}

.macau {
	background-color: #3498db;
}

.hengqin {
	background-color: #e74c3c;
}

.campus {
	background-color: #9b59b6;
}

.zhuhai {
	background-color: #f39c12;
}

.dorm {
	background-color: #2ecc71;
}

.area-detail {
	flex: 1;
}

.area-name {
	font-size: 34rpx;
	color: #333333;
	font-weight: bold;
	display: block;
	margin-bottom: 5rpx;
}

.area-count {
	font-size: 26rpx;
	color: #999999;
}

.arrow {
	font-size: 36rpx;
	color: #cccccc;
	margin-left: 10rpx;
}
</style>