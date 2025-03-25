<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn">
				<text>←</text>
			</view>
			<text class="page-title">澳科食堂榜</text>
			<view class="header-icons">
				<text class="icon">•••</text>
				<text class="icon">⦿</text>
			</view>
		</view>
		
		<view class="search-box">
			<input type="text" placeholder="搜索食堂..." v-model="searchText" />
			<text class="search-icon">🔍</text>
		</view>
		
		<view class="header">
			<text class="title">澳科食堂</text>
			<text class="subtitle">浏览各食堂的真实评价</text>
		</view>
		
		<view class="canteen-list">
			<view class="canteen-item" v-for="(item, index) in filteredCanteens" :key="index" @click="navigateToShops(item.id)">
				<view class="canteen-icon-box" :style="{ backgroundColor: getRandomColor() }">
					<text>{{item.name.slice(0, 2)}}</text>
				</view>
				<view class="canteen-detail">
					<text class="canteen-name">{{item.name}}</text>
					<text class="canteen-count">{{item.location}} | {{item.businessHours}}</text>
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
			searchText: '',
			canteens: [
				{
					id: 1,
					name: '厨艺天地',
					image: '/static/canteen/culinary.jpg',
					rating: 4.5,
					location: 'A座1楼',
					businessHours: '07:00-22:00',
					tags: ['中餐', '西餐', '自助']
				},
				{
					id: 2,
					name: '麦当劳',
					image: '/static/canteen/mcd.jpg',
					rating: 4.2,
					location: 'B座1楼',
					businessHours: '24小时营业',
					tags: ['快餐', '汉堡', '炸鸡']
				},
				{
					id: 3,
					name: '点聚',
					image: '/static/canteen/dianju.jpg',
					rating: 4.3,
					location: 'C座1楼',
					businessHours: '10:00-22:00',
					tags: ['粤式', '早茶', '小吃']
				}
			]
		}
	},
	computed: {
		filteredCanteens() {
			if (!this.searchText) return this.canteens;
			const searchLower = this.searchText.toLowerCase();
			return this.canteens.filter(canteen => 
				canteen.name.toLowerCase().includes(searchLower) ||
				canteen.tags.some(tag => tag.toLowerCase().includes(searchLower))
			);
		}
	},
	methods: {
		navigateToShops(canteenId) {
			uni.navigateTo({
				url: `/pages/canteen/shop-list?canteenId=${canteenId}`
			});
		},
		getRandomColor() {
			const colors = ['#3498db', '#e74c3c', '#9b59b6', '#f39c12', '#2ecc71'];
			return colors[Math.floor(Math.random() * colors.length)];
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

.canteen-list {
	padding: 0 15rpx;
}

.canteen-item {
	display: flex;
	align-items: center;
	padding: 25rpx 20rpx;
	margin-bottom: 15rpx;
	background-color: #ffffff;
	border-radius: 8rpx;
	box-shadow: 0 1rpx 4rpx rgba(0, 0, 0, 0.05);
}

.canteen-icon-box {
	width: 80rpx;
	height: 80rpx;
	border-radius: 40rpx;
	display: flex;
	justify-content: center;
	align-items: center;
	margin-right: 20rpx;
}

.canteen-icon-box text {
	color: #ffffff;
	font-size: 32rpx;
	font-weight: bold;
}

.canteen-detail {
	flex: 1;
}

.canteen-name {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 5rpx;
}

.canteen-count {
	font-size: 24rpx;
	color: #666666;
}

.arrow {
	color: #999999;
	font-size: 32rpx;
	margin-left: 10rpx;
}
</style>