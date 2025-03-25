<template>
	<view class="container">
		<view class="header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{areaInfo.name}}房源列表</text>
		</view>
		
		<view class="search-box">
			<input type="text" placeholder="搜索房源..." v-model="searchText" />
			<text class="search-icon">🔍</text>
		</view>
		
		<view class="area-info-card" v-if="!loading">
			<view class="area-info-title">{{areaInfo.name}}概况</view>
			<view class="area-info-stats">
				<view class="area-stat">
					<text class="stat-value">{{areaInfo.count}}</text>
					<text class="stat-label">房源数量</text>
				</view>
				<view class="area-stat">
					<text class="stat-value">{{areaInfo.reviews}}</text>
					<text class="stat-label">评价数量</text>
				</view>
				<view class="area-stat">
					<text class="stat-value">{{getAverageRating()}}</text>
					<text class="stat-label">平均评分</text>
				</view>
			</view>
			<view class="area-info-desc" v-if="areaInfo.description">
				{{areaInfo.description}}
			</view>
		</view>
		
		<view class="filter-bar" v-if="!loading && houses.length > 0">
			<view class="filter-item" :class="{ active: activeFilter === 'default' }" @click="setFilter('default')">
				默认排序
			</view>
			<view class="filter-item" :class="{ active: activeFilter === 'rating' }" @click="setFilter('rating')">
				评分最高
			</view>
			<view class="filter-item" :class="{ active: activeFilter === 'reviews' }" @click="setFilter('reviews')">
				评价最多
			</view>
		</view>
		
		<view class="housing-list">
			<template v-if="loading">
				<view class="loading">加载中...</view>
			</template>
			<template v-else-if="filteredHouses.length === 0">
				<view class="empty">暂无房源数据</view>
			</template>
			<template v-else>
				<view class="housing-card" v-for="(item, index) in filteredHouses" :key="index" @click="goToHouseDetail(item.id)" hover-class="card-hover">
					<view class="housing-card-header">
						<text class="housing-name">{{item.name}}</text>
						<text class="housing-tag">{{item.type}}</text>
					</view>
					<view class="housing-card-body">
						<view class="housing-info">
							<text class="info-area">{{item.area}}㎡</text>
							<text class="info-divider">|</text>
							<text class="info-text">{{item.info || '暂无详细信息'}}</text>
						</view>
						<view class="housing-rating">
							<view class="rating-stars">
								<text v-for="n in 5" :key="n" :class="['star', n <= Math.round(item.rating) ? 'active' : '']">★</text>
							</view>
							<text class="rating-value">{{item.rating.toFixed(1)}}</text>
							<text class="review-count">({{item.reviewCount || 0}}条评价)</text>
						</view>
					</view>
					<view class="housing-card-footer">
						<text class="price-text">¥{{item.price || '暂无'}} / 月</text>
						<view class="action-btn">查看详情</view>
					</view>
				</view>
			</template>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			statusBarHeight: 20,
			areaId: '',
			loading: true,
			areaInfo: {},
			houses: [],
			filteredHouses: [],
			activeFilter: 'default',
			searchText: ''
		}
	},
	watch: {
		searchText() {
			this.filterHouses();
		}
	},
	onLoad(options) {
		// 获取状态栏高度
		try {
			uni.getSystemInfo({
				success: (res) => {
					this.statusBarHeight = res.statusBarHeight;
				},
				fail: () => {
					this.statusBarHeight = 20;
				}
			});
		} catch (error) {
			this.statusBarHeight = 20;
		}

		if (options.id) {
			this.areaId = options.id;
			this.loadAreaData();
		} else {
			uni.showToast({
				title: '参数错误',
				icon: 'none'
			});
			setTimeout(() => {
				this.goBack();
			}, 1500);
		}
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		getAverageRating() {
			if (!this.areaInfo || !this.areaInfo.rating) return '暂无';
			return this.areaInfo.rating.toFixed(1);
		},
		loadAreaData() {
			this.loading = true;
			try {
				// 模拟加载数据
				setTimeout(() => {
					// 根据区域ID加载对应数据
					const areaData = this.getMockAreaData(this.areaId);
					this.areaInfo = areaData || {};
					// 确保areaInfo有count属性
					if (this.areaInfo && !this.areaInfo.count && this.areaInfo.houses) {
						this.areaInfo.count = this.areaInfo.houses.length;
					}
					this.houses = areaData ? areaData.houses || [] : [];
					this.filteredHouses = [...this.houses];
					this.loading = false;
				}, 800);
			} catch (error) {
				console.error('加载数据失败:', error);
				uni.showToast({
					title: '加载失败，请重试',
					icon: 'none'
				});
				this.loading = false;
			}
		},
		getMockAreaData(areaId) {
			// 模拟数据库
			const mockDatabase = {
				'hq': { 
					id: 'hq', 
					name: '横琴区', 
					rating: 4.7, 
					reviewCount: 128,
					description: '横琴区位于珠海市南部，与澳门一水之隔，是澳科大学生租房的热门区域。交通便利，生活配套完善，租金相对较高。',
					houses: [
						{ 
							id: 'hq1', 
							name: '华融琴海湾', 
							info: '步行至口岸', 
							rating: 4.8, 
							price: 3500,
							area: 65,
							type: '2室1厅',
							reviewCount: 32
						},
						{ 
							id: 'hq2', 
							name: '中冶盛世国际广场', 
							info: '步行5分钟', 
							rating: 4.7, 
							price: 3200,
							area: 60,
							type: '1室1厅',
							reviewCount: 28
						},
						{ 
							id: 'hq3', 
							name: '华发首府', 
							info: '公交直达', 
							rating: 4.6, 
							price: 3800,
							area: 70,
							type: '2室2厅',
							reviewCount: 35
						},
						{ 
							id: 'hq4', 
							name: '横琴万象城公寓', 
							info: '商圈中心', 
							rating: 4.5, 
							price: 4000,
							area: 75,
							type: '3室1厅',
							reviewCount: 33
						}
					]
				},
				'xq': { 
					id: 'xq', 
					name: '香洲区', 
					rating: 4.5, 
					reviewCount: 96,
					description: '香洲区是珠海市的中心城区，商业繁华，生活便利，但距离澳科大学较远，需要乘坐公交或地铁通勤。',
					houses: [
						{ 
							id: 'xq1', 
							name: '拱北豪庭', 
							info: '近拱北口岸', 
							rating: 4.6, 
							price: 3000,
							area: 60,
							type: '2室1厅'
						},
						{ 
							id: 'xq2', 
							name: '香洲万科城', 
							info: '近公交站', 
							rating: 4.4, 
							price: 2800,
							area: 55,
							type: '1室1厅'
						}
					]
				},
				'c': { 
					id: 'c', 
					name: '校内宿舍', 
					rating: 4.3, 
					reviewCount: 156,
					description: '校内宿舍位于澳科大学校园内，交通最为便利，价格相对较低，但舒适度和隐私性较差，需要遵守学校的各项规定。',
					houses: [
						{ 
							id: 'c1', 
							name: 'M座', 
							info: '男生四人间，靠近图书馆', 
							rating: 4.3, 
							price: 1200,
							area: 25,
							type: '四人间'
						},
						{ 
							id: 'c2', 
							name: 'S座', 
							info: '女生四人间，靠近食堂', 
							rating: 4.4, 
							price: 1200,
							area: 25,
							type: '四人间'
						},
						{ 
							id: 'c3', 
							name: 'P座', 
							info: '研究生公寓，独立卫浴', 
							rating: 4.7, 
							price: 1800,
							area: 20,
							type: '单人间'
						}
					]
				}
			};
			
			return mockDatabase[areaId] || null;
		},
		setFilter(filter) {
			this.activeFilter = filter;
			this.filterHouses();
		},
		filterHouses() {
			// 确保houses数组存在
			if (!Array.isArray(this.houses)) {
				this.houses = [];
			}
			
			let result = [...this.houses];
			
			// 应用搜索过滤
			if (this.searchText) {
				const searchLower = this.searchText.toLowerCase();
				result = result.filter(house => {
					// 确保house对象及其属性存在
					const nameMatch = house.name ? house.name.toLowerCase().includes(searchLower) : false;
					const infoMatch = house.info ? house.info.toLowerCase().includes(searchLower) : false;
					const typeMatch = house.type ? house.type.toLowerCase().includes(searchLower) : false;
					return nameMatch || infoMatch || typeMatch;
				});
			}
			
			// 应用排序过滤
			switch(this.activeFilter) {
				case 'rating':
					result.sort((a, b) => b.rating - a.rating);
					break;
				case 'reviews':
					result.sort((a, b) => (b.reviewCount || 0) - (a.reviewCount || 0));
					break;
				case 'default':
					// 默认排序，不做特殊处理
					break;
				default:
					// 默认不做特殊排序
					break;
			}
			
			this.filteredHouses = result;
		},
		goToHouseDetail(houseId) {
			uni.navigateTo({
				url: `/pages/housing/house-detail?id=${houseId}&area=${this.areaId}`
			});
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
	padding-top: 120rpx;
}

.header {
	background-color: #3498db;
	padding: 20rpx;
	display: flex;
	align-items: center;
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	z-index: 100;
}

.back-btn {
	color: #ffffff;
	font-size: 36rpx;
	padding: 0 20rpx;
}

.header-title {
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	flex: 1;
	text-align: center;
}

.search-box {
	margin: 20rpx;
	position: relative;
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.search-box input {
	padding-right: 60rpx;
	height: 60rpx;
	font-size: 28rpx;
}

.search-icon {
	position: absolute;
	right: 20rpx;
	top: 50%;
	transform: translateY(-50%);
	color: #999;
}

.area-info-card {
	background-color: #ffffff;
	border-radius: 12rpx;
	padding: 30rpx;
	margin-bottom: 20rpx;
	box-shadow: 0 2rpx 4rpx rgba(0,0,0,0.1);
}

.area-info-title {
	font-size: 32rpx;
	font-weight: bold;
	margin-bottom: 20rpx;
	color: #333;
}

.area-info-stats {
	display: flex;
	justify-content: space-around;
	margin-bottom: 20rpx;
}

.area-stat {
	text-align: center;
}

.stat-value {
	font-size: 36rpx;
	font-weight: bold;
	color: #f39c12;
	display: block;
}

.stat-label {
	font-size: 24rpx;
	color: #666;
	margin-top: 8rpx;
}

.area-info-desc {
	font-size: 26rpx;
	color: #666;
	line-height: 1.6;
}

.filter-bar {
	display: flex;
	background-color: #ffffff;
	padding: 20rpx 30rpx;
	margin-bottom: 20rpx;
	border-radius: 8rpx;
	box-shadow: 0 2rpx 4rpx rgba(0,0,0,0.1);
}

.filter-item {
	padding: 10rpx 30rpx;
	font-size: 28rpx;
	color: #666;
	border-radius: 30rpx;
	margin-right: 20rpx;
}

.filter-item.active {
	background-color: #f39c12;
	color: #ffffff;
}

.housing-list {
	padding: 20rpx;
}

.housing-card {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 24rpx;
	box-shadow: 0 2rpx 8rpx rgba(0,0,0,0.1);
	transition: all 0.3s ease;
}

.housing-card:hover {
	transform: translateY(-2rpx);
	box-shadow: 0 4rpx 12rpx rgba(0,0,0,0.15);
}

.housing-card-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 16rpx;
}

.housing-name {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
}

.housing-tag {
	font-size: 24rpx;
	color: #666666;
	background-color: #f5f5f5;
	padding: 4rpx 12rpx;
	border-radius: 6rpx;
}

.housing-card-body {
	padding: 12rpx 0;
}

.housing-info {
	display: flex;
	align-items: center;
	margin-bottom: 12rpx;
}

.info-area {
	font-size: 26rpx;
	color: #666666;
}

.info-divider {
	margin: 0 12rpx;
	color: #dddddd;
}

.info-text {
	font-size: 26rpx;
	color: #666666;
}

.housing-rating {
	display: flex;
	align-items: center;
}

.rating-stars {
	display: flex;
	margin-right: 12rpx;
}

.star {
	color: #dddddd;
	font-size: 28rpx;
	margin-right: 2rpx;
}

.star.active {
	color: #f39c12;
}

.rating-value {
	font-size: 28rpx;
	color: #f39c12;
	font-weight: bold;
	margin-right: 8rpx;
}

.review-count {
	font-size: 24rpx;
	color: #999999;
}

.housing-card-footer {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-top: 16rpx;
	padding-top: 16rpx;
	border-top: 1rpx solid #f5f5f5;
}

.price-text {
	font-size: 32rpx;
	color: #e74c3c;
	font-weight: bold;
}

.action-btn {
	font-size: 24rpx;
	color: #3498db;
	padding: 8rpx 16rpx;
	border: 1rpx solid #3498db;
	border-radius: 6rpx;
}

.loading, .empty {
	text-align: center;
	padding: 60rpx;
	color: #999999;
	font-size: 28rpx;
	background-color: #ffffff;
	border-radius: 12rpx;
	margin: 20rpx;
}
</style>