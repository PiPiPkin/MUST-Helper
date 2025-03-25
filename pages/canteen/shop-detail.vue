<template>
	<view class="container">
		<view class="loading-overlay" v-if="isLoading">
			<view class="loading-spinner"></view>
			<text class="loading-text">加载中...</text>
		</view>
		<!-- 顶部导航栏 -->
		<view class="header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{shop.name || '店铺详情'}}</text>
		</view>
		
		<!-- 店铺信息 -->
		<view class="shop-info">
			<view class="shop-header">
				<text class="shop-name">{{shop.name || '加载中...'}}</text>
				<view class="shop-tags">
					<text class="tag" v-for="(tag, index) in shop.tags" :key="index">{{tag}}</text>
				</view>
			</view>
			<text class="shop-code" v-if="shop.code">{{shop.code}}</text>
			<text class="shop-code" v-if="shop.code">{{shop.code}}</text>
			<text class="shop-description">{{shop.description || '暂无描述'}}</text>
		</view>
		
		<!-- 评分区 -->
		<view class="rating-section">
			<view class="overall-rating">
				<text class="rating-value">{{shop.rating ? shop.rating.toFixed(1) : '0.0'}}</text>
				<view class="stars">
					<text v-for="n in 5" :key="n" class="star" 
						  :class="{ 'filled': n <= Math.round(shop.rating || 0) }">★</text>
				</view>
				<text class="review-count">{{shop.reviewCount || 0}}人评价</text>
			</view>
			
			<view class="rating-details">
				<view class="rating-item">
					<text class="rating-label">口味</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.tasteRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.tasteRating ? shop.tasteRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">价格</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.priceRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.priceRating ? shop.priceRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">卫生</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.hygieneRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.hygieneRating ? shop.hygieneRating.toFixed(1) : '0.0'}}</text>
				</view>
			</view>
			
			<button class="rate-btn" @click="showRatingPanel">我要评分</button>
		</view>
		
		
		
		<!-- 评论区 -->
		<view class="comment-section">
			<view class="section-title">
				<text>评论 ({{comments.length}})</text>
			</view>
			
			<view class="comment-list">
				<view v-if="comments.length === 0" class="no-comment">
					<text>暂无评论，快来发表第一条评论吧</text>
				</view>
				<view class="comment-item" v-for="(item, index) in comments" :key="index">
					<view class="comment-header">
						<image class="user-avatar" :src="item.userAvatar || '/static/images/avatars/default.jpg'" mode="aspectFill"></image>
						<view class="comment-user-info">
							<text class="user-name">{{item.userName}}</text>
							<view class="comment-rating">
								<text v-for="n in 5" :key="n" class="star" 
									  :class="{ 'filled': n <= Math.round(item.rating) }">★</text>
								<text class="rating-text">{{item.rating.toFixed(1)}}</text>
							</view>
						</view>
						<text class="comment-time">{{item.time}}</text>
					</view>
					<text class="comment-content">{{item.content}}</text>
					<view class="comment-footer">
						<view class="like-btn" @click="toggleLike(index)" :class="{'liked': item.isLiked}">
							<text class="like-icon">👍</text>
							<text class="like-count">{{item.likeCount}}</text>
						</view>
						<view class="delete-btn" v-if="item.userName === '我'" @click="confirmDeleteComment(index)">
							<text class="delete-icon">🗑️</text>
							<text>删除</text>
						</view>
					</view>
				</view>
			</view>
			
			<view class="comment-input-box" :class="{'expanded': isCommentExpanded}">
				<view class="input-wrapper" @click="expandCommentInput">
					<textarea v-if="isCommentExpanded" 
							   class="comment-textarea" 
							   v-model="newComment" 
							   placeholder="分享你对这家店的评价、推荐菜品、用餐体验..."
							   :focus="isCommentExpanded"
							   auto-height></textarea>
					<input v-else 
							type="text" 
							placeholder="分享你对这家店的评价、推荐菜品、用餐体验..." 
							v-model="newComment" />
				</view>
				<button class="submit-btn" @click="submitComment">发表</button>
			</view>
		</view>
		
		<!-- 评分面板 -->
		<view class="rating-panel" v-if="showRating">
			<view class="rating-panel-content">
				<view class="panel-header">
					<text class="panel-title">评分</text>
					<text class="close-btn" @click="hideRatingPanel">×</text>
				</view>
				
				<view class="panel-body">
					<view class="panel-rating-item">
						<text class="panel-rating-label">口味</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.taste }"
								  @click="userRating.taste = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">价格</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.price }"
								  @click="userRating.price = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">卫生</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.hygiene }"
								  @click="userRating.hygiene = n">★</text>
						</view>
					</view>
				</view>
				
				<button class="submit-rating-btn" @click="submitRating">提交评分</button>
			</view>
		</view>
	</view>
</template>

<style>
.container {
	min-height: 100vh;
	background-color: #f5f5f5;
	position: relative;
}

.loading-overlay {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(255, 255, 255, 0.9);
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	z-index: 9999;
}

.loading-spinner {
	width: 60rpx;
	height: 60rpx;
	border: 6rpx solid #f3f3f3;
	border-top: 6rpx solid #3498db;
	border-radius: 50%;
	animation: spin 1s linear infinite;
}

.loading-text {
	margin-top: 20rpx;
	color: #666666;
	font-size: 28rpx;
}

@keyframes spin {
	0% { transform: rotate(0deg); }
	100% { transform: rotate(360deg); }
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
	flex: 1;
	color: #ffffff;
	font-size: 36rpx;
	font-weight: bold;
	text-align: center;
}

.shop-info {
	margin-bottom: 40rpx;
}

.shop-header {
	margin-bottom: 20rpx;
}

.shop-name {
	font-size: 36rpx;
	font-weight: bold;
	color: #333;
	margin-bottom: 10rpx;
	display: block;
}

.shop-tags {
	display: flex;
	flex-wrap: wrap;
	gap: 10rpx;
	margin-top: 10rpx;
}

.tag {
	padding: 4rpx 12rpx;
	background-color: #eef7fd;
	border-radius: 4rpx;
	font-size: 24rpx;
	color: #3498db;
}

.shop-description {
	font-size: 28rpx;
	color: #333;
	line-height: 1.6;
}

.rating-section {
	background-color: #f8f9fa;
	border-radius: 16rpx;
	padding: 30rpx;
	margin-bottom: 40rpx;
}

.overall-rating {
	text-align: center;
	margin-bottom: 30rpx;
}

.rating-value {
	font-size: 48rpx;
	font-weight: bold;
	color: #f39c12;
}

.stars {
	margin: 10rpx 0;
}

.star {
	color: #ddd;
	font-size: 36rpx;
}

.star.filled {
	color: #f39c12;
}

.review-count {
	font-size: 24rpx;
	color: #666;
}

.rating-details {
	margin-bottom: 30rpx;
}

.rating-item {
	display: flex;
	align-items: center;
	margin-bottom: 20rpx;
}

.rating-label {
	width: 120rpx;
	font-size: 28rpx;
	color: #333;
}

.rating-stars {
	flex: 1;
	display: flex;
	margin: 0 20rpx;
}

.rating-score {
	font-size: 28rpx;
	color: #f39c12;
}

.rate-btn {
	width: 100%;
	height: 80rpx;
	line-height: 80rpx;
	text-align: center;
	background-color: #3498db;
	color: #fff;
	border-radius: 40rpx;
	font-size: 28rpx;
}

.rating-panel {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	z-index: 1000;
	animation: fadeIn 0.3s ease-in-out;
}

.rating-panel-content {
	background-color: #ffffff;
	border-radius: 12rpx;
	width: 80%;
	max-width: 600rpx;
	padding: 30rpx;
}

.panel-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 30rpx;
}

.panel-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
}

.close-btn {
	font-size: 40rpx;
	color: #999999;
	padding: 10rpx;
}

.panel-body {
	padding: 20rpx 0;
}

.panel-rating-item {
	display: flex;
	align-items: center;
	margin-bottom: 30rpx;
	padding: 20rpx;
	background-color: #f8f9fa;
	border-radius: 8rpx;
	transition: all 0.3s ease;
}

.panel-rating-item:hover {
	background-color: #e9ecef;
	transform: translateX(10rpx);
}

.panel-rating-label {
	width: 120rpx;
	font-size: 28rpx;
	color: #333333;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.panel-rating-stars {
	flex: 1;
	display: flex;
	gap: 10rpx;
	justify-content: center;
}

.panel-star {
	font-size: 40rpx;
	color: #ddd;
}

.panel-star.filled {
	color: #f39c12;
}

.submit-rating-btn {
	background-color: #3498db;
	color: #ffffff;
	border-radius: 8rpx;
	font-size: 28rpx;
	padding: 16rpx 0;
	margin-top: 20rpx;
}

.dish-section {
	background-color: #ffffff;
	margin-top: 20rpx;
	padding: 20rpx;
}

.section-title {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 20rpx;
}

.dish-scroll {
	width: 100%;
}

.dish-list {
	display: flex;
	gap: 20rpx;
	padding: 10rpx 0;
}

.dish-item {
	flex-shrink: 0;
	width: 200rpx;
}

.dish-image {
	width: 200rpx;
	height: 200rpx;
	border-radius: 8rpx;
}

.dish-name {
	font-size: 26rpx;
	color: #333333;
	margin-top: 10rpx;
}

.dish-price {
	font-size: 24rpx;
	color: #e74c3c;
	margin-top: 6rpx;
}

/* 评论区样式 */
.comment-section {
	margin-top: 40rpx;
}

.section-title {
	font-size: 32rpx;
	font-weight: bold;
	margin-bottom: 30rpx;
}

.comment-list {
	margin-bottom: 30rpx;
}

.no-comment {
	text-align: center;
	padding: 40rpx 0;
	color: #999;
	font-size: 28rpx;
}

.comment-item {
	margin-bottom: 30rpx;
	padding-bottom: 30rpx;
	border-bottom: 1rpx solid #eee;
}

.comment-header {
	display: flex;
	align-items: center;
	margin-bottom: 16rpx;
}

.user-avatar {
	width: 80rpx;
	height: 80rpx;
	border-radius: 50%;
	margin-right: 20rpx;
}

.comment-user-info {
	flex: 1;
}

.user-name {
	font-size: 28rpx;
	font-weight: bold;
	color: #333;
	margin-bottom: 6rpx;
	display: block;
}

.comment-rating {
	display: flex;
	align-items: center;
}

.comment-rating .star {
	font-size: 24rpx;
}

.rating-text {
	font-size: 24rpx;
	color: #f39c12;
	margin-left: 10rpx;
}

.comment-time {
	font-size: 24rpx;
	color: #999;
}

.comment-content {
	font-size: 28rpx;
	color: #333;
	line-height: 1.6;
	margin-bottom: 16rpx;
	display: block;
}

.comment-footer {
	display: flex;
	align-items: center;
}

.like-btn {
	display: flex;
	align-items: center;
	font-size: 24rpx;
	color: #666;
	margin-right: 30rpx;
}

.like-icon {
	margin-right: 6rpx;
}

.like-count {
	font-size: 24rpx;
}

.like-btn.liked {
	color: #e74c3c;
}

.like-btn.liked .like-icon {
	color: #e74c3c;
}

.delete-btn {
	display: flex;
	align-items: center;
	font-size: 24rpx;
	color: #666;
}

.delete-icon {
	margin-right: 6rpx;
}

.comment-input-box {
	display: flex;
	align-items: center;
	background-color: #f8f9fa;
	border-radius: 40rpx;
	padding: 10rpx 20rpx;
}

.comment-input-box.expanded {
	background-color: #fff;
	border: 1rpx solid #eee;
	border-radius: 12rpx;
	padding: 20rpx;
}

.input-wrapper {
	flex: 1;
}

.comment-textarea {
	width: 100%;
	min-height: 120rpx;
	font-size: 28rpx;
	line-height: 1.5;
}

.submit-btn {
	background-color: #3498db;
	color: #ffffff;
	border-radius: 40rpx;
	font-size: 28rpx;
	padding: 10rpx 30rpx;
	margin-left: 20rpx;
}
.rating-panel {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.rating-panel-content {
    background-color: #ffffff;
    border-radius: 12rpx;
    width: 80%;
    max-width: 600rpx;
    padding: 30rpx;
}

.panel-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30rpx;
}

.panel-title {
    font-size: 32rpx;
    font-weight: bold;
    color: #333333;
}

.close-btn {
    font-size: 40rpx;
    color: #999999;
    padding: 10rpx;
}

.panel-body {
    padding: 20rpx 0;
}

.panel-rating-item {
    display: flex;
    align-items: center;
    margin-bottom: 30rpx;
}

.panel-rating-label {
    width: 120rpx;
    font-size: 28rpx;
    color: #333333;
}

.panel-rating-stars {
    flex: 1;
    display: flex;
    justify-content: center;
    gap: 10rpx;
}

.panel-star {
    font-size: 40rpx;
    color: #ddd;
}

.panel-star.filled {
    color: #f39c12;
}

.submit-rating-btn {
    background-color: #3498db;
    color: #ffffff;
    border-radius: 40rpx;
    font-size: 28rpx;
    padding: 16rpx 0;
    margin-top: 20rpx;
}
</style>

<script>
export default {
	data() {
		return {
			shopId: null,
			canteenId: null,
			showRating: false,
			newComment: '',
			isCommentExpanded: false,
			isLiking: false,
			isLoading: true,
			userRating: {
				taste: 0,
				price: 0,
				hygiene: 0
			},
			shop: {
				name: '加载中...',
				image: '',
				rating: 0,
				tasteRating: 0,
				priceRating: 0,
				hygieneRating: 0,
				reviewCount: 0,
				dishes: [],
				tags: [],
				averagePrice: 0,
				monthlySales: 0
			},
			comments: []
		}
	},
	onLoad(options) {
		console.log('店铺详情页面加载，参数:', options);
		
		if (options.shopId) {
			this.shopId = parseInt(options.shopId);
			this.canteenId = options.canteenId ? parseInt(options.canteenId) : null;
			this.getShopDetail();
		} else {
			uni.showToast({
				title: '店铺ID不存在',
				icon: 'none'
			});
			setTimeout(() => {
				this.goBack();
			}, 1500);
		}
	},
	methods: {
		goBack() {
			console.log('返回上一页');
			const pages = getCurrentPages();
			console.log('当前页面栈:', pages.length);
			
			if (pages.length <= 1) {
				// 如果当前是第一个页面，直接跳转到食堂列表页
				console.log('尝试跳转到食堂列表页');
				uni.switchTab({
					url: '/pages/canteen/index',
					success: function() {
						console.log('跳转成功');
					},
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
				console.log('尝试返回上一页');
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
		showRatingPanel() {
			this.showRating = true;
		},
		hideRatingPanel() {
			this.showRating = false;
			this.userRating = {
				taste: 0,
				price: 0,
				hygiene: 0
			};
		},
		submitRating() {
			// 确保至少有一项评分不为0
			if (this.userRating.taste === 0 && this.userRating.price === 0 && this.userRating.hygiene === 0) {
				uni.showToast({
					title: '请至少评分一项',
					icon: 'none'
				});
				return;
			}
			
			// 计算平均分时，只计算非0项
			let totalScore = 0;
			let validItems = 0;
			
			if (this.userRating.taste > 0) {
				totalScore += this.userRating.taste;
				validItems++;
			}
			
			if (this.userRating.price > 0) {
				totalScore += this.userRating.price;
				validItems++;
			}
			
			if (this.userRating.hygiene > 0) {
				totalScore += this.userRating.hygiene;
				validItems++;
			}
			
			// 计算平均分 - 即使所有项都是1星也能正常计算
			const avgRating = validItems > 0 ? Number((totalScore / validItems).toFixed(1)) : 0;
			
			console.log('提交评分:', this.userRating, '平均分:', avgRating);
			
			// 使用精确计算更新评分
			const newCount = this.shop.reviewCount + 1;
			
			// 更新各项评分 - 确保1星评分也能正常更新
			if (this.userRating.taste > 0) {
				this.shop.tasteRating = Number(((this.shop.tasteRating * this.shop.reviewCount + this.userRating.taste) / newCount).toFixed(1));
			}
			
			if (this.userRating.price > 0) {
				this.shop.priceRating = Number(((this.shop.priceRating * this.shop.reviewCount + this.userRating.price) / newCount).toFixed(1));
			}
			
			if (this.userRating.hygiene > 0) {
				this.shop.hygieneRating = Number(((this.shop.hygieneRating * this.shop.reviewCount + this.userRating.hygiene) / newCount).toFixed(1));
			}
			
			// 更新总评分
			this.shop.rating = Number(((this.shop.rating * this.shop.reviewCount + avgRating) / newCount).toFixed(1));
			this.shop.reviewCount = newCount;
			
			uni.showToast({
				title: '评分成功',
				icon: 'success'
			});
			
			this.hideRatingPanel();
		},
		async getShopDetail() {
			try {
				console.log('获取店铺ID:', this.shopId);
				this.isLoading = true;
				
				// 模拟店铺数据
				const shopsData = {
				101: {
					id: 101,
					name: '南洋八打',
					image: '/static/shops/nanyang.jpg',
					rating: 4.6,
					tasteRating: 4.7,
					priceRating: 4.3,  // 修改：environmentRating -> priceRating
					hygieneRating: 4.5, // 修改：serviceRating -> hygieneRating
					reviewCount: 86,
					averagePrice: 28,
					monthlySales: 1200,
					tags: ['东南亚', '咖喱', '海南鸡饭'],
					dishes: [
						{
							id: 1,
							name: '海南鸡饭',
							price: 25,
							image: '/static/dishes/hainanchicken.jpg'
						},
						{
							id: 2,
							name: '咖喱鸡',
							price: 28,
							image: '/static/dishes/currychicken.jpg'
						},
						{
							id: 3,
							name: '椰浆饭',
							price: 22,
							image: '/static/dishes/coconutrice.jpg'
						}
					]
				},
				102: {
					id: 102,
					name: '隆江猪脚饭',
					image: '/static/shops/longjiang.jpg',
					rating: 4.7,
					tasteRating: 4.8,
					priceRating: 4.5,  // 修改：environmentRating -> priceRating
					hygieneRating: 4.6, // 修改：serviceRating -> hygieneRating
					reviewCount: 124,
					averagePrice: 32,
					monthlySales: 1500,
					tags: ['粤式', '猪脚', '烧腊'],
					dishes: [
						{
							id: 1,
							name: '招牌猪脚饭',
							price: 32,
							image: '/static/dishes/pigfoot.jpg'
						},
						{
							id: 2,
							name: '叉烧饭',
							price: 30,
							image: '/static/dishes/charsiu.jpg'
						},
						{
							id: 3,
							name: '烧鸭饭',
							price: 30,
							image: '/static/dishes/roastduck.jpg'
						}
					]
				}
			};
            // 模拟网络延迟
            await new Promise(resolve => setTimeout(resolve, 500));
            
            // 获取店铺详情数据
            const shopDetail = shopsData[this.shopId];
            if (shopDetail) {
                this.shop = {...shopDetail};
                this.isLoading = false;
                
                // 模拟评论数据
                const commentsData = {
                    101: [
                        {
                            id: 1,
                            userName: '美食达人',
                            userAvatar: '/static/images/avatars/user1.jpg',
                            rating: 4.5,
                            content: '海南鸡饭非常正宗，鸡肉嫩滑多汁，配上特制的酱料简直绝配！店内环境也很干净，服务态度好。',
                            time: '2023-05-15',
                            likeCount: 12,
                            isLiked: false
                        },
                        {
                            id: 2,
                            userName: '小吃货',
                            userAvatar: '/static/images/avatars/user2.jpg',
                            rating: 5.0,
                            content: '咖喱鸡超级好吃，香料味道浓郁但不辣，很适合不能吃辣的人。价格也很实惠，一个人吃刚刚好。',
                            time: '2023-05-10',
                            likeCount: 8,
                            isLiked: false
                        }
                    ],
                    102: [
                        {
                            id: 1,
                            userName: '肉食主义',
                            userAvatar: '/static/images/avatars/user3.jpg',
                            rating: 4.8,
                            content: '猪脚饭真的太香了！猪脚软烂入味，配上卤汁拌饭简直绝了。每次来都必点，强烈推荐！',
                            time: '2023-05-18',
                            likeCount: 15,
                            isLiked: false
                        }
                    ]
                };
            
            // 设置评论数据
            this.comments = commentsData[this.shopId] || [];
            console.log('评论数据加载完成:', this.comments);
            } else {
                throw new Error('店铺不存在');
            }
        } catch (error) {
            console.error('获取店铺详情失败:', error);
            this.isLoading = false;
            uni.showToast({
                title: error.message || '获取店铺信息失败',
                icon: 'none'
            });
            setTimeout(() => {
                this.goBack();
            }, 1500);
        }
        },
        
        // 添加其他必要的方法
        expandCommentInput() {
            this.isCommentExpanded = true;
        },
        
        submitComment() {
            if (!this.newComment.trim()) {
                uni.showToast({
                    title: '评论内容不能为空',
                    icon: 'none'
                });
                return;
            }
            
            const newComment = {
                id: Date.now(),
                userName: '我',
                userAvatar: '/static/images/avatars/default.jpg',
                rating: 5.0,
                content: this.newComment,
                time: new Date().toISOString().split('T')[0],
                likeCount: 0,
                isLiked: false
            };
            
            this.comments.unshift(newComment);
            this.newComment = '';
            this.isCommentExpanded = false;
            
            uni.showToast({
                title: '评论成功',
                icon: 'success'
            });
        },
        
        toggleLike(index) {
            if (this.isLiking) return;
            this.isLiking = true;
            
            const comment = this.comments[index];
            if (comment.isLiked) {
                comment.likeCount--;
            } else {
                comment.likeCount++;
            }
            comment.isLiked = !comment.isLiked;
            
            setTimeout(() => {
                this.isLiking = false;
            }, 300);
        },
        
        confirmDeleteComment(index) {
            uni.showModal({
                title: '确认删除',
                content: '确定要删除这条评论吗？',
                success: (res) => {
                    if (res.confirm) {
                        this.comments.splice(index, 1);
                        uni.showToast({
                            title: '删除成功',
                            icon: 'success'
                        });
                    }
                }
            });
        }
    }
}
</script>
