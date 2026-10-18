# SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmFeAddComplete

- RVA: `0x002DFEE0`–`0x002E0318` (길이 `1,080` bytes)
- VA: `0x00000001402DFEE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00070B4C`
- 디코드: `266`개 명령, `1,080/1,080` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002DFF20` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x002DFF9A` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002DFFBF` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x002DFFF8` → [B_TREE<_SM_PAGE_KEY,SMKM_STORE_MGR<SM_TRAITS>::SMKM_FRONTEND_ENTRY,4096,B_TREE_DUMMY_NODE_POOL,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../2E/B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS_SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TREE__function_002E07C0.md) (function, `0x002E07C0`)
- `0x002E010B` → [B_TREE<_SM_PAGE_KEY,SMKM_STORE_MGR<SM_TRAITS>::SMKM_FRONTEND_ENTRY,4096,B_TREE_DUMMY_NODE_POOL,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeIteratorFromSearchResult](../2E/B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS_SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TREE__function_002E07E0.md) (function, `0x002E07E0`)
- `0x002E019E` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x002E01C3` → [KiCheckForKernelApcDelivery](../2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x002E01CF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x002E0258` → [B_TREE<_SM_PAGE_KEY,SMKM_STORE_MGR<SM_TRAITS>::SMKM_FRONTEND_ENTRY,4096,B_TREE_DUMMY_NODE_POOL,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeDeleteEx](../26/B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS_SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TREE__function_00266C00.md) (function, `0x00266C00`)
- `0x002E02A3` → [ExfTryToWakePushLock](../26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x002E02D3` → [SmArrayGrow](../3A/SmArrayGrow_function_003AC6C8.md) (function, `0x003AC6C8`)
- `0x002E02FB` → [B_TREE<_SM_PAGE_KEY,SMKM_STORE_MGR<SM_TRAITS>::SMKM_FRONTEND_ENTRY,4096,B_TREE_DUMMY_NODE_POOL,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeSearchResultDeref](../2E/B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS_SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TREE__function_002E07C0.md) (function, `0x002E07C0`)

### Direct callers
- [sub_006D8E6C](../6D/Unknown_function_006D8E6C.md) at `0x006D8E88`

### Static image references
- `0x002DFEFC` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002E0305` → [sub_006DDF40](../6D/Unknown_function_006DDF40.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002DFEE0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
002DFEE5  55                              push rbp
002DFEE6  56                              push rsi
002DFEE7  57                              push rdi
002DFEE8  41 54                           push r12
002DFEEA  41 55                           push r13
002DFEEC  41 56                           push r14
002DFEEE  41 57                           push r15
002DFEF0  48 8D 6C 24 E1                  lea rbp, [rsp - 0x1f]
002DFEF5  48 81 EC 00 01 00 00            sub rsp, 0x100
002DFEFC  48 8B 05 3D A8 B2 00            mov rax, qword ptr [rip + 0xb2a83d]
002DFF03  48 33 C4                        xor rax, rsp
002DFF06  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
002DFF0A  8B 1A                           mov ebx, dword ptr [rdx]
002DFF0C  4C 8B F9                        mov r15, rcx
002DFF0F  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
002DFF14  48 8D 4D 87                     lea rcx, [rbp - 0x79]
002DFF18  33 D2                           xor edx, edx
002DFF1A  41 B8 80 00 00 00               mov r8d, 0x80
002DFF20  E8 1B 6D 3E 00                  call 0x1406c6c40
002DFF25  44 8B 6D 7F                     mov r13d, dword ptr [rbp + 0x7f]
002DFF29  48 8D 45 87                     lea rax, [rbp - 0x79]
002DFF2D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002DFF32  45 33 E4                        xor r12d, r12d
002DFF35  41 8B C5                        mov eax, r13d
002DFF38  48 C7 44 24 48 00 00 00 00      mov qword ptr [rsp + 0x48], 0
002DFF41  83 E0 01                        and eax, 1
002DFF44  48 C7 44 24 50 00 00 00 00      mov qword ptr [rsp + 0x50], 0
002DFF4D  48 C7 44 24 60 00 00 00 00      mov qword ptr [rsp + 0x60], 0
002DFF56  0F 57 C0                        xorps xmm0, xmm0
002DFF59  C7 44 24 58 00 00 00 00         mov dword ptr [rsp + 0x58], 0
002DFF61  45 8D 74 24 01                  lea r14d, [r12 + 1]
002DFF66  C7 44 24 5C 08 00 00 00         mov dword ptr [rsp + 0x5c], 8
002DFF6E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
002DFF72  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
002DFF77  41 F6 C5 02                     test r13b, 2
002DFF7B  75 50                           jne 0x1402dffcd
002DFF7D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002DFF86  49 8D 8F B8 01 00 00            lea rcx, [r15 + 0x1b8]
002DFF8D  45 33 C0                        xor r8d, r8d
002DFF90  33 D2                           xor edx, edx
002DFF92  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
002DFF99  90                              nop
002DFF9A  E8 91 02 F3 FF                  call 0x140210230
002DFF9F  F0 49 0F BA AF B8 01 00 00 00   lock bts qword ptr [r15 + 0x1b8], 0
002DFFA9  48 8B F0                        mov rsi, rax
002DFFAC  73 16                           jae 0x1402dffc4
002DFFAE  4D 8D 87 B8 01 00 00            lea r8, [r15 + 0x1b8]
002DFFB5  48 8B D0                        mov rdx, rax
002DFFB8  49 8D 8F B8 01 00 00            lea rcx, [r15 + 0x1b8]
002DFFBF  E8 CC FC F2 FF                  call 0x14020fc90
002DFFC4  48 85 F6                        test rsi, rsi
002DFFC7  74 04                           je 0x1402dffcd
002DFFC9  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
002DFFCD  0F 10 4C 24 20                  movups xmm1, xmmword ptr [rsp + 0x20]
002DFFD2  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
002DFFD7  66 0F 6F C1                     movdqa xmm0, xmm1
002DFFDB  66 48 0F 7E CE                  movq rsi, xmm1
002DFFE0  66 0F 73 D8 08                  psrldq xmm0, 8
002DFFE5  66 48 0F 7E C7                  movq rdi, xmm0
002DFFEA  45 85 F6                        test r14d, r14d
002DFFED  0F 84 2A 01 00 00               je 0x1402e011d
002DFFF3  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002DFFF8  E8 C3 07 00 00                  call 0x1402e07c0
002DFFFD  83 7C 24 58 FF                  cmp dword ptr [rsp + 0x58], -1
002E0002  0F 84 F0 01 00 00               je 0x1402e01f8
002E0008  49 8B 87 C0 01 00 00            mov rax, qword ptr [r15 + 0x1c0]
002E000F  BF 01 00 00 00                  mov edi, 1
002E0014  48 85 C0                        test rax, rax
002E0017  74 0E                           je 0x1402e0027
002E0019  0F B6 48 02                     movzx ecx, byte ptr [rax + 2]
002E001D  39 4C 24 5C                     cmp dword ptr [rsp + 0x5c], ecx
002E0021  0F 82 A2 02 00 00               jb 0x1402e02c9
002E0027  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
002E002C  4D 8B 97 C0 01 00 00            mov r10, qword ptr [r15 + 0x1c0]
002E0033  4D 85 D2                        test r10, r10
002E0036  0F 84 71 02 00 00               je 0x1402e02ad
002E003C  0F 1F 40 00                     nop dword ptr [rax]
002E0040  41 8B 0A                        mov ecx, dword ptr [r10]
002E0043  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002E0049  0F B7 C1                        movzx eax, cx
002E004C  C1 E9 18                        shr ecx, 0x18
002E004F  84 C9                           test cl, cl
002E0051  75 67                           jne 0x1402e00ba
002E0053  85 C0                           test eax, eax
002E0055  74 29                           je 0x1402e0080
002E0057  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
002E0060  41 8D 0C 00                     lea ecx, [r8 + rax]
002E0064  D1 E9                           shr ecx, 1
002E0066  44 8B C9                        mov r9d, ecx
002E0069  48 03 C9                        add rcx, rcx
002E006C  41 39 5C CA 10                  cmp dword ptr [r10 + rcx*8 + 0x10], ebx
002E0071  72 02                           jb 0x1402e0075
002E0073  75 40                           jne 0x1402e00b5
002E0075  45 8B C1                        mov r8d, r9d
002E0078  41 8D 48 01                     lea ecx, [r8 + 1]
002E007C  3B C8                           cmp ecx, eax
002E007E  75 E0                           jne 0x1402e0060
002E0080  85 FF                           test edi, edi
002E0082  74 17                           je 0x1402e009b
002E0084  8B C8                           mov ecx, eax
002E0086  48 FF C1                        inc rcx
002E0089  4D 89 13                        mov qword ptr [r11], r10
002E008C  48 C1 E1 04                     shl rcx, 4
002E0090  49 03 CA                        add rcx, r10
002E0093  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
002E0097  49 83 C3 10                     add r11, 0x10
002E009B  85 C0                           test eax, eax
002E009D  0F 84 61 01 00 00               je 0x1402e0204
002E00A3  FF C8                           dec eax
002E00A5  48 C1 E0 04                     shl rax, 4
002E00A9  48 83 C0 18                     add rax, 0x18
002E00AD  49 03 C2                        add rax, r10
002E00B0  4C 8B 10                        mov r10, qword ptr [rax]
002E00B3  EB 8B                           jmp 0x1402e0040
002E00B5  41 8B C1                        mov eax, r9d
002E00B8  EB BE                           jmp 0x1402e0078
002E00BA  85 C0                           test eax, eax
002E00BC  74 1F                           je 0x1402e00dd
002E00BE  66 90                           nop
002E00C0  41 8D 0C 00                     lea ecx, [r8 + rax]
002E00C4  D1 E9                           shr ecx, 1
002E00C6  8B D1                           mov edx, ecx
002E00C8  41 39 5C CA 10                  cmp dword ptr [r10 + rcx*8 + 0x10], ebx
002E00CD  0F 82 1D 01 00 00               jb 0x1402e01f0
002E00D3  8B C2                           mov eax, edx
002E00D5  41 8D 48 01                     lea ecx, [r8 + 1]
002E00D9  3B C8                           cmp ecx, eax
002E00DB  75 E3                           jne 0x1402e00c0
002E00DD  4D 89 13                        mov qword ptr [r11], r10
002E00E0  48 8D 40 02                     lea rax, [rax + 2]
002E00E4  49 8D 04 C2                     lea rax, [r10 + rax*8]
002E00E8  49 89 43 08                     mov qword ptr [r11 + 8], rax
002E00EC  85 FF                           test edi, edi
002E00EE  74 11                           je 0x1402e0101
002E00F0  4C 2B 5C 24 40                  sub r11, qword ptr [rsp + 0x40]
002E00F5  49 C1 FB 04                     sar r11, 4
002E00F9  41 FF C3                        inc r11d
002E00FC  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
002E0101  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
002E0106  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
002E010B  E8 D0 06 00 00                  call 0x1402e07e0
002E0110  48 8B 7C 24 28                  mov rdi, qword ptr [rsp + 0x28]
002E0115  45 33 F6                        xor r14d, r14d
002E0118  48 8B 74 24 20                  mov rsi, qword ptr [rsp + 0x20]
002E011D  48 85 F6                        test rsi, rsi
002E0120  0F 84 C9 01 00 00               je 0x1402e02ef
002E0126  8B 06                           mov eax, dword ptr [rsi]
002E0128  48 83 C7 08                     add rdi, 8
002E012C  0F B7 C0                        movzx eax, ax
002E012F  48 8B D7                        mov rdx, rdi
002E0132  48 83 C0 02                     add rax, 2
002E0136  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
002E013B  48 8D 04 C6                     lea rax, [rsi + rax*8]
002E013F  48 3B F8                        cmp rdi, rax
002E0142  0F 83 27 01 00 00               jae 0x1402e026f
002E0148  F6 42 07 01                     test byte ptr [rdx + 7], 1
002E014C  0F 85 BF 00 00 00               jne 0x1402e0211
002E0152  80 7A 06 01                     cmp byte ptr [rdx + 6], 1
002E0156  75 0D                           jne 0x1402e0165
002E0158  45 85 ED                        test r13d, r13d
002E015B  0F 84 B9 00 00 00               je 0x1402e021a
002E0161  C6 42 06 03                     mov byte ptr [rdx + 6], 3
002E0165  41 FF C4                        inc r12d
002E0168  44 3B 64 24 34                  cmp r12d, dword ptr [rsp + 0x34]
002E016D  0F 85 F5 00 00 00               jne 0x1402e0268
002E0173  44 8B 6D 7F                     mov r13d, dword ptr [rbp + 0x7f]
002E0177  41 F6 C5 02                     test r13b, 2
002E017B  75 4B                           jne 0x1402e01c8
002E017D  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002E0184  F0 49 0F C1 87 B8 01 00 00      lock xadd qword ptr [r15 + 0x1b8], rax
002E018D  24 06                           and al, 6
002E018F  3C 02                           cmp al, 2
002E0191  0F 84 05 01 00 00               je 0x1402e029c
002E0197  49 8D 8F B8 01 00 00            lea rcx, [r15 + 0x1b8]
002E019E  E8 5D 14 00 00                  call 0x1402e1600
002E01A3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002E01AC  90                              nop
002E01AD  66 83 80 E6 01 00 00 01         add word ptr [rax + 0x1e6], 1
002E01B5  75 11                           jne 0x1402e01c8
002E01B7  48 05 98 00 00 00               add rax, 0x98
002E01BD  90                              nop
002E01BE  48 39 00                        cmp qword ptr [rax], rax
002E01C1  74 05                           je 0x1402e01c8
002E01C3  E8 B8 2A 00 00                  call 0x1402e2c80
002E01C8  48 8B 4D 0F                     mov rcx, qword ptr [rbp + 0xf]
002E01CC  48 33 CC                        xor rcx, rsp
002E01CF  E8 6C C4 3C 00                  call 0x1406ac640
002E01D4  48 8B 9C 24 50 01 00 00         mov rbx, qword ptr [rsp + 0x150]
002E01DC  48 81 C4 00 01 00 00            add rsp, 0x100
002E01E3  41 5F                           pop r15
002E01E5  41 5E                           pop r14
002E01E7  41 5D                           pop r13
002E01E9  41 5C                           pop r12
002E01EB  5F                              pop rdi
002E01EC  5E                              pop rsi
002E01ED  5D                              pop rbp
002E01EE  C3                              ret
002E01EF  CC                              int3
002E01F0  44 8B C2                        mov r8d, edx
002E01F3  E9 DD FE FF FF                  jmp 0x1402e00d5
002E01F8  33 FF                           xor edi, edi
002E01FA  4C 8D 5C 24 48                  lea r11, [rsp + 0x48]
002E01FF  E9 28 FE FF FF                  jmp 0x1402e002c
002E0204  49 8D 42 08                     lea rax, [r10 + 8]
002E0208  4D 8B 52 08                     mov r10, qword ptr [r10 + 8]
002E020C  E9 2F FE FF FF                  jmp 0x1402e0040
002E0211  45 85 ED                        test r13d, r13d
002E0214  0F 85 4B FF FF FF               jne 0x1402e0165
002E021A  C6 42 06 00                     mov byte ptr [rdx + 6], 0
002E021E  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
002E0222  83 F8 FF                        cmp eax, -1
002E0225  0F 84 BA 00 00 00               je 0x1402e02e5
002E022B  85 C0                           test eax, eax
002E022D  0F 84 B2 00 00 00               je 0x1402e02e5
002E0233  8D 48 FF                        lea ecx, [rax - 1]
002E0236  48 C1 E1 04                     shl rcx, 4
002E023A  48 03 4C 24 40                  add rcx, qword ptr [rsp + 0x40]
002E023F  48 39 31                        cmp qword ptr [rcx], rsi
002E0242  0F 85 AE 00 00 00               jne 0x1402e02f6
002E0248  48 89 79 08                     mov qword ptr [rcx + 8], rdi
002E024C  49 8D 8F C0 01 00 00            lea rcx, [r15 + 0x1c0]
002E0253  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002E0258  E8 A3 69 F8 FF                  call 0x140266c00
002E025D  41 BE 01 00 00 00               mov r14d, 1
002E0263  E9 FD FE FF FF                  jmp 0x1402e0165
002E0268  FF C3                           inc ebx
002E026A  E9 7B FD FF FF                  jmp 0x1402dffea
002E026F  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
002E0273  48 8D 48 10                     lea rcx, [rax + 0x10]
002E0277  48 85 C0                        test rax, rax
002E027A  75 0E                           jne 0x1402e028a
002E027C  33 D2                           xor edx, edx
002E027E  48 85 C0                        test rax, rax
002E0281  48 0F 45 D1                     cmovne rdx, rcx
002E0285  E9 BE FE FF FF                  jmp 0x1402e0148
002E028A  48 8B F0                        mov rsi, rax
002E028D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002E0292  48 8B F9                        mov rdi, rcx
002E0295  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
002E029A  EB E0                           jmp 0x1402e027c
002E029C  49 8D 8F B8 01 00 00            lea rcx, [r15 + 0x1b8]
002E02A3  E8 28 5B F8 FF                  call 0x140265dd0
002E02A8  E9 EA FE FF FF                  jmp 0x1402e0197
002E02AD  85 FF                           test edi, edi
002E02AF  0F 85 4C FE FF FF               jne 0x1402e0101
002E02B5  49 C7 03 00 00 00 00            mov qword ptr [r11], 0
002E02BC  49 C7 43 08 00 00 00 00         mov qword ptr [r11 + 8], 0
002E02C4  E9 38 FE FF FF                  jmp 0x1402e0101
002E02C9  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
002E02CE  4C 8D 44 24 5C                  lea r8, [rsp + 0x5c]
002E02D3  E8 F0 C3 0C 00                  call 0x1403ac6c8
002E02D8  85 C0                           test eax, eax
002E02DA  0F 84 21 FE FF FF               je 0x1402e0101
002E02E0  E9 42 FD FF FF                  jmp 0x1402e0027
002E02E5  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
002E02EA  E9 50 FF FF FF                  jmp 0x1402e023f
002E02EF  33 D2                           xor edx, edx
002E02F1  E9 52 FE FF FF                  jmp 0x1402e0148
002E02F6  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002E02FB  E8 C0 04 00 00                  call 0x1402e07c0
002E0300  83 7C 24 58 FF                  cmp dword ptr [rsp + 0x58], -1
002E0305  0F 85 35 DC 3F 00               jne 0x1406ddf40
002E030B  0F 10 44 24 20                  movups xmm0, xmmword ptr [rsp + 0x20]
002E0310  0F 11 01                        movups xmmword ptr [rcx], xmm0
002E0313  E9 34 FF FF FF                  jmp 0x1402e024c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_MGR_SM_TRAITS___SmFeAddComplete(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m57;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p5C;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 11708477)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m104 = a3;
    a2 = 0;
    result = memset(v_stack_mD0, a2, 128, a4);
    v_stack_mF8 = v_stack_mD0;
    v_r12 = 0;
    v_stack_mF0 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a5)))) & (1));
    v_stack_mE8 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_mDC = 8;
    v_stack_m108 = (unsigned int)(result);
    v_stack_m118 = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) != 0) goto loc_002DFFCD;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 440, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 440;
        a2 = result;
        a1 = a1 + 440;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_r12 + 1);
    }
loc_002DFFEA:
    if ((unsigned int)(v_r12 + 1) == 0) goto loc_002E011D;
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(a1, v_stack_mF8, a3, a4);
    if (v_stack_mE0 == -1) goto loc_002E01F8;
    if (*(unsigned __int64 *)(a1 + 448) == 0) goto loc_002E0027;
    if (v_stack_mDC < ((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 448) + 2)))) goto loc_002E02C9;
loc_002E0027:
loc_002E002C:
    if (*(unsigned __int64 *)(a1 + 448) == 0) goto loc_002E02AD;
loc_002E0040:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448)))) >> (24));
    if ((unsigned __int8)(a1) != 0) goto loc_002E00BA;
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448))))) == 0) goto loc_002E0080;
loc_002E0060:
    a1 = (unsigned int)(((unsigned int)(0xFFFFFFFFULL) + (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448)))) * 1) >> (1));
    a1 = (a1) + (a1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 448) + a1 * 8 + 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_002E0075;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 448) + a1 * 8 + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_002E00B5;
loc_002E0075:
loc_002E0078:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1)) != ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448))))))) goto loc_002E0060;
loc_002E0080:
    v_r11 = v_stack_mF8;
    if (1 != 0) {
        a1 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448)))));
        a1 = (a1) + 1;
        *(unsigned __int64 *)(v_stack_mF8) = *(unsigned __int64 *)(a1 + 448);
        a1 = (a1) << (4);
        a1 = (a1) + (*(unsigned __int64 *)(a1 + 448));
        *(unsigned __int64 *)(v_stack_mF8 + 8) = a1;
        v_r11 = (v_stack_mF8) + (16);
    }
    if ((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448))))) == 0) goto loc_002E0204;
    result = (unsigned int)(((unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 448))))) - 1);
    result = (result) << (4);
    result = (result) + (24);
    result = (result) + (*(unsigned __int64 *)(a1 + 448));
    goto loc_002E0040;
loc_002E00B5:
    goto loc_002E0078;
loc_002E00BA:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))) == 0) goto loc_002E00DD;
loc_002E00C0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) * 1) >> (1));
    if ((*(unsigned int *)(*(unsigned __int64 *)(result) + a1 * 8 + 16)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a2))))) goto loc_002E01F0;
loc_002E00D5:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1))))))) goto loc_002E00C0;
loc_002E00DD:
    *(unsigned __int64 *)(v_r11) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(v_r11 + 8) = *(unsigned __int64 *)(result) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 2 * 8;
    if (1 != 0) {
        v_r11 = (v_r11) - (v_stack_mF8);
        v_r11 = (v_r11) >> (4);
        v_r11 = (unsigned int)((v_r11) + 1);
        v_stack_mE0 = (unsigned int)(v_r11);
    }
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a1)))) + 1, v_stack_m118, v_stack_mF8, (unsigned int)((unsigned int)(a1)));
    v_r14 = 0;
loc_002E011D:
    if (v_stack_m118 == 0) goto loc_002E02EF;
    v_rdi = (v_stack_m110) + (8);
    result = ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m118)))) + (2);
    v_stack_m110 = v_rdi;
    if (v_rdi >= (v_stack_m118 + result * 8)) goto loc_002E026F;
loc_002E0148:
    if (((*(unsigned __int8 *)(v_rdi + 7)) & (1)) != 0) goto loc_002E0211;
    if ((*(unsigned __int8 *)(v_rdi + 6)) != 1) goto loc_002E0165;
    if ((unsigned int)((unsigned int)(v_stack_m108)) == 0) goto loc_002E021A;
    *(unsigned __int8 *)(v_rdi + 6) = 3;
loc_002E0165:
    v_r12 = (unsigned int)((v_r12) + 1);
    if (((unsigned int)(v_r12)) != v_stack_m104) goto loc_002E0268;
    if ((((unsigned __int8)((unsigned int)(a5))) & (2)) != 0) goto loc_002E01C8;
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_002E029C;
loc_002E0197:
    result = KeAbPostRelease(a1 + 440, v_rdi, v_stack_mF8, (unsigned int)((unsigned int)(a1)));
    if (((unsigned __int8)(result)) != 2) goto loc_002E01C8;
    result = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (152);
    if ((*(unsigned __int64 *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(a1 + 440, v_rdi, v_stack_mF8, (unsigned int)((unsigned int)(a1)));
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rdi, v_stack_mF8, (unsigned int)((unsigned int)(a1)));
    v_rsp = (v_rsp) + (256);
    return result;
loc_002E01F0:
    goto loc_002E00D5;
loc_002E01F8:
    v_rdi = 0;
    goto loc_002E002C;
loc_002E0204:
    goto loc_002E0040;
loc_002E0211:
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_002E0165;
loc_002E021A:
    *(unsigned __int8 *)(v_rdi + 6) = 0;
    if (((unsigned int)((unsigned int)(v_stack_p58))) == -1) goto loc_002E02E5;
    if ((unsigned int)((unsigned int)(v_stack_p58)) == 0) goto loc_002E02E5;
    a1 = ((unsigned int)(v_stack_p58) - 1) << (4);
    a1 = (a1) + (v_stack_p40);
loc_002E023F:
    if ((*(unsigned __int64 *)(a1)) != v_stack_m118) goto loc_002E02F6;
    *(unsigned __int64 *)(a1 + 8) = 0;
loc_002E024C:
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(a1 + 448, v_stack_p40, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(a1)));
    goto loc_002E0165;
loc_002E0268:
    v_rbx = (unsigned int)((v_stack_p18) + 1);
    goto loc_002DFFEA;
loc_002E026F:
    if (*(unsigned __int64 *)(v_stack_m118 + 8) != 0) goto loc_002E028A;
loc_002E027C:
    a2 = 0;
    if (*(unsigned __int64 *)(v_stack_m118 + 8) != 0) { a2 = *(unsigned __int64 *)(v_stack_m118 + 8) + 16; }
    goto loc_002E0148;
loc_002E028A:
    v_stack_p20 = *(unsigned __int64 *)(v_stack_m118 + 8);
    v_stack_p28 = *(unsigned __int64 *)(v_stack_m118 + 8) + 16;
    goto loc_002E027C;
loc_002E029C:
    result = ExfTryToWakePushLock(a1 + 440, a2, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)(a1)));
    goto loc_002E0197;
loc_002E02AD:
    if ((unsigned int)(*(unsigned __int64 *)(v_stack_m118 + 8) + 16) != 0) goto loc_002E0101;
    *(unsigned __int64 *)(v_stack_p48) = 0;
    *(unsigned __int64 *)(v_stack_p48 + 8) = 0;
    goto loc_002E0101;
loc_002E02C9:
    result = SmArrayGrow(a1 + 440, a2, v_stack_p5C, v_stack_p40);
    if ((unsigned int)(result) == 0) goto loc_002E0101;
    goto loc_002E0027;
loc_002E02E5:
    goto loc_002E023F;
loc_002E02EF:
    a2 = 0;
    goto loc_002E0148;
loc_002E02F6:
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(v_stack_p48, v_stack_p40, v_stack_p5C, v_stack_p40);
    *(unsigned __int64 *)(v_stack_p48) = v_xmm0;
    goto loc_002E024C;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_MGR_SM_TRAITS___SmFeAddComplete(void *Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m48;
    uint64_t v_stack_m57;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p58;
    uint64_t v_stack_p5C;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0xB2A83D)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m104 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_mD0, Arg2, 128, Arg4);
    v_stack_mF8 = v_stack_mD0;
    local_r12 = 0;
    v_stack_mF0 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg5)))) & (1));
    v_stack_mE8 = 0;
    v_stack_mD8 = 0;
    v_stack_mE0 = 0;
    v_stack_mDC = 8;
    v_stack_m108 = (uint32_t)(result);
    v_stack_m118 = v_xmm0;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) != 0) goto loc_002DFFCD;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 440, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 440;
        Arg2 = result;
        Arg1 = Arg1 + 440;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_r12 + 1);
    }
loc_002DFFEA:
    if ((uint32_t)(local_r12 + 1) == 0) goto loc_002E011D;
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(Arg1, v_stack_mF8, Arg3, Arg4);
    if (v_stack_mE0 == -1) goto loc_002E01F8;
    if (*(uint64_t *)(arg1 + 0x1C0) == 0) goto loc_002E0027;
    if (v_stack_mDC < ((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x1C0) + 0x2)))) goto loc_002E02C9;
loc_002E0027:
loc_002E002C:
    if (*(uint64_t *)(arg1 + 0x1C0) == 0) goto loc_002E02AD;
loc_002E0040:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0)))) >> (24));
    if ((uint8_t)(Arg1) != 0) goto loc_002E00BA;
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0))))) == 0) goto loc_002E0080;
loc_002E0060:
    Arg1 = (uint32_t)(((uint32_t)(0xFFFFFFFFULL) + (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0)))) * 1) >> (1));
    Arg1 = (Arg1) + (Arg1);
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0) + arg1 * 8 + 0x10)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_002E0075;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0) + arg1 * 8 + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_002E00B5;
loc_002E0075:
loc_002E0078:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1)) != ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0))))))) goto loc_002E0060;
loc_002E0080:
    local_r11 = v_stack_mF8;
    if (1 != 0) {
        Arg1 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0)))));
        Arg1 = (Arg1) + 1;
        *(uint64_t *)(v_stack_mF8) = *(uint64_t *)(arg1 + 0x1C0);
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) + (*(uint64_t *)(arg1 + 0x1C0));
        *(void **)(v_stack_mF8 + 0x8) = Arg1;
        local_r11 = (v_stack_mF8) + (16);
    }
    if ((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0))))) == 0) goto loc_002E0204;
    result = (uint32_t)(((uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x1C0))))) - 1);
    result = (result) << (4);
    result = (result) + (24);
    result = (result) + (*(uint64_t *)(arg1 + 0x1C0));
    goto loc_002E0040;
loc_002E00B5:
    goto loc_002E0078;
loc_002E00BA:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))) == 0) goto loc_002E00DD;
loc_002E00C0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) * 1) >> (1));
    if ((*(uint32_t *)(*(uint64_t *)(result) + arg1 * 8 + 0x10)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))))) goto loc_002E01F0;
loc_002E00D5:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1))))))) goto loc_002E00C0;
loc_002E00DD:
    *(uint64_t *)(local_r11) = *(uint64_t *)(result);
    *(uint64_t *)(local_r11 + 0x8) = *(uint64_t *)(result) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 2 * 8;
    if (1 != 0) {
        local_r11 = (local_r11) - (v_stack_mF8);
        local_r11 = (local_r11) >> (4);
        local_r11 = (uint32_t)((local_r11) + 1);
        v_stack_mE0 = (uint32_t)(local_r11);
    }
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg1)))) + 1, v_stack_m118, v_stack_mF8, (uint32_t)((uint32_t)(Arg1)));
    local_r14 = 0;
loc_002E011D:
    if (v_stack_m118 == 0) goto loc_002E02EF;
    local_rdi = (v_stack_m110) + (8);
    result = ((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m118)))) + (2);
    v_stack_m110 = local_rdi;
    if (local_rdi >= (v_stack_m118 + result * 8)) goto loc_002E026F;
loc_002E0148:
    if (((*(uint8_t *)(local_rdi + 0x7)) & (1)) != 0) goto loc_002E0211;
    if ((*(uint8_t *)(local_rdi + 0x6)) != 1) goto loc_002E0165;
    if ((uint32_t)((uint32_t)(v_stack_m108)) == 0) goto loc_002E021A;
    *(uint8_t *)(local_rdi + 0x6) = 3;
loc_002E0165:
    local_r12 = (uint32_t)((local_r12) + 1);
    if (((uint32_t)(local_r12)) != v_stack_m104) goto loc_002E0268;
    if ((((uint8_t)((uint32_t)(Arg5))) & (2)) != 0) goto loc_002E01C8;
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_002E029C;
loc_002E0197:
    result = KeAbPostRelease(Arg1 + 440, local_rdi, v_stack_mF8, (uint32_t)((uint32_t)(Arg1)));
    if (((uint8_t)(result)) != 2) goto loc_002E01C8;
    result = (*(uint64_t *)(gs_base + (0 + 0x188))) + (152);
    if ((*(uint64_t *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(Arg1 + 440, local_rdi, v_stack_mF8, (uint32_t)((uint32_t)(Arg1)));
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rdi, v_stack_mF8, (uint32_t)((uint32_t)(Arg1)));
    local_rsp = (local_rsp) + (256);
    return result;
loc_002E01F0:
    goto loc_002E00D5;
loc_002E01F8:
    local_rdi = 0;
    goto loc_002E002C;
loc_002E0204:
    goto loc_002E0040;
loc_002E0211:
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_002E0165;
loc_002E021A:
    *(uint8_t *)(local_rdi + 0x6) = 0;
    if (((uint32_t)((uint32_t)(v_stack_p58))) == -1) goto loc_002E02E5;
    if ((uint32_t)((uint32_t)(v_stack_p58)) == 0) goto loc_002E02E5;
    Arg1 = ((uint32_t)(v_stack_p58) - 1) << (4);
    Arg1 = (Arg1) + (v_stack_p40);
loc_002E023F:
    if ((*(uint64_t *)(arg1)) != v_stack_m118) goto loc_002E02F6;
    *(uint64_t *)(arg1 + 0x8) = 0;
loc_002E024C:
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(Arg1 + 448, v_stack_p40, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(Arg1)));
    goto loc_002E0165;
loc_002E0268:
    local_rbx = (uint32_t)((v_stack_p18) + 1);
    goto loc_002DFFEA;
loc_002E026F:
    if (*(uint64_t *)(v_stack_m118 + 0x8) != 0) goto loc_002E028A;
loc_002E027C:
    Arg2 = 0;
    if (*(uint64_t *)(v_stack_m118 + 0x8) != 0) { Arg2 = *(uint64_t *)(v_stack_m118 + 0x8) + 16; }
    goto loc_002E0148;
loc_002E028A:
    v_stack_p20 = *(uint64_t *)(v_stack_m118 + 0x8);
    v_stack_p28 = *(uint64_t *)(v_stack_m118 + 0x8) + 16;
    goto loc_002E027C;
loc_002E029C:
    result = ExfTryToWakePushLock(Arg1 + 440, Arg2, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)(Arg1)));
    goto loc_002E0197;
loc_002E02AD:
    if ((uint32_t)(*(uint64_t *)(v_stack_m118 + 0x8) + 16) != 0) goto loc_002E0101;
    *(uint64_t *)(v_stack_p48) = 0;
    *(uint64_t *)(v_stack_p48 + 0x8) = 0;
    goto loc_002E0101;
loc_002E02C9:
    result = SmArrayGrow(Arg1 + 440, Arg2, v_stack_p5C, v_stack_p40);
    if ((uint32_t)(result) == 0) goto loc_002E0101;
    goto loc_002E0027;
loc_002E02E5:
    goto loc_002E023F;
loc_002E02EF:
    Arg2 = 0;
    goto loc_002E0148;
loc_002E02F6:
    result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(v_stack_p48, v_stack_p40, v_stack_p5C, v_stack_p40);
    *(uint64_t *)(v_stack_p48) = v_xmm0;
    goto loc_002E024C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1B8` | `64` | `R` |
| `Arg1` | `+ 0x1B8` | `64` | `R/W` |
| `Arg1` | `+ 0x1C0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DFEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
