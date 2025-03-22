<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">{{areaInfo.name}}房源列表</text>
			<view class="header-icons">
				<text class="icon">•••</text>
				<text class="icon">⦿</text>
			</view>
		</view>
		
		<view class="search-box">
			<input type="text" placeholder="搜索小区..." v-model="searchText" />
			<text class="search-icon">🔍</text>
		</view>
		
		<view class="housing-list">
			<template v-if="loading">
				<view class="loading">加载中...</view>
			</template>
			<template v-else-if="housings.length === 0">
				<view class="empty">暂无房源数据</view>
			</template>
			<template v-else>
				<view class="housing-item" v-for="(item, index) in filteredHousings" :key="index" @click="navigateToDetail(item.id)">
					<view class="housing-name">{{item.name}}</view>
					<view class="housing-info">{{item.info}}</view>
					<view class="housing-meta">
						<text class="rating-value">{{item.rating.toFixed(1)}}</text>
						<view class="rating-stars">
							<text v-for="n in 5" :key="n" :class="['star', n <= Math.floor(item.rating) ? 'active' : '']">★</text>
						</view>
						<text class="review-count">{{item.reviewCount}}条评价</text>
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
			areaId: '',
			searchText: '',
			loading: true,
			areaInfo: {
				name: '加载中...',
				count: 0,
				reviews: 0
			},
			housings: []
		}
	},
	computed: {
		filteredHousings() {
			if (!this.searchText) return this.housings;
			const searchLower = this.searchText.toLowerCase();
			return this.housings.filter(housing => 
				housing.name.toLowerCase().includes(searchLower) ||
				housing.info.toLowerCase().includes(searchLower)
			);
		}
	},
	onLoad(options) {
		this.loading = true; // 确保初始状态为加载中
		if (options.id) {
			this.areaId = options.id;
			this.loadAreaData();
		} else {
			uni.showToast({
				title: '参数错误',
				icon: 'none'
			});
			this.loading = false; // 出错时也要更新状态
			setTimeout(() => {
				this.goBack();
			}, 1500);
		}
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		loadAreaData() {
			try {
				// 模拟网络请求延迟
				setTimeout(() => {
					// 区域基本信息
					const areasData = {
						'macau': { name: '澳门', count: 12, reviews: 328 },
						'hengqin': { name: '横琴', count: 18, reviews: 256 },
						'campus': { name: '校内宿舍', count: 8, reviews: 187 },
						'zhuhai': { name: '珠海', count: 15, reviews: 142 },
						'campus-dorm': { name: '校区宿舍', count: 5, reviews: 98 }
					};
					
					// 横琴小区数据
					const hengqinHousings = [
						{ id: 'hq1', name: '华融琴海湾', info: '步行至口岸', rating: 4.8, reviewCount: 42 },
						{ id: 'hq2', name: '中冶盛世国际广场', info: '步行5分钟', rating: 4.7, reviewCount: 38 },
						{ id: 'hq3', name: '信德口岸商务中心', info: '步行2分钟', rating: 4.9, reviewCount: 45 },
						{ id: 'hq4', name: '华发悦府', info: '通勤15分钟', rating: 4.6, reviewCount: 32 },
						{ id: 'hq5', name: '华发首府', info: '步行15分钟', rating: 4.5, reviewCount: 28 },
						{ id: 'hq6', name: '保利国际广场', info: '近口岸，商住两用', rating: 4.7, reviewCount: 36 },
						{ id: 'hq7', name: '荔枝湾花园', info: '南区/北区，性价比高', rating: 4.4, reviewCount: 25 },
						{ id: 'hq8', name: '龙光玖龙玺', info: '步行10分钟', rating: 4.6, reviewCount: 30 },
						{ id: 'hq9', name: '横琴新家园', info: '租金较低', rating: 4.2, reviewCount: 18 },
						{ id: 'hq10', name: '中海名钻', info: '近口岸', rating: 4.8, reviewCount: 40 },
						{ id: 'hq11', name: '横琴中央汇', info: '商住两用，交通便利', rating: 4.7, reviewCount: 35 }
					];
					
					// 校内宿舍数据
					const campusHousings = [
						{ id: 'c1', name: 'M座', info: '男生四人间，靠近图书馆', rating: 4.3, reviewCount: 56 },
						{ id: 'c2', name: 'F座', info: '男生四人间，近篮球场', rating: 4.2, reviewCount: 48 },
						{ id: 'c3', name: 'G座', info: '女生五人间，无电梯', rating: 3.9, reviewCount: 42 },
						{ id: 'c4', name: 'P座', info: '女生四人间，15层电梯楼', rating: 4.5, reviewCount: 60 },
						{ id: 'c5', name: 'L座', info: '男女分层混住', rating: 4.1, reviewCount: 38 }
					];
					
					// 校区宿舍数据
					const campusDormHousings = [
						{ id: 'cd1', name: '擎天汇', info: '酒店式公寓，通勤20分钟', rating: 4.6, reviewCount: 32 },
						{ id: 'cd2', name: '海擎天', info: '澳门本岛，通勤50分钟', rating: 4.2, reviewCount: 28 },
						{ id: 'cd3', name: '国兴', info: '澳门半岛宿舍', rating: 4.4, reviewCount: 30 },
						{ id: 'cd4', name: '半岛宿舍', info: '澳门半岛', rating: 4.3, reviewCount: 25 }
					];
					
					// 澳门房源数据
					const macauHousings = [
						{ id: 'm1', name: '皇朝广场', info: '澳门半岛，近关闸', rating: 4.7, reviewCount: 52 },
						{ id: 'm2', name: '新口岸花园', info: '近威尼斯人', rating: 4.8, reviewCount: 48 },
						{ id: 'm3', name: '黄金海岸', info: '氹仔岛，近大学', rating: 4.9, reviewCount: 56 },
						{ id: 'm4', name: '御景湾', info: '路环岛，环境优美', rating: 4.6, reviewCount: 42 },
						{ id: 'm5', name: '海擎天', info: '澳门半岛，近关闸', rating: 4.5, reviewCount: 38 },
						{ id: 'm6', name: '濠庭都会', info: '氹仔岛，近澳门大学', rating: 4.7, reviewCount: 45 },
						{ id: 'm7', name: '宝龙花园', info: '澳门半岛，近葡京', rating: 4.4, reviewCount: 36 },
						{ id: 'm8', name: '海岸花园', info: '路环岛，环境优美', rating: 4.8, reviewCount: 50 }
					];
					
					// 珠海房源数据
					const zhuhaiHousings = [
						{ id: 'z1', name: '拱北花园', info: '近拱北口岸', rating: 4.5, reviewCount: 40 },
						{ id: 'z2', name: '华发商都', info: '近九洲港', rating: 4.6, reviewCount: 38 },
						{ id: 'z3', name: '格力海岸', info: '环境优美', rating: 4.7, reviewCount: 42 },
						{ id: 'z4', name: '中信红树湾', info: '近唐家湾', rating: 4.4, reviewCount: 35 },
						{ id: 'z5', name: '华发峰尚', info: '近拱北口岸', rating: 4.8, reviewCount: 45 },
						{ id: 'z6', name: '九洲城', info: '近九洲港', rating: 4.3, reviewCount: 32 },
						{ id: 'z7', name: '华发四季', info: '环境优美', rating: 4.6, reviewCount: 38 },
						{ id: 'z8', name: '中海名钻', info: '近唐家湾', rating: 4.5, reviewCount: 36 }
					];
					
					// 设置区域信息
					this.areaInfo = areasData[this.areaId] || { name: '未知区域', count: 0, reviews: 0 };
					
					// 根据区域ID加载对应数据
					switch(this.areaId) {
						case 'hengqin':
							this.housings = hengqinHousings;
							break;
						case 'campus':
							this.housings = campusHousings;
							break;
						case 'campus-dorm':
							this.housings = campusDormHousings;
							break;
						case 'macau':
							// 添加澳门数据
							this.housings = macauHousings || [];
							break;
						case 'zhuhai':
							// 添加珠海数据
							this.housings = zhuhaiHousings || [];
							break;
						default:
							this.housings = [];
					}
					
					this.loading = false; // 数据加载完成
				}, 500);
			} catch (error) {
				console.error('加载数据失败:', error);
				this.loading = false; // 出错时也要更新状态
				uni.showToast({
					title: '加载失败，请重试',
					icon: 'none'
				});
			}
		}, // 确保这里有逗号
		navigateToDetail(houseId) {
			console.log('准备跳转到房源详情页', houseId, this.areaId);
			uni.navigateTo({
				url: `/pages/housing/house-detail?id=${houseId}&area=${this.areaId}`,
				success: function() {
					console.log('跳转成功');
				},
				fail: function(err) {
					console.error('跳转失败', err);
					uni.showToast({
						title: '页面跳转失败',
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
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.search-icon {
	position: absolute;
	right: 40rpx;
	top: 30rpx;
	font-size: 32rpx;
	color: #3498db;
}

.housing-list {
	padding: 20rpx;
}

.housing-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 30rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.housing-name {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	display: block;
	margin-bottom: 10rpx;
}

.housing-info {
	font-size: 28rpx;
	color: #666666;
	display: block;
	margin-bottom: 20rpx;
}

.housing-meta {
	display: flex;
	align-items: center;
}

.rating-value {
	font-size: 40rpx;
	font-weight: bold;
	color: #f39c12;
	margin-right: 20rpx;
}

.rating-stars {
	display: flex;
	margin-right: 20rpx;
}

.star {
	color: #dddddd;
	font-size: 28rpx;
}

.star.active {
	color: #f39c12;
}

.review-count {
	font-size: 24rpx;
	color: #999999;
}

.loading, .empty {
	text-align: center;
	padding: 40rpx;
	color: #999999;
	font-size: 28rpx;
	background-color: #ffffff;
	border-radius: 12rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}