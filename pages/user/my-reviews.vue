
<template>
	<view class="container">
		<view class="top-header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="page-title">我的评价</text>
		</view>
		
		<view class="review-list">
			<template v-if="loading">
				<view class="loading">加载中...</view>
			</template>
			<template v-else-if="reviews.length === 0">
				<view class="empty">暂无评价记录</view>
			</template>
			<template v-else>
				<view class="review-item" v-for="(item, index) in reviews" :key="index" @click="viewDetail(item)">
					<view class="review-header">
						<text class="review-type">{{getTypeName(item.type)}}</text>
						<text class="review-time">{{item.time}}</text>
					</view>
					<view class="review-target">{{item.targetName}}</view>
					<view class="review-rating">
						<view class="rating-stars">
							<text v-for="n in 5" :key="n" :class="['star', n <= item.rating ? 'active' : '']">★</text>
						</view>
						<text class="rating-value">{{item.rating.toFixed(1)}}</text>
					</view>
					<view class="review-content">{{item.content}}</view>
				</view>
			</template>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			loading: true,
			reviews: []
		}
	},
	onLoad() {
		this.loadReviews();
	},
	methods: {
		goBack() {
			uni.navigateBack();
		},
		loadReviews() {
			// 模拟加载数据
			setTimeout(() => {
				this.reviews = [
					{
						id: 1,
						type: 'course',
						targetId: 'c001',
						targetName: '数据结构与算法',
						rating: 4.5,
						content: '老师讲解清晰，课程内容丰富，作业难度适中，推荐选修！',
						time: '2023-11-15'
					},
					{
						id: 2,
						type: 'canteen',
						targetId: 'f001',
						targetName: '学生食堂一楼',
						rating: 3.5,
						content: '价格实惠，但是菜品种类较少，高峰期排队时间长。',
						time: '2023-11-10'
					},
					{
						id: 3,
						type: 'housing',
						targetId: 'h001',
						targetName: '华发首府',
						rating: 4.8,
						content: '环境很好，交通便利，房间宽敞明亮，物业服务到位，就是价格有点贵。',
						time: '2023-11-05'
					},
					{
						id: 4,
						type: 'course',
						targetId: 'c002',
						targetName: '计算机网络',
						rating: 4.0,
						content: '课程内容实用，但是实验环节有些复杂，需要花费较多时间。',
						time: '2023-10-28'
					}
				];
				this.loading = false;
			}, 800);
		},
		getTypeName(type) {
			const typeMap = {
				'course': '课程评价',
				'canteen': '美食评价',
				'housing': '租房评价'
			};
			return typeMap[type] || '未知类型';
		},
		viewDetail(item) {
			// 根据不同类型跳转到不同详情页
			let url = '';
			switch(item.type) {
				case 'course':
					url = `/pages/course/course-detail?id=${item.targetId}`;
					break;
				case 'canteen':
					url = `/pages/canteen/shop-detail?id=${item.targetId}`;
					break;
				case 'housing':
					url = `/pages/housing/house-detail?id=${item.targetId}`;
					break;
				default:
					return;
			}
			
			uni.navigateTo({
				url: url
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

.review-list {
	padding: 20rpx;
}

.review-item {
	background-color: #ffffff;
	border-radius: 12rpx;
	margin-bottom: 20rpx;
	padding: 20rpx;
	box-shadow: 0 2rpx 10rpx rgba(0,0,0,0.1);
}

.review-header {
	display: flex;
	justify-content: space-between;
	margin-bottom: 10rpx;
}

.review-type {
	font-size: 24rpx;
	color: #3498db;
	background-color: rgba(52, 152, 219, 0.1);
	padding: 4rpx 12rpx;
	border-radius: 20rpx;
}

.review-time {
	font-size: 24rpx;
	color: #999999;
}

.review-target {
	font-size: 32rpx;
	font-weight: bold;
	color: #333333;
	margin-bottom: 10rpx;
}

.review-rating {
	display: flex;
	align-items: center;
	margin-bottom: 10rpx;
}

.rating-stars {
	display: flex;
	margin-right: 10rpx;
}

.star {
	color: #dddddd;
	font-size: 28rpx;
}

.star.active {
	color: #f39c12;
}

.rating-value {
	font-size: 28rpx;
	color: #f39c12;
	font-weight: bold;
}

.review-content {
	font-size: 28rpx;
	color: #666666;
	line-height: 1.5;
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
</style>