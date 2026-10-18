# SepParseElamCertResources

- RVA: `0x00AAC43C`–`0x00AAC85F` (길이 `1,059` bytes)
- VA: `0x0000000140AAC43C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BBEF0`
- 디코드: `304`개 명령, `1,059/1,059` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00AAC6CE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AAC78C` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00AAC7F2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AAC813` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x00AAC838` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SeRegisterElamCertResources](../79/SeRegisterElamCertResources_function_0079B8C8.md) at `0x0079B94A`

### Static image references
- `0x00AAC45B` → RVA `0x00E0A740` (`.data`; read)
- `0x00AAC7C7` → RVA `0x00F04E90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x00AAC6CE` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AAC78C` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00AAC7F2` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AAC813` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (`PAGE` → `.text`)
  - `0x00AAC838` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAC43C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00AAC441  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
00AAC446  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AAC44B  57                              push rdi
00AAC44C  41 54                           push r12
00AAC44E  41 55                           push r13
00AAC450  41 56                           push r14
00AAC452  41 57                           push r15
00AAC454  48 81 EC 50 02 00 00            sub rsp, 0x250
00AAC45B  48 8B 05 DE E2 35 00            mov rax, qword ptr [rip + 0x35e2de]
00AAC462  48 33 C4                        xor rax, rsp
00AAC465  48 89 84 24 40 02 00 00         mov qword ptr [rsp + 0x240], rax
00AAC46D  45 33 D2                        xor r10d, r10d
00AAC470  48 8D 42 FE                     lea rax, [rdx - 2]
00AAC474  45 8B C2                        mov r8d, r10d
00AAC477  41 BB 0D 00 00 C0               mov r11d, 0xc000000d
00AAC47D  48 3D FD FF 00 00               cmp rax, 0xfffd
00AAC483  0F 87 A1 03 00 00               ja 0x140aac82a
00AAC489  0F B7 01                        movzx eax, word ptr [rcx]
00AAC48C  4C 8D 24 11                     lea r12, [rcx + rdx]
00AAC490  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00AAC494  48 8D 71 02                     lea rsi, [rcx + 2]
00AAC498  45 8B EA                        mov r13d, r10d
00AAC49B  BF 20 00 00 00                  mov edi, 0x20
00AAC4A0  8D 5F E2                        lea ebx, [rdi - 0x1e]
00AAC4A3  44 3B E8                        cmp r13d, eax
00AAC4A6  0F 83 73 03 00 00               jae 0x140aac81f
00AAC4AC  48 8D 46 02                     lea rax, [rsi + 2]
00AAC4B0  49 3B C4                        cmp rax, r12
00AAC4B3  0F 87 71 03 00 00               ja 0x140aac82a
00AAC4B9  49 8B CC                        mov rcx, r12
00AAC4BC  48 2B CE                        sub rcx, rsi
00AAC4BF  48 D1 E9                        shr rcx, 1
00AAC4C2  48 85 F6                        test rsi, rsi
00AAC4C5  0F 84 5F 03 00 00               je 0x140aac82a
00AAC4CB  48 81 F9 FF FF FF 7F            cmp rcx, 0x7fffffff
00AAC4D2  0F 87 52 03 00 00               ja 0x140aac82a
00AAC4D8  48 8B D1                        mov rdx, rcx
00AAC4DB  48 8B C6                        mov rax, rsi
00AAC4DE  48 85 C9                        test rcx, rcx
00AAC4E1  74 0F                           je 0x140aac4f2
00AAC4E3  66 44 39 10                     cmp word ptr [rax], r10w
00AAC4E7  74 09                           je 0x140aac4f2
00AAC4E9  48 03 C3                        add rax, rbx
00AAC4EC  48 83 EA 01                     sub rdx, 1
00AAC4F0  75 F1                           jne 0x140aac4e3
00AAC4F2  48 8B C2                        mov rax, rdx
00AAC4F5  48 F7 D8                        neg rax
00AAC4F8  1B C0                           sbb eax, eax
00AAC4FA  F7 D0                           not eax
00AAC4FC  41 23 C3                        and eax, r11d
00AAC4FF  48 85 D2                        test rdx, rdx
00AAC502  74 05                           je 0x140aac509
00AAC504  48 2B CA                        sub rcx, rdx
00AAC507  EB 03                           jmp 0x140aac50c
00AAC509  49 8B CA                        mov rcx, r10
00AAC50C  48 85 D2                        test rdx, rdx
00AAC50F  0F 84 18 03 00 00               je 0x140aac82d
00AAC515  4C 8D 79 01                     lea r15, [rcx + 1]
00AAC519  4E 8D 3C 7E                     lea r15, [rsi + r15*2]
00AAC51D  4D 8D 77 02                     lea r14, [r15 + 2]
00AAC521  4D 3B F4                        cmp r14, r12
00AAC524  0F 83 00 03 00 00               jae 0x140aac82a
00AAC52A  41 8B EA                        mov ebp, r10d
00AAC52D  41 B1 01                        mov r9b, 1
00AAC530  66 44 39 16                     cmp word ptr [rsi], r10w
00AAC534  0F 84 F0 00 00 00               je 0x140aac62a
00AAC53A  83 FD 40                        cmp ebp, 0x40
00AAC53D  0F 83 E7 02 00 00               jae 0x140aac82a
00AAC543  8B C5                           mov eax, ebp
00AAC545  45 84 C9                        test r9b, r9b
00AAC548  75 16                           jne 0x140aac560
00AAC54A  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00AAC552  4C 03 C0                        add r8, rax
00AAC555  41 8A 10                        mov dl, byte ptr [r8]
00AAC558  C0 E2 04                        shl dl, 4
00AAC55B  41 88 10                        mov byte ptr [r8], dl
00AAC55E  EB 1B                           jmp 0x140aac57b
00AAC560  48 83 F8 40                     cmp rax, 0x40
00AAC564  0F 83 A9 02 00 00               jae 0x140aac813
00AAC56A  4C 8D 84 24 80 00 00 00         lea r8, [rsp + 0x80]
00AAC572  41 8A D2                        mov dl, r10b
00AAC575  4C 03 C0                        add r8, rax
00AAC578  45 88 10                        mov byte ptr [r8], r10b
00AAC57B  0F B7 0E                        movzx ecx, word ptr [rsi]
00AAC57E  83 F9 41                        cmp ecx, 0x41
00AAC581  77 3E                           ja 0x140aac5c1
00AAC583  74 60                           je 0x140aac5e5
00AAC585  83 F9 34                        cmp ecx, 0x34
00AAC588  77 15                           ja 0x140aac59f
00AAC58A  74 30                           je 0x140aac5bc
00AAC58C  2B CF                           sub ecx, edi
00AAC58E  74 05                           je 0x140aac595
00AAC590  83 E9 10                        sub ecx, 0x10
00AAC593  EB 12                           jmp 0x140aac5a7
00AAC595  45 84 C9                        test r9b, r9b
00AAC598  75 7C                           jne 0x140aac616
00AAC59A  E9 8B 02 00 00                  jmp 0x140aac82a
00AAC59F  83 E9 35                        sub ecx, 0x35
00AAC5A2  74 18                           je 0x140aac5bc
00AAC5A4  83 E9 01                        sub ecx, 1
00AAC5A7  74 13                           je 0x140aac5bc
00AAC5A9  83 E9 01                        sub ecx, 1
00AAC5AC  74 0E                           je 0x140aac5bc
00AAC5AE  83 E9 01                        sub ecx, 1
00AAC5B1  74 09                           je 0x140aac5bc
00AAC5B3  83 F9 01                        cmp ecx, 1
00AAC5B6  0F 85 6E 02 00 00               jne 0x140aac82a
00AAC5BC  80 EA 30                        sub dl, 0x30
00AAC5BF  EB 49                           jmp 0x140aac60a
00AAC5C1  83 F9 61                        cmp ecx, 0x61
00AAC5C4  77 24                           ja 0x140aac5ea
00AAC5C6  74 3F                           je 0x140aac607
00AAC5C8  83 E9 42                        sub ecx, 0x42
00AAC5CB  74 18                           je 0x140aac5e5
00AAC5CD  83 E9 01                        sub ecx, 1
00AAC5D0  74 13                           je 0x140aac5e5
00AAC5D2  83 E9 01                        sub ecx, 1
00AAC5D5  74 0E                           je 0x140aac5e5
00AAC5D7  83 E9 01                        sub ecx, 1
00AAC5DA  74 09                           je 0x140aac5e5
00AAC5DC  83 F9 01                        cmp ecx, 1
00AAC5DF  0F 85 45 02 00 00               jne 0x140aac82a
00AAC5E5  80 EA 37                        sub dl, 0x37
00AAC5E8  EB 20                           jmp 0x140aac60a
00AAC5EA  83 E9 62                        sub ecx, 0x62
00AAC5ED  74 18                           je 0x140aac607
00AAC5EF  83 E9 01                        sub ecx, 1
00AAC5F2  74 13                           je 0x140aac607
00AAC5F4  83 E9 01                        sub ecx, 1
00AAC5F7  74 0E                           je 0x140aac607
00AAC5F9  83 E9 01                        sub ecx, 1
00AAC5FC  74 09                           je 0x140aac607
00AAC5FE  83 F9 01                        cmp ecx, 1
00AAC601  0F 85 23 02 00 00               jne 0x140aac82a
00AAC607  80 EA 57                        sub dl, 0x57
00AAC60A  02 16                           add dl, byte ptr [rsi]
00AAC60C  41 88 10                        mov byte ptr [r8], dl
00AAC60F  45 84 C9                        test r9b, r9b
00AAC612  75 02                           jne 0x140aac616
00AAC614  FF C5                           inc ebp
00AAC616  66 39 3E                        cmp word ptr [rsi], di
00AAC619  74 07                           je 0x140aac622
00AAC61B  45 84 C9                        test r9b, r9b
00AAC61E  41 0F 94 C1                     sete r9b
00AAC622  48 03 F3                        add rsi, rbx
00AAC625  E9 06 FF FF FF                  jmp 0x140aac530
00AAC62A  45 84 C9                        test r9b, r9b
00AAC62D  0F 84 F7 01 00 00               je 0x140aac82a
00AAC633  41 0F B7 0F                     movzx ecx, word ptr [r15]
00AAC637  81 E9 04 80 00 00               sub ecx, 0x8004
00AAC63D  74 13                           je 0x140aac652
00AAC63F  83 E9 08                        sub ecx, 8
00AAC642  74 0E                           je 0x140aac652
00AAC644  83 E9 01                        sub ecx, 1
00AAC647  74 09                           je 0x140aac652
00AAC649  83 F9 01                        cmp ecx, 1
00AAC64C  0F 85 D8 01 00 00               jne 0x140aac82a
00AAC652  49 8B CC                        mov rcx, r12
00AAC655  49 2B CE                        sub rcx, r14
00AAC658  48 D1 E9                        shr rcx, 1
00AAC65B  4D 85 F6                        test r14, r14
00AAC65E  0F 84 C6 01 00 00               je 0x140aac82a
00AAC664  48 81 F9 FF FF FF 7F            cmp rcx, 0x7fffffff
00AAC66B  0F 87 B9 01 00 00               ja 0x140aac82a
00AAC671  48 8B D1                        mov rdx, rcx
00AAC674  49 8B C6                        mov rax, r14
00AAC677  48 85 C9                        test rcx, rcx
00AAC67A  74 0F                           je 0x140aac68b
00AAC67C  66 44 39 10                     cmp word ptr [rax], r10w
00AAC680  74 09                           je 0x140aac68b
00AAC682  48 03 C3                        add rax, rbx
00AAC685  48 83 EA 01                     sub rdx, 1
00AAC689  75 F1                           jne 0x140aac67c
00AAC68B  48 8B C2                        mov rax, rdx
00AAC68E  48 F7 D8                        neg rax
00AAC691  1B C0                           sbb eax, eax
00AAC693  F7 D0                           not eax
00AAC695  41 23 C3                        and eax, r11d
00AAC698  48 85 D2                        test rdx, rdx
00AAC69B  74 05                           je 0x140aac6a2
00AAC69D  48 2B CA                        sub rcx, rdx
00AAC6A0  EB 03                           jmp 0x140aac6a5
00AAC6A2  49 8B CA                        mov rcx, r10
00AAC6A5  48 85 D2                        test rdx, rdx
00AAC6A8  0F 84 7F 01 00 00               je 0x140aac82d
00AAC6AE  48 8D 59 01                     lea rbx, [rcx + 1]
00AAC6B2  41 8B FA                        mov edi, r10d
00AAC6B5  49 8D 1C 5F                     lea rbx, [r15 + rbx*2]
00AAC6B9  48 8D 73 02                     lea rsi, [rbx + 2]
00AAC6BD  48 85 C9                        test rcx, rcx
00AAC6C0  0F 84 FE 00 00 00               je 0x140aac7c4
00AAC6C6  BA 3B 00 00 00                  mov edx, 0x3b
00AAC6CB  49 8B CE                        mov rcx, r14
00AAC6CE  E8 8D 53 A5 FF                  call 0x140501a60
00AAC6D3  45 33 D2                        xor r10d, r10d
00AAC6D6  48 85 C0                        test rax, rax
00AAC6D9  48 0F 45 D8                     cmovne rbx, rax
00AAC6DD  48 85 DB                        test rbx, rbx
00AAC6E0  0F 84 D7 00 00 00               je 0x140aac7bd
00AAC6E6  48 8B C3                        mov rax, rbx
00AAC6E9  49 2B C6                        sub rax, r14
00AAC6EC  48 D1 F8                        sar rax, 1
00AAC6EF  48 83 F8 40                     cmp rax, 0x40
00AAC6F3  0F 83 2B 01 00 00               jae 0x140aac824
00AAC6F9  45 8B C2                        mov r8d, r10d
00AAC6FC  41 B9 02 00 00 00               mov r9d, 2
00AAC702  4C 3B F3                        cmp r14, rbx
00AAC705  74 23                           je 0x140aac72a
00AAC707  8B D7                           mov edx, edi
00AAC709  48 C1 E2 06                     shl rdx, 6
00AAC70D  41 0F B7 06                     movzx eax, word ptr [r14]
00AAC711  4D 03 F1                        add r14, r9
00AAC714  41 8B C8                        mov ecx, r8d
00AAC717  41 FF C0                        inc r8d
00AAC71A  48 03 CA                        add rcx, rdx
00AAC71D  66 89 84 4C C0 00 00 00         mov word ptr [rsp + rcx*2 + 0xc0], ax
00AAC725  4C 3B F3                        cmp r14, rbx
00AAC728  75 E3                           jne 0x140aac70d
00AAC72A  41 8B C0                        mov eax, r8d
00AAC72D  66 45 03 C0                     add r8w, r8w
00AAC731  8B CF                           mov ecx, edi
00AAC733  48 C1 E1 06                     shl rcx, 6
00AAC737  48 03 C8                        add rcx, rax
00AAC73A  8B D7                           mov edx, edi
00AAC73C  48 C1 E2 07                     shl rdx, 7
00AAC740  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00AAC748  48 03 C2                        add rax, rdx
00AAC74B  66 44 89 94 4C C0 00 00 00      mov word ptr [rsp + rcx*2 + 0xc0], r10w
00AAC754  8B CF                           mov ecx, edi
00AAC756  48 03 C9                        add rcx, rcx
00AAC759  66 44 89 44 CC 48               mov word ptr [rsp + rcx*8 + 0x48], r8w
00AAC75F  66 45 03 C1                     add r8w, r9w
00AAC763  66 44 89 44 CC 4A               mov word ptr [rsp + rcx*8 + 0x4a], r8w
00AAC769  48 89 44 CC 50                  mov qword ptr [rsp + rcx*8 + 0x50], rax
00AAC76E  0F B7 03                        movzx eax, word ptr [rbx]
00AAC771  66 85 C0                        test ax, ax
00AAC774  74 45                           je 0x140aac7bb
00AAC776  49 03 D9                        add rbx, r9
00AAC779  0F B7 03                        movzx eax, word ptr [rbx]
00AAC77C  66 85 C0                        test ax, ax
00AAC77F  74 3A                           je 0x140aac7bb
00AAC781  BA 3B 00 00 00                  mov edx, 0x3b
00AAC786  48 8B CB                        mov rcx, rbx
00AAC789  4C 8B F3                        mov r14, rbx
00AAC78C  E8 CF 52 A5 FF                  call 0x140501a60
00AAC791  45 33 D2                        xor r10d, r10d
00AAC794  48 8B D8                        mov rbx, rax
00AAC797  48 85 C0                        test rax, rax
00AAC79A  75 12                           jne 0x140aac7ae
00AAC79C  48 83 C8 FF                     or rax, 0xffffffffffffffff
00AAC7A0  48 FF C0                        inc rax
00AAC7A3  66 45 39 14 46                  cmp word ptr [r14 + rax*2], r10w
00AAC7A8  75 F6                           jne 0x140aac7a0
00AAC7AA  49 8D 1C 46                     lea rbx, [r14 + rax*2]
00AAC7AE  FF C7                           inc edi
00AAC7B0  83 FF 03                        cmp edi, 3
00AAC7B3  0F 82 24 FF FF FF               jb 0x140aac6dd
00AAC7B9  EB 02                           jmp 0x140aac7bd
00AAC7BB  FF C7                           inc edi
00AAC7BD  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00AAC7C2  EB 03                           jmp 0x140aac7c7
00AAC7C4  49 8B CA                        mov rcx, r10
00AAC7C7  48 8B 05 C2 86 45 00            mov rax, qword ptr [rip + 0x4586c2]
00AAC7CE  48 85 C0                        test rax, rax
00AAC7D1  74 46                           je 0x140aac819
00AAC7D3  45 0F B7 0F                     movzx r9d, word ptr [r15]
00AAC7D7  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
00AAC7DF  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00AAC7E4  44 8B C5                        mov r8d, ebp
00AAC7E7  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00AAC7EB  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00AAC7F0  B1 07                           mov cl, 7
00AAC7F2  E8 D9 E2 C0 FF                  call 0x1406baad0
00AAC7F7  45 33 D2                        xor r10d, r10d
00AAC7FA  44 8B C0                        mov r8d, eax
00AAC7FD  85 C0                           test eax, eax
00AAC7FF  78 1E                           js 0x140aac81f
00AAC801  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
00AAC805  41 FF C5                        inc r13d
00AAC808  41 BB 0D 00 00 C0               mov r11d, 0xc000000d
00AAC80E  E9 88 FC FF FF                  jmp 0x140aac49b
00AAC813  E8 C4 97 A4 FF                  call 0x1404f5fdc
00AAC818  CC                              int3
00AAC819  41 B8 BB 00 00 C0               mov r8d, 0xc00000bb
00AAC81F  41 8B C0                        mov eax, r8d
00AAC822  EB 09                           jmp 0x140aac82d
00AAC824  41 BB 0D 00 00 C0               mov r11d, 0xc000000d
00AAC82A  41 8B C3                        mov eax, r11d
00AAC82D  48 8B 8C 24 40 02 00 00         mov rcx, qword ptr [rsp + 0x240]
00AAC835  48 33 CC                        xor rcx, rsp
00AAC838  E8 03 FE BF FF                  call 0x1406ac640
00AAC83D  4C 8D 9C 24 50 02 00 00         lea r11, [rsp + 0x250]
00AAC845  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00AAC849  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00AAC84D  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00AAC851  49 8B E3                        mov rsp, r11
00AAC854  41 5F                           pop r15
00AAC856  41 5E                           pop r14
00AAC858  41 5D                           pop r13
00AAC85A  41 5C                           pop r12
00AAC85C  5F                              pop rdi
00AAC85D  C3                              ret
00AAC85E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepParseElamCertResources(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (592);
    result = (*(unsigned __int64 *)(v_rip + 3531486)) ^ (v_rsp);
    v_stack_m38 = result;
    v_r10 = 0;
    if ((a2 - 2) > 0xFFFDULL) goto loc_00AAC82A;
    v_stack_m238 = (unsigned int)(*(unsigned __int16 *)(a1));
loc_00AAC49B:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(a1)))) goto loc_00AAC81F;
    if ((a1 + 2 + 2) > (a1 + a2 * 1)) goto loc_00AAC82A;
    a1 = (a1 + a2 * 1) - (a1 + 2);
    a1 = (a1) >> (1);
    if (a1 + 2 == 0) goto loc_00AAC82A;
    if (a1 > 0x7FFFFFFFULL) goto loc_00AAC82A;
    if (a1 == 0) goto loc_00AAC4F2;
loc_00AAC4E3:
    if ((*(unsigned __int16 *)(a1 + 2)) == 0) goto loc_00AAC4F2;
    result = (a1 + 2) + (32 - 30);
    a2 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00AAC4E3;
loc_00AAC4F2:
    result = -(a2);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC000000DULL))));
    if (a2 == 0) goto loc_00AAC509;
    a1 = (a1) - (a2);
    goto loc_00AAC50C;
loc_00AAC509:
loc_00AAC50C:
    if (a2 == 0) goto loc_00AAC82D;
    if ((a1 + 2 + 0 + 1 * 2 + 2) >= (a1 + a2 * 1)) goto loc_00AAC82A;
loc_00AAC530:
    if ((*(unsigned __int16 *)(a1 + 2)) == 0) goto loc_00AAC62A;
    if (0 >= 64) goto loc_00AAC82A;
    if (1 != 0) goto loc_00AAC560;
    a3 = (v_stack_m1F8) + (0);
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a3)) << (4));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    goto loc_00AAC57B;
loc_00AAC560:
    if (0 >= 64) goto loc_00AAC813;
    a3 = (v_stack_m1F8) + (0);
    *(unsigned __int8 *)(a3) = 0;
loc_00AAC57B:
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) > 65) goto loc_00AAC5C1;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) == 65) goto loc_00AAC5E5;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) > 52) goto loc_00AAC59F;
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) == 52) goto loc_00AAC5BC;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 2)) - (32));
    if (condition_is_equal) goto loc_00AAC595;
    a1 = (unsigned int)((a1) - (16));
    goto loc_00AAC5A7;
loc_00AAC595:
    if (1 != 0) goto loc_00AAC616;
    goto loc_00AAC82A;
loc_00AAC59F:
    a1 = (unsigned int)((a1) - (53));
    if (condition_is_equal) goto loc_00AAC5BC;
    a1 = (unsigned int)((a1) - (1));
loc_00AAC5A7:
    if (condition_is_equal) goto loc_00AAC5BC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC5BC;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC5BC;
    if (((unsigned int)(a1)) != 1) goto loc_00AAC82A;
loc_00AAC5BC:
    a2 = (unsigned __int8)((0) - (48));
    goto loc_00AAC60A;
loc_00AAC5C1:
    if (((unsigned int)(a1)) > 97) goto loc_00AAC5EA;
    if (((unsigned int)(a1)) == 97) goto loc_00AAC607;
    a1 = (unsigned int)((a1) - (66));
    if (condition_is_equal) goto loc_00AAC5E5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    if (((unsigned int)(a1)) != 1) goto loc_00AAC82A;
loc_00AAC5E5:
    a2 = (unsigned __int8)((a2) - (55));
    goto loc_00AAC60A;
loc_00AAC5EA:
    a1 = (unsigned int)((a1) - (98));
    if (condition_is_equal) goto loc_00AAC607;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    if (((unsigned int)(a1)) != 1) goto loc_00AAC82A;
loc_00AAC607:
    a2 = (unsigned __int8)((a2) - (87));
loc_00AAC60A:
    a2 = (unsigned __int8)((a2) + (*(unsigned __int8 *)(a1 + 2)));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    v_rbp = 0;
    if (1 == 0) {
        v_rbp = (unsigned int)((0) + 1);
    }
    if ((*(unsigned __int16 *)(a1 + 2)) != 32) {
        a4 = (1 == 0) ? 1 : 0;
    }
    v_rsi = (a1 + 2) + (32 - 30);
    goto loc_00AAC530;
loc_00AAC62A:
    if ((unsigned __int8)(a4) == 0) goto loc_00AAC82A;
    a1 = (unsigned int)((*(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2)) - (0x8004ULL));
    if (condition_is_equal) goto loc_00AAC652;
    a1 = (unsigned int)((a1) - (8));
    if (condition_is_equal) goto loc_00AAC652;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00AAC652;
    if (((unsigned int)(a1)) != 1) goto loc_00AAC82A;
loc_00AAC652:
    a1 = (a1 + a2 * 1) - (a1 + 2 + 0 + 1 * 2 + 2);
    a1 = (a1) >> (1);
    if (a1 + 2 + 0 + 1 * 2 + 2 == 0) goto loc_00AAC82A;
    if (a1 > 0x7FFFFFFFULL) goto loc_00AAC82A;
    if (a1 == 0) goto loc_00AAC68B;
loc_00AAC67C:
    if ((*(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2 + 2)) == 0) goto loc_00AAC68B;
    result = (a1 + 2 + 0 + 1 * 2 + 2) + (32 - 30);
    a2 = (a1) - (1);
    if (condition_is_not_equal) goto loc_00AAC67C;
loc_00AAC68B:
    result = -(a2);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xC000000DULL))));
    if (a2 == 0) goto loc_00AAC6A2;
    a1 = (a1) - (a2);
    goto loc_00AAC6A5;
loc_00AAC6A2:
loc_00AAC6A5:
    if (a2 == 0) goto loc_00AAC82D;
    if (0 == 0) goto loc_00AAC7C4;
    result = wcschr(a1 + 2 + 0 + 1 * 2 + 2, 59, a3, a4);
    v_r10 = 0;
    v_rbx = a1 + 2 + 0 + 1 * 2 + 0 + 1 * 2;
    if (result != 0) { v_rbx = result; }
loc_00AAC6DD:
    if (v_rbx == 0) goto loc_00AAC7BD;
    result = (v_rbx) - (a1 + 2 + 0 + 1 * 2 + 2);
    result = (result) >> (1);
    if (result >= 64) goto loc_00AAC824;
    if ((a1 + 2 + 0 + 1 * 2 + 2) == v_rbx) goto loc_00AAC72A;
    a2 = (0) << (6);
loc_00AAC70D:
    v_r14 = (a1 + 2 + 0 + 1 * 2 + 2) + (2);
    a3 = (unsigned int)((0) + 1);
    a1 = (0) + (a2);
    *(unsigned __int16 *)(v_rsp + a1 * 2 + 192) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2 + 2));
    if (v_r14 != v_rbx) goto loc_00AAC70D;
loc_00AAC72A:
    a3 = (unsigned __int16)((a3) + ((unsigned __int16)(a3)));
    a1 = (0) << (6);
    a1 = (a1) + ((unsigned int)((unsigned int)(a3)));
    a2 = (0) << (7);
    result = (v_stack_m1B8) + (a2);
    *(unsigned __int16 *)(v_rsp + a1 * 2 + 192) = 0;
    a1 = (0) + (0);
    *(unsigned __int16 *)(v_rsp + a1 * 8 + 72) = (unsigned __int16)(a3);
    a3 = (unsigned __int16)((a3) + (2));
    *(unsigned __int16 *)(v_rsp + a1 * 8 + 74) = (unsigned __int16)(a3);
    *(unsigned __int64 *)(v_rsp + a1 * 8 + 80) = result;
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AAC7BB;
    v_rbx = (v_rbx) + (2);
    if ((unsigned __int16)(*(unsigned __int16 *)(v_rbx)) == 0) goto loc_00AAC7BB;
    result = wcschr(v_rbx, 59, a3, 2);
    v_r10 = 0;
    if (result != 0) goto loc_00AAC7AE;
    result = (result) | (-1);
loc_00AAC7A0:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rbx + result * 2)) != 0) goto loc_00AAC7A0;
loc_00AAC7AE:
    v_rdi = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rdi)) < 3) goto loc_00AAC6DD;
    goto loc_00AAC7BD;
loc_00AAC7BB:
    v_rdi = (unsigned int)((v_rdi) + 1);
loc_00AAC7BD:
    goto loc_00AAC7C7;
loc_00AAC7C4:
loc_00AAC7C7:
    if (*(unsigned __int64 *)(v_rip + 4556482) == 0) goto loc_00AAC819;
    v_stack_m248 = 0;
    v_stack_m250 = (unsigned int)(v_rdi);
    v_stack_m258 = 0;
    result = guard_dispatch_icall(7, v_stack_m1F8, (unsigned int)((unsigned int)(v_rbp)), *(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2));
    v_r10 = 0;
    if (sign_flag) goto loc_00AAC81F;
    v_r13 = (unsigned int)((0) + 1);
    goto loc_00AAC49B;
loc_00AAC813:
    result = _report_rangecheckfailure(7, v_stack_m1F8, (unsigned int)((unsigned int)(result)), *(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2));
loc_00AAC819:
loc_00AAC81F:
    goto loc_00AAC82D;
loc_00AAC824:
loc_00AAC82A:
loc_00AAC82D:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m1F8, (unsigned int)(0xC00000BBULL), *(unsigned __int16 *)(a1 + 2 + 0 + 1 * 2));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepParseElamCertResources(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m230;
    uint32_t v_stack_m238;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (592);
    result = (*(uint64_t *)(v_rip + 0x35E2DE)) ^ (local_rsp);
    v_stack_m38 = result;
    local_r10 = 0;
    if ((Arg2 - 2) > 0xFFFDULL) goto loc_00AAC82A;
    v_stack_m238 = (uint32_t)(*(uint16_t *)(arg1));
loc_00AAC49B:
    if (0 >= ((uint32_t)(*(uint16_t *)(arg1)))) goto loc_00AAC81F;
    if ((Arg1 + 2 + 2) > (Arg1 + Arg2 * 1)) goto loc_00AAC82A;
    Arg1 = (Arg1 + Arg2 * 1) - (Arg1 + 2);
    Arg1 = (Arg1) >> (1);
    if (Arg1 + 2 == 0) goto loc_00AAC82A;
    if (Arg1 > 0x7FFFFFFFULL) goto loc_00AAC82A;
    if (Arg1 == NULL) goto loc_00AAC4F2;
loc_00AAC4E3:
    if ((*(uint16_t *)(arg1 + 0x2)) == 0) goto loc_00AAC4F2;
    result = (Arg1 + 2) + (32 - 30);
    Arg2 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00AAC4E3;
loc_00AAC4F2:
    result = -(Arg2);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC000000DULL))));
    if (Arg2 == NULL) goto loc_00AAC509;
    Arg1 = (Arg1) - (Arg2);
    goto loc_00AAC50C;
loc_00AAC509:
loc_00AAC50C:
    if (Arg2 == NULL) goto loc_00AAC82D;
    if ((Arg1 + 2 + 0 + 1 * 2 + 2) >= (Arg1 + Arg2 * 1)) goto loc_00AAC82A;
loc_00AAC530:
    if ((*(uint16_t *)(arg1 + 0x2)) == 0) goto loc_00AAC62A;
    if (0 >= 64) goto loc_00AAC82A;
    if (1 != 0) goto loc_00AAC560;
    a3 = (v_stack_m1F8) + (0);
    Arg2 = (uint8_t)((*(uint8_t *)(a3)) << (4));
    *(uint8_t *)(a3) = (uint8_t)(Arg2);
    goto loc_00AAC57B;
loc_00AAC560:
    if (0 >= 64) goto loc_00AAC813;
    a3 = (v_stack_m1F8) + (0);
    *(uint8_t *)(a3) = 0;
loc_00AAC57B:
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) > 65) goto loc_00AAC5C1;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) == 65) goto loc_00AAC5E5;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) > 52) goto loc_00AAC59F;
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) == 52) goto loc_00AAC5BC;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x2)) - (32));
    if (condition_is_equal) goto loc_00AAC595;
    Arg1 = (uint32_t)((Arg1) - (16));
    goto loc_00AAC5A7;
loc_00AAC595:
    if (1 != 0) goto loc_00AAC616;
    goto loc_00AAC82A;
loc_00AAC59F:
    Arg1 = (uint32_t)((Arg1) - (53));
    if (condition_is_equal) goto loc_00AAC5BC;
    Arg1 = (uint32_t)((Arg1) - (1));
loc_00AAC5A7:
    if (condition_is_equal) goto loc_00AAC5BC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC5BC;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC5BC;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AAC82A;
loc_00AAC5BC:
    Arg2 = (uint8_t)((0) - (48));
    goto loc_00AAC60A;
loc_00AAC5C1:
    if (((uint32_t)(Arg1)) > 97) goto loc_00AAC5EA;
    if (((uint32_t)(Arg1)) == 97) goto loc_00AAC607;
    Arg1 = (uint32_t)((Arg1) - (66));
    if (condition_is_equal) goto loc_00AAC5E5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC5E5;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AAC82A;
loc_00AAC5E5:
    Arg2 = (uint8_t)((Arg2) - (55));
    goto loc_00AAC60A;
loc_00AAC5EA:
    Arg1 = (uint32_t)((Arg1) - (98));
    if (condition_is_equal) goto loc_00AAC607;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC607;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AAC82A;
loc_00AAC607:
    Arg2 = (uint8_t)((Arg2) - (87));
loc_00AAC60A:
    Arg2 = (uint8_t)((Arg2) + (*(uint8_t *)(arg1 + 0x2)));
    *(uint8_t *)(a3) = (uint8_t)(Arg2);
    local_rbp = 0;
    if (1 == 0) {
        local_rbp = (uint32_t)((0) + 1);
    }
    if ((*(uint16_t *)(arg1 + 0x2)) != 32) {
        a4 = (1 == 0) ? 1 : 0;
    }
    local_rsi = (Arg1 + 2) + (32 - 30);
    goto loc_00AAC530;
loc_00AAC62A:
    if ((uint8_t)(a4) == 0) goto loc_00AAC82A;
    Arg1 = (uint32_t)((*(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2)) - (0x8004ULL));
    if (condition_is_equal) goto loc_00AAC652;
    Arg1 = (uint32_t)((Arg1) - (8));
    if (condition_is_equal) goto loc_00AAC652;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00AAC652;
    if (((uint32_t)(Arg1)) != 1) goto loc_00AAC82A;
loc_00AAC652:
    Arg1 = (Arg1 + Arg2 * 1) - (Arg1 + 2 + 0 + 1 * 2 + 2);
    Arg1 = (Arg1) >> (1);
    if (Arg1 + 2 + 0 + 1 * 2 + 2 == 0) goto loc_00AAC82A;
    if (Arg1 > 0x7FFFFFFFULL) goto loc_00AAC82A;
    if (Arg1 == NULL) goto loc_00AAC68B;
loc_00AAC67C:
    if ((*(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2 + 0x2)) == 0) goto loc_00AAC68B;
    result = (Arg1 + 2 + 0 + 1 * 2 + 2) + (32 - 30);
    Arg2 = (Arg1) - (1);
    if (condition_is_not_equal) goto loc_00AAC67C;
loc_00AAC68B:
    result = -(Arg2);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xC000000DULL))));
    if (Arg2 == NULL) goto loc_00AAC6A2;
    Arg1 = (Arg1) - (Arg2);
    goto loc_00AAC6A5;
loc_00AAC6A2:
loc_00AAC6A5:
    if (Arg2 == NULL) goto loc_00AAC82D;
    if (0 == 0) goto loc_00AAC7C4;
    result = wcschr(Arg1 + 2 + 0 + 1 * 2 + 2, 59, a3, a4);
    local_r10 = 0;
    local_rbx = Arg1 + 2 + 0 + 1 * 2 + 0 + 1 * 2;
    if (result != 0) { local_rbx = result; }
loc_00AAC6DD:
    if (local_rbx == 0) goto loc_00AAC7BD;
    result = (local_rbx) - (Arg1 + 2 + 0 + 1 * 2 + 2);
    result = (result) >> (1);
    if (result >= 64) goto loc_00AAC824;
    if ((Arg1 + 2 + 0 + 1 * 2 + 2) == local_rbx) goto loc_00AAC72A;
    Arg2 = (0) << (6);
loc_00AAC70D:
    local_r14 = (Arg1 + 2 + 0 + 1 * 2 + 2) + (2);
    a3 = (uint32_t)((0) + 1);
    Arg1 = (0) + (Arg2);
    *(uint16_t *)(local_rsp + arg1 * 2 + 0xC0) = (uint16_t)(*(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2 + 0x2));
    if (local_r14 != local_rbx) goto loc_00AAC70D;
loc_00AAC72A:
    a3 = (uint16_t)((a3) + ((uint16_t)(a3)));
    Arg1 = (0) << (6);
    Arg1 = (Arg1) + ((uint32_t)((uint32_t)(a3)));
    Arg2 = (0) << (7);
    result = (v_stack_m1B8) + (Arg2);
    *(uint16_t *)(local_rsp + arg1 * 2 + 0xC0) = 0;
    Arg1 = (0) + (0);
    *(uint16_t *)(local_rsp + arg1 * 8 + 0x48) = (uint16_t)(a3);
    a3 = (uint16_t)((a3) + (2));
    *(uint16_t *)(local_rsp + arg1 * 8 + 0x4A) = (uint16_t)(a3);
    *(uint64_t *)(local_rsp + arg1 * 8 + 0x50) = result;
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AAC7BB;
    local_rbx = (local_rbx) + (2);
    if ((uint16_t)(*(uint16_t *)(local_rbx)) == 0) goto loc_00AAC7BB;
    result = wcschr(local_rbx, 59, a3, 2);
    local_r10 = 0;
    if (result != 0) goto loc_00AAC7AE;
    result = (result) | (-1);
loc_00AAC7A0:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rbx + result * 2)) != 0) goto loc_00AAC7A0;
loc_00AAC7AE:
    local_rdi = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rdi)) < 3) goto loc_00AAC6DD;
    goto loc_00AAC7BD;
loc_00AAC7BB:
    local_rdi = (uint32_t)((local_rdi) + 1);
loc_00AAC7BD:
    goto loc_00AAC7C7;
loc_00AAC7C4:
loc_00AAC7C7:
    if (*(uint64_t *)(v_rip + 0x4586C2) == 0) goto loc_00AAC819;
    v_stack_m248 = 0;
    v_stack_m250 = (uint32_t)(local_rdi);
    v_stack_m258 = 0;
    result = guard_dispatch_icall(7, v_stack_m1F8, (uint32_t)((uint32_t)(local_rbp)), *(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2));
    local_r10 = 0;
    if (sign_flag) goto loc_00AAC81F;
    local_r13 = (uint32_t)((0) + 1);
    goto loc_00AAC49B;
loc_00AAC813:
    result = _report_rangecheckfailure(7, v_stack_m1F8, (uint32_t)((uint32_t)(result)), *(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2));
loc_00AAC819:
loc_00AAC81F:
    goto loc_00AAC82D;
loc_00AAC824:
loc_00AAC82A:
loc_00AAC82D:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m1F8, (uint32_t)(0xC00000BBULL), *(uint16_t *)(arg1 + 0x2 + 0x0 + 0x1 * 2));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0 + rdx*1` | `64` | `R` |
| `Arg1` | `+ 0x2` | `64` | `R` |
| `Arg2` | `- 0x2` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAC43C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
