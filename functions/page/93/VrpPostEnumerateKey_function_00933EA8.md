# VrpPostEnumerateKey

- RVA: `0x00933EA8`–`0x009345D1` (길이 `1,833` bytes)
- VA: `0x0000000140933EA8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008F0B4`
- 디코드: `380`개 명령, `1,833/1,833` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x00933F2C` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (function, `0x0041E720`)
- `0x00933F77` → [ExGetPreviousMode](../../text/44/ExGetPreviousMode_function_0044C3A0.md) (function, `0x0044C3A0`)
- `0x00933FDF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0093400F` → [VrpOutputBufferParameter](VrpOutputBufferParameter_function_0093461C.md) (function, `0x0093461C`)
- `0x00934038` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0093406B` → [VrpOutputBufferParameter](VrpOutputBufferParameter_function_0093461C.md) (function, `0x0093461C`)
- `0x00934119` → [VrpBuildKeyPath](VrpBuildKeyPath_function_00934650.md) (function, `0x00934650`)
- `0x0093412C` → [VrpLockJobContextShared](VrpLockJobContextShared_function_009349E8.md) (function, `0x009349E8`)
- `0x00934147` → [VrpFindExactNamespaceNode](VrpFindExactNamespaceNode_function_00934748.md) (function, `0x00934748`)
- `0x00934176` → [VrpUnlockJobContextShared](VrpUnlockJobContextShared_function_009345D8.md) (function, `0x009345D8`)
- `0x00934190` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009341D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009341EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00934209` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0093421B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009343C9` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (function, `0x0041C830`)
- `0x00934485` → [ObOpenObjectByPointer](../8B/ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x009344B3` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x009344D4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00934510` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (function, `0x006AD710`)
- `0x00934555` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009345BA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x009345C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [VrpRegistryCallback](../86/VrpRegistryCallback_function_00867450.md) at `0x008675DD`

### Static image references
- `0x00933EC2` → RVA `0x00E0A740` (`.data`; read)
- `0x00933F9A` → RVA `0x00E0A630` (`.data`; read)
- `0x00934161` → RVA `0x00002F28` (`.rdata`; read)
- `0x0093432C` → RVA `0x0005A9C5` (`.rdata`; read)
- `0x0093433C` → RVA `0x00E0A638` (`.data`; read)
- `0x00934360` → RVA `0x0005A9CF` (`.rdata`; read)
- `0x00934385` → RVA `0x0005BCFD` (`.rdata`; read)
- `0x0093438C` → RVA `0x00043590` (`.rdata`; read)
- `0x009343C2` → RVA `0x00E0A650` (`.data`; read)
- `0x00934468` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x00934561` → RVA `0x00002F30` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **16**
  - `0x00933F2C` → [EtwActivityIdControl](../../text/41/EtwActivityIdControl_function_0041E720.md) (`PAGE` → `.text`)
  - `0x00933F77` → [ExGetPreviousMode](../../text/44/ExGetPreviousMode_function_0044C3A0.md) (`PAGE` → `.text`)
  - `0x00933FDF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00934038` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00934190` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009341D8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009341EE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00934209` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0093421B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009343C9` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (`PAGE` → `.text`)
  - `0x009344B3` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x009344D4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00934510` → [ZwEnumerateKey](../../text/6A/ZwEnumerateKey_function_006AD710.md) (`PAGE` → `.text`)
  - `0x00934555` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009345BA` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x009345C7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0093414F` → [sub_00B246DA + 0x76](../B2/Unknown_function_00B246DA.md) (`tail-transfer`)
  - `0x00934595` → [sub_00B246DA](../B2/Unknown_function_00B246DA.md) (`tail-transfer`)
  - `0x009345A2` → [sub_00B246DA](../B2/Unknown_function_00B246DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00933EA8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00933EAD  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00933EB2  57                              push rdi
00933EB3  41 54                           push r12
00933EB5  41 55                           push r13
00933EB7  41 56                           push r14
00933EB9  41 57                           push r15
00933EBB  48 81 EC 00 02 00 00            sub rsp, 0x200
00933EC2  48 8B 05 77 68 4D 00            mov rax, qword ptr [rip + 0x4d6877]
00933EC9  48 33 C4                        xor rax, rsp
00933ECC  48 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rax
00933ED4  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00933ED9  48 8B F9                        mov rdi, rcx
00933EDC  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00933EE4  48 89 94 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdx
00933EEC  0F 57 C0                        xorps xmm0, xmm0
00933EEF  0F 11 84 24 B0 00 00 00         movups xmmword ptr [rsp + 0xb0], xmm0
00933EF7  0F 57 C9                        xorps xmm1, xmm1
00933EFA  0F 11 4C 24 70                  movups xmmword ptr [rsp + 0x70], xmm1
00933EFF  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
00933F07  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
00933F0F  0F 11 84 24 F8 00 00 00         movups xmmword ptr [rsp + 0xf8], xmm0
00933F17  0F 11 84 24 08 01 00 00         movups xmmword ptr [rsp + 0x108], xmm0
00933F1F  48 8D 94 24 08 01 00 00         lea rdx, [rsp + 0x108]
00933F27  B9 03 00 00 00                  mov ecx, 3
00933F2C  E8 EF A7 AE FF                  call 0x14041e720
00933F31  33 DB                           xor ebx, ebx
00933F33  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
00933F3B  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00933F3F  4C 8B 7F 28                     mov r15, qword ptr [rdi + 0x28]
00933F43  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
00933F4B  4C 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r15
00933F53  48 89 9C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rbx
00933F5B  48 8B 77 10                     mov rsi, qword ptr [rdi + 0x10]
00933F5F  48 89 B4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rsi
00933F67  44 8B F3                        mov r14d, ebx
00933F6A  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
00933F6F  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
00933F77  E8 24 84 B1 FF                  call 0x14044c3a0
00933F7C  44 8A C0                        mov r8b, al
00933F7F  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00933F83  89 5C 24 5C                     mov dword ptr [rsp + 0x5c], ebx
00933F87  44 8B EB                        mov r13d, ebx
00933F8A  48 89 5C 24 68                  mov qword ptr [rsp + 0x68], rbx
00933F8F  8B 7F 08                        mov edi, dword ptr [rdi + 8]
00933F92  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
00933F9A  83 3D 8F 66 4D 00 05            cmp dword ptr [rip + 0x4d668f], 5
00933FA1  0F 87 C6 05 00 00               ja 0x14093456d
00933FA7  41 BC 05 00 00 80               mov r12d, 0x80000005
00933FAD  85 FF                           test edi, edi
00933FAF  0F 88 28 04 00 00               js 0x1409343dd
00933FB5  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00933FB8  48 8B 56 10                     mov rdx, qword ptr [rsi + 0x10]
00933FBC  48 8B CB                        mov rcx, rbx
00933FBF  8B FB                           mov edi, ebx
00933FC1  41 BF 56 52 65 67               mov r15d, 0x67655256
00933FC7  41 80 F8 01                     cmp r8b, 1
00933FCB  0F 85 49 04 00 00               jne 0x14093441a
00933FD1  85 C0                           test eax, eax
00933FD3  74 1B                           je 0x140933ff0
00933FD5  8B D0                           mov edx, eax
00933FD7  45 8B C7                        mov r8d, r15d
00933FDA  B9 00 01 00 00                  mov ecx, 0x100
00933FDF  E8 0C E1 24 00                  call 0x140b820f0
00933FE4  48 8B C8                        mov rcx, rax
00933FE7  48 85 C0                        test rax, rax
00933FEA  0F 84 3E 05 00 00               je 0x14093452e
00933FF0  48 8B C1                        mov rax, rcx
00933FF3  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00933FF8  85 FF                           test edi, edi
00933FFA  0F 88 57 01 00 00               js 0x140934157
00934000  4C 8D 4E 10                     lea r9, [rsi + 0x10]
00934004  44 8B 46 18                     mov r8d, dword ptr [rsi + 0x18]
00934008  48 8B D0                        mov rdx, rax
0093400B  8A 4C 24 40                     mov cl, byte ptr [rsp + 0x40]
0093400F  E8 08 06 00 00                  call 0x14093461c
00934014  8B F8                           mov edi, eax
00934016  85 C0                           test eax, eax
00934018  0F 88 39 01 00 00               js 0x140934157
0093401E  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
00934022  8B FB                           mov edi, ebx
00934024  80 7C 24 40 01                  cmp byte ptr [rsp + 0x40], 1
00934029  75 1B                           jne 0x140934046
0093402B  45 8B C7                        mov r8d, r15d
0093402E  BA 04 00 00 00                  mov edx, 4
00934033  B9 00 01 00 00                  mov ecx, 0x100
00934038  E8 B3 E0 24 00                  call 0x140b820f0
0093403D  48 85 C0                        test rax, rax
00934040  0F 84 F5 04 00 00               je 0x14093453b
00934046  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0093404B  4C 8B E8                        mov r13, rax
0093404E  85 FF                           test edi, edi
00934050  0F 88 01 01 00 00               js 0x140934157
00934056  4C 8D 4E 20                     lea r9, [rsi + 0x20]
0093405A  41 B8 04 00 00 00               mov r8d, 4
00934060  49 8B D5                        mov rdx, r13
00934063  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
00934068  41 8A CD                        mov cl, r13b
0093406B  E8 AC 05 00 00                  call 0x14093461c
00934070  8B F8                           mov edi, eax
00934072  85 C0                           test eax, eax
00934074  0F 88 59 03 00 00               js 0x1409343d3
0093407A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00934082  41 80 FD 01                     cmp r13b, 1
00934086  75 25                           jne 0x1409340ad
00934088  39 59 08                        cmp dword ptr [rcx + 8], ebx
0093408B  7C 20                           jl 0x1409340ad
0093408D  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00934090  85 C0                           test eax, eax
00934092  0F 85 65 03 00 00               jne 0x1409343fd
00934098  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0093409B  83 E8 10                        sub eax, 0x10
0093409E  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009340A3  41 39 46 0C                     cmp dword ptr [r14 + 0xc], eax
009340A7  0F 87 B4 00 00 00               ja 0x140934161
009340AD  8B 41 08                        mov eax, dword ptr [rcx + 8]
009340B0  41 BE 23 00 00 C0               mov r14d, 0xc0000023
009340B6  41 3B C6                        cmp eax, r14d
009340B9  0F 84 97 03 00 00               je 0x140934456
009340BF  41 3B C4                        cmp eax, r12d
009340C2  0F 84 8E 03 00 00               je 0x140934456
009340C8  83 7E 0C 02                     cmp dword ptr [rsi + 0xc], 2
009340CC  0F 84 84 03 00 00               je 0x140934456
009340D2  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009340D7  41 BD 00 00 00 80               mov r13d, 0x80000000
009340DD  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
009340E0  85 C0                           test eax, eax
009340E2  0F 85 3F 03 00 00               jne 0x140934427
009340E8  41 0F B7 46 0C                  movzx eax, word ptr [r14 + 0xc]
009340ED  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
009340F2  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
009340F7  49 8D 46 10                     lea rax, [r14 + 0x10]
009340FB  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00934100  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00934108  48 83 C1 10                     add rcx, 0x10
0093410C  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
00934114  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00934119  E8 32 05 00 00                  call 0x140934650
0093411E  8B F8                           mov edi, eax
00934120  85 C0                           test eax, eax
00934122  78 33                           js 0x140934157
00934124  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
00934129  48 8B CF                        mov rcx, rdi
0093412C  E8 B7 08 00 00                  call 0x1409349e8
00934131  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
00934139  45 33 C0                        xor r8d, r8d
0093413C  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
00934144  48 8B CF                        mov rcx, rdi
00934147  E8 FC 05 00 00                  call 0x140934748
0093414C  48 85 C0                        test rax, rax
0093414F  0F 85 FB 05 1F 00               jne 0x140b24750
00934155  8B FB                           mov edi, ebx
00934157  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
0093415C  44 8A 6C 24 40                  mov r13b, byte ptr [rsp + 0x40]
00934161  4C 8D 25 C0 ED 6C FF            lea r12, [rip - 0x931240]
00934168  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
0093416D  39 5C 24 58                     cmp dword ptr [rsp + 0x58], ebx
00934171  74 08                           je 0x14093417b
00934173  48 8B C8                        mov rcx, rax
00934176  E8 5D 04 00 00                  call 0x1409345d8
0093417B  85 FF                           test edi, edi
0093417D  0F 88 BB 00 00 00               js 0x14093423e
00934183  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
0093418B  48 85 C9                        test rcx, rcx
0093418E  74 05                           je 0x140934195
00934190  E8 1B 91 D7 FF                  call 0x1406ad2b0
00934195  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0093419D  48 85 C9                        test rcx, rcx
009341A0  0F 85 14 04 00 00               jne 0x1409345ba
009341A6  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
009341AE  48 85 C9                        test rcx, rcx
009341B1  0F 85 0D 04 00 00               jne 0x1409345c4
009341B7  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009341BF  48 85 C0                        test rax, rax
009341C2  0F 85 87 03 00 00               jne 0x14093454f
009341C8  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009341D0  48 85 C9                        test rcx, rcx
009341D3  74 08                           je 0x1409341dd
009341D5  41 8B D7                        mov edx, r15d
009341D8  E8 93 E6 24 00                  call 0x140b82870
009341DD  41 80 FD 01                     cmp r13b, 1
009341E1  75 2B                           jne 0x14093420e
009341E3  4D 85 F6                        test r14, r14
009341E6  74 0B                           je 0x1409341f3
009341E8  41 8B D7                        mov edx, r15d
009341EB  49 8B CE                        mov rcx, r14
009341EE  E8 7D E6 24 00                  call 0x140b82870
009341F3  41 80 FD 01                     cmp r13b, 1
009341F7  75 15                           jne 0x14093420e
009341F9  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
009341FE  48 85 C0                        test rax, rax
00934201  74 0B                           je 0x14093420e
00934203  41 8B D7                        mov edx, r15d
00934206  48 8B C8                        mov rcx, rax
00934209  E8 62 E6 24 00                  call 0x140b82870
0093420E  8B C7                           mov eax, edi
00934210  48 8B 8C 24 F0 01 00 00         mov rcx, qword ptr [rsp + 0x1f0]
00934218  48 33 CC                        xor rcx, rsp
0093421B  E8 20 84 D7 FF                  call 0x1406ac640
00934220  4C 8D 9C 24 00 02 00 00         lea r11, [rsp + 0x200]
00934228  49 8B 5B 40                     mov rbx, qword ptr [r11 + 0x40]
0093422C  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00934230  49 8B E3                        mov rsp, r11
00934233  41 5F                           pop r15
00934235  41 5E                           pop r14
00934237  41 5D                           pop r13
00934239  41 5C                           pop r12
0093423B  5F                              pop rdi
0093423C  C3                              ret
0093423D  CC                              int3
0093423E  83 3D EB 63 4D 00 02            cmp dword ptr [rip + 0x4d63eb], 2
00934245  0F 86 38 FF FF FF               jbe 0x140934183
0093424B  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
0093424E  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00934252  48 8D 44 24 64                  lea rax, [rsp + 0x64]
00934257  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0093425F  48 C7 84 24 48 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x148], 4
0093426B  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
00934273  48 39 58 18                     cmp qword ptr [rax + 0x18], rbx
00934277  0F 85 34 03 00 00               jne 0x1409345b1
0093427D  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00934282  49 8B 44 24 08                  mov rax, qword ptr [r12 + 8]
00934287  48 8D 94 24 68 01 00 00         lea rdx, [rsp + 0x168]
0093428F  48 89 94 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdx
00934297  48 C7 84 24 58 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x158], 2
009342A3  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009342AB  89 8C 24 68 01 00 00            mov dword ptr [rsp + 0x168], ecx
009342B2  89 9C 24 6C 01 00 00            mov dword ptr [rsp + 0x16c], ebx
009342B9  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009342C1  48 85 C9                        test rcx, rcx
009342C4  0F 84 95 02 00 00               je 0x14093455f
009342CA  0F B7 84 24 B0 00 00 00         movzx eax, word ptr [rsp + 0xb0]
009342D2  0F B7 C0                        movzx eax, ax
009342D5  48 8D 94 24 88 01 00 00         lea rdx, [rsp + 0x188]
009342DD  48 89 94 24 70 01 00 00         mov qword ptr [rsp + 0x170], rdx
009342E5  48 C7 84 24 78 01 00 00 02 00 00 00  mov qword ptr [rsp + 0x178], 2
009342F1  48 89 8C 24 80 01 00 00         mov qword ptr [rsp + 0x180], rcx
009342F9  89 84 24 88 01 00 00            mov dword ptr [rsp + 0x188], eax
00934300  89 9C 24 8C 01 00 00            mov dword ptr [rsp + 0x18c], ebx
00934307  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
0093430B  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00934310  48 89 84 24 90 01 00 00         mov qword ptr [rsp + 0x190], rax
00934318  48 C7 84 24 98 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x198], 4
00934324  C7 44 24 70 00 00 00 0B         mov dword ptr [rsp + 0x70], 0xb000000
0093432C  0F B7 05 92 66 72 FF            movzx eax, word ptr [rip - 0x8d996e]
00934333  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
00934337  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
0093433C  48 8B 05 F5 62 4D 00            mov rax, qword ptr [rip + 0x4d62f5]
00934343  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
0093434B  0F B7 00                        movzx eax, word ptr [rax]
0093434E  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
00934355  C7 84 24 2C 01 00 00 02 00 00 00  mov dword ptr [rsp + 0x12c], 2
00934360  48 8D 05 68 66 72 FF            lea rax, [rip - 0x8d9998]
00934367  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
0093436F  C7 84 24 38 01 00 00 74 00 00 00  mov dword ptr [rsp + 0x138], 0x74
0093437A  C7 84 24 3C 01 00 00 01 00 00 00  mov dword ptr [rsp + 0x13c], 1
00934385  48 8D 05 71 79 72 FF            lea rax, [rip - 0x8d868f]
0093438C  48 8D 0D FD F1 70 FF            lea rcx, [rip - 0x8f0e03]
00934393  2B C1                           sub eax, ecx
00934395  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00934399  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
0093439D  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
009343A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009343AA  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
009343B2  45 33 C9                        xor r9d, r9d
009343B5  4C 8D 84 24 08 01 00 00         lea r8, [rsp + 0x108]
009343BD  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
009343C2  48 8B 0D 87 62 4D 00            mov rcx, qword ptr [rip + 0x4d6287]
009343C9  E8 62 84 AE FF                  call 0x14041c830
009343CE  E9 B0 FD FF FF                  jmp 0x140934183
009343D3  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
009343D8  E9 84 FD FF FF                  jmp 0x140934161
009343DD  81 FF 23 00 00 C0               cmp edi, 0xc0000023
009343E3  0F 84 CC FB FF FF               je 0x140933fb5
009343E9  41 3B FC                        cmp edi, r12d
009343EC  0F 84 C3 FB FF FF               je 0x140933fb5
009343F2  41 BF 56 52 65 67               mov r15d, 0x67655256
009343F8  E9 5F FD FF FF                  jmp 0x14093415c
009343FD  83 F8 01                        cmp eax, 1
00934400  0F 85 A7 FC FF FF               jne 0x1409340ad
00934406  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
00934409  83 E8 18                        sub eax, 0x18
0093440C  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00934411  41 39 46 14                     cmp dword ptr [r14 + 0x14], eax
00934415  E9 8D FC FF FF                  jmp 0x1409340a7
0093441A  48 8B C2                        mov rax, rdx
0093441D  48 89 54 24 48                  mov qword ptr [rsp + 0x48], rdx
00934422  E9 D1 FB FF FF                  jmp 0x140933ff8
00934427  48 39 9C 24 A8 00 00 00         cmp qword ptr [rsp + 0xa8], rbx
0093442F  0F 85 B3 FC FF FF               jne 0x1409340e8
00934435  83 F8 01                        cmp eax, 1
00934438  0F 85 07 01 00 00               jne 0x140934545
0093443E  41 0F B7 46 14                  movzx eax, word ptr [r14 + 0x14]
00934443  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
00934448  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
0093444D  49 8D 46 18                     lea rax, [r14 + 0x18]
00934451  E9 A5 FC FF FF                  jmp 0x1409340fb
00934456  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
0093445E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00934463  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
00934468  48 8B 05 51 26 69 00            mov rax, qword ptr [rip + 0x692651]
0093446F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00934474  41 B9 3F 00 0F 00               mov r9d, 0xf003f
0093447A  45 33 C0                        xor r8d, r8d
0093447D  BA 40 02 00 00                  mov edx, 0x240
00934482  48 8B 0E                        mov rcx, qword ptr [rsi]
00934485  E8 96 2F F8 FF                  call 0x1408b7420
0093448A  8B F8                           mov edi, eax
0093448C  85 C0                           test eax, eax
0093448E  0F 88 3F FF FF FF               js 0x1409343d3
00934494  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
00934499  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0093449E  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
009344A2  45 33 C9                        xor r9d, r9d
009344A5  45 33 C0                        xor r8d, r8d
009344A8  8B 56 08                        mov edx, dword ptr [rsi + 8]
009344AB  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009344B3  E8 58 92 D7 FF                  call 0x1406ad710
009344B8  8B F8                           mov edi, eax
009344BA  41 BD 00 00 00 80               mov r13d, 0x80000000
009344C0  41 03 C5                        add eax, r13d
009344C3  41 85 C5                        test r13d, eax
009344C6  74 5C                           je 0x140934524
009344C8  8B 54 24 5C                     mov edx, dword ptr [rsp + 0x5c]
009344CC  45 8B C7                        mov r8d, r15d
009344CF  B9 00 01 00 00                  mov ecx, 0x100
009344D4  E8 17 DC 24 00                  call 0x140b820f0
009344D9  4C 8B F0                        mov r14, rax
009344DC  48 85 C0                        test rax, rax
009344DF  0F 84 C2 00 00 00               je 0x1409345a7
009344E5  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009344ED  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
009344F2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009344F7  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
009344FB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009344FF  4D 8B CE                        mov r9, r14
00934502  45 33 C0                        xor r8d, r8d
00934505  8B 56 08                        mov edx, dword ptr [rsi + 8]
00934508  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00934510  E8 FB 91 D7 FF                  call 0x1406ad710
00934515  8B F8                           mov edi, eax
00934517  85 C0                           test eax, eax
00934519  0F 89 BE FB FF FF               jns 0x1409340dd
0093451F  E9 33 FC FF FF                  jmp 0x140934157
00934524  41 3B FE                        cmp edi, r14d
00934527  74 9F                           je 0x1409344c8
00934529  E9 29 FC FF FF                  jmp 0x140934157
0093452E  BF 9A 00 00 C0                  mov edi, 0xc000009a
00934533  48 8B C3                        mov rax, rbx
00934536  E9 BD FA FF FF                  jmp 0x140933ff8
0093453B  BF 9A 00 00 C0                  mov edi, 0xc000009a
00934540  E9 09 FB FF FF                  jmp 0x14093404e
00934545  BF 0D 00 00 C0                  mov edi, 0xc000000d
0093454A  E9 08 FC FF FF                  jmp 0x140934157
0093454F  41 8B D7                        mov edx, r15d
00934552  48 8B C8                        mov rcx, rax
00934555  E8 16 E3 24 00                  call 0x140b82870
0093455A  E9 69 FC FF FF                  jmp 0x1409341c8
0093455F  8B C3                           mov eax, ebx
00934561  48 8B 0D C8 E9 6C FF            mov rcx, qword ptr [rip - 0x931638]
00934568  E9 65 FD FF FF                  jmp 0x1409342d2
0093456D  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00934570  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00934574  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00934579  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
00934581  48 C7 84 24 C8 01 00 00 04 00 00 00  mov qword ptr [rsp + 0x1c8], 4
0093458D  49 39 5F 18                     cmp qword ptr [r15 + 0x18], rbx
00934591  49 8D 47 10                     lea rax, [r15 + 0x10]
00934595  0F 85 3F 01 1F 00               jne 0x140b246da
0093459B  48 8D 05 86 E9 6C FF            lea rax, [rip - 0x93167a]
009345A2  E9 33 01 1F 00                  jmp 0x140b246da
009345A7  BF 9A 00 00 C0                  mov edi, 0xc000009a
009345AC  E9 A6 FB FF FF                  jmp 0x140934157
009345B1  4C 8D 60 10                     lea r12, [rax + 0x10]
009345B5  E9 C3 FC FF FF                  jmp 0x14093427d
009345BA  E8 F1 8C D7 FF                  call 0x1406ad2b0
009345BF  E9 E2 FB FF FF                  jmp 0x1409341a6
009345C4  41 8B D7                        mov edx, r15d
009345C7  E8 A4 E2 24 00                  call 0x140b82870
009345CC  E9 E6 FB FF FF                  jmp 0x1409341b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpPostEnumerateKey(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m18C;
    unsigned __int16 v_stack_m18E;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A4;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int16 v_stack_m1B6;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int8 v_stack_m1E8;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (512);
    result = (*(unsigned __int64 *)(v_rip + 5073015)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m1D8 = a2;
    v_stack_m1A0 = a1;
    v_stack_m158 = a2;
    v_stack_m178 = v_xmm0;
    v_stack_m1B8 = v_xmm1;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = v_xmm0;
    result = EtwActivityIdControl(3, v_stack_m120, a3, a4);
    v_rbx = 0;
    v_stack_m180 = 0;
    v_stack_m1D0 = 0;
    v_stack_m198 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m168 = *(unsigned __int64 *)(a1 + 40);
    v_stack_m1A8 = 0;
    v_stack_m160 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m1E0 = 0;
    v_stack_m188 = 0;
    result = ExGetPreviousMode(3, v_stack_m120, a3, a4);
    v_stack_m1E8 = (unsigned __int8)(result);
    v_stack_m1CC = 0;
    v_stack_m1C0 = 0;
    v_stack_m190 = 0;
    if ((*(unsigned int *)(v_rip + 5072527)) > 5) goto loc_0093456D;
    if (sign_flag) goto loc_009343DD;
loc_00933FB5:
    if (((unsigned __int8)((unsigned __int8)(result))) != 1) goto loc_0093441A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 24))) == 0) goto loc_00933FF0;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 24)))), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), a4);
    if (result == 0) goto loc_0093452E;
loc_00933FF0:
    v_stack_m1E0 = result;
loc_00933FF8:
    if (sign_flag) goto loc_00934157;
    result = VrpOutputBufferParameter(v_stack_m1E8, result, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 24)), *(unsigned __int64 *)(a1 + 16) + 16);
    if (sign_flag) goto loc_00934157;
    if (v_stack_m1E8 != 1) goto loc_00934046;
    result = ExAllocatePool2(256, 4, (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), *(unsigned __int64 *)(a1 + 16) + 16);
    if (result == 0) goto loc_0093453B;
loc_00934046:
    v_stack_m1C0 = result;
loc_0093404E:
    if (sign_flag) goto loc_00934157;
    result = VrpOutputBufferParameter((unsigned __int8)(v_stack_m1E8), result, 4, *(unsigned __int64 *)(a1 + 16) + 32);
    if (sign_flag) goto loc_009343D3;
    if (((unsigned __int8)(v_stack_m1E8)) != 1) goto loc_009340AD;
    if ((*(unsigned int *)(v_stack_m1A0 + 8)) < 0) goto loc_009340AD;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 12))) != 0) goto loc_009343FD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 24))) - (16));
loc_009340A7:
    if ((*(unsigned int *)(v_stack_m1E0 + 12)) > ((unsigned int)(result))) goto loc_00934161;
loc_009340AD:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 8)))) == ((unsigned int)((unsigned int)(0xC0000023ULL)))) goto loc_00934456;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 8)))) == ((unsigned int)((unsigned int)(0x80000005ULL)))) goto loc_00934456;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 12)) == 2) goto loc_00934456;
loc_009340DD:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 12))) != 0) goto loc_00934427;
loc_009340E8:
    v_stack_m1B6 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1E0 + 12));
    v_stack_m1B8 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1E0 + 12));
loc_009340FB:
    v_stack_m1B0 = v_stack_m1E0 + 16;
    a1 = (v_stack_m198) + (16);
    result = VrpBuildKeyPath(a1, v_stack_m1B8, v_stack_m178, *(unsigned __int64 *)(a1 + 16) + 32);
    if (sign_flag) goto loc_00934157;
    result = VrpLockJobContextShared(v_stack_m1D8, v_stack_m1B8, v_stack_m178, *(unsigned __int64 *)(a1 + 16) + 32);
    v_stack_m1D0 = 1;
    a3 = 0;
    result = VrpFindExactNamespaceNode(v_stack_m1D8, v_stack_m178, a3, *(unsigned __int64 *)(a1 + 16) + 32);
loc_00934157:
loc_0093415C:
loc_00934161:
    result = v_stack_m1D8;
    if (v_stack_m1D0 != 0) {
        a1 = v_stack_m1D8;
        result = VrpUnlockJobContextShared(a1, v_stack_m178, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    }
    if (sign_flag) goto loc_0093423E;
loc_00934183:
    if (v_stack_m1A8 != 0) {
        result = ZwClose(v_stack_m1A8, v_stack_m178, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    }
    if (v_stack_m190 != 0) goto loc_009345BA;
loc_009341A6:
    if (v_stack_m188 != 0) goto loc_009345C4;
loc_009341B7:
    if (v_stack_m180 != 0) goto loc_0093454F;
loc_009341C8:
    result = v_stack_m180;
    if (v_stack_m170 != 0) {
        a2 = (unsigned int)((unsigned int)(0x67655256ULL));
        result = ExFreePoolWithTag(v_stack_m170, a2, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    }
    if (((unsigned __int8)(v_stack_m1E8)) != 1) goto loc_0093420E;
    if (v_stack_m1E0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x67655256ULL));
        a1 = v_stack_m1E0;
        result = ExFreePoolWithTag(a1, a2, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    }
    if (((unsigned __int8)(v_stack_m1E8)) != 1) goto loc_0093420E;
    result = v_stack_m1C0;
    if (v_stack_m1C0 != 0) {
        a2 = (unsigned int)((unsigned int)(0x67655256ULL));
        a1 = v_stack_m1C0;
        result = ExFreePoolWithTag(a1, a2, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, *(unsigned __int64 *)(a1 + 16) + 32);
    return result;
loc_0093423E:
    if ((*(unsigned int *)(v_rip + 5071851)) <= 2) goto loc_00934183;
    v_stack_m19C = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 12)));
    v_stack_mC0 = v_stack_m19C;
    v_stack_mB8 = 4;
    if ((*(unsigned __int64 *)(v_stack_m170 + 24)) != (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_009345B1;
loc_0093427D:
    v_stack_mB0 = v_stack_m98;
    v_stack_mA8 = 2;
    v_stack_mA0 = *(unsigned __int64 *)(v_rip - 9638464 + 8);
    v_stack_m98 = (unsigned int)(*(unsigned __int16 *)(v_rip - 9638464));
    v_stack_m94 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    if (v_stack_m148 == 0) goto loc_0093455F;
loc_009342D2:
    v_stack_m90 = v_stack_m78;
    v_stack_m88 = 2;
    v_stack_m80 = v_stack_m148;
    v_stack_m78 = (unsigned int)((unsigned __int16)(v_stack_m150));
    v_stack_m74 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    v_stack_m1A0 = 0;
    v_stack_m70 = v_stack_m1A0;
    v_stack_m68 = 4;
    v_stack_m190 = 0xB000000ULL;
    v_stack_m18C = (unsigned int)(*(unsigned __int16 *)(v_rip - 9279854));
    v_stack_m188 = *(unsigned __int64 *)(v_stack_m28 + 64);
    v_stack_mE0 = *(unsigned __int64 *)(v_rip + 5071605);
    v_stack_mD8 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 5071605)));
    v_stack_mD4 = 2;
    v_stack_mD0 = v_rip - 9279896;
    v_stack_mC8 = 116;
    v_stack_mC4 = 1;
    result = (unsigned int)((v_rip - 9275023) - ((unsigned int)(v_rip - 9375235)));
    v_stack_m1A8 = (unsigned int)(result);
    v_stack_m1D8 = v_stack_mE0;
    v_stack_m1E0 = 8;
    a4 = 0;
    result = EtwWriteTransfer(*(unsigned __int64 *)(v_rip + 5071495), v_stack_m190, v_stack_mF8, a4);
    goto loc_00934183;
loc_009343D3:
    goto loc_00934161;
loc_009343DD:
    if (0 == 0xC0000023ULL) goto loc_00933FB5;
    if (0 == ((unsigned int)(v_rip - 9638464))) goto loc_00933FB5;
    goto loc_0093415C;
loc_009343FD:
    if (((unsigned int)(result)) != 1) goto loc_009340AD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 24))) - (24));
    goto loc_009340A7;
loc_0093441A:
    v_stack_m1B8 = v_stack_m190;
    goto loc_00933FF8;
loc_00934427:
    if (v_stack_m158 != (*(unsigned __int64 *)(v_stack_m28 + 64))) goto loc_009340E8;
    if (((unsigned int)(v_stack_m190)) != 1) goto loc_00934545;
    v_stack_m18E = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1B8 + 20));
    v_stack_m190 = (unsigned __int16)(*(unsigned __int16 *)(v_stack_m1B8 + 20));
    goto loc_009340FB;
loc_00934456:
    v_stack_m1D0 = v_stack_m180;
    v_stack_m1D8 = (unsigned __int8)(v_stack_m1E8);
    v_stack_m1E0 = *(unsigned __int64 *)(v_rip + 6891089);
    a3 = 0;
    result = ObOpenObjectByPointer(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72)), 576, a3, (unsigned int)(0xF003FULL));
    if (sign_flag) goto loc_009343D3;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64));
    a4 = 0;
    a3 = 0;
    result = ZwEnumerateKey(v_stack_m180, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)), a3, a4);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) == 0) goto loc_00934524;
loc_009344C8:
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m1A4), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), a4);
    if (result == 0) goto loc_009345A7;
    v_stack_m158 = result;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = (unsigned int)((unsigned int)(v_stack_m1A4));
    a3 = 0;
    result = ZwEnumerateKey(v_stack_m180, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 8)), a3, result);
    if (!sign_flag) goto loc_009340DD;
    goto loc_00934157;
loc_00934524:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == ((unsigned int)(result))) goto loc_009344C8;
    goto loc_00934157;
loc_0093452E:
    goto loc_00933FF8;
loc_0093453B:
    goto loc_0093404E;
loc_00934545:
    goto loc_00934157;
loc_0093454F:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 64), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), a3, result);
    goto loc_009341C8;
loc_0093455F:
    goto loc_009342D2;
loc_0093456D:
    v_stack_m1A0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 12)));
    v_stack_m40 = v_stack_m1A0;
    v_stack_m38 = 4;
loc_009345A7:
    goto loc_00934157;
loc_009345B1:
    goto loc_0093427D;
loc_009345BA:
    result = ZwClose(*(unsigned __int64 *)(v_rip - 9639480), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), a3, result);
    goto loc_009341A6;
loc_009345C4:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip - 9639480), (unsigned int)((unsigned int)((unsigned int)(0x67655256ULL))), a3, result);
    goto loc_009341B7;
}
```

## 5. (Beta) C Style

```c
int64_t VrpPostEnumerateKey(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m18C;
    uint16_t v_stack_m18E;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A4;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint16_t v_stack_m1B6;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint8_t v_stack_m1E8;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (512);
    result = (*(uint64_t *)(v_rip + 0x4D6877)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m1D8 = Arg2;
    v_stack_m1A0 = Arg1;
    v_stack_m158 = Arg2;
    v_stack_m178 = v_xmm0;
    v_stack_m1B8 = v_xmm1;
    v_stack_m150 = v_xmm0;
    v_stack_m140 = v_xmm0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = v_xmm0;
    result = EtwActivityIdControl(3, v_stack_m120, a3, a4);
    local_rbx = 0;
    v_stack_m180 = 0;
    v_stack_m1D0 = 0;
    v_stack_m198 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m168 = *(uint64_t *)(arg1 + 0x28);
    v_stack_m1A8 = 0;
    v_stack_m160 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m1E0 = 0;
    v_stack_m188 = 0;
    result = ExGetPreviousMode(3, v_stack_m120, a3, a4);
    v_stack_m1E8 = (uint8_t)(result);
    v_stack_m1CC = 0;
    v_stack_m1C0 = 0;
    v_stack_m190 = 0;
    if ((*(uint32_t *)(v_rip + 0x4D668F)) > 5) goto loc_0093456D;
    if (sign_flag) goto loc_009343DD;
loc_00933FB5:
    if (((uint8_t)((uint8_t)(result))) != 1) goto loc_0093441A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x18))) == 0) goto loc_00933FF0;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x18)))), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), a4);
    if (result == 0) goto loc_0093452E;
loc_00933FF0:
    v_stack_m1E0 = result;
loc_00933FF8:
    if (sign_flag) goto loc_00934157;
    result = VrpOutputBufferParameter(v_stack_m1E8, result, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x18)), *(uint64_t *)(arg1 + 0x10) + 16);
    if (sign_flag) goto loc_00934157;
    if (v_stack_m1E8 != 1) goto loc_00934046;
    result = ExAllocatePool2(256, 4, (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), *(uint64_t *)(arg1 + 0x10) + 16);
    if (result == 0) goto loc_0093453B;
loc_00934046:
    v_stack_m1C0 = result;
loc_0093404E:
    if (sign_flag) goto loc_00934157;
    result = VrpOutputBufferParameter((uint8_t)(v_stack_m1E8), result, 4, *(uint64_t *)(arg1 + 0x10) + 32);
    if (sign_flag) goto loc_009343D3;
    if (((uint8_t)(v_stack_m1E8)) != 1) goto loc_009340AD;
    if ((*(uint32_t *)(v_stack_m1A0 + 0x8)) < 0) goto loc_009340AD;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0xC))) != 0) goto loc_009343FD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x18))) - (16));
loc_009340A7:
    if ((*(uint32_t *)(v_stack_m1E0 + 0xC)) > ((uint32_t)(result))) goto loc_00934161;
loc_009340AD:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x8)))) == ((uint32_t)((uint32_t)(0xC0000023ULL)))) goto loc_00934456;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x8)))) == ((uint32_t)((uint32_t)(0x80000005ULL)))) goto loc_00934456;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0xC)) == 2) goto loc_00934456;
loc_009340DD:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0xC))) != 0) goto loc_00934427;
loc_009340E8:
    v_stack_m1B6 = (uint16_t)(*(uint16_t *)(v_stack_m1E0 + 0xC));
    v_stack_m1B8 = (uint16_t)(*(uint16_t *)(v_stack_m1E0 + 0xC));
loc_009340FB:
    v_stack_m1B0 = v_stack_m1E0 + 16;
    Arg1 = (v_stack_m198) + (16);
    result = VrpBuildKeyPath(Arg1, v_stack_m1B8, v_stack_m178, *(uint64_t *)(arg1 + 0x10) + 32);
    if (sign_flag) goto loc_00934157;
    result = VrpLockJobContextShared(v_stack_m1D8, v_stack_m1B8, v_stack_m178, *(uint64_t *)(arg1 + 0x10) + 32);
    v_stack_m1D0 = 1;
    a3 = 0;
    result = VrpFindExactNamespaceNode(v_stack_m1D8, v_stack_m178, a3, *(uint64_t *)(arg1 + 0x10) + 32);
loc_00934157:
loc_0093415C:
loc_00934161:
    result = v_stack_m1D8;
    if (v_stack_m1D0 != 0) {
        Arg1 = v_stack_m1D8;
        result = VrpUnlockJobContextShared(Arg1, v_stack_m178, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    }
    if (sign_flag) goto loc_0093423E;
loc_00934183:
    if (v_stack_m1A8 != 0) {
        result = ZwClose(v_stack_m1A8, v_stack_m178, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    }
    if (v_stack_m190 != 0) goto loc_009345BA;
loc_009341A6:
    if (v_stack_m188 != 0) goto loc_009345C4;
loc_009341B7:
    if (v_stack_m180 != 0) goto loc_0093454F;
loc_009341C8:
    result = v_stack_m180;
    if (v_stack_m170 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x67655256ULL));
        result = ExFreePoolWithTag(v_stack_m170, Arg2, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    }
    if (((uint8_t)(v_stack_m1E8)) != 1) goto loc_0093420E;
    if (v_stack_m1E0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x67655256ULL));
        Arg1 = v_stack_m1E0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    }
    if (((uint8_t)(v_stack_m1E8)) != 1) goto loc_0093420E;
    result = v_stack_m1C0;
    if (v_stack_m1C0 != 0) {
        Arg2 = (uint32_t)((uint32_t)(0x67655256ULL));
        Arg1 = v_stack_m1C0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, *(uint64_t *)(arg1 + 0x10) + 32);
    return result;
loc_0093423E:
    if ((*(uint32_t *)(v_rip + 0x4D63EB)) <= 2) goto loc_00934183;
    v_stack_m19C = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC)));
    v_stack_mC0 = v_stack_m19C;
    v_stack_mB8 = 4;
    if ((*(uint64_t *)(v_stack_m170 + 0x18)) != (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_009345B1;
loc_0093427D:
    v_stack_mB0 = v_stack_m98;
    v_stack_mA8 = 2;
    v_stack_mA0 = *(uint64_t *)(v_rip - 0x931240 + 0x8);
    v_stack_m98 = (uint32_t)(*(uint16_t *)(v_rip - 0x931240));
    v_stack_m94 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    if (v_stack_m148 == 0) goto loc_0093455F;
loc_009342D2:
    v_stack_m90 = v_stack_m78;
    v_stack_m88 = 2;
    v_stack_m80 = v_stack_m148;
    v_stack_m78 = (uint32_t)((uint16_t)(v_stack_m150));
    v_stack_m74 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    v_stack_m1A0 = 0;
    v_stack_m70 = v_stack_m1A0;
    v_stack_m68 = 4;
    v_stack_m190 = 0xB000000ULL;
    v_stack_m18C = (uint32_t)(*(uint16_t *)(v_rip - 0x8D996E));
    v_stack_m188 = *(uint64_t *)(v_stack_m28 + 0x40);
    v_stack_mE0 = *(uint64_t *)(v_rip + 0x4D62F5);
    v_stack_mD8 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x4D62F5)));
    v_stack_mD4 = 2;
    v_stack_mD0 = v_rip - 9279896;
    v_stack_mC8 = 116;
    v_stack_mC4 = 1;
    result = (uint32_t)((v_rip - 9275023) - ((uint32_t)(v_rip - 9375235)));
    v_stack_m1A8 = (uint32_t)(result);
    v_stack_m1D8 = v_stack_mE0;
    v_stack_m1E0 = 8;
    a4 = 0;
    result = EtwWriteTransfer(*(uint64_t *)(v_rip + 0x4D6287), v_stack_m190, v_stack_mF8, a4);
    goto loc_00934183;
loc_009343D3:
    goto loc_00934161;
loc_009343DD:
    if (0 == 0xC0000023ULL) goto loc_00933FB5;
    if (0 == ((uint32_t)(v_rip - 9638464))) goto loc_00933FB5;
    goto loc_0093415C;
loc_009343FD:
    if (((uint32_t)(result)) != 1) goto loc_009340AD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x18))) - (24));
    goto loc_009340A7;
loc_0093441A:
    v_stack_m1B8 = v_stack_m190;
    goto loc_00933FF8;
loc_00934427:
    if (v_stack_m158 != (*(uint64_t *)(v_stack_m28 + 0x40))) goto loc_009340E8;
    if (((uint32_t)(v_stack_m190)) != 1) goto loc_00934545;
    v_stack_m18E = (uint16_t)(*(uint16_t *)(v_stack_m1B8 + 0x14));
    v_stack_m190 = (uint16_t)(*(uint16_t *)(v_stack_m1B8 + 0x14));
    goto loc_009340FB;
loc_00934456:
    v_stack_m1D0 = v_stack_m180;
    v_stack_m1D8 = (uint8_t)(v_stack_m1E8);
    v_stack_m1E0 = *(uint64_t *)(v_rip + 0x692651);
    a3 = 0;
    result = ObOpenObjectByPointer(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48)), 576, a3, (uint32_t)(0xF003FULL));
    if (sign_flag) goto loc_009343D3;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40));
    a4 = 0;
    a3 = 0;
    result = ZwEnumerateKey(v_stack_m180, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)), a3, a4);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) == 0) goto loc_00934524;
loc_009344C8:
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m1A4), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), a4);
    if (result == 0) goto loc_009345A7;
    v_stack_m158 = result;
    v_stack_m1D8 = v_stack_m1A4;
    v_stack_m1E0 = (uint32_t)((uint32_t)(v_stack_m1A4));
    a3 = 0;
    result = ZwEnumerateKey(v_stack_m180, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x8)), a3, result);
    if (!sign_flag) goto loc_009340DD;
    goto loc_00934157;
loc_00934524:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == ((uint32_t)(result))) goto loc_009344C8;
    goto loc_00934157;
loc_0093452E:
    goto loc_00933FF8;
loc_0093453B:
    goto loc_0093404E;
loc_00934545:
    goto loc_00934157;
loc_0093454F:
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x40), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), a3, result);
    goto loc_009341C8;
loc_0093455F:
    goto loc_009342D2;
loc_0093456D:
    v_stack_m1A0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC)));
    v_stack_m40 = v_stack_m1A0;
    v_stack_m38 = 4;
loc_009345A7:
    goto loc_00934157;
loc_009345B1:
    goto loc_0093427D;
loc_009345BA:
    result = ZwClose(*(uint64_t *)(v_rip - 0x931638), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), a3, result);
    goto loc_009341A6;
loc_009345C4:
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip - 0x931638), (uint32_t)((uint32_t)((uint32_t)(0x67655256ULL))), a3, result);
    goto loc_009341B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00933EA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
