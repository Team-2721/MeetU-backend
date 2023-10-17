from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import serializers, schemata
from .permissions import IsLogOut
from .serializers import RegisterSerializer

#회원가입

class RegisterUserView(APIView):
    
    @swagger_auto_schema(tags=["회원가입 (users/register)"], operation_id="register")

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["내 정보 확인 (users/me)"], operation_id="my profile")
    def get(self, request):
        user = request.user

        serializer = serializers.MeSerializer(user, context={"request": request})

        return Response(
            {"ok": True, "data": serializer.data}, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        tags=["회원정보 수정 (users/me/update)"],
        request_body=schemata.login_schema,
        operation_id="update my profile",
    )
    #수정
    def patch(self, request):
        user = request.user
        serializer = serializers.MeSerializer(user, data=request.data, partial=True)
        #serializer = MeSerializer(user, data=request.data, partial=True)  # partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "data": serializer.data})
        
        return Response({"ok": False, "detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        tags=["회원정보 탈퇴 (users/me/delete)"],
        request_body=schemata.login_schema,
        operation_id="delete my profile",
    )
    #삭제
    def delete(self, request):
        user = request.user
        user.delete()

        return Response({"ok": True}, status=status.HTTP_200_OK)


class LoginView(APIView):
    permission_classes = [IsLogOut]

    @swagger_auto_schema(
        tags=["로그인 (users/login)"],
        request_body=schemata.login_schema,
        operation_id="user login",
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"ok": False, "detail": "username 혹은 password을 입력해 주세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user_model = get_user_model()
            user = user_model.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return Response({"ok": True, "detail": "로그인 되었습니다."})
            else:
                # 비밀번호가 틀린 경우
                return Response(
                    {"ok": False, "detail": "잘못된 회원 정보입니다."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            # 존재하지 않는 회원인 경우
            return Response(
                {"ok": False, "detail": "잘못된 회원 정보입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(tags=["로그아웃 (users/logout)"], operation_id="user logout")
    def post(self, request):
        logout(request)
        return Response({"ok": True})
    
class UpdateMeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        tags=["회원정보 수정 (users/update)"],
        request_body=schemata.login_schema,
        operation_id="update my profile",
    )
    #수정
    def patch(self, request):
        user = request.user
        serializer = serializers.MeSerializer(user, data=request.data, partial=True)
        #serializer = MeSerializer(user, data=request.data, partial=True)  # partial=True to update a data partially

        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "data": serializer.data})
        
        return Response({"ok": False, "detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        tags=["회원정보 탈퇴 (users/delete)"],
        request_body=schemata.login_schema,
        operation_id="delete my profile",
    )
    #삭제
    def delete(self, request):
        user = request.user
        user.delete()

        return Response({"ok": True}, status=status.HTTP_200_OK)
    