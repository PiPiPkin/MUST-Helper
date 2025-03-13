<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header">
			<text class="header-title">食堂榜</text>
		</view>
		
		<!-- 食堂列表 -->
		<view class="content">
			<view class="search-box">
				<input type="text" placeholder="搜索食堂..." v-model="searchText" />
				<text class="search-icon">🔍</text>
			</view>
			
			<view class="canteen-list">
				<view class="canteen-item" v-for="(item, index) in filteredCanteens" :key="index" 
					  @click="navigateToShops(item.id)">
					<image class="canteen-image" :src="item.image" mode="aspectFill"></image>
					<view class="canteen-info">
						<view class="canteen-header">
							<text class="canteen-name">{{item.name}}</text>
							<view class="rating">
								<text class="rating-score">{{item.rating.toFixed(1)}}</text>
								<view class="stars">
									<text v-for="n in 5" :key="n" class="star" 
										  :class="{ 'filled': n <= Math.round(item.rating) }">★</text>
								</view>
							</view>
						</view>
						<view class="canteen-meta">
							<text class="location">{{item.location}}</text>
							<text class="business-hours">{{item.businessHours}}</text>
						</view>
						<view class="tags">
							<text class="tag" v-for="(tag, tagIndex) in item.tags" :key="tagIndex">{{tag}}</text>
						</view>
					</view>
				</view>
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
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
}

.header {
	background-color: #3498db;
	padding: 20rpx;
	text-align: center;
}

.header-title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
}

.content {
	padding: 20rpx;
}

.search-box {
	position: relative;
	margin-bottom: 20rpx;
}

.search-box input {
	width: 100%;
	height: 80rpx;
	background-color: #ffffff;
	border-radius: 40rpx;
	padding: 0 80rpx 0 30rpx;
	font-size: 28rpx;
}

.search-icon {
	position: absolute;
	right: 30rpx;
	top: 50%;
	transform: translateY(-50%);
	font-size: 32rpx;
}

.canteen-list {
	display: flex;
	flex-direction: column;
	gap: 20rpx;
}

.canteen-item {
	background-color: #ffffff;
	border-radius: 16rpx;
	overflow: hidden;
	box-shadow: 0 2rpx 10rpx rgba(0, 0, 0, 0.05);
}

.canteen-image {
	width: 100%;
	height: 300rpx;
}

.canteen-info {
	padding: 20rpx;
}

.canteen-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 10rpx;
}

.canteen-name {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
}

.rating {
	display: flex;
	align-items: center;
	gap: 10rpx;
}

.rating-score {
	font-size: 32rpx;
	color: #f39c12;
	font-weight: bold;
}

.stars {
	display: flex;
}

.star {
	color: #dddddd;
	font-size: 24rpx;
}

.star.filled {
	color: #f39c12;
}

.canteen-meta {
	display: flex;
	gap: 20rpx;
	margin-bottom: 10rpx;
}

.location, .business-hours {
	font-size: 24rpx;
	color: #666666;
}

.tags {
	display: flex;
	flex-wrap: wrap;
	gap: 10rpx;
}

.tag {
	font-size: 24rpx;
	color: #3498db;
	background-color: #eef7fd;
	padding: 4rpx 12rpx;
	border-radius: 6rpx;
}
</style>