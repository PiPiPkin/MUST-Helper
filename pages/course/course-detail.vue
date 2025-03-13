<template>
	<view class="container">
		<!-- 顶部导航栏 -->
		<view class="header">
			<view class="back-btn" @click="goBack">
				<text>←</text>
			</view>
			<text class="header-title">{{course.name || '课程详情'}}</text>
		</view>
		
		<!-- 课程信息 -->
		<view class="course-info">
			<view class="course-header">
				<text class="course-name">{{course.name || '加载中...'}}</text>
				<text class="course-code">{{course.code || ''}}</text>
			</view>
			<text class="course-credits" v-if="course.credits">{{course.credits}}学分</text>
			<text class="course-description">{{course.description || '暂无描述'}}</text>
		</view>
		
		<!-- 评分区 -->
		<view class="rating-section">
			<view class="overall-rating">
				<text class="rating-value">{{course.rating ? course.rating.toFixed(1) : '0.0'}}</text>
				<view class="stars">
					<text v-for="n in 5" :key="n" class="star" 
						  :class="{ 'filled': n <= Math.round(course.rating || 0) }">★</text>
				</view>
				<text class="review-count">{{course.reviewCount || 0}}人评价</text>
			</view>
			
			<view class="rating-details">
				<view class="rating-item">
					<text class="rating-label">容易度</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(course.difficultyRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{course.difficultyRating ? course.difficultyRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">收获</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(course.harvestRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{course.harvestRating ? course.harvestRating.toFixed(1) : '0.0'}}</text>
				</view>
				<view class="rating-item">
					<text class="rating-label">拿分</text>
					<view class="rating-stars">
						<text v-for="n in 5" :key="n" class="star" 
							  :class="{ 'filled': n <= Math.round(course.scoreRating || 0) }">★</text>
					</view>
					<text class="rating-score">{{course.scoreRating ? course.scoreRating.toFixed(1) : '0.0'}}</text>
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
							   placeholder="分享你的课程体验、学习方法、考试技巧..."
							   :focus="isCommentExpanded"
							   auto-height></textarea>
					<input v-else 
							type="text" 
							placeholder="分享你的课程体验、学习方法、考试技巧..." 
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
						<text class="panel-rating-label">容易度</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.difficulty }"
								  @click="userRating.difficulty = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">收获</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.harvest }"
								  @click="userRating.harvest = n">★</text>
						</view>
					</view>
					<view class="panel-rating-item">
						<text class="panel-rating-label">拿分</text>
						<view class="panel-rating-stars">
							<text v-for="n in 5" :key="n" class="panel-star" 
								  :class="{ 'filled': n <= userRating.score }"
								  @click="userRating.score = n">★</text>
						</view>
					</view>
				</view>
				
				<button class="submit-rating-btn" @click="submitRating">提交评分</button>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	beforeCreate() {
		// 在组件实例创建之前就定义这个方法
		this.getFlowerSentData = function() {
			console.log('送花功能已禁用');
			return Promise.resolve({});
		};
	},
	data() {
		return {
			courseId: null,
			showRating: false,
			newComment: '',
			isCommentExpanded: false,
			isLiking: false,
			userRating: {
				difficulty: 0,
				harvest: 0,
				score: 0
			},
			course: {
				id: 0,
				code: '',
				name: '',
				credits: 0,
				rating: 0,
				difficultyRating: 0,
				harvestRating: 0,
				scoreRating: 0,
				reviewCount: 0,
				description: ''
			},
			comments: []
		}
	},
	onLoad(options) {
		console.log('课程详情页面加载，参数:', options);
		
		if (options.courseId) {
			this.courseId = parseInt(options.courseId);
			this.getCourseDetail();
		} else {
			uni.showToast({
				title: '课程ID不存在',
				icon: 'none'
			});
			setTimeout(() => {
				this.goBack();
			}, 1500);
		}
	},
	methods: {
		// 确保方法也在 methods 中定义
		getFlowerSentData() {
			console.log('送花功能已禁用');
			return Promise.resolve({});
		},
		goBack() {
			console.log('返回上一页');
			// 修改返回逻辑，确保能正确处理
			const pages = getCurrentPages();
			console.log('当前页面栈:', pages.length);
			
			if (pages.length <= 1) {
				// 如果当前是第一个页面，直接跳转到课程列表页
				console.log('尝试跳转到课程列表页');
				uni.switchTab({
					url: '/pages/course/index',
					success: function() {
						console.log('跳转成功');
					},
					fail: function(err) {
						console.error('跳转失败:', err);
						// 尝试使用 reLaunch 作为备选方案
						uni.reLaunch({
							url: '/pages/course/index'
						});
					}
				});
			} else {
				// 如果不是第一个页面，则正常返回
				console.log('尝试返回上一页');
				uni.navigateBack({
					fail: function(err) {
						console.error('返回失败:', err);
						// 如果返回失败，尝试跳转到课程列表页
						uni.switchTab({
							url: '/pages/course/index'
						});
					}
				});
			}
		},
		getCourseDetail() {
			console.log('获取课程ID:', this.courseId);
			
			const coursesData = {
				101: {
					id: 101,
					code: 'CS460',
					name: '计算机视觉',
					credits: 3,
					rating: 4.8,
					difficultyRating: 3.5,
					harvestRating: 4.7,
					scoreRating: 4.2,
					reviewCount: 56,
					description: '本科目介绍计算机视觉的基本概念，内容包括：图像生成，边缘检测，滤波，特征，光流，三维重建，物体检测，识别及跟踪。'
				},
				102: {
					id: 102,
					code: 'CS462',
					name: '机器学习',
					credits: 3,
					rating: 4.9,
					difficultyRating: 3.8,
					harvestRating: 4.9,
					scoreRating: 4.3,
					reviewCount: 78,
					description: '本课程介绍机器学习的基本概念和算法，包括监督学习、无监督学习和强化学习等内容。'
				}
			};
			
			const commentsData = {
				101: [
					{
						id: 1,
						userName: '学霸一号',
						userAvatar: '/static/images/avatars/avatar1.jpg',
						rating: 5.0,
						content: '这门课非常有趣，老师讲解清晰，实验也很有挑战性。期末考试难度适中，平时认真听课就能拿高分。',
						time: '2023-10-15',
						likeCount: 24,
						isLiked: false
					},
					{
						id: 2,
						userName: '编程爱好者',
						userAvatar: '/static/images/avatars/avatar2.jpg',
						rating: 4.5,
						content: '课程内容很丰富，但是作业量有点大，需要投入较多时间。不过学到的知识对找工作很有帮助，值得学习。',
						time: '2023-10-10',
						likeCount: 18,
						isLiked: false
					}
				],
				102: [
					{
						id: 1,
						userName: 'AI研究者',
						userAvatar: '/static/images/avatars/avatar3.jpg',
						rating: 5.0,
						content: '机器学习是AI领域的基础课程，内容非常实用。老师讲解深入浅出，作业和项目设计得很好。',
						time: '2023-10-18',
						likeCount: 32,
						isLiked: false
					}
				]
			};
			
			setTimeout(() => {
				this.course = coursesData[this.courseId] || {
					id: this.courseId,
					code: '未知课程',
					name: '未知课程',
					credits: 0,
					rating: 0,
					difficultyRating: 0,
					harvestRating: 0,
					scoreRating: 0,
					reviewCount: 0,
					description: '暂无课程描述'
				};
				
				this.comments = commentsData[this.courseId] || [];
				
				console.log('课程数据加载完成:', this.course);
			}, 500);
		},
		showRatingPanel() {
			this.showRating = true;
		},
		hideRatingPanel() {
			this.showRating = false;
		},
		submitRating() {
			if (this.userRating.difficulty === 0 || this.userRating.harvest === 0 || this.userRating.score === 0) {
				uni.showToast({
					title: '请完成所有评分项',
					icon: 'none'
				});
				return;
			}
			
			// 使用精确计算方法计算平均分
			const avgRating = Number(((this.userRating.difficulty + this.userRating.harvest + this.userRating.score) / 3).toFixed(1));
			
			console.log('提交评分:', this.userRating, '平均分:', avgRating);
			
			// 使用精确计算更新评分
			const newCount = this.course.reviewCount + 1;
			this.course.difficultyRating = Number(((this.course.difficultyRating * this.course.reviewCount + this.userRating.difficulty) / newCount).toFixed(1));
			this.course.harvestRating = Number(((this.course.harvestRating * this.course.reviewCount + this.userRating.harvest) / newCount).toFixed(1));
			this.course.scoreRating = Number(((this.course.scoreRating * this.course.reviewCount + this.userRating.score) / newCount).toFixed(1));
			this.course.rating = Number(((this.course.rating * this.course.reviewCount + avgRating) / newCount).toFixed(1));
			this.course.reviewCount = newCount;
			
			this.hideRatingPanel();
			
			uni.showToast({
				title: '评分成功',
				icon: 'success'
			});
		},
		expandCommentInput() {
			this.isCommentExpanded = true;
		},
		submitComment() {
			const content = this.newComment.trim();
			if (!content) {
				uni.showToast({
					title: '评论内容不能为空',
					icon: 'none'
				});
				return;
			}
			
			if (content.length > 500) {
				uni.showToast({
					title: '评论内容不能超过500字',
					icon: 'none'
				});
				return;
			}
			
			const newComment = {
				id: this.comments.length + 1,
				userName: '我',
				userAvatar: '/static/images/avatars/default.jpg',
				rating: 5.0,
				content: content,
				time: new Date().toISOString().split('T')[0],
				likeCount: 0,
				isLiked: false
			};
			
			this.comments.unshift(newComment);
			
			this.newComment = '';
			this.isCommentExpanded = false;
			
			uni.showModal({
				title: '感谢你的评论！',
				content: '你的分享将帮助更多同学了解这门课程。希望你在澳科保姆平台有愉快的体验！',
				showCancel: false,
				confirmText: '太棒了',
				success: () => {
					console.log('用户确认了感谢提示');
				}
			});
		},
		toggleLike(index) {
			// 防止重复点击
			if (this.isLiking) return;
			this.isLiking = true;
			
			// 切换点赞状态
			this.comments[index].isLiked = !this.comments[index].isLiked;
			
			// 更新点赞数
			if (this.comments[index].isLiked) {
				this.comments[index].likeCount++;
			} else {
				this.comments[index].likeCount--;
			}
			
			// 延迟重置点击状态
			setTimeout(() => {
				this.isLiking = false;
			}, 500);
		},
		// 添加缺失的方法
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

<style>
/* 添加缺失的基础样式 */
.container {
	padding: 30rpx;
}

.header {
	display: flex;
	align-items: center;
	margin-bottom: 30rpx;
}

.back-btn {
	width: 60rpx;
	height: 60rpx;
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 40rpx;
}

.header-title {
	flex: 1;
	text-align: center;
	font-size: 32rpx;
	font-weight: bold;
	margin-right: 60rpx;
}

.course-info {
	margin-bottom: 40rpx;
}

.course-header {
	margin-bottom: 20rpx;
}

.course-name {
	font-size: 36rpx;
	font-weight: bold;
	color: #333;
	margin-bottom: 10rpx;
	display: block;
}

.course-code {
	font-size: 28rpx;
	color: #666;
	display: block;
}

.course-credits {
	font-size: 28rpx;
	color: #666;
	margin-bottom: 20rpx;
	display: block;
}

.course-description {
	font-size: 28rpx;
	color: #333;
	line-height: 1.6;
}

/* 评分区样式 */
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

/* 补充缺失的样式 */
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

.no-comment {
	text-align: center;
	padding: 40rpx 0;
	color: #999;
	font-size: 28rpx;
}

.comment-input-box {
	display: flex;
	align-items: center;
	background-color: #f8f9fa;
	border-radius: 40rpx;
	padding: 10rpx 20rpx;
}

.comment-input-box.expanded {
	flex-direction: column;
	align-items: stretch;
}

.input-wrapper {
	flex: 1;
}

.comment-textarea {
	width: 100%;
	min-height: 120rpx;
	font-size: 28rpx;
	padding: 10rpx 0;
}

.comment-input-box input {
	height: 60rpx;
	font-size: 28rpx;
	width: 100%;
}

.submit-btn {
	width: 120rpx;
	height: 60rpx;
	line-height: 60rpx;
	text-align: center;
	background-color: #3498db;
	color: #fff;
	border-radius: 30rpx;
	font-size: 28rpx;
	margin-left: 20rpx;
}

/* 评分面板样式 */
.rating-panel {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	z-index: 999;
}

.rating-panel-content {
	width: 80%;
	background-color: #fff;
	border-radius: 16rpx;
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
}

.close-btn {
	font-size: 40rpx;
	color: #999;
}

.panel-body {
	margin-bottom: 30rpx;
}

.panel-rating-item {
	margin-bottom: 30rpx;
}

.panel-rating-label {
	font-size: 28rpx;
	color: #333;
	margin-bottom: 16rpx;
	display: block;
}

.panel-rating-stars {
	display: flex;
}

.panel-star {
	font-size: 40rpx;
	color: #ddd;
	margin-right: 10rpx;
}

.panel-star.filled {
	color: #f39c12;
}

.submit-rating-btn {
	width: 100%;
	height: 80rpx;
	line-height: 80rpx;
	text-align: center;
	background-color: #3498db;
	color: #fff;
	border-radius: 40rpx;
	font-size: 28rpx;
}
</style>