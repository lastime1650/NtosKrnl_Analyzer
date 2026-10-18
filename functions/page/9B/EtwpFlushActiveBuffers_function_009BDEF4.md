# EtwpFlushActiveBuffers

- RVA: `0x009BDEF4`–`0x009BE306` (길이 `1,042` bytes)
- VA: `0x00000001409BDEF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009F2D8`
- 디코드: `274`개 명령, `1,042/1,042` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **13**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009BDF3C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009BDF73` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009BDFC5` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (function, `0x003EB940`)
- `0x009BE01A` → [EtwpLockUnlockBufferList](../../text/41/EtwpLockUnlockBufferList_function_00419B88.md) (function, `0x00419B88`)
- `0x009BE05C` → [EtwpAdjustFreeBuffers](EtwpAdjustFreeBuffers_function_009BE91C.md) (function, `0x009BE91C`)
- `0x009BE064` → [EtwpWaitForBufferReferenceCount](EtwpWaitForBufferReferenceCount_function_009BDEC0.md) (function, `0x009BDEC0`)
- `0x009BE08B` → [EtwpFlushBuffer](EtwpFlushBuffer_function_009BF570.md) (function, `0x009BF570`)
- `0x009BE0AF` → [EtwpEnqueueAvailableBuffer](../../text/2F/EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (function, `0x002FE7DC`)
- `0x009BE0F8` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (function, `0x002FE6B0`)
- `0x009BE11A` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x009BE183` → [EtwpPrepareDirtyBuffer](../../text/2F/EtwpPrepareDirtyBuffer_function_002FE750.md) (function, `0x002FE750`)
- `0x009BE1E7` → [EtwpRealtimeSendEmptyMarker](EtwpRealtimeSendEmptyMarker_function_009BF4CC.md) (function, `0x009BF4CC`)
- `0x009BE2A6` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (function, `0x002FE6B0`)
- `0x009BE2EC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [EtwpLogger](EtwpLogger_function_009BE310.md) at `0x009BE4F3`
- [EtwpLogger](EtwpLogger_function_009BE310.md) at `0x009BE562`
- [EtwpLogger](EtwpLogger_function_009BE310.md) at `0x009BE6C8`
- [EtwpLogger](EtwpLogger_function_009BE310.md) at `0x009BE87A`

### Static image references
- `0x009BDF13` → RVA `0x00E0A740` (`.data`; read)
- `0x009BE10B` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x009BDF3C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009BDF73` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009BDFC5` → [EtwpQueryUsedProcessorCount](../../text/3E/EtwpQueryUsedProcessorCount_function_003EB940.md) (`PAGE` → `.text`)
  - `0x009BE01A` → [EtwpLockUnlockBufferList](../../text/41/EtwpLockUnlockBufferList_function_00419B88.md) (`PAGE` → `.text`)
  - `0x009BE0AF` → [EtwpEnqueueAvailableBuffer](../../text/2F/EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (`PAGE` → `.text`)
  - `0x009BE0F8` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (`PAGE` → `.text`)
  - `0x009BE11A` → [KeGetPrcb](../../text/2D/KeGetPrcb_function_002D85D0.md) (`PAGE` → `.text`)
  - `0x009BE183` → [EtwpPrepareDirtyBuffer](../../text/2F/EtwpPrepareDirtyBuffer_function_002FE750.md) (`PAGE` → `.text`)
  - `0x009BE2A6` → [EtwpRequestFlushTimer](../../text/2F/EtwpRequestFlushTimer_function_002FE6B0.md) (`PAGE` → `.text`)
  - `0x009BE2EC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x009BE28E` → [sub_00B2E9B2 + 0x1F](../B2/Unknown_function_00B2E9B2.md) (`tail-transfer`)
  - `0x009BE29C` → [sub_00B2E9B2 + 0x1F](../B2/Unknown_function_00B2E9B2.md) (`tail-transfer`)
  - `0x009BE2C3` → [sub_00B2E9B2](../B2/Unknown_function_00B2E9B2.md) (`tail-transfer`)
  - `0x009BE2C9` → [sub_00B2E9B2 + 0x11](../B2/Unknown_function_00B2E9B2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009BDEF4  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
009BDEF9  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
009BDEFE  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
009BDF03  57                              push rdi
009BDF04  41 54                           push r12
009BDF06  41 55                           push r13
009BDF08  41 56                           push r14
009BDF0A  41 57                           push r15
009BDF0C  48 81 EC 50 01 00 00            sub rsp, 0x150
009BDF13  48 8B 05 26 C8 44 00            mov rax, qword ptr [rip + 0x44c826]
009BDF1A  48 33 C4                        xor rax, rsp
009BDF1D  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009BDF25  44 8B EA                        mov r13d, edx
009BDF28  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
009BDF2C  48 8B F9                        mov rdi, rcx
009BDF2F  33 D2                           xor edx, edx
009BDF31  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
009BDF36  41 B8 00 01 00 00               mov r8d, 0x100
009BDF3C  E8 FF 8C D0 FF                  call 0x1406c6c40
009BDF41  45 33 C0                        xor r8d, r8d
009BDF44  4C 39 87 20 03 00 00            cmp qword ptr [rdi + 0x320], r8
009BDF4B  75 4D                           jne 0x1409bdf9a
009BDF4D  4C 39 87 68 01 00 00            cmp qword ptr [rdi + 0x168], r8
009BDF54  75 44                           jne 0x1409bdf9a
009BDF56  44 39 87 D0 00 00 00            cmp dword ptr [rdi + 0xd0], r8d
009BDF5D  0F 87 3E 03 00 00               ja 0x1409be2a1
009BDF63  B8 03 01 00 00                  mov eax, 0x103
009BDF68  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
009BDF70  48 33 CC                        xor rcx, rsp
009BDF73  E8 C8 E6 CE FF                  call 0x1406ac640
009BDF78  4C 8D 9C 24 50 01 00 00         lea r11, [rsp + 0x150]
009BDF80  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
009BDF84  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
009BDF88  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
009BDF8C  49 8B E3                        mov rsp, r11
009BDF8F  41 5F                           pop r15
009BDF91  41 5E                           pop r14
009BDF93  41 5D                           pop r13
009BDF95  41 5C                           pop r12
009BDF97  5F                              pop rdi
009BDF98  C3                              ret
009BDF99  CC                              int3
009BDF9A  48 8B 87 28 05 00 00            mov rax, qword ptr [rdi + 0x528]
009BDFA1  4C 8D 7C 24 40                  lea r15, [rsp + 0x40]
009BDFA6  48 85 C0                        test rax, rax
009BDFA9  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
009BDFAE  41 8B F0                        mov esi, r8d
009BDFB1  4C 0F 45 F8                     cmovne r15, rax
009BDFB5  F7 47 0C 00 00 04 00            test dword ptr [rdi + 0xc], 0x40000
009BDFBC  0F 85 EA 01 00 00               jne 0x1409be1ac
009BDFC2  48 8B CF                        mov rcx, rdi
009BDFC5  E8 76 D9 A2 FF                  call 0x1403eb940
009BDFCA  8B E8                           mov ebp, eax
009BDFCC  83 ED 01                        sub ebp, 1
009BDFCF  78 46                           js 0x1409be017
009BDFD1  4C 63 E5                        movsxd r12, ebp
009BDFD4  4D 8B F7                        mov r14, r15
009BDFD7  49 C1 E4 06                     shl r12, 6
009BDFDB  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
009BDFDE  0F BA E0 1C                     bt eax, 0x1c
009BDFE2  0F 83 1C 01 00 00               jae 0x1409be104
009BDFE8  48 8D 97 80 00 00 00            lea rdx, [rdi + 0x80]
009BDFEF  48 8B 1A                        mov rbx, qword ptr [rdx]
009BDFF2  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
009BDFF6  74 16                           je 0x1409be00e
009BDFF8  45 85 ED                        test r13d, r13d
009BDFFB  0F 85 3A 01 00 00               jne 0x1409be13b
009BE001  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
009BE005  48 85 C0                        test rax, rax
009BE008  0F 85 90 01 00 00               jne 0x1409be19e
009BE00E  49 83 EC 40                     sub r12, 0x40
009BE012  83 ED 01                        sub ebp, 1
009BE015  79 C4                           jns 0x1409bdfdb
009BE017  48 8B CF                        mov rcx, rdi
009BE01A  E8 69 BB A5 FF                  call 0x140419b88
009BE01F  45 33 C0                        xor r8d, r8d
009BE022  4D 8B F0                        mov r14, r8
009BE025  85 F6                           test esi, esi
009BE027  0F 8F C4 01 00 00               jg 0x1409be1f1
009BE02D  45 0F B7 F8                     movzx r15d, r8w
009BE031  41 8B E8                        mov ebp, r8d
009BE034  4D 85 F6                        test r14, r14
009BE037  0F 84 8F 01 00 00               je 0x1409be1cc
009BE03D  49 8B 1E                        mov rbx, qword ptr [r14]
009BE040  41 8B C0                        mov eax, r8d
009BE043  45 85 ED                        test r13d, r13d
009BE046  0F 95 C0                        setne al
009BE049  89 44 24 24                     mov dword ptr [rsp + 0x24], eax
009BE04D  48 85 DB                        test rbx, rbx
009BE050  49 8D 76 E0                     lea rsi, [r14 - 0x20]
009BE054  48 8B CF                        mov rcx, rdi
009BE057  66 44 0F 44 F8                  cmove r15w, ax
009BE05C  E8 BB 08 00 00                  call 0x1409be91c
009BE061  48 8B CE                        mov rcx, rsi
009BE064  E8 57 FE FF FF                  call 0x1409bdec0
009BE069  33 C9                           xor ecx, ecx
009BE06B  49 89 0E                        mov qword ptr [r14], rcx
009BE06E  44 8B E9                        mov r13d, ecx
009BE071  F7 47 0C 00 00 04 00            test dword ptr [rdi + 0xc], 0x40000
009BE078  0F 85 50 02 00 00               jne 0x1409be2ce
009BE07E  44 8B F1                        mov r14d, ecx
009BE081  45 0F B7 C7                     movzx r8d, r15w
009BE085  48 8B D6                        mov rdx, rsi
009BE088  48 8B CF                        mov rcx, rdi
009BE08B  E8 E0 14 00 00                  call 0x1409bf570
009BE090  8B 4F 0C                        mov ecx, dword ptr [rdi + 0xc]
009BE093  44 8B E0                        mov r12d, eax
009BE096  33 C0                           xor eax, eax
009BE098  48 8B D6                        mov rdx, rsi
009BE09B  66 89 46 34                     mov word ptr [rsi + 0x34], ax
009BE09F  0F BA E1 12                     bt ecx, 0x12
009BE0A3  0F 82 3A 02 00 00               jb 0x1409be2e3
009BE0A9  45 33 C0                        xor r8d, r8d
009BE0AC  48 8B CF                        mov rcx, rdi
009BE0AF  E8 28 07 94 FF                  call 0x1402fe7dc
009BE0B4  45 33 C0                        xor r8d, r8d
009BE0B7  4C 8B F3                        mov r14, rbx
009BE0BA  48 85 DB                        test rbx, rbx
009BE0BD  74 03                           je 0x1409be0c2
009BE0BF  48 8B 1B                        mov rbx, qword ptr [rbx]
009BE0C2  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
009BE0C6  45 85 E4                        test r12d, r12d
009BE0C9  41 0F 45 EC                     cmovne ebp, r12d
009BE0CD  4D 85 F6                        test r14, r14
009BE0D0  0F 85 77 FF FF FF               jne 0x1409be04d
009BE0D6  44 39 87 D0 00 00 00            cmp dword ptr [rdi + 0xd0], r8d
009BE0DD  76 1E                           jbe 0x1409be0fd
009BE0DF  44 39 44 24 28                  cmp dword ptr [rsp + 0x28], r8d
009BE0E4  74 17                           je 0x1409be0fd
009BE0E6  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
009BE0E9  0F BA E0 1C                     bt eax, 0x1c
009BE0ED  0F 82 03 02 00 00               jb 0x1409be2f6
009BE0F3  33 D2                           xor edx, edx
009BE0F5  48 8B CF                        mov rcx, rdi
009BE0F8  E8 B3 05 94 FF                  call 0x1402fe6b0
009BE0FD  8B C5                           mov eax, ebp
009BE0FF  E9 64 FE FF FF                  jmp 0x1409bdf68
009BE104  48 8B 87 50 05 00 00            mov rax, qword ptr [rdi + 0x550]
009BE10B  48 3B 05 96 89 60 00            cmp rax, qword ptr [rip + 0x608996]
009BE112  0F 85 98 01 00 00               jne 0x1409be2b0
009BE118  8B CD                           mov ecx, ebp
009BE11A  E8 B1 A4 91 FF                  call 0x1402d85d0
009BE11F  45 33 C0                        xor r8d, r8d
009BE122  48 8B 80 A8 8B 00 00            mov rax, qword ptr [rax + 0x8ba8]
009BE129  48 8B 80 40 01 00 00            mov rax, qword ptr [rax + 0x140]
009BE130  8B 0F                           mov ecx, dword ptr [rdi]
009BE132  48 8D 14 C8                     lea rdx, [rax + rcx*8]
009BE136  E9 B4 FE FF FF                  jmp 0x1409bdfef
009BE13B  8B 47 04                        mov eax, dword ptr [rdi + 4]
009BE13E  F0 0F C1 43 08                  lock xadd dword ptr [rbx + 8], eax
009BE143  3B 47 04                        cmp eax, dword ptr [rdi + 4]
009BE146  76 5F                           jbe 0x1409be1a7
009BE148  0F 0D 0A                        prefetchw byte ptr [rdx]
009BE14B  48 8B 0A                        mov rcx, qword ptr [rdx]
009BE14E  48 8B C1                        mov rax, rcx
009BE151  48 33 C3                        xor rax, rbx
009BE154  48 83 F8 0F                     cmp rax, 0xf
009BE158  77 0A                           ja 0x1409be164
009BE15A  48 8B C1                        mov rax, rcx
009BE15D  F0 4C 0F B1 02                  lock cmpxchg qword ptr [rdx], r8
009BE162  75 35                           jne 0x1409be199
009BE164  48 8B C1                        mov rax, rcx
009BE167  48 83 E0 F0                     and rax, 0xfffffffffffffff0
009BE16B  48 3B C3                        cmp rax, rbx
009BE16E  0F 85 4C 01 00 00               jne 0x1409be2c0
009BE174  83 E1 0F                        and ecx, 0xf
009BE177  F7 D9                           neg ecx
009BE179  F0 01 48 0C                     lock add dword ptr [rax + 0xc], ecx
009BE17D  48 8B D0                        mov rdx, rax
009BE180  48 8B CF                        mov rcx, rdi
009BE183  E8 C8 05 94 FF                  call 0x1402fe750
009BE188  45 33 C0                        xor r8d, r8d
009BE18B  49 89 1E                        mov qword ptr [r14], rbx
009BE18E  FF C6                           inc esi
009BE190  49 83 C6 08                     add r14, 8
009BE194  E9 75 FE FF FF                  jmp 0x1409be00e
009BE199  48 8B C8                        mov rcx, rax
009BE19C  EB B0                           jmp 0x1409be14e
009BE19E  49 89 06                        mov qword ptr [r14], rax
009BE1A1  4C 89 43 20                     mov qword ptr [rbx + 0x20], r8
009BE1A5  EB E7                           jmp 0x1409be18e
009BE1A7  89 43 04                        mov dword ptr [rbx + 4], eax
009BE1AA  EB 9C                           jmp 0x1409be148
009BE1AC  49 8B C0                        mov rax, r8
009BE1AF  48 87 87 80 00 00 00            xchg qword ptr [rdi + 0x80], rax
009BE1B6  48 85 C0                        test rax, rax
009BE1B9  0F 84 63 FE FF FF               je 0x1409be022
009BE1BF  49 89 07                        mov qword ptr [r15], rax
009BE1C2  BE 01 00 00 00                  mov esi, 1
009BE1C7  E9 56 FE FF FF                  jmp 0x1409be022
009BE1CC  45 85 ED                        test r13d, r13d
009BE1CF  0F 84 28 FF FF FF               je 0x1409be0fd
009BE1D5  8B 8F 30 03 00 00               mov ecx, dword ptr [rdi + 0x330]
009BE1DB  F6 C1 08                        test cl, 8
009BE1DE  0F 84 19 FF FF FF               je 0x1409be0fd
009BE1E4  48 8B CF                        mov rcx, rdi
009BE1E7  E8 E0 12 00 00                  call 0x1409bf4cc
009BE1EC  E9 0C FF FF FF                  jmp 0x1409be0fd
009BE1F1  48 63 DE                        movsxd rbx, esi
009BE1F4  49 8D 77 F8                     lea rsi, [r15 - 8]
009BE1F8  48 8D 34 DE                     lea rsi, [rsi + rbx*8]
009BE1FC  41 BA 01 00 00 00               mov r10d, 1
009BE202  4D 8B C8                        mov r9, r8
009BE205  49 3B DA                        cmp rbx, r10
009BE208  77 3B                           ja 0x1409be245
009BE20A  4B 8B 14 CF                     mov rdx, qword ptr [r15 + r9*8]
009BE20E  48 8D 4A 20                     lea rcx, [rdx + 0x20]
009BE212  48 8B 01                        mov rax, qword ptr [rcx]
009BE215  4B 89 04 CF                     mov qword ptr [r15 + r9*8], rax
009BE219  48 85 C0                        test rax, rax
009BE21C  74 17                           je 0x1409be235
009BE21E  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
009BE221  85 C0                           test eax, eax
009BE223  7E 5F                           jle 0x1409be284
009BE225  4C 89 31                        mov qword ptr [rcx], r14
009BE228  4C 8B F1                        mov r14, rcx
009BE22B  48 85 DB                        test rbx, rbx
009BE22E  7F CC                           jg 0x1409be1fc
009BE230  E9 F8 FD FF FF                  jmp 0x1409be02d
009BE235  48 8B 06                        mov rax, qword ptr [rsi]
009BE238  48 FF CB                        dec rbx
009BE23B  4B 89 04 CF                     mov qword ptr [r15 + r9*8], rax
009BE23F  48 83 EE 08                     sub rsi, 8
009BE243  EB D9                           jmp 0x1409be21e
009BE245  4D 8B D8                        mov r11, r8
009BE248  4E 8D 04 D5 00 00 00 00         lea r8, [r10*8]
009BE250  4B 8B 04 38                     mov rax, qword ptr [r8 + r15]
009BE254  48 8B 50 10                     mov rdx, qword ptr [rax + 0x10]
009BE258  4B 8B 04 3B                     mov rax, qword ptr [r11 + r15]
009BE25C  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
009BE260  49 8B C2                        mov rax, r10
009BE263  48 3B D1                        cmp rdx, rcx
009BE266  49 0F 4E C1                     cmovle rax, r9
009BE26A  49 FF C2                        inc r10
009BE26D  48 3B D1                        cmp rdx, rcx
009BE270  4C 8B C8                        mov r9, rax
009BE273  4D 0F 4E C3                     cmovle r8, r11
009BE277  4D 8B D8                        mov r11, r8
009BE27A  4C 3B D3                        cmp r10, rbx
009BE27D  7C C9                           jl 0x1409be248
009BE27F  45 33 C0                        xor r8d, r8d
009BE282  EB 86                           jmp 0x1409be20a
009BE284  8B 42 04                        mov eax, dword ptr [rdx + 4]
009BE287  83 F8 48                        cmp eax, 0x48
009BE28A  77 99                           ja 0x1409be225
009BE28C  85 C0                           test eax, eax
009BE28E  0F 85 3D 07 17 00               jne 0x140b2e9d1
009BE294  8B 42 08                        mov eax, dword ptr [rdx + 8]
009BE297  83 F8 48                        cmp eax, 0x48
009BE29A  77 89                           ja 0x1409be225
009BE29C  E9 30 07 17 00                  jmp 0x140b2e9d1
009BE2A1  33 D2                           xor edx, edx
009BE2A3  48 8B CF                        mov rcx, rdi
009BE2A6  E8 05 04 94 FF                  call 0x1402fe6b0
009BE2AB  E9 B3 FC FF FF                  jmp 0x1409bdf63
009BE2B0  48 8B 80 40 11 00 00            mov rax, qword ptr [rax + 0x1140]
009BE2B7  4A 8B 04 20                     mov rax, qword ptr [rax + r12]
009BE2BB  E9 70 FE FF FF                  jmp 0x1409be130
009BE2C0  48 85 C0                        test rax, rax
009BE2C3  0F 85 E9 06 17 00               jne 0x140b2e9b2
009BE2C9  E9 F5 06 17 00                  jmp 0x140b2e9c3
009BE2CE  4C 8B 6E 38                     mov r13, qword ptr [rsi + 0x38]
009BE2D2  4C 8B 76 40                     mov r14, qword ptr [rsi + 0x40]
009BE2D6  48 89 4E 38                     mov qword ptr [rsi + 0x38], rcx
009BE2DA  48 89 4E 40                     mov qword ptr [rsi + 0x40], rcx
009BE2DE  E9 9E FD FF FF                  jmp 0x1409be081
009BE2E3  4D 8B C6                        mov r8, r14
009BE2E6  41 8B CC                        mov ecx, r12d
009BE2E9  49 8B C5                        mov rax, r13
009BE2EC  E8 DF C7 CF FF                  call 0x1406baad0
009BE2F1  E9 BE FD FF FF                  jmp 0x1409be0b4
009BE2F6  44 38 44 24 20                  cmp byte ptr [rsp + 0x20], r8b
009BE2FB  0F 84 FC FD FF FF               je 0x1409be0fd
009BE301  E9 ED FD FF FF                  jmp 0x1409be0f3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpFlushActiveBuffers(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned __int8 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 4507686)) ^ (v_rsp);
    v_stack_m38 = result;
    v_stack_m150 = a2;
    a2 = 0;
    result = memset(v_stack_m138, a2, 256, a4);
    a3 = 0;
    if ((*(unsigned __int64 *)(a1 + 800)) != 0) goto loc_009BDF9A;
    if ((*(unsigned __int64 *)(a1 + 360)) != 0) goto loc_009BDF9A;
    if ((*(unsigned int *)(a1 + 208)) > 0) goto loc_009BE2A1;
loc_009BDF63:
loc_009BDF68:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_009BDF9A:
    v_stack_m130 = 0;
    v_r15 = v_stack_m110;
    if (*(unsigned __int64 *)(a1 + 1320) != 0) { v_r15 = *(unsigned __int64 *)(a1 + 1320); }
    if (((*(unsigned int *)(a1 + 12)) & (0x40000ULL)) != 0) goto loc_009BE1AC;
    result = EtwpQueryUsedProcessorCount(a1, a2, a3, a4);
    v_rbp = (unsigned int)(((unsigned int)((unsigned int)(result))) - (1));
    if (sign_flag) goto loc_009BE017;
    v_r12 = ((int)((unsigned int)(v_rbp))) << (6);
loc_009BDFDB:
    if (condition_is_above_or_equal) goto loc_009BE104;
loc_009BDFEF:
    v_rbx = (*(unsigned __int64 *)(a1 + 128)) & (-16);
    if (condition_is_equal) goto loc_009BE00E;
    if ((unsigned int)((unsigned int)(a2)) != 0) goto loc_009BE13B;
    if (*(unsigned __int64 *)(v_rbx + 32) != 0) goto loc_009BE19E;
loc_009BE00E:
    v_r12 = (v_r12) - (64);
    v_rbp = (unsigned int)((v_rbp) - (1));
    if (!sign_flag) goto loc_009BDFDB;
loc_009BE017:
    result = EtwpLockUnlockBufferList(a1, a1 + 128, a3, a4);
    a3 = 0;
loc_009BE022:
    if (condition_is_greater) goto loc_009BE1F1;
loc_009BE02D:
    if (0 == 0) goto loc_009BE1CC;
    result = ((unsigned int)((unsigned int)(a2)) != 0) ? 1 : 0;
    v_stack_m12C = (unsigned int)(result);
loc_009BE04D:
    v_r15 = 0;
    if (*(unsigned __int64 *)(0) == 0) { v_r15 = (unsigned __int16)(result); }
    result = EtwpAdjustFreeBuffers(a1, a1 + 128, a3, a4);
    result = EtwpWaitForBufferReferenceCount(0 - 32, a1 + 128, a3, a4);
    a1 = 0;
    *(unsigned __int64 *)(0) = 0;
    if (((*(unsigned int *)(a1 + 12)) & (0x40000ULL)) != 0) goto loc_009BE2CE;
loc_009BE081:
    result = EtwpFlushBuffer(0, 0 - 32, (unsigned __int16)(v_r15), a4);
    result = 0;
    *(unsigned __int16 *)(0 - 32 + 52) = 0;
    if (condition_is_below) goto loc_009BE2E3;
    a3 = 0;
    result = EtwpEnqueueAvailableBuffer(0, 0 - 32, a3, a4);
loc_009BE0B4:
    a3 = 0;
    v_rbx = *(unsigned __int64 *)(0);
    if (*(unsigned __int64 *)(0) != 0) {
        v_rbx = *(unsigned __int64 *)(*(unsigned __int64 *)(0));
    }
    v_rbp = 0;
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) { v_rbp = (unsigned int)((unsigned int)((unsigned int)(result))); }
    if (*(unsigned __int64 *)(0) != 0) goto loc_009BE04D;
    if ((*(unsigned int *)(a1 + 208)) <= 0) goto loc_009BE0FD;
    if (v_stack_m128 == 0) goto loc_009BE0FD;
    if (v_stack_m128 < 0) goto loc_009BE2F6;
loc_009BE0F3:
    a2 = 0;
    result = EtwpRequestFlushTimer(0, a2, a3, a4);
loc_009BE0FD:
    goto loc_009BDF68;
loc_009BE104:
    if ((*(unsigned __int64 *)(a1 + 1360)) != (*(unsigned __int64 *)(v_rip + 6326678))) goto loc_009BE2B0;
    result = KeGetPrcb((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    a3 = 0;
loc_009BE130:
    goto loc_009BDFEF;
loc_009BE13B:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) <= (*(unsigned int *)(a1 + 4))) goto loc_009BE1A7;
loc_009BE148:
loc_009BE14E:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 35752) + 320) + (unsigned int)(*(unsigned int *)(a1)) * 8)) ^ (v_rbx);
    if (result > 15) goto loc_009BE164;
    if (result != 15) goto loc_009BE199;
loc_009BE164:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 35752) + 320) + (unsigned int)(*(unsigned int *)(a1)) * 8)) & (-16);
    if (result != v_rbx) goto loc_009BE2C0;
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 35752) + 320) + (unsigned int)(*(unsigned int *)(a1)) * 8)) & (15));
    a1 = (unsigned int)(-(a1));
    result = EtwpPrepareDirtyBuffer(a1, result, a3, a4);
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(0)) = v_rbx;
loc_009BE18E:
    v_rsi = (unsigned int)((0 - 32) + 1);
    v_r14 = (*(unsigned __int64 *)(0)) + (8);
    goto loc_009BE00E;
loc_009BE199:
    goto loc_009BE14E;
loc_009BE19E:
    *(unsigned __int64 *)(v_r14) = result;
    *(unsigned __int64 *)(v_rbx + 32) = 0;
    goto loc_009BE18E;
loc_009BE1A7:
    *(unsigned int *)(v_rbx + 4) = (unsigned int)(result);
    goto loc_009BE148;
loc_009BE1AC:
    if (0 == 0) goto loc_009BE022;
    *(unsigned __int64 *)(v_r15) = 0;
    goto loc_009BE022;
loc_009BE1CC:
    if (0 == 0) goto loc_009BE0FD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (8)) == 0) goto loc_009BE0FD;
    result = EtwpRealtimeSendEmptyMarker(a1, result, a3, a4);
    goto loc_009BE0FD;
loc_009BE1F1:
loc_009BE1FC:
    if (((int)(1)) > 1) goto loc_009BE245;
loc_009BE20A:
    *(unsigned __int64 *)(v_r15 + 0 * 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 0 * 8) + 32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 0 * 8) + 32) == 0) goto loc_009BE235;
loc_009BE21E:
    if (condition_is_less_or_equal) goto loc_009BE284;
loc_009BE225:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 0 * 8) + 32) = v_r14;
    if (condition_is_greater) goto loc_009BE1FC;
    goto loc_009BE02D;
loc_009BE235:
    v_rbx = ((int)(1)) - 1;
    *(unsigned __int64 *)(v_r15 + 0 * 8) = *(unsigned __int64 *)(v_r15 - 8 + (int)(1) * 8);
    v_rsi = (v_r15 - 8 + (int)(1) * 8) - (8);
    goto loc_009BE21E;
loc_009BE245:
loc_009BE248:
    result = 1;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(1 * 8 + v_r15 * 1) + 16)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + v_r15 * 1) + 16))) { result = 0; }
    v_r10 = (1) + 1;
    a3 = 1 * 8;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(1 * 8 + v_r15 * 1) + 16)) <= (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + v_r15 * 1) + 16))) { a3 = 0; }
    if (v_r10 < v_rbx) goto loc_009BE248;
    a3 = 0;
    goto loc_009BE20A;
loc_009BE284:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(1 * 8 + v_r15 * 1) + 16) + 4)))) > 72) goto loc_009BE225;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(1 * 8 + v_r15 * 1) + 16) + 8)))) > 72) goto loc_009BE225;
loc_009BE2A1:
    a2 = 0;
    result = EtwpRequestFlushTimer(a1, a2, a3, result);
    goto loc_009BDF63;
loc_009BE2B0:
    goto loc_009BE130;
loc_009BE2C0:
loc_009BE2CE:
    *(unsigned __int64 *)(v_rsi + 56) = a1;
    *(unsigned __int64 *)(v_rsi + 64) = a1;
    goto loc_009BE081;
loc_009BE2E3:
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a2, *(unsigned __int64 *)(v_rsi + 64), result);
    goto loc_009BE0B4;
loc_009BE2F6:
    if (v_stack_m130 == ((unsigned __int8)(*(unsigned __int64 *)(v_rsi + 64)))) goto loc_009BE0FD;
    goto loc_009BE0F3;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpFlushActiveBuffers(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m110;
    uint32_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint8_t v_stack_m130;
    uint64_t v_stack_m138;
    uint32_t v_stack_m150;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x44C826)) ^ (local_rsp);
    v_stack_m38 = result;
    v_stack_m150 = Arg2;
    Arg2 = 0;
    result = memset(v_stack_m138, Arg2, 256, a4);
    a3 = 0;
    if ((*(uint64_t *)(arg1 + 0x320)) != 0) goto loc_009BDF9A;
    if ((*(uint64_t *)(arg1 + 0x168)) != 0) goto loc_009BDF9A;
    if ((*(uint32_t *)(arg1 + 0xD0)) > 0) goto loc_009BE2A1;
loc_009BDF63:
loc_009BDF68:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_009BDF9A:
    v_stack_m130 = 0;
    local_r15 = v_stack_m110;
    if (*(uint64_t *)(arg1 + 0x528) != 0) { local_r15 = *(uint64_t *)(arg1 + 0x528); }
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x40000ULL)) != 0) goto loc_009BE1AC;
    result = EtwpQueryUsedProcessorCount(Arg1, Arg2, a3, a4);
    local_rbp = (uint32_t)(((uint32_t)((uint32_t)(result))) - (1));
    if (sign_flag) goto loc_009BE017;
    local_r12 = ((int32_t)((uint32_t)(local_rbp))) << (6);
loc_009BDFDB:
    if (condition_is_above_or_equal) goto loc_009BE104;
loc_009BDFEF:
    local_rbx = (*(uint64_t *)(arg1 + 0x80)) & (-16);
    if (condition_is_equal) goto loc_009BE00E;
    if ((uint32_t)((uint32_t)(Arg2)) != 0) goto loc_009BE13B;
    if (*(uint64_t *)(local_rbx + 0x20) != 0) goto loc_009BE19E;
loc_009BE00E:
    local_r12 = (local_r12) - (64);
    local_rbp = (uint32_t)((local_rbp) - (1));
    if (!sign_flag) goto loc_009BDFDB;
loc_009BE017:
    result = EtwpLockUnlockBufferList(Arg1, Arg1 + 128, a3, a4);
    a3 = 0;
loc_009BE022:
    if (condition_is_greater) goto loc_009BE1F1;
loc_009BE02D:
    if (0 == 0) goto loc_009BE1CC;
    result = ((uint32_t)((uint32_t)(Arg2)) != 0) ? 1 : 0;
    v_stack_m12C = (uint32_t)(result);
loc_009BE04D:
    local_r15 = 0;
    if (*(uint64_t *)(0) == 0) { local_r15 = (uint16_t)(result); }
    result = EtwpAdjustFreeBuffers(Arg1, Arg1 + 128, a3, a4);
    result = EtwpWaitForBufferReferenceCount(0 - 32, Arg1 + 128, a3, a4);
    Arg1 = 0;
    *(uint64_t *)(0) = 0;
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x40000ULL)) != 0) goto loc_009BE2CE;
loc_009BE081:
    result = EtwpFlushBuffer(0, 0 - 32, (uint16_t)(local_r15), a4);
    result = 0;
    *(uint16_t *)(0 - 0x20 + 0x34) = 0;
    if (condition_is_below) goto loc_009BE2E3;
    a3 = 0;
    result = EtwpEnqueueAvailableBuffer(0, 0 - 32, a3, a4);
loc_009BE0B4:
    a3 = 0;
    local_rbx = *(uint64_t *)(0);
    if (*(uint64_t *)(0) != 0) {
        local_rbx = *(uint64_t *)(*(uint64_t *)(0));
    }
    local_rbp = 0;
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) { local_rbp = (uint32_t)((uint32_t)((uint32_t)(result))); }
    if (*(uint64_t *)(0) != 0) goto loc_009BE04D;
    if ((*(uint32_t *)(arg1 + 0xD0)) <= 0) goto loc_009BE0FD;
    if (v_stack_m128 == 0) goto loc_009BE0FD;
    if (v_stack_m128 < 0) goto loc_009BE2F6;
loc_009BE0F3:
    Arg2 = 0;
    result = EtwpRequestFlushTimer(0, Arg2, a3, a4);
loc_009BE0FD:
    goto loc_009BDF68;
loc_009BE104:
    if ((*(uint64_t *)(arg1 + 0x550)) != (*(uint64_t *)(v_rip + 0x608996))) goto loc_009BE2B0;
    result = KeGetPrcb((uint32_t)((uint32_t)(local_rbp)), Arg2, a3, a4);
    a3 = 0;
loc_009BE130:
    goto loc_009BDFEF;
loc_009BE13B:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) <= (*(uint32_t *)(arg1 + 0x4))) goto loc_009BE1A7;
loc_009BE148:
loc_009BE14E:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8BA8) + 0x140) + (uint32_t)(*(uint32_t *)(arg1)) * 8)) ^ (local_rbx);
    if (result > 15) goto loc_009BE164;
    if (result != 15) goto loc_009BE199;
loc_009BE164:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8BA8) + 0x140) + (uint32_t)(*(uint32_t *)(arg1)) * 8)) & (-16);
    if (result != local_rbx) goto loc_009BE2C0;
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8BA8) + 0x140) + (uint32_t)(*(uint32_t *)(arg1)) * 8)) & (15));
    Arg1 = (uint32_t)(-(Arg1));
    result = EtwpPrepareDirtyBuffer(Arg1, result, a3, a4);
    a3 = 0;
    *(uint64_t *)(*(uint64_t *)(0)) = local_rbx;
loc_009BE18E:
    local_rsi = (uint32_t)((0 - 32) + 1);
    local_r14 = (*(uint64_t *)(0)) + (8);
    goto loc_009BE00E;
loc_009BE199:
    goto loc_009BE14E;
loc_009BE19E:
    *(uint64_t *)(local_r14) = result;
    *(uint64_t *)(local_rbx + 0x20) = 0;
    goto loc_009BE18E;
loc_009BE1A7:
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)(result);
    goto loc_009BE148;
loc_009BE1AC:
    if (0 == 0) goto loc_009BE022;
    *(uint64_t *)(local_r15) = 0;
    goto loc_009BE022;
loc_009BE1CC:
    if (0 == 0) goto loc_009BE0FD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (8)) == 0) goto loc_009BE0FD;
    result = EtwpRealtimeSendEmptyMarker(Arg1, result, a3, a4);
    goto loc_009BE0FD;
loc_009BE1F1:
loc_009BE1FC:
    if (((int32_t)(1)) > 1) goto loc_009BE245;
loc_009BE20A:
    *(uint64_t *)(local_r15 + 0x0 * 8) = *(uint64_t *)(*(uint64_t *)(local_r15 + 0x0 * 8) + 0x20);
    if (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x0 * 8) + 0x20) == 0) goto loc_009BE235;
loc_009BE21E:
    if (condition_is_less_or_equal) goto loc_009BE284;
loc_009BE225:
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x0 * 8) + 0x20) = local_r14;
    if (condition_is_greater) goto loc_009BE1FC;
    goto loc_009BE02D;
loc_009BE235:
    local_rbx = ((int32_t)(1)) - 1;
    *(uint64_t *)(local_r15 + 0x0 * 8) = *(uint64_t *)(local_r15 - 0x8 + (int32_t)(1) * 8);
    local_rsi = (local_r15 - 8 + (int32_t)(1) * 8) - (8);
    goto loc_009BE21E;
loc_009BE245:
loc_009BE248:
    result = 1;
    if ((*(uint64_t *)(*(uint64_t *)(1 * 8 + local_r15 * 1) + 0x10)) <= (*(uint64_t *)(*(uint64_t *)(0 + local_r15 * 1) + 0x10))) { result = 0; }
    local_r10 = (1) + 1;
    a3 = 1 * 8;
    if ((*(uint64_t *)(*(uint64_t *)(1 * 8 + local_r15 * 1) + 0x10)) <= (*(uint64_t *)(*(uint64_t *)(0 + local_r15 * 1) + 0x10))) { a3 = 0; }
    if (local_r10 < local_rbx) goto loc_009BE248;
    a3 = 0;
    goto loc_009BE20A;
loc_009BE284:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(1 * 8 + local_r15 * 1) + 0x10) + 0x4)))) > 72) goto loc_009BE225;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(1 * 8 + local_r15 * 1) + 0x10) + 0x8)))) > 72) goto loc_009BE225;
loc_009BE2A1:
    Arg2 = 0;
    result = EtwpRequestFlushTimer(Arg1, Arg2, a3, result);
    goto loc_009BDF63;
loc_009BE2B0:
    goto loc_009BE130;
loc_009BE2C0:
loc_009BE2CE:
    *(void **)(local_rsi + 0x38) = Arg1;
    *(void **)(local_rsi + 0x40) = Arg1;
    goto loc_009BE081;
loc_009BE2E3:
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg2, *(uint64_t *)(local_rsi + 0x40), result);
    goto loc_009BE0B4;
loc_009BE2F6:
    if (v_stack_m130 == ((uint8_t)(*(uint64_t *)(local_rsi + 0x40)))) goto loc_009BE0FD;
    goto loc_009BE0F3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R/W` |
| `Arg1` | `+ 0xD0` | `32` | `R` |
| `Arg1` | `+ 0x168` | `64` | `R` |
| `Arg1` | `+ 0x320` | `64` | `R` |
| `Arg1` | `+ 0x330` | `32` | `R` |
| `Arg1` | `+ 0x528` | `64` | `R` |
| `Arg1` | `+ 0x550` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BDEF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
