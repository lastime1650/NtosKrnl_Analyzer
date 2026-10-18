# PopQueryMostRecentWakeSourceInfo

- RVA: `0x0075C630`–`0x0075C9FF` (길이 `975` bytes)
- VA: `0x000000014075C630`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC2D0`
- 디코드: `277`개 명령, `975/975` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x0075C6CE` → [PopGetMostRecentWakeInfo](../../text/4B/PopGetMostRecentWakeInfo_function_004BE4F8.md) (function, `0x004BE4F8`)
- `0x0075C84C` → [PopGetCallerContextFromBuffer](../A3/PopGetCallerContextFromBuffer_function_00A39AAC.md) (function, `0x00A39AAC`)
- `0x0075C859` → [PopWakeInfoDereference](../../text/4C/PopWakeInfoDereference_function_004C74AC.md) (function, `0x004C74AC`)
- `0x0075C9BA` → [PopCloneUnicodeString](../AA/PopCloneUnicodeString_function_00AA3E20.md) (function, `0x00AA3E20`)
- `0x0075C9D8` → [PopCloneUnicodeString](../AA/PopCloneUnicodeString_function_00AA3E20.md) (function, `0x00AA3E20`)

### Direct callers
- [PopDiagTracePowerTransitionEnd](../AD/PopDiagTracePowerTransitionEnd_function_00AD24DC.md) at `0x00AD258E`

### Static image references
- `0x0075C665` → RVA `0x00AFE5E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C727` → RVA `0x00AFFEC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C780` → RVA `0x00B01DF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C7AB` → RVA `0x00B01DC0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C7D6` → RVA `0x00B01D90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C7FE` → RVA `0x00B01D70` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C87F` → RVA `0x00B01D60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C8A8` → RVA `0x00B01E10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C8FE` → RVA `0x00B01E40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C925` → RVA `0x00B01E20` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0075C96E` → RVA `0x00AFE540` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0075C6CE` → [PopGetMostRecentWakeInfo](../../text/4B/PopGetMostRecentWakeInfo_function_004BE4F8.md) (`PAGE` → `.text`)
  - `0x0075C859` → [PopWakeInfoDereference](../../text/4C/PopWakeInfoDereference_function_004C74AC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0075C630  48 8B C4                        mov rax, rsp
0075C633  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0075C637  48 89 68 18                     mov qword ptr [rax + 0x18], rbp
0075C63B  48 89 70 20                     mov qword ptr [rax + 0x20], rsi
0075C63F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0075C643  57                              push rdi
0075C644  41 54                           push r12
0075C646  41 55                           push r13
0075C648  41 56                           push r14
0075C64A  41 57                           push r15
0075C64C  48 83 EC 20                     sub rsp, 0x20
0075C650  4C 8B 6C 24 78                  mov r13, qword ptr [rsp + 0x78]
0075C655  33 C9                           xor ecx, ecx
0075C657  4C 8B A4 24 80 00 00 00         mov r12, qword ptr [rsp + 0x80]
0075C65F  4D 8B F9                        mov r15, r9
0075C662  0F 57 C0                        xorps xmm0, xmm0
0075C665  4C 8D 0D 74 1F 3A 00            lea r9, [rip + 0x3a1f74]
0075C66C  BB FF 7F 00 00                  mov ebx, 0x7fff
0075C671  49 8B F8                        mov rdi, r8
0075C674  48 8B F2                        mov rsi, rdx
0075C677  41 88 4D 00                     mov byte ptr [r13], cl
0075C67B  0F 11 02                        movups xmmword ptr [rdx], xmm0
0075C67E  41 88 0C 24                     mov byte ptr [r12], cl
0075C682  44 8D 41 02                     lea r8d, [rcx + 2]
0075C686  8B D3                           mov edx, ebx
0075C688  49 8B C1                        mov rax, r9
0075C68B  66 39 08                        cmp word ptr [rax], cx
0075C68E  74 0B                           je 0x14075c69b
0075C690  49 03 C0                        add rax, r8
0075C693  48 83 EA 01                     sub rdx, 1
0075C697  75 F2                           jne 0x14075c68b
0075C699  EB 1D                           jmp 0x14075c6b8
0075C69B  48 8B C3                        mov rax, rbx
0075C69E  48 2B C2                        sub rax, rdx
0075C6A1  48 85 F6                        test rsi, rsi
0075C6A4  74 12                           je 0x14075c6b8
0075C6A6  66 03 C0                        add ax, ax
0075C6A9  4C 89 4E 08                     mov qword ptr [rsi + 8], r9
0075C6AD  66 89 06                        mov word ptr [rsi], ax
0075C6B0  66 41 03 C0                     add ax, r8w
0075C6B4  66 89 46 02                     mov word ptr [rsi + 2], ax
0075C6B8  4C 8B 74 24 70                  mov r14, qword ptr [rsp + 0x70]
0075C6BD  0F 57 C0                        xorps xmm0, xmm0
0075C6C0  0F 57 C9                        xorps xmm1, xmm1
0075C6C3  41 0F 11 0F                     movups xmmword ptr [r15], xmm1
0075C6C7  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0075C6CB  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C6CE  E8 25 1E D6 FF                  call 0x1404be4f8
0075C6D3  45 33 C9                        xor r9d, r9d
0075C6D6  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
0075C6DB  4C 8B C0                        mov r8, rax
0075C6DE  48 85 C0                        test rax, rax
0075C6E1  0F 84 77 01 00 00               je 0x14075c85e
0075C6E7  44 39 48 28                     cmp dword ptr [rax + 0x28], r9d
0075C6EB  0F 84 65 01 00 00               je 0x14075c856
0075C6F1  48 8B 68 20                     mov rbp, qword ptr [rax + 0x20]
0075C6F5  8B 55 10                        mov edx, dword ptr [rbp + 0x10]
0075C6F8  85 D2                           test edx, edx
0075C6FA  0F 84 6B 02 00 00               je 0x14075c96b
0075C700  83 EA 01                        sub edx, 1
0075C703  0F 84 9C 01 00 00               je 0x14075c8a5
0075C709  83 EA 01                        sub edx, 1
0075C70C  0F 84 6A 01 00 00               je 0x14075c87c
0075C712  83 EA 01                        sub edx, 1
0075C715  0F 84 E0 00 00 00               je 0x14075c7fb
0075C71B  83 FA 01                        cmp edx, 1
0075C71E  0F 85 32 01 00 00               jne 0x14075c856
0075C724  0F 57 C0                        xorps xmm0, xmm0
0075C727  4C 8D 15 92 37 3A 00            lea r10, [rip + 0x3a3792]
0075C72E  0F 11 06                        movups xmmword ptr [rsi], xmm0
0075C731  49 8B C2                        mov rax, r10
0075C734  41 8D 51 02                     lea edx, [r9 + 2]
0075C738  48 8B CB                        mov rcx, rbx
0075C73B  66 44 39 08                     cmp word ptr [rax], r9w
0075C73F  74 0B                           je 0x14075c74c
0075C741  48 03 C2                        add rax, rdx
0075C744  48 83 E9 01                     sub rcx, 1
0075C748  75 F1                           jne 0x14075c73b
0075C74A  EB 1C                           jmp 0x14075c768
0075C74C  48 8B C3                        mov rax, rbx
0075C74F  48 2B C1                        sub rax, rcx
0075C752  48 85 F6                        test rsi, rsi
0075C755  74 11                           je 0x14075c768
0075C757  66 03 C0                        add ax, ax
0075C75A  4C 89 56 08                     mov qword ptr [rsi + 8], r10
0075C75E  66 89 06                        mov word ptr [rsi], ax
0075C761  66 03 C2                        add ax, dx
0075C764  66 89 46 02                     mov word ptr [rsi + 2], ax
0075C768  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
0075C76B  85 C9                           test ecx, ecx
0075C76D  74 64                           je 0x14075c7d3
0075C76F  83 E9 01                        sub ecx, 1
0075C772  74 34                           je 0x14075c7a8
0075C774  83 F9 01                        cmp ecx, 1
0075C777  0F 85 D9 00 00 00               jne 0x14075c856
0075C77D  0F 57 C0                        xorps xmm0, xmm0
0075C780  4C 8D 15 69 56 3A 00            lea r10, [rip + 0x3a5669]
0075C787  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C78A  49 8B C2                        mov rax, r10
0075C78D  48 8B CB                        mov rcx, rbx
0075C790  66 44 39 08                     cmp word ptr [rax], r9w
0075C794  0F 84 AF 01 00 00               je 0x14075c949
0075C79A  48 03 C2                        add rax, rdx
0075C79D  48 83 E9 01                     sub rcx, 1
0075C7A1  75 ED                           jne 0x14075c790
0075C7A3  E9 AE 00 00 00                  jmp 0x14075c856
0075C7A8  0F 57 C0                        xorps xmm0, xmm0
0075C7AB  4C 8D 15 0E 56 3A 00            lea r10, [rip + 0x3a560e]
0075C7B2  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C7B5  49 8B C2                        mov rax, r10
0075C7B8  48 8B CB                        mov rcx, rbx
0075C7BB  66 44 39 08                     cmp word ptr [rax], r9w
0075C7BF  0F 84 84 01 00 00               je 0x14075c949
0075C7C5  48 03 C2                        add rax, rdx
0075C7C8  48 83 E9 01                     sub rcx, 1
0075C7CC  75 ED                           jne 0x14075c7bb
0075C7CE  E9 83 00 00 00                  jmp 0x14075c856
0075C7D3  0F 57 C0                        xorps xmm0, xmm0
0075C7D6  4C 8D 15 B3 55 3A 00            lea r10, [rip + 0x3a55b3]
0075C7DD  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C7E0  49 8B C2                        mov rax, r10
0075C7E3  48 8B CB                        mov rcx, rbx
0075C7E6  66 44 39 08                     cmp word ptr [rax], r9w
0075C7EA  0F 84 59 01 00 00               je 0x14075c949
0075C7F0  48 03 C2                        add rax, rdx
0075C7F3  48 83 E9 01                     sub rcx, 1
0075C7F7  75 ED                           jne 0x14075c7e6
0075C7F9  EB 5B                           jmp 0x14075c856
0075C7FB  0F 57 C0                        xorps xmm0, xmm0
0075C7FE  4C 8D 05 6B 55 3A 00            lea r8, [rip + 0x3a556b]
0075C805  0F 11 06                        movups xmmword ptr [rsi], xmm0
0075C808  49 8B C0                        mov rax, r8
0075C80B  48 8B CB                        mov rcx, rbx
0075C80E  BA 02 00 00 00                  mov edx, 2
0075C813  66 44 39 08                     cmp word ptr [rax], r9w
0075C817  74 0B                           je 0x14075c824
0075C819  48 03 C2                        add rax, rdx
0075C81C  48 83 E9 01                     sub rcx, 1
0075C820  75 F1                           jne 0x14075c813
0075C822  EB 19                           jmp 0x14075c83d
0075C824  48 2B D9                        sub rbx, rcx
0075C827  48 85 F6                        test rsi, rsi
0075C82A  74 11                           je 0x14075c83d
0075C82C  66 03 DB                        add bx, bx
0075C82F  4C 89 46 08                     mov qword ptr [rsi + 8], r8
0075C833  66 89 1E                        mov word ptr [rsi], bx
0075C836  66 03 DA                        add bx, dx
0075C839  66 89 5E 02                     mov word ptr [rsi + 2], bx
0075C83D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
0075C842  4D 8B CE                        mov r9, r14
0075C845  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0075C849  4D 8B C7                        mov r8, r15
0075C84C  E8 5B D2 2D 00                  call 0x140a39aac
0075C851  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0075C856  49 8B C8                        mov rcx, r8
0075C859  E8 4E AC D6 FF                  call 0x1404c74ac
0075C85E  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
0075C863  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0075C868  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
0075C86D  48 83 C4 20                     add rsp, 0x20
0075C871  41 5F                           pop r15
0075C873  41 5E                           pop r14
0075C875  41 5D                           pop r13
0075C877  41 5C                           pop r12
0075C879  5F                              pop rdi
0075C87A  C3                              ret
0075C87B  CC                              int3
0075C87C  0F 57 C0                        xorps xmm0, xmm0
0075C87F  4C 8D 05 DA 54 3A 00            lea r8, [rip + 0x3a54da]
0075C886  0F 11 06                        movups xmmword ptr [rsi], xmm0
0075C889  49 8B C0                        mov rax, r8
0075C88C  48 8B CB                        mov rcx, rbx
0075C88F  BA 02 00 00 00                  mov edx, 2
0075C894  66 44 39 08                     cmp word ptr [rax], r9w
0075C898  74 8A                           je 0x14075c824
0075C89A  48 03 C2                        add rax, rdx
0075C89D  48 83 E9 01                     sub rcx, 1
0075C8A1  75 F1                           jne 0x14075c894
0075C8A3  EB 98                           jmp 0x14075c83d
0075C8A5  0F 57 C0                        xorps xmm0, xmm0
0075C8A8  4C 8D 15 61 55 3A 00            lea r10, [rip + 0x3a5561]
0075C8AF  0F 11 06                        movups xmmword ptr [rsi], xmm0
0075C8B2  49 8B C2                        mov rax, r10
0075C8B5  48 8B CB                        mov rcx, rbx
0075C8B8  BA 02 00 00 00                  mov edx, 2
0075C8BD  66 44 39 08                     cmp word ptr [rax], r9w
0075C8C1  74 0B                           je 0x14075c8ce
0075C8C3  48 03 C2                        add rax, rdx
0075C8C6  48 83 E9 01                     sub rcx, 1
0075C8CA  75 F1                           jne 0x14075c8bd
0075C8CC  EB 1C                           jmp 0x14075c8ea
0075C8CE  48 8B C3                        mov rax, rbx
0075C8D1  48 2B C1                        sub rax, rcx
0075C8D4  48 85 F6                        test rsi, rsi
0075C8D7  74 11                           je 0x14075c8ea
0075C8D9  66 03 C0                        add ax, ax
0075C8DC  4C 89 56 08                     mov qword ptr [rsi + 8], r10
0075C8E0  66 89 06                        mov word ptr [rsi], ax
0075C8E3  66 03 C2                        add ax, dx
0075C8E6  66 89 46 02                     mov word ptr [rsi + 2], ax
0075C8EA  8B 4D 18                        mov ecx, dword ptr [rbp + 0x18]
0075C8ED  83 E9 01                        sub ecx, 1
0075C8F0  74 30                           je 0x14075c922
0075C8F2  83 F9 01                        cmp ecx, 1
0075C8F5  0F 85 5B FF FF FF               jne 0x14075c856
0075C8FB  0F 57 C0                        xorps xmm0, xmm0
0075C8FE  4C 8D 15 3B 55 3A 00            lea r10, [rip + 0x3a553b]
0075C905  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C908  49 8B C2                        mov rax, r10
0075C90B  48 8B CB                        mov rcx, rbx
0075C90E  66 44 39 08                     cmp word ptr [rax], r9w
0075C912  74 35                           je 0x14075c949
0075C914  48 03 C2                        add rax, rdx
0075C917  48 83 E9 01                     sub rcx, 1
0075C91B  75 F1                           jne 0x14075c90e
0075C91D  E9 34 FF FF FF                  jmp 0x14075c856
0075C922  0F 57 C0                        xorps xmm0, xmm0
0075C925  4C 8D 15 F4 54 3A 00            lea r10, [rip + 0x3a54f4]
0075C92C  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C92F  49 8B C2                        mov rax, r10
0075C932  48 8B CB                        mov rcx, rbx
0075C935  66 44 39 08                     cmp word ptr [rax], r9w
0075C939  74 0E                           je 0x14075c949
0075C93B  48 03 C2                        add rax, rdx
0075C93E  48 83 E9 01                     sub rcx, 1
0075C942  75 F1                           jne 0x14075c935
0075C944  E9 0D FF FF FF                  jmp 0x14075c856
0075C949  48 2B D9                        sub rbx, rcx
0075C94C  48 85 FF                        test rdi, rdi
0075C94F  0F 84 01 FF FF FF               je 0x14075c856
0075C955  66 03 DB                        add bx, bx
0075C958  4C 89 57 08                     mov qword ptr [rdi + 8], r10
0075C95C  66 89 1F                        mov word ptr [rdi], bx
0075C95F  66 03 DA                        add bx, dx
0075C962  66 89 5F 02                     mov word ptr [rdi + 2], bx
0075C966  E9 EB FE FF FF                  jmp 0x14075c856
0075C96B  0F 57 C0                        xorps xmm0, xmm0
0075C96E  4C 8D 05 CB 1B 3A 00            lea r8, [rip + 0x3a1bcb]
0075C975  0F 11 06                        movups xmmword ptr [rsi], xmm0
0075C978  49 8B C0                        mov rax, r8
0075C97B  48 8B CB                        mov rcx, rbx
0075C97E  BA 02 00 00 00                  mov edx, 2
0075C983  66 44 39 08                     cmp word ptr [rax], r9w
0075C987  74 0B                           je 0x14075c994
0075C989  48 03 C2                        add rax, rdx
0075C98C  48 83 E9 01                     sub rcx, 1
0075C990  75 F1                           jne 0x14075c983
0075C992  EB 19                           jmp 0x14075c9ad
0075C994  48 2B D9                        sub rbx, rcx
0075C997  48 85 F6                        test rsi, rsi
0075C99A  74 11                           je 0x14075c9ad
0075C99C  66 03 DB                        add bx, bx
0075C99F  4C 89 46 08                     mov qword ptr [rsi + 8], r8
0075C9A3  66 89 1E                        mov word ptr [rsi], bx
0075C9A6  66 03 DA                        add bx, dx
0075C9A9  66 89 5E 02                     mov word ptr [rsi + 2], bx
0075C9AD  0F 57 C0                        xorps xmm0, xmm0
0075C9B0  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0075C9B4  49 8B D7                        mov rdx, r15
0075C9B7  0F 11 07                        movups xmmword ptr [rdi], xmm0
0075C9BA  E8 61 74 34 00                  call 0x140aa3e20
0075C9BF  33 DB                           xor ebx, ebx
0075C9C1  85 C0                           test eax, eax
0075C9C3  78 0C                           js 0x14075c9d1
0075C9C5  66 41 39 5F 02                  cmp word ptr [r15 + 2], bx
0075C9CA  74 05                           je 0x14075c9d1
0075C9CC  41 C6 45 00 01                  mov byte ptr [r13], 1
0075C9D1  48 8D 4D 18                     lea rcx, [rbp + 0x18]
0075C9D5  49 8B D6                        mov rdx, r14
0075C9D8  E8 43 74 34 00                  call 0x140aa3e20
0075C9DD  85 C0                           test eax, eax
0075C9DF  0F 88 6C FE FF FF               js 0x14075c851
0075C9E5  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0075C9EA  66 41 39 5E 02                  cmp word ptr [r14 + 2], bx
0075C9EF  0F 84 61 FE FF FF               je 0x14075c856
0075C9F5  41 C6 04 24 01                  mov byte ptr [r12], 1
0075C9FA  E9 57 FE FF FF                  jmp 0x14075c856
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopQueryMostRecentWakeSourceInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (32);
    a1 = 0;
    *(unsigned __int8 *)(a6) = 0;
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int8 *)(a7) = 0;
loc_0075C68B:
    if ((*(unsigned __int16 *)(v_rip + 3809140)) == 0) goto loc_0075C69B;
    result = (v_rip + 3809140) + (a1 + 2);
    a2 = ((unsigned int)((unsigned int)((unsigned int)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_0075C68B;
    goto loc_0075C6B8;
loc_0075C69B:
    result = ((unsigned int)(0x7FFFULL)) - (a2);
    if (a2 != 0) {
        result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
        *(unsigned __int64 *)(a2 + 8) = v_rip + 3809140;
        *(unsigned __int16 *)(a2) = (unsigned __int16)(result);
        result = (unsigned __int16)((result) + ((unsigned __int16)(a1 + 2)));
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(result);
    }
    *(unsigned __int64 *)(a4) = v_xmm1;
    *(unsigned __int64 *)(a5) = v_xmm0;
    *(unsigned __int64 *)(a3) = v_xmm0;
    result = PopGetMostRecentWakeInfo(a1, a2, a1 + 2, v_rip + 3809140);
    a4 = 0;
    v_stack_p30 = result;
    if (result == 0) goto loc_0075C85E;
    if ((*(unsigned int *)(result + 40)) == 0) goto loc_0075C856;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 16))) == 0) goto loc_0075C96B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 16))) - (1));
    if (condition_is_equal) goto loc_0075C8A5;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0075C87C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0075C7FB;
    if (((unsigned int)(a2)) != 1) goto loc_0075C856;
    *(unsigned __int64 *)(a2) = v_xmm0;
loc_0075C73B:
    if ((*(unsigned __int16 *)(v_rip + 3815314)) == 0) goto loc_0075C74C;
    result = (v_rip + 3815314) + (a4 + 2);
    a1 = ((unsigned int)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C73B;
    goto loc_0075C768;
loc_0075C74C:
    result = ((unsigned int)(0x7FFFULL)) - (a1);
    if (a2 != 0) {
        result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
        *(unsigned __int64 *)(a2 + 8) = v_rip + 3815314;
        *(unsigned __int16 *)(a2) = (unsigned __int16)(result);
        result = (unsigned __int16)((result) + ((unsigned __int16)(a4 + 2)));
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(result);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 24))) == 0) goto loc_0075C7D3;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 24))) - (1));
    if (condition_is_equal) goto loc_0075C7A8;
    if (((unsigned int)(a1)) != 1) goto loc_0075C856;
    *(unsigned __int64 *)(a3) = v_xmm0;
loc_0075C790:
    if ((*(unsigned __int16 *)(v_rip + 3823209)) == 0) goto loc_0075C949;
    result = (v_rip + 3823209) + (a4 + 2);
    a1 = ((unsigned int)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C790;
    goto loc_0075C856;
loc_0075C7A8:
    *(unsigned __int64 *)(a3) = v_xmm0;
loc_0075C7BB:
    if ((*(unsigned __int16 *)(v_rip + 3823118)) == 0) goto loc_0075C949;
    result = (v_rip + 3823118) + (a4 + 2);
    a1 = ((unsigned int)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C7BB;
    goto loc_0075C856;
loc_0075C7D3:
    *(unsigned __int64 *)(a3) = v_xmm0;
loc_0075C7E6:
    if ((*(unsigned __int16 *)(v_rip + 3823027)) == 0) goto loc_0075C949;
    result = (v_rip + 3823027) + (a4 + 2);
    a1 = ((unsigned int)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C7E6;
    goto loc_0075C856;
loc_0075C7FB:
    *(unsigned __int64 *)(a2) = v_xmm0;
loc_0075C813:
    if ((*(unsigned __int16 *)(v_rip + 3822955)) == 0) goto loc_0075C824;
    result = (v_rip + 3822955) + (2);
    a1 = ((unsigned int)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C813;
    goto loc_0075C83D;
loc_0075C824:
    v_rbx = ((unsigned int)(0x7FFFULL)) - (a1);
    if (a2 != 0) {
        v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)(v_rbx)));
        *(unsigned __int64 *)(a2 + 8) = v_rip + 3822955;
        *(unsigned __int16 *)(a2) = (unsigned __int16)(v_rbx);
        v_rbx = (unsigned __int16)((v_rbx) + (2));
        *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(v_rbx);
    }
    result = PopGetCallerContextFromBuffer(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 24), v_stack_p8, 0, a5);
loc_0075C851:
loc_0075C856:
    result = PopWakeInfoDereference(a6, v_stack_p8, a6, a5);
loc_0075C85E:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0075C87C:
    *(unsigned __int64 *)(v_stack_p20) = v_xmm0;
loc_0075C894:
    if ((*(unsigned __int16 *)(v_rip + 3822810)) == ((unsigned __int16)(a5))) goto loc_0075C824;
    result = (v_rip + 3822810) + (2);
    a1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C894;
    goto loc_0075C83D;
loc_0075C8A5:
    *(unsigned __int64 *)(v_stack_p20) = v_xmm0;
loc_0075C8BD:
    if ((*(unsigned __int16 *)(v_rip + 3822945)) == ((unsigned __int16)(a5))) goto loc_0075C8CE;
    result = (v_rip + 3822945) + (2);
    a1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C8BD;
    goto loc_0075C8EA;
loc_0075C8CE:
    result = (v_stack_p10) - (a1);
    if (v_stack_p20 != 0) {
        result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
        *(unsigned __int64 *)(v_stack_p20 + 8) = v_rip + 3822945;
        *(unsigned __int16 *)(v_stack_p20) = (unsigned __int16)(result);
        result = (unsigned __int16)((result) + (2));
        *(unsigned __int16 *)(v_stack_p20 + 2) = (unsigned __int16)(result);
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 24))) - (1));
    if (condition_is_equal) goto loc_0075C922;
    if (((unsigned int)(a1)) != 1) goto loc_0075C856;
    *(unsigned __int64 *)(a3) = v_xmm0;
loc_0075C90E:
    if ((*(unsigned __int16 *)(v_rip + 3822907)) == ((unsigned __int16)(a5))) goto loc_0075C949;
    result = (v_rip + 3822907) + (2);
    a1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C90E;
    goto loc_0075C856;
loc_0075C922:
    *(unsigned __int64 *)(a3) = v_xmm0;
loc_0075C935:
    if ((*(unsigned __int16 *)(v_rip + 3822836)) == ((unsigned __int16)(a5))) goto loc_0075C949;
    result = (v_rip + 3822836) + (2);
    a1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C935;
    goto loc_0075C856;
loc_0075C949:
    v_rbx = (v_stack_p10) - (a1);
    if (a3 == 0) goto loc_0075C856;
    v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)(v_rbx)));
    *(unsigned __int64 *)(a3 + 8) = v_rip + 3822836;
    *(unsigned __int16 *)(a3) = (unsigned __int16)(v_rbx);
    v_rbx = (unsigned __int16)((v_rbx) + (2));
    *(unsigned __int16 *)(a3 + 2) = (unsigned __int16)(v_rbx);
    goto loc_0075C856;
loc_0075C96B:
    *(unsigned __int64 *)(v_stack_p20) = v_xmm0;
loc_0075C983:
    if ((*(unsigned __int16 *)(v_rip + 3808203)) == ((unsigned __int16)(a5))) goto loc_0075C994;
    result = (v_rip + 3808203) + (2);
    a1 = (v_rbx) - (1);
    if (condition_is_not_equal) goto loc_0075C983;
    goto loc_0075C9AD;
loc_0075C994:
    v_rbx = (v_rbx) - (a1);
    if (v_stack_p20 != 0) {
        v_rbx = (unsigned __int16)((v_rbx) + ((unsigned __int16)(v_rbx)));
        *(unsigned __int64 *)(v_stack_p20 + 8) = v_rip + 3808203;
        *(unsigned __int16 *)(v_stack_p20) = (unsigned __int16)(v_rbx);
        v_rbx = (unsigned __int16)((v_rbx) + (2));
        *(unsigned __int16 *)(v_stack_p20 + 2) = (unsigned __int16)(v_rbx);
    }
    *(unsigned __int64 *)(a3) = v_xmm0;
    result = PopCloneUnicodeString(v_stack_p18 + 40, 0, v_rip + 3808203, a5);
    v_rbx = 0;
    if (sign_flag) goto loc_0075C9D1;
    if ((*(unsigned __int16 *)(a4 + 2)) != 0) {
        *(unsigned __int8 *)(a6) = 1;
    }
    result = PopCloneUnicodeString(v_stack_p18 + 24, a5, v_rip + 3808203, a5);
    if (sign_flag) goto loc_0075C851;
    if ((*(unsigned __int16 *)(a5 + 2)) == 0) goto loc_0075C856;
    *(unsigned __int8 *)(a7) = 1;
    goto loc_0075C856;
}
```

## 5. (Beta) C Style

```c
int64_t PopQueryMostRecentWakeSourceInfo(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, void *Arg5, void *Arg6, void *Arg7)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (32);
    Arg1 = 0;
    *(uint8_t *)(arg6) = 0;
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint8_t *)(arg7) = 0;
loc_0075C68B:
    if ((*(uint16_t *)(v_rip + 0x3A1F74)) == 0) goto loc_0075C69B;
    result = (v_rip + 3809140) + (Arg1 + 2);
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(0x7FFFULL)))) - (1);
    if (condition_is_not_equal) goto loc_0075C68B;
    goto loc_0075C6B8;
loc_0075C69B:
    result = ((uint32_t)(0x7FFFULL)) - (Arg2);
    if (Arg2 != NULL) {
        result = (uint16_t)((result) + ((uint16_t)(result)));
        *(uint64_t *)(arg2 + 0x8) = v_rip + 3809140;
        *(uint16_t *)(arg2) = (uint16_t)(result);
        result = (uint16_t)((result) + ((uint16_t)(Arg1 + 2)));
        *(uint16_t *)(arg2 + 0x2) = (uint16_t)(result);
    }
    *(uint64_t *)(arg4) = v_xmm1;
    *(uint64_t *)(arg5) = v_xmm0;
    *(uint64_t *)(arg3) = v_xmm0;
    result = PopGetMostRecentWakeInfo(Arg1, Arg2, Arg1 + 2, v_rip + 3809140);
    Arg4 = 0;
    v_stack_p30 = result;
    if (result == 0) goto loc_0075C85E;
    if ((*(uint32_t *)(result + 0x28)) == 0) goto loc_0075C856;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x10))) == 0) goto loc_0075C96B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x10))) - (1));
    if (condition_is_equal) goto loc_0075C8A5;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0075C87C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0075C7FB;
    if (((uint32_t)(Arg2)) != 1) goto loc_0075C856;
    *(uint64_t *)(arg2) = v_xmm0;
loc_0075C73B:
    if ((*(uint16_t *)(v_rip + 0x3A3792)) == 0) goto loc_0075C74C;
    result = (v_rip + 3815314) + (Arg4 + 2);
    Arg1 = ((uint32_t)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C73B;
    goto loc_0075C768;
loc_0075C74C:
    result = ((uint32_t)(0x7FFFULL)) - (Arg1);
    if (Arg2 != NULL) {
        result = (uint16_t)((result) + ((uint16_t)(result)));
        *(uint64_t *)(arg2 + 0x8) = v_rip + 3815314;
        *(uint16_t *)(arg2) = (uint16_t)(result);
        result = (uint16_t)((result) + ((uint16_t)(Arg4 + 2)));
        *(uint16_t *)(arg2 + 0x2) = (uint16_t)(result);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x18))) == 0) goto loc_0075C7D3;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x18))) - (1));
    if (condition_is_equal) goto loc_0075C7A8;
    if (((uint32_t)(Arg1)) != 1) goto loc_0075C856;
    *(uint64_t *)(arg3) = v_xmm0;
loc_0075C790:
    if ((*(uint16_t *)(v_rip + 0x3A5669)) == 0) goto loc_0075C949;
    result = (v_rip + 3823209) + (Arg4 + 2);
    Arg1 = ((uint32_t)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C790;
    goto loc_0075C856;
loc_0075C7A8:
    *(uint64_t *)(arg3) = v_xmm0;
loc_0075C7BB:
    if ((*(uint16_t *)(v_rip + 0x3A560E)) == 0) goto loc_0075C949;
    result = (v_rip + 3823118) + (Arg4 + 2);
    Arg1 = ((uint32_t)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C7BB;
    goto loc_0075C856;
loc_0075C7D3:
    *(uint64_t *)(arg3) = v_xmm0;
loc_0075C7E6:
    if ((*(uint16_t *)(v_rip + 0x3A55B3)) == 0) goto loc_0075C949;
    result = (v_rip + 3823027) + (Arg4 + 2);
    Arg1 = ((uint32_t)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C7E6;
    goto loc_0075C856;
loc_0075C7FB:
    *(uint64_t *)(arg2) = v_xmm0;
loc_0075C813:
    if ((*(uint16_t *)(v_rip + 0x3A556B)) == 0) goto loc_0075C824;
    result = (v_rip + 3822955) + (2);
    Arg1 = ((uint32_t)(0x7FFFULL)) - (1);
    if (condition_is_not_equal) goto loc_0075C813;
    goto loc_0075C83D;
loc_0075C824:
    local_rbx = ((uint32_t)(0x7FFFULL)) - (Arg1);
    if (Arg2 != NULL) {
        local_rbx = (uint16_t)((local_rbx) + ((uint16_t)(local_rbx)));
        *(uint64_t *)(arg2 + 0x8) = v_rip + 3822955;
        *(uint16_t *)(arg2) = (uint16_t)(local_rbx);
        local_rbx = (uint16_t)((local_rbx) + (2));
        *(uint16_t *)(arg2 + 0x2) = (uint16_t)(local_rbx);
    }
    result = PopGetCallerContextFromBuffer(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x18), v_stack_p8, 0, Arg5);
loc_0075C851:
loc_0075C856:
    result = PopWakeInfoDereference(Arg6, v_stack_p8, Arg6, Arg5);
loc_0075C85E:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0075C87C:
    *(uint64_t *)(v_stack_p20) = v_xmm0;
loc_0075C894:
    if ((*(uint16_t *)(v_rip + 0x3A54DA)) == ((uint16_t)(Arg5))) goto loc_0075C824;
    result = (v_rip + 3822810) + (2);
    Arg1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C894;
    goto loc_0075C83D;
loc_0075C8A5:
    *(uint64_t *)(v_stack_p20) = v_xmm0;
loc_0075C8BD:
    if ((*(uint16_t *)(v_rip + 0x3A5561)) == ((uint16_t)(Arg5))) goto loc_0075C8CE;
    result = (v_rip + 3822945) + (2);
    Arg1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C8BD;
    goto loc_0075C8EA;
loc_0075C8CE:
    result = (v_stack_p10) - (Arg1);
    if (v_stack_p20 != 0) {
        result = (uint16_t)((result) + ((uint16_t)(result)));
        *(uint64_t *)(v_stack_p20 + 0x8) = v_rip + 3822945;
        *(uint16_t *)(v_stack_p20) = (uint16_t)(result);
        result = (uint16_t)((result) + (2));
        *(uint16_t *)(v_stack_p20 + 0x2) = (uint16_t)(result);
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x18))) - (1));
    if (condition_is_equal) goto loc_0075C922;
    if (((uint32_t)(Arg1)) != 1) goto loc_0075C856;
    *(uint64_t *)(arg3) = v_xmm0;
loc_0075C90E:
    if ((*(uint16_t *)(v_rip + 0x3A553B)) == ((uint16_t)(Arg5))) goto loc_0075C949;
    result = (v_rip + 3822907) + (2);
    Arg1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C90E;
    goto loc_0075C856;
loc_0075C922:
    *(uint64_t *)(arg3) = v_xmm0;
loc_0075C935:
    if ((*(uint16_t *)(v_rip + 0x3A54F4)) == ((uint16_t)(Arg5))) goto loc_0075C949;
    result = (v_rip + 3822836) + (2);
    Arg1 = (v_stack_p10) - (1);
    if (condition_is_not_equal) goto loc_0075C935;
    goto loc_0075C856;
loc_0075C949:
    local_rbx = (v_stack_p10) - (Arg1);
    if (Arg3 == NULL) goto loc_0075C856;
    local_rbx = (uint16_t)((local_rbx) + ((uint16_t)(local_rbx)));
    *(uint64_t *)(arg3 + 0x8) = v_rip + 3822836;
    *(uint16_t *)(arg3) = (uint16_t)(local_rbx);
    local_rbx = (uint16_t)((local_rbx) + (2));
    *(uint16_t *)(arg3 + 0x2) = (uint16_t)(local_rbx);
    goto loc_0075C856;
loc_0075C96B:
    *(uint64_t *)(v_stack_p20) = v_xmm0;
loc_0075C983:
    if ((*(uint16_t *)(v_rip + 0x3A1BCB)) == ((uint16_t)(Arg5))) goto loc_0075C994;
    result = (v_rip + 3808203) + (2);
    Arg1 = (local_rbx) - (1);
    if (condition_is_not_equal) goto loc_0075C983;
    goto loc_0075C9AD;
loc_0075C994:
    local_rbx = (local_rbx) - (Arg1);
    if (v_stack_p20 != 0) {
        local_rbx = (uint16_t)((local_rbx) + ((uint16_t)(local_rbx)));
        *(uint64_t *)(v_stack_p20 + 0x8) = v_rip + 3808203;
        *(uint16_t *)(v_stack_p20) = (uint16_t)(local_rbx);
        local_rbx = (uint16_t)((local_rbx) + (2));
        *(uint16_t *)(v_stack_p20 + 0x2) = (uint16_t)(local_rbx);
    }
    *(uint64_t *)(arg3) = v_xmm0;
    result = PopCloneUnicodeString(v_stack_p18 + 40, 0, v_rip + 3808203, Arg5);
    local_rbx = 0;
    if (sign_flag) goto loc_0075C9D1;
    if ((*(uint16_t *)(arg4 + 0x2)) != 0) {
        *(uint8_t *)(arg6) = 1;
    }
    result = PopCloneUnicodeString(v_stack_p18 + 24, Arg5, v_rip + 3808203, Arg5);
    if (sign_flag) goto loc_0075C851;
    if ((*(uint16_t *)(arg5 + 0x2)) == 0) goto loc_0075C856;
    *(uint8_t *)(arg7) = 1;
    goto loc_0075C856;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg3` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x0` | `128` | `R` |
| `Arg4` | `+ 0x2` | `16` | `R` |
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x2` | `16` | `R` |
| `Arg6` | `+ 0x0` | `8` | `W` |
| `Arg7` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0075C630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
