<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{shop.name || '店铺详情'}}</text>
		</view>
		
		<!-- 店铺信息 -->
		<view class="shop-info">
			<image class="shop-banner" :src="shop.image" mode="aspectFill"></image>
			<view class="shop-header">
				<text class="shop-name">{{shop.name || '加载中...'}}</text>
				<view class="shop-meta">
					<view class="rating">
						<text class="rating-value">{{shop.rating ? shop.rating.toFixed(1) : '0.0'}}</text>
						<view class="stars">
							<text v-for="n in 5" :key="n" class="star" 
								  :class="{ 'filled': n <= Math.round(shop.rating || 0) }">★</text>
						</view>
					</view>
					<text class="review-count">{{shop.reviewCount || 0}}人评价</text>
				</view>
				<view class="shop-tags">
					<text class="tag" v-for="(tag, index) in shop.tags" :key="index">{{tag}}</text>
				</view>
				<view class="shop-details">
					<text class="price">人均 ¥{{shop.averagePrice}}</text>
					<text class="monthly-sales">月售{{shop.monthlySales}}单</text>
				</view>
			</view>
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
					<text class="rating-label">口味 🍽️</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.tasteRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.tasteRating ? shop.tasteRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">价格 💰</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.priceRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.priceRating ? shop.priceRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">卫生 🧹</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(shop.hygieneRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{shop.hygieneRating ? shop.hygieneRating.toFixed(1) : '0.0'}}</text>
				</view>
			</view>
			
			<button class="rate-btn" @click="showRatingPanel">我要评分</button>
		</view>
		
		<!-- 菜品推荐 -->
		<view class="dish-section" v-if="shop.dishes && shop.dishes.length > 0">
			<view class="section-title">
				<text>招牌菜品</text>
			</view>
			<scroll-view class="dish-scroll" scroll-x>
				<view class="dish-list">
					<view class="dish-item" v-for="(dish, index) in shop.dishes" :key="index">
						<image class="dish-image" :src="dish.image" mode="aspectFill"></image>
						<text class="dish-name">{{dish.name}}</text>
						<text class="dish-price">¥{{dish.price}}</text>
					</view>
				</view>
			</scroll-view>
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
					<view class="comment-images" v-if="item.images && item.images.length > 0">
						<image v-for="(img, imgIndex) in item.images" :key="imgIndex" 
							   :src="img" mode="aspectFill" class="comment-image"
							   @click="previewImage(item.images, imgIndex)"></image>
					</view>
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
						<text class="panel-rating-label">口味 🍽️</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.taste }"
								  @click="userRating.taste = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">价格 💰</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.price }"
								  @click="userRating.price = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">卫生 🧹</text>
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
.rating-panel {
	position: fixed;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	background-color: rgba(0, 0, 0, 0.5);
	z-index: 999;
	display: flex;
	justify-content: center;
	align-items: center;
}

.rating-panel-content {
	background-color: #ffffff;
	border-radius: 16rpx;
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
	display: flex;
	flex-direction: column;
	gap: 20rpx;
}

.panel-rating-item {
	display: flex;
	align-items: center;
	gap: 20rpx;
}

.panel-rating-label {
	width: 120rpx;
	font-size: 28rpx;
	color: #666666;
}

.panel-rating-stars {
	display: flex;
	gap: 10rpx;
}

.panel-star {
	font-size: 40rpx;
	color: #dddddd;
	padding: 10rpx;
}

.panel-star.filled {
	color: #f39c12;
}

.submit-rating-btn {
	margin-top: 30rpx;
	background-color: #3498db;
	color: #ffffff;
	height: 80rpx;
	line-height: 80rpx;
	border-radius: 40rpx;
	font-size: 28rpx;
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
				dishes: []
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
			if (!this.userRating.taste || !this.userRating.price || !this.userRating.hygiene) {
				uni.showToast({
					title: '请完成所有评分项',
					icon: 'none'
				});
				return;
			}
			
			// 计算平均评分
			const avgRating = (this.userRating.taste + this.userRating.price + this.userRating.hygiene) / 3;
			
			// TODO: 发送评分到服务器
			console.log('提交评分:', this.userRating);
			
			// 更新本地显示
			this.shop.tasteRating = (this.shop.tasteRating * this.shop.reviewCount + this.userRating.taste) / (this.shop.reviewCount + 1);
			this.shop.priceRating = (this.shop.priceRating * this.shop.reviewCount + this.userRating.price) / (this.shop.reviewCount + 1);
			this.shop.hygieneRating = (this.shop.hygieneRating * this.shop.reviewCount + this.userRating.hygiene) / (this.shop.reviewCount + 1);
			this.shop.rating = (this.shop.rating * this.shop.reviewCount + avgRating) / (this.shop.reviewCount + 1);
			this.shop.reviewCount++;
			
			uni.showToast({
				title: '评分成功',
				icon: 'success'
			});
			
			this.hideRatingPanel();
		},
		getShopDetail() {
			console.log('获取店铺ID:', this.shopId);
			
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
            // 获取店铺详情数据
            const shopDetail = shopsData[this.shopId];
            if (shopDetail) {
                this.shop = shopDetail;
                
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
                uni.showToast({
                    title: '店铺不存在',
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
