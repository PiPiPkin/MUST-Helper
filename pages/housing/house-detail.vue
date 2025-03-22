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
				
				<!-- 评分详情区域 -->
				<view class="rating-detail-box">
					<view class="rating-overview">
						<text class="rating-big">{{houseInfo.rating.toFixed(1)}}</text>
						<view class="rating-stars-big">
							<text v-for="n in 5" :key="n" class="star" 
								  :class="{ 'filled': n <= Math.round(houseInfo.rating) }">★</text>
						</view>
						<text class="review-count-big">{{houseInfo.reviewCount}}人评价</text>
					</view>
					
					<view class="rating-dimensions">
						<view class="dimension-item">
							<text class="dimension-name">租金与性价比</text>
							<view class="dimension-stars">
								<text v-for="n in 5" :key="n" class="star" 
									  :class="{ 'filled': n <= Math.round(houseInfo.priceRating || 4.5) }">★</text>
							</view>
							<text class="dimension-score">{{(houseInfo.priceRating || 4.5).toFixed(1)}}</text>
						</view>
						
						<view class="dimension-item">
							<text class="dimension-name">地理位置与便利性</text>
							<view class="dimension-stars">
								<text v-for="n in 5" :key="n" class="star" 
									  :class="{ 'filled': n <= Math.round(houseInfo.locationRating || 4.3) }">★</text>
							</view>
							<text class="dimension-score">{{(houseInfo.locationRating || 4.3).toFixed(1)}}</text>
						</view>
						
						<view class="dimension-item">
							<text class="dimension-name">安全与舒适度</text>
							<view class="dimension-stars">
								<text v-for="n in 5" :key="n" class="star" 
									  :class="{ 'filled': n <= Math.round(houseInfo.comfortRating || 4.7) }">★</text>
							</view>
							<text class="dimension-score">{{(houseInfo.comfortRating || 4.7).toFixed(1)}}</text>
						</view>
					</view>
					
					<button class="rate-btn" @click="showRateModal">我要评分</button>
				</view>
				
				<!-- 评价列表 -->
				<view class="reviews-section">
					<view class="section-header">
						<text class="section-title">评价 ({{houseInfo.reviews ? houseInfo.reviews.length : 0}})</text>
					</view>
					
					<view v-if="!houseInfo.reviews || houseInfo.reviews.length === 0" class="no-reviews">
						暂无评价，快来发表第一条评价吧！
					</view>
					
					<view v-else class="review-list">
						<view class="review-item" v-for="(review, index) in houseInfo.reviews" :key="index">
							<view class="review-header">
								<text class="reviewer-name">{{review.username}}</text>
								<view class="review-stars">
									<text v-for="n in 5" :key="n" class="star" 
										  :class="{ 'filled': n <= Math.round(review.rating) }">★</text>
									<text class="review-rating">{{review.rating.toFixed(1)}}</text>
								</view>
								<text class="review-date">{{review.date}}</text>
							</view>
							<text class="review-content">{{review.content}}</text>
							<view class="review-likes">
								<text class="like-icon">👍</text>
								<text class="like-count">{{review.likes || 0}}</text>
							</view>
						</view>
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
					priceRating: 4.5,
					locationRating: 4.9,
					comfortRating: 4.7,
					description: '华融琴海湾位于横琴口岸附近，交通便利，步行可达口岸。小区环境优美，配套设施齐全，是澳科大学生租房的理想选择。',
					reviews: [
						{
							username: '租房达人',
							rating: 5.0,
							date: '2023-10-15',
							content: '位置非常好，步行到口岸只需5分钟，房间干净整洁，小区环境也很好，安保措施到位。性价比很高，推荐！',
							likes: 24
						},
						{
							username: '小澳同学',
							rating: 4.5,
							date: '2023-09-28',
							content: '房子整体不错，交通便利，但是租金稍微有点高。房东人很好，有问题都能及时解决。',
							likes: 18
						}
					]
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
					priceRating: 4.6,
					locationRating: 4.8,
					comfortRating: 4.5,
					description: '中冶盛世国际广场位于横琴新区，距离口岸步行约5分钟，周边配套齐全，交通便利，是学生租房的不错选择。',
					reviews: [
						{
							username: '横琴租客',
							rating: 4.8,
							date: '2023-10-05',
							content: '地理位置很好，去澳门上学很方便。房间采光不错，物业服务也很到位。',
							likes: 15
						}
					]
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
					priceRating: 4.8,
					locationRating: 5.0,
					comfortRating: 3.8,
					description: 'M座宿舍位于校内，靠近图书馆，环境安静，适合学习。宿舍为四人间，配有独立卫浴、空调、书桌等基本设施。',
					reviews: [
						{
							username: '学霸一号',
							rating: 4.5,
							date: '2023-09-20',
							content: '宿舍位置很好，离图书馆和教学楼都很近。四人间空间还算宽敞，就是洗澡时间有限制，热水供应不是很稳定。',
							likes: 32
						},
						{
							username: '夜猫子',
							rating: 4.0,
							date: '2023-08-15',
							content: '总体来说还不错，性价比高，但是隔音效果一般，晚上有点炒。',
							likes: 10
						}
					]
				}
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
		},
		showRateModal() {
			uni.showToast({
				title: '评分功能开发中',
				icon: 'none'
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

/* 评分详情区域样式 */
.rating-detail-box {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
	background-color: #f9f9f9;
}

.rating-overview {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 20rpx 0;
	margin-bottom: 20rpx;
	border-bottom: 1rpx dashed #eeeeee;
}

.rating-big {
	font-size: 60rpx;
	font-weight: bold;
	color: #f39c12;
	line-height: 1;
	margin-bottom: 10rpx;
}

.rating-stars-big {
	display: flex;
	margin-bottom: 10rpx;
}

.rating-stars-big .star {
	font-size: 36rpx;
	margin: 0 2rpx;
}

.review-count-big {
	font-size: 26rpx;
	color: #999999;
}

.rating-dimensions {
	padding: 10rpx 0;
}

.dimension-item {
	display: flex;
	align-items: center;
	margin-bottom: 15rpx;
}

.dimension-name {
	width: 240rpx;
	font-size: 28rpx;
	color: #666666;
}

.dimension-stars {
	flex: 1;
	display: flex;
}

.dimension-stars .star {
	font-size: 28rpx;
	margin-right: 4rpx;
}

.dimension-score {
	width: 60rpx;
	text-align: right;
	font-size: 28rpx;
	font-weight: bold;
	color: #f39c12;
}

.rate-btn {
	margin-top: 20rpx;
	background-color: #f39c12;
	color: #ffffff;
	font-size: 30rpx;
	height: 70rpx;
	line-height: 70rpx;
	border-radius: 35rpx;
}

/* 评价列表样式 */
.reviews-section {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
}

.section-header {
	margin-bottom: 15rpx;
}

.section-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
}

.no-reviews {
	text-align: center;
	padding: 30rpx 0;
	color: #999999;
	font-size: 28rpx;
}

.review-list {
	padding: 10rpx 0;
}

.review-item {
	padding: 15rpx 0;
	border-bottom: 1rpx solid #f0f0f0;
}

.review-header {
	display: flex;
	align-items: center;
	margin-bottom: 10rpx;
}

.reviewer-name {
	font-size: 28rpx;
	font-weight: bold;
	color: #333333;
	margin-right: 15rpx;
}

.review-stars {
	display: flex;
	align-items: center;
	margin-right: 15rpx;
}

.review-stars .star {
	font-size: 24rpx;
	margin-right: 2rpx;
}

.review-rating {
	font-size: 24rpx;
	color: #f39c12;
	margin-left: 5rpx;
}

.review-date {
	font-size: 24rpx;
	color: #999999;
	margin-left: auto;
}

.review-content {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.5;
	margin-bottom: 10rpx;
}

.review-likes {
	display: flex;
	align-items: center;
}

.like-icon {
	font-size: 24rpx;
	color: #999999;
	margin-right: 5rpx;
}

.like-count {
	font-size: 24rpx;
	color: #999999;
}

.house-description {
	padding: 20rpx;
	border-bottom: 1rpx solid #eeeeee;
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