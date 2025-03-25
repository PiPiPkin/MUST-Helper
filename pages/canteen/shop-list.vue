<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header" :style="{ paddingTop: statusBarHeight + 'px' }">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{canteen.name || '店铺列表'}}</text>
		</view>
		
		<!-- 搜索框 -->
		<view class="search-box">
			<input type="text" placeholder="搜索店铺..." v-model="searchText" />
			<text class="search-icon">🔍</text>
		</view>
		
		<!-- 店铺列表 -->
		<view class="shop-list">
			<view class="shop-item" v-for="(item, index) in filteredShops" :key="index" 
				  @click="navigateToShopDetail(item.id)">
				<view class="shop-info">
					<text class="shop-name">{{item.name}}</text>
					<view class="shop-rating">
						<text class="rating-value">{{item.rating.toFixed(1)}}</text>
						<view class="rating-stars">
							<text v-for="n in 5" :key="n" :class="['star', n <= Math.floor(item.rating) ? 'active' : '']">★</text>
						</view>
					</view>
					<view class="tags">
						<text class="tag" v-for="(tag, tagIndex) in item.tags" :key="tagIndex">{{tag}}</text>
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
			statusBarHeight: 20,
			canteenId: 0,
			searchText: '',
			canteen: {
				name: '加载中...'
			},
			allShops: {
				// 厨艺天地的店铺
				1: [
					{
						id: 101,
						name: '南洋巴打',
						image: '/static/shops/nanyang.jpg',
						rating: 4.6,
						averagePrice: 28,
						
						tags: ['铁板', '咖喱', '海南鸡饭']
					},
					{
						id: 102,
						name: '隆江猪脚饭',
						image: '/static/shops/longjiang.jpg',
						rating: 4.7,
						averagePrice: 32,
						
						tags: ['粤式', '猪脚', '烧腊']
					},
					{
						id: 103,
						name: '小两口',
						image: '/static/shops/xiaoliangkou.jpg',
						rating: 4.4,
						averagePrice: 25,
						
						tags: ['川菜', '湘菜', '小炒']
					},
					{
						id: 104,
						name: '面点王',
						image: '/static/shops/miandianwang.jpg',
						rating: 4.5,
						averagePrice: 18,
						
						tags: ['面食', '早餐', '小吃']
					},
					{
						id: 105,
						name: '粤式烧腊',
						image: '/static/shops/yueshi.jpg',
						rating: 4.8,
						averagePrice: 35,
						
						tags: ['烧腊', '粤式', '快餐']
					}
				],
				// 麦当劳的店铺
				2: [
					{
						id: 201,
						name: '麦当劳主店',
						image: '/static/shops/mcd_main.jpg',
						rating: 4.2,
						averagePrice: 30,
						
						tags: ['汉堡', '炸鸡', '快餐']
					}
				],
				// OK便利店
				3: [
					{
						id: 301,
						name: 'OK便利店',
						image: '/static/shops/ok_store.jpg',
						rating: 4.0,
						averagePrice: 15,
						
						tags: ['零食', '饮料', '便当']
					}
				],
				// 点绽
				4: [
					{
						id: 401,
						name: '点绽甜品',
						image: '/static/shops/dianzhan_dessert.jpg',
						rating: 4.5,
						averagePrice: 22,
						
						tags: ['甜品', '奶茶', '冰淇淋']
					},
					{
						id: 402,
						name: '点绽小食',
						image: '/static/shops/dianzhan_snack.jpg',
						rating: 4.3,
						averagePrice: 18,
						
						tags: ['小吃', '粤式', '点心']
					}
				],
				// 点聚
				5: [
					{
						id: 501,
						name: '点聚茶餐厅',
						image: '/static/shops/dianju_restaurant.jpg',
						rating: 4.4,
						averagePrice: 35,
						
						tags: ['港式', '茶餐厅', '早茶']
					},
					{
						id: 502,
						name: '点聚烧腊',
						image: '/static/shops/dianju_roast.jpg',
						rating: 4.6,
						averagePrice: 40,
						
						tags: ['烧腊', '粤式', '快餐']
					}
				],
				// 季节
				6: [
					{
						id: 601,
						name: '季节快餐',
						image: '/static/shops/season_fast.jpg',
						rating: 4.1,
						averagePrice: 25,
						
						tags: ['中餐', '快餐', '套餐']
					},
					{
						id: 602,
						name: '季节面馆',
						image: '/static/shops/season_noodle.jpg',
						rating: 4.2,
						averagePrice: 22,
					
						tags: ['面食', '小吃', '快餐']
					}
				],
				// 其他店
				7: [
					{
						id: 701,
						name: '咖啡角',
						image: '/static/shops/coffee_corner.jpg',
						rating: 4.3,
						averagePrice: 20,
						
						tags: ['咖啡', '甜点', '轻食']
					},
					{
						id: 702,
						name: '水果吧',
						image: '/static/shops/fruit_bar.jpg',
						rating: 4.4,
						averagePrice: 15,
						
						tags: ['水果', '果汁', '健康']
					}
				]
			},
			shops: []
		}
	},
	computed: {
		filteredShops() {
			if (!this.searchText) return this.shops;
			const searchLower = this.searchText.toLowerCase();
			return this.shops.filter(shop => 
				shop.name.toLowerCase().includes(searchLower) ||
				shop.tags.some(tag => tag.toLowerCase().includes(searchLower))
			);
		}
	},
	onLoad(options) {
		// 获取状态栏高度
		try {
			uni.getSystemInfo({
				success: (res) => {
					this.statusBarHeight = res.statusBarHeight;
					console.log('获取系统信息成功:', res);
				},
				fail: (err) => {
					console.error('获取系统信息失败:', err);
					this.statusBarHeight = 20;
				}
			});
		} catch (error) {
			console.error('获取系统信息异常:', error);
			this.statusBarHeight = 20;
		}

		if (options.canteenId) {
			this.canteenId = parseInt(options.canteenId);
			// 添加错误处理
			try {
				// 这里应该调用接口获取食堂信息
				this.loadCanteenData();
			} catch (error) {
				console.error('加载食堂数据失败:', error);
				uni.showToast({
					title: '加载失败，请重试',
					icon: 'none'
				});
			}
		}
	},
	methods: {
		// 添加数据加载方法
		async loadCanteenData() {
			try {
				uni.showLoading({
					title: '加载中...'
				});

				console.log('加载食堂ID:', this.canteenId);
				
				// 模拟食堂数据
				const canteensData = {
					1: { id: 1, name: '厨艺天地' },
					2: { id: 2, name: '麦当劳' },
					3: { id: 3, name: 'OK便利店' },
					4: { id: 4, name: '点绽' },
					5: { id: 5, name: '点聚' },
					6: { id: 6, name: '季节' },
					7: { id: 7, name: '其他店' }
				};
				
				// 使用Promise包装异步操作
				await new Promise(resolve => setTimeout(resolve, 500));

				// 设置食堂信息
				this.canteen = canteensData[this.canteenId] || { id: this.canteenId, name: '未知食堂' };
				
				// 设置该食堂下的店铺
				this.shops = this.allShops[this.canteenId] || [];
				
				console.log('食堂数据加载完成:', this.canteen);
				console.log('店铺数据加载完成:', this.shops);

				uni.hideLoading();
			} catch (error) {
				console.error('加载数据失败:', error);
				uni.hideLoading();
				uni.showToast({
					title: '加载失败，请重试',
					icon: 'none'
				});
			}
		},
		
		goBack() {
			console.log('返回上一页');
			const pages = getCurrentPages();
			
			if (pages.length <= 1) {
				// 如果当前是第一个页面，直接跳转到食堂列表页
				uni.switchTab({
					url: '/pages/canteen/index',
					fail: function(err) {
						console.error('跳转失败:', err);
						// 尝试使用 reLaunch 作为备选方案
						uni.reLaunch({
							url: '/pages/canteen/index'
						});
					}
				});
			} else {
				// 如果不是第一个页面，则正常返回
				uni.navigateBack({
					fail: function(err) {
						console.error('返回失败:', err);
						// 如果返回失败，尝试跳转到食堂列表页
						uni.switchTab({
							url: '/pages/canteen/index'
						});
					}
				});
			}
		},
		
		navigateToShopDetail(shopId) {
			uni.navigateTo({
				url: `/pages/canteen/shop-detail?shopId=${shopId}&canteenId=${this.canteenId}`
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
	padding: 20rpx 30rpx;
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
	flex: 1;
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	text-align: center;
}

.search-box {
	position: fixed;
	top: calc(var(--status-bar-height) + 80rpx);
	left: 0;
	right: 0;
	padding: 20rpx;
	background-color: #3498db;
	z-index: 99;
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
	top: 50%;
	transform: translateY(-50%);
	font-size: 32rpx;
	color: #999;
}

.shop-list {
	padding: calc(var(--status-bar-height) + 180rpx) 20rpx 20rpx;
}

.shop-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0, 0, 0, 0.1);
}

.shop-info {
	display: flex;
	flex-direction: column;
	gap: 10rpx;
}

.shop-name {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
}

.shop-rating {
	display: flex;
	align-items: center;
	gap: 10rpx;
}

.rating-value {
	font-size: 28rpx;
	color: #f39c12;
	font-weight: bold;
}

.rating-stars {
	display: flex;
	gap: 4rpx;
}

.star {
	color: #ddd;
	font-size: 24rpx;
}

.star.active {
	color: #f39c12;
}

.review-count {
	font-size: 24rpx;
	color: #666;
}

.tags {
	display: flex;
	flex-wrap: wrap;
	gap: 10rpx;
	margin-top: 10rpx;
}

.tag {
	padding: 2rpx 10rpx;
	background-color: #eef7fd;
	border-radius: 4rpx;
	font-size: 22rpx;
	color: #3498db;
}

.shop-hours {
	color: #888888;
}

.content {
	padding: 15rpx;
}
</style>