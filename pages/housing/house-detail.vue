<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">{{houseInfo.name || '房源详情'}}</text>
			<view class="header-icons">
				<text class="icon">•••</text>
				<text class="icon">⦿</text>
			</view>
		</view>
		
		<view class="content">
			<view v-if="loading" class="loading">
				加载中...
			</view>
			<view v-else-if="!houseInfo.id" class="empty">
				暂无房源数据
			</view>
			<view v-else class="house-detail">
				<view class="house-header">
					<text class="house-name">{{houseInfo.name}}</text>
					<view class="house-rating">
						<text class="rating-score">{{houseInfo.rating.toFixed(1)}}</text>
						<view class="stars">
							<text v-for="n in 5" :key="n" class="star" 
								  :class="{ 'filled': n <= Math.round(houseInfo.rating) }">★</text>
						</view>
						<text class="review-count">{{houseInfo.reviewCount}}条评价</text>
					</view>
				</view>
				
				<view class="house-info">
					<view class="info-item">
						<text class="info-label">位置</text>
						<text class="info-value">{{houseInfo.info}}</text>
					</view>
					<view class="info-item">
						<text class="info-label">价格</text>
						<text class="info-value">¥{{houseInfo.price || '暂无价格'}}/月</text>
					</view>
					<view class="info-item">
						<text class="info-label">面积</text>
						<text class="info-value">{{houseInfo.area || '暂无数据'}}㎡</text>
					</view>
					<view class="info-item">
						<text class="info-label">房型</text>
						<text class="info-value">{{houseInfo.type || '暂无数据'}}</text>
					</view>
				</view>
				
				<view class="house-description">
					<text class="section-title">房源描述</text>
					<text class="description-text">{{houseInfo.description || '暂无描述信息'}}</text>
				</view>
				
				<view class="contact-section">
					<button class="contact-btn" @click="contactOwner">联系房东</button>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			houseId: '',
			areaId: '',
			loading: true,
			houseInfo: {}
		}
	},
	onLoad(options) {
		if (options.id && options.area) {
			this.houseId = options.id;
			this.areaId = options.area;
			this.loadHouseData();
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
		loadHouseData() {
			this.loading = true;
			try {
				// 模拟加载数据
				setTimeout(() => {
					// 根据区域ID和房源ID加载对应数据
					const houseData = this.getMockHouseData(this.areaId, this.houseId);
					this.houseInfo = houseData || {};
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
		getMockHouseData(areaId, houseId) {
			// 模拟数据库
			const mockDatabase = {
				// 横琴房源详情
				'hq1': { 
					id: 'hq1', 
					name: '华融琴海湾', 
					info: '步行至口岸', 
					rating: 4.8, 
					reviewCount: 42,
					price: 3500,
					area: 65,
					type: '2室1厅',
					description: '华融琴海湾位于横琴口岸附近，交通便利，步行可达口岸。小区环境优美，配套设施齐全，是澳科大学生租房的理想选择。'
				},
				'hq2': { 
					id: 'hq2', 
					name: '中冶盛世国际广场', 
					info: '步行5分钟', 
					rating: 4.7, 
					reviewCount: 38,
					price: 3200,
					area: 60,
					type: '1室1厅',
					description: '中冶盛世国际广场位于横琴新区，距离口岸步行约5分钟，周边配套齐全，交通便利，是学生租房的不错选择。'
				},
				// 校内宿舍详情
				'c1': { 
					id: 'c1', 
					name: 'M座', 
					info: '男生四人间，靠近图书馆', 
					rating: 4.3, 
					reviewCount: 56,
					price: 1200,
					area: 25,
					type: '四人间',
					description: 'M座宿舍位于校内，靠近图书馆，环境安静，适合学习。宿舍为四人间，配有独立卫浴、空调、书桌等基本设施。'
				},
				// 其他区域房源详情可以继续添加
			};
			
			return mockDatabase[houseId] || null;
		},
		contactOwner() {
			uni.showModal({
				title: '联系房东',
				content: '是否拨打房东电话：13800138000？',
				success: function (res) {
					if (res.confirm) {
						uni.makePhoneCall({
							phoneNumber: '13800138000'
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

.content {
	padding: 20rpx;
}

.loading, .empty {
	text-align: center;
	padding: 40rpx;
	color: #999999;
	font-size: 28rpx;
}

.house-detail {
	background-color: #ffffff;
	border-radius: 10rpx;
	overflow: hidden;
	box-shadow: 0 2rpx 6rpx rgba(0, 0, 0, 0.1);
}

.house-header {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
}

.house-name {
	font-size: 36rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
}

.house-rating {
	display: flex;
	align-items: center;
	gap: 10rpx;
}

.rating-score {
	font-size: 28rpx;
	color: #f39c12;
	font-weight: bold;
}

.stars {
	display: flex;
}

.star {
	color: #dddddd;
	font-size: 28rpx;
}

.star.filled {
	color: #f39c12;
}

.review-count {
	font-size: 24rpx;
	color: #999999;
}

.house-info {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
}

.info-item {
	display: flex;
	justify-content: space-between;
	margin-bottom: 15rpx;
}

.info-label {
	font-size: 28rpx;
	color: #666666;
}

.info-value {
	font-size: 28rpx;
	color: #333333;
	font-weight: bold;
}

.house-description {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
}

.section-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 15rpx;
}

.description-text {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.5;
}

.contact-section {
	padding: 30rpx 20rpx;
}

.contact-btn {
	background-color: #3498db;
	color: #ffffff;
	font-size: 32rpx;
	height: 80rpx;
	line-height: 80rpx;
	border-radius: 40rpx;
}