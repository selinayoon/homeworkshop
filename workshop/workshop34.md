## workshop34

# REST API

1.일반적인 REST API에서 게시글(Post)에 대한 각각의 CRUD에 대응되는 HTTP methods
와 Url을 작성하시오.

| CRUD                | HTTP methods | url               |
| ------------------- | ------------ | ----------------- |
| 리소스의 목록       | GET          | `posts/`          |
| 리소스생성          | POST         | `posts/`          |
| 리소스 중 하나 표시 | GET          | `posts/<int:id>/` |
| 리소스 수정         | PUT          | `posts/<int:id>/` |
| 리소스 삭제         | DELETE       | `posts/<int:id>/` |

