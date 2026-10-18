# CcUnmapInactiveViewsInternal

- RVA: `0x0027174C`–`0x00271D5C` (길이 `1,552` bytes)
- VA: `0x000000014027174C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00065AE0`
- 디코드: `385`개 명령, `1,552/1,552` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **33**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00271806` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00271810` → [CcReferenceVacbArray](CcReferenceVacbArray_function_00271D70.md) (function, `0x00271D70`)
- `0x00271830` → [CcRecalculateVacbArrayHighwaterMark](CcRecalculateVacbArrayHighwaterMark_function_00271DC4.md) (function, `0x00271DC4`)
- `0x0027183D` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x0027186E` → [RtlRandom](../../page/A6/RtlRandom_function_00A65C60.md) (function, `0x00A65C60`)
- `0x002718B9` → [CcDereferenceVacbArray](../44/CcDereferenceVacbArray_function_004427B0.md) (function, `0x004427B0`)
- `0x00271926` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00271951` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00271970` → [CcReferenceSharedCacheMapByVacb](../26/CcReferenceSharedCacheMapByVacb_function_0026FCBC.md) (function, `0x0026FCBC`)
- `0x00271990` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x002719A3` → [CcAcquireBcbLockAndVacbLock](../26/CcAcquireBcbLockAndVacbLock_function_0026FC58.md) (function, `0x0026FC58`)
- `0x002719E8` → [CcGetVacbLargeOffset](../38/CcGetVacbLargeOffset_function_0038A590.md) (function, `0x0038A590`)
- `0x00271A69` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (function, `0x009E9600`)
- `0x00271A74` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x00271A9C` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x00271AB1` → [CcSetVacbInFreeList](../26/CcSetVacbInFreeList_function_0026FBB0.md) (function, `0x0026FBB0`)
- `0x00271ABD` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)
- `0x00271ACE` → [KeAcquireInStackQueuedSpinLock](KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00271AD6` → [CcDecrementOpenCount](../38/CcDecrementOpenCount_function_0038B75C.md) (function, `0x0038B75C`)
- `0x00271AE0` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00271B44` → [CcSetVacbLargeOffset](CcSetVacbLargeOffset_function_002733D0.md) (function, `0x002733D0`)
- `0x00271B90` → [CcDereferenceVacbArray](../44/CcDereferenceVacbArray_function_004427B0.md) (function, `0x004427B0`)
- `0x00271BC9` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x00271BEC` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00271C6F` → [CcGetRandomVacbArrayWithReference](../4A/CcGetRandomVacbArrayWithReference_function_004A98AC.md) (function, `0x004A98AC`)
- `0x00271CD3` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x00271CE4` → [KeAcquireInStackQueuedSpinLock](KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00271CEC` → [CcDecrementOpenCount](../38/CcDecrementOpenCount_function_0038B75C.md) (function, `0x0038B75C`)
- `0x00271CF6` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x00271D08` → [CcReleaseBcbLockAndVacbLock](../2D/CcReleaseBcbLockAndVacbLock_function_002DFDF0.md) (function, `0x002DFDF0`)
- `0x00271D19` → [KeAcquireInStackQueuedSpinLock](KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x00271D21` → [CcDecrementOpenCount](../38/CcDecrementOpenCount_function_0038B75C.md) (function, `0x0038B75C`)
- `0x00271D2B` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)

### Direct callers
- [CcGetVacbMiss](CcGetVacbMiss_function_00272900.md) at `0x00272D96`
- [CcUnmapInactiveViews](../4B/CcUnmapInactiveViews_function_004BA2DC.md) at `0x004BA303`

### Static image references
- `0x002717DC` → RVA `0x00E65BB0` (`.data`; read)
- `0x00271867` → RVA `0x00E0A898` (`.data`; read)
- `0x002718A7` → RVA `0x00E65BB4` (`.data`; read/write)
- `0x00271A28` → RVA `0x00F8F498` (`.data`; read)
- `0x00271BAE` → RVA `0x00F8F580` (`.data`; read)
- `0x00271BCE` → RVA `0x00F8F5C0` (`.data`; read)
- `0x00271C0C` → RVA `0x00E65BB8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0027186E` → [RtlRandom](../../page/A6/RtlRandom_function_00A65C60.md) (`.text` → `PAGE`)
  - `0x00271A69` → [CcUnmapVacb](../../page/9E/CcUnmapVacb_function_009E9600.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00271CBE` → [sub_006DA07A](../6D/Unknown_function_006DA07A.md) (`tail-transfer`)
  - `0x00271CC8` → [sub_006DA07A](../6D/Unknown_function_006DA07A.md) (`tail-transfer`)
  - `0x00271D57` → [sub_006DA07A + 0xA](../6D/Unknown_function_006DA07A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0027174C  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00271751  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00271755  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0027175A  53                              push rbx
0027175B  55                              push rbp
0027175C  56                              push rsi
0027175D  57                              push rdi
0027175E  41 54                           push r12
00271760  41 55                           push r13
00271762  41 56                           push r14
00271764  41 57                           push r15
00271766  48 83 EC 68                     sub rsp, 0x68
0027176A  83 4C 24 2C FF                  or dword ptr [rsp + 0x2c], 0xffffffff
0027176F  33 C9                           xor ecx, ecx
00271771  41 8B C0                        mov eax, r8d
00271774  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00271779  45 33 C0                        xor r8d, r8d
0027177C  0F 57 C0                        xorps xmm0, xmm0
0027177F  44 89 44 24 24                  mov dword ptr [rsp + 0x24], r8d
00271784  45 8B E0                        mov r12d, r8d
00271787  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
0027178C  41 8B F0                        mov esi, r8d
0027178F  44 89 44 24 34                  mov dword ptr [rsp + 0x34], r8d
00271794  45 8B F8                        mov r15d, r8d
00271797  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
0027179C  45 8B E8                        mov r13d, r8d
0027179F  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
002717A4  45 8B F0                        mov r14d, r8d
002717A7  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
002717AC  41 8B E8                        mov ebp, r8d
002717AF  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
002717B4  4D 85 C9                        test r9, r9
002717B7  0F 85 C2 04 00 00               jne 0x140271c7f
002717BD  83 E0 01                        and eax, 1
002717C0  40 8A F8                        mov dil, al
002717C3  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
002717CA  40 80 F7 01                     xor dil, 1
002717CE  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
002717D3  44 3B E2                        cmp r12d, edx
002717D6  0F 83 AA 03 00 00               jae 0x140271b86
002717DC  3B 2D CE 43 BF 00               cmp ebp, dword ptr [rip + 0xbf43ce]
002717E2  0F 87 5C 05 00 00               ja 0x140271d44
002717E8  48 85 F6                        test rsi, rsi
002717EB  0F 85 5F 03 00 00               jne 0x140271b50
002717F1  83 CB FF                        or ebx, 0xffffffff
002717F4  89 5C 24 2C                     mov dword ptr [rsp + 0x2c], ebx
002717F8  40 84 FF                        test dil, dil
002717FB  0F 85 6E 04 00 00               jne 0x140271c6f
00271801  8D 4E 04                        lea ecx, [rsi + 4]
00271804  8B DD                           mov ebx, ebp
00271806  E8 75 25 00 00                  call 0x140273d80
0027180B  40 8A F8                        mov dil, al
0027180E  8B CB                           mov ecx, ebx
00271810  E8 5B 05 00 00                  call 0x140271d70
00271815  48 8B F0                        mov rsi, rax
00271818  33 C0                           xor eax, eax
0027181A  48 85 F6                        test rsi, rsi
0027181D  75 0E                           jne 0x14027182d
0027181F  FF C3                           inc ebx
00271821  81 FB 00 05 00 00               cmp ebx, 0x500
00271827  72 E5                           jb 0x14027180e
00271829  8B F0                           mov esi, eax
0027182B  EB 08                           jmp 0x140271835
0027182D  48 8B CE                        mov rcx, rsi
00271830  E8 8F 05 00 00                  call 0x140271dc4
00271835  40 8A D7                        mov dl, dil
00271838  B9 04 00 00 00                  mov ecx, 4
0027183D  E8 FE 0C 00 00                  call 0x140272540
00271842  40 8A 7C 24 20                  mov dil, byte ptr [rsp + 0x20]
00271847  FF C5                           inc ebp
00271849  45 33 C0                        xor r8d, r8d
0027184C  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
00271850  48 85 F6                        test rsi, rsi
00271853  74 87                           je 0x1402717dc
00271855  8B 5C 24 2C                     mov ebx, dword ptr [rsp + 0x2c]
00271859  83 7E 04 01                     cmp dword ptr [rsi + 4], 1
0027185D  74 55                           je 0x1402718b4
0027185F  40 84 FF                        test dil, dil
00271862  74 6C                           je 0x1402718d0
00271864  41 8B D8                        mov ebx, r8d
00271867  48 8D 0D 2A 90 B9 00            lea rcx, [rip + 0xb9902a]
0027186E  E8 ED 43 7F 00                  call 0x140a65c60
00271873  8B 4E 08                        mov ecx, dword ptr [rsi + 8]
00271876  33 D2                           xor edx, edx
00271878  FF C1                           inc ecx
0027187A  F7 F1                           div ecx
0027187C  8B CA                           mov ecx, edx
0027187E  48 8D 04 95 02 00 00 00         lea rax, [rdx*4 + 2]
00271886  48 03 C1                        add rax, rcx
00271889  48 8D 3C C6                     lea rdi, [rsi + rax*8]
0027188D  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00271891  48 FF C8                        dec rax
00271894  48 83 F8 FD                     cmp rax, -3
00271898  0F 86 8A 03 00 00               jbe 0x140271c28
0027189E  33 C0                           xor eax, eax
002718A0  FF C3                           inc ebx
002718A2  83 FB 10                        cmp ebx, 0x10
002718A5  76 C0                           jbe 0x140271867
002718A7  FF 05 07 43 BF 00               inc dword ptr [rip + 0xbf4307]
002718AD  40 8A F8                        mov dil, al
002718B0  88 44 24 20                     mov byte ptr [rsp + 0x20], al
002718B4  33 D2                           xor edx, edx
002718B6  48 8B CE                        mov rcx, rsi
002718B9  E8 F2 0E 1D 00                  call 0x1404427b0
002718BE  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
002718C5  45 33 C0                        xor r8d, r8d
002718C8  41 8B F0                        mov esi, r8d
002718CB  E9 03 FF FF FF                  jmp 0x1402717d3
002718D0  83 FB FF                        cmp ebx, -1
002718D3  75 09                           jne 0x1402718de
002718D5  8B 5E 08                        mov ebx, dword ptr [rsi + 8]
002718D8  FF C3                           inc ebx
002718DA  89 5C 24 2C                     mov dword ptr [rsp + 0x2c], ebx
002718DE  85 DB                           test ebx, ebx
002718E0  74 D2                           je 0x1402718b4
002718E2  49 B9 00 00 E0 FF FF FF 00 00   movabs r9, 0xffffffe00000
002718EC  FF CB                           dec ebx
002718EE  8B FB                           mov edi, ebx
002718F0  48 83 C7 02                     add rdi, 2
002718F4  48 8D 3C 9F                     lea rdi, [rdi + rbx*4]
002718F8  48 8D 3C FE                     lea rdi, [rsi + rdi*8]
002718FC  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00271900  48 FF C8                        dec rax
00271903  48 83 F8 FD                     cmp rax, -3
00271907  0F 86 FA 01 00 00               jbe 0x140271b07
0027190D  49 8B F8                        mov rdi, r8
00271910  85 DB                           test ebx, ebx
00271912  75 D8                           jne 0x1402718ec
00271914  89 5C 24 2C                     mov dword ptr [rsp + 0x2c], ebx
00271918  48 85 FF                        test rdi, rdi
0027191B  0F 84 19 04 00 00               je 0x140271d3a
00271921  B9 04 00 00 00                  mov ecx, 4
00271926  E8 55 24 00 00                  call 0x140273d80
0027192B  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
0027192F  33 DB                           xor ebx, ebx
00271931  48 FF C9                        dec rcx
00271934  40 8A E8                        mov bpl, al
00271937  48 83 F9 FD                     cmp rcx, -3
0027193B  0F 86 0A 03 00 00               jbe 0x140271c4b
00271941  40 8A D5                        mov dl, bpl
00271944  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
00271949  B9 04 00 00 00                  mov ecx, 4
0027194E  4C 8B F3                        mov r14, rbx
00271951  E8 EA 0B 00 00                  call 0x140272540
00271956  E9 94 01 00 00                  jmp 0x140271aef
0027195B  49 33 CE                        xor rcx, r14
0027195E  48 B8 00 00 E0 FF FF FF 00 00   movabs rax, 0xffffffe00000
00271968  48 85 C8                        test rax, rcx
0027196B  75 D4                           jne 0x140271941
0027196D  48 8B CF                        mov rcx, rdi
00271970  E8 47 E3 FF FF                  call 0x14026fcbc
00271975  84 C0                           test al, al
00271977  74 C8                           je 0x140271941
00271979  48 8B 5F 10                     mov rbx, qword ptr [rdi + 0x10]
0027197D  40 8A D5                        mov dl, bpl
00271980  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
00271984  B9 04 00 00 00                  mov ecx, 4
00271989  44 8B BF 98 00 00 00            mov r15d, dword ptr [rdi + 0x98]
00271990  E8 AB 0B 00 00                  call 0x140272540
00271995  41 C1 EF 09                     shr r15d, 9
00271999  48 8B D7                        mov rdx, rdi
0027199C  41 83 E7 01                     and r15d, 1
002719A0  41 8B CF                        mov ecx, r15d
002719A3  E8 B0 E2 FF FF                  call 0x14026fc58
002719A8  4C 8B AF 18 02 00 00            mov r13, qword ptr [rdi + 0x218]
002719AF  4C 39 AC 24 B0 00 00 00         cmp qword ptr [rsp + 0xb0], r13
002719B7  0F 85 45 03 00 00               jne 0x140271d02
002719BD  33 D2                           xor edx, edx
002719BF  48 85 DB                        test rbx, rbx
002719C2  0F 88 3A 03 00 00               js 0x140271d02
002719C8  48 8B 6F 20                     mov rbp, qword ptr [rdi + 0x20]
002719CC  48 3B DD                        cmp rbx, rbp
002719CF  0F 8D 2D 03 00 00               jge 0x140271d02
002719D5  48 81 FD 00 00 00 02            cmp rbp, 0x2000000
002719DC  0F 8E 77 01 00 00               jle 0x140271b59
002719E2  48 8B D3                        mov rdx, rbx
002719E5  48 8B CF                        mov rcx, rdi
002719E8  E8 A3 8B 11 00                  call 0x14038a590
002719ED  4C 8B F0                        mov r14, rax
002719F0  33 D2                           xor edx, edx
002719F2  4D 85 F6                        test r14, r14
002719F5  0F 84 D2 02 00 00               je 0x140271ccd
002719FB  66 41 39 56 10                  cmp word ptr [r14 + 0x10], dx
00271A00  0F 85 C7 02 00 00               jne 0x140271ccd
00271A06  48 81 FD 00 00 00 02            cmp rbp, 0x2000000
00271A0D  0F 8F 25 01 00 00               jg 0x140271b38
00271A13  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00271A17  8B CB                           mov ecx, ebx
00271A19  48 C1 E9 12                     shr rcx, 0x12
00271A1D  48 89 14 C8                     mov qword ptr [rax + rcx*8], rdx
00271A21  F0 FF 8F 24 02 00 00            lock dec dword ptr [rdi + 0x224]
00271A28  8B 05 6A DA D1 00               mov eax, dword ptr [rip + 0xd1da6a]
00271A2E  8B 5C 24 34                     mov ebx, dword ptr [rsp + 0x34]
00271A32  41 39 85 E0 04 00 00            cmp dword ptr [r13 + 0x4e0], eax
00271A39  0F 82 50 02 00 00               jb 0x140271c8f
00271A3F  8B EA                           mov ebp, edx
00271A41  85 DB                           test ebx, ebx
00271A43  0F 85 4B 02 00 00               jne 0x140271c94
00271A49  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
00271A4D  83 E1 FD                        and ecx, 0xfffffffd
00271A50  48 83 7C 24 40 00               cmp qword ptr [rsp + 0x40], 0
00271A56  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00271A5A  0F 84 0C 01 00 00               je 0x140271b6c
00271A60  44 8B C1                        mov r8d, ecx
00271A63  48 8B D7                        mov rdx, rdi
00271A66  49 8B CE                        mov rcx, r14
00271A69  E8 92 7B 77 00                  call 0x1409e9600
00271A6E  48 8B D7                        mov rdx, rdi
00271A71  41 8B CF                        mov ecx, r15d
00271A74  E8 77 E3 06 00                  call 0x1402dfdf0
00271A79  33 D2                           xor edx, edx
00271A7B  85 ED                           test ebp, ebp
00271A7D  0F 85 40 02 00 00               jne 0x140271cc3
00271A83  41 FF C4                        inc r12d
00271A86  44 8D 7A 01                     lea r15d, [rdx + 1]
00271A8A  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
00271A8F  85 DB                           test ebx, ebx
00271A91  0F 85 12 02 00 00               jne 0x140271ca9
00271A97  B9 04 00 00 00                  mov ecx, 4
00271A9C  E8 DF 22 00 00                  call 0x140273d80
00271AA1  49 83 66 08 00                  and qword ptr [r14 + 8], 0
00271AA6  44 8A C5                        mov r8b, bpl
00271AA9  49 8B D6                        mov rdx, r14
00271AAC  49 8B CD                        mov rcx, r13
00271AAF  8A D8                           mov bl, al
00271AB1  E8 FA E0 FF FF                  call 0x14026fbb0
00271AB6  8A D3                           mov dl, bl
00271AB8  B9 04 00 00 00                  mov ecx, 4
00271ABD  E8 7E 0A 00 00                  call 0x140272540
00271AC2  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
00271AC9  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00271ACE  E8 CD 3C 00 00                  call 0x1402757a0
00271AD3  48 8B CF                        mov rcx, rdi
00271AD6  E8 81 9C 11 00                  call 0x14038b75c
00271ADB  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00271AE0  E8 FB 11 0D 00                  call 0x140342ce0
00271AE5  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00271AEA  44 8B 6C 24 38                  mov r13d, dword ptr [rsp + 0x38]
00271AEF  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
00271AF6  45 33 C0                        xor r8d, r8d
00271AF9  8B 6C 24 28                     mov ebp, dword ptr [rsp + 0x28]
00271AFD  40 8A 7C 24 20                  mov dil, byte ptr [rsp + 0x20]
00271B02  E9 CC FC FF FF                  jmp 0x1402717d3
00271B07  66 44 39 47 10                  cmp word ptr [rdi + 0x10], r8w
00271B0C  0F 85 FB FD FF FF               jne 0x14027190d
00271B12  48 8B 07                        mov rax, qword ptr [rdi]
00271B15  48 85 C0                        test rax, rax
00271B18  0F 84 EF FD FF FF               je 0x14027190d
00271B1E  4D 85 F6                        test r14, r14
00271B21  0F 84 ED FD FF FF               je 0x140271914
00271B27  49 33 C6                        xor rax, r14
00271B2A  49 85 C1                        test r9, rax
00271B2D  0F 85 DA FD FF FF               jne 0x14027190d
00271B33  E9 DC FD FF FF                  jmp 0x140271914
00271B38  45 33 C9                        xor r9d, r9d
00271B3B  45 33 C0                        xor r8d, r8d
00271B3E  48 8B D3                        mov rdx, rbx
00271B41  48 8B CF                        mov rcx, rdi
00271B44  E8 87 18 00 00                  call 0x1402733d0
00271B49  33 D2                           xor edx, edx
00271B4B  E9 D1 FE FF FF                  jmp 0x140271a21
00271B50  8B 5C 24 2C                     mov ebx, dword ptr [rsp + 0x2c]
00271B54  E9 06 FD FF FF                  jmp 0x14027185f
00271B59  48 8B 47 58                     mov rax, qword ptr [rdi + 0x58]
00271B5D  8B CB                           mov ecx, ebx
00271B5F  48 C1 E9 12                     shr rcx, 0x12
00271B63  4C 8B 34 C8                     mov r14, qword ptr [rax + rcx*8]
00271B67  E9 86 FE FF FF                  jmp 0x1402719f2
00271B6C  39 94 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], edx
00271B73  0F 84 E7 FE FF FF               je 0x140271a60
00271B79  49 8B 06                        mov rax, qword ptr [r14]
00271B7C  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00271B81  E9 DA FE FF FF                  jmp 0x140271a60
00271B86  48 85 F6                        test rsi, rsi
00271B89  74 17                           je 0x140271ba2
00271B8B  33 D2                           xor edx, edx
00271B8D  48 8B CE                        mov rcx, rsi
00271B90  E8 1B 0C 1D 00                  call 0x1404427b0
00271B95  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
00271B9C  45 33 C0                        xor r8d, r8d
00271B9F  41 8B F0                        mov esi, r8d
00271BA2  45 85 ED                        test r13d, r13d
00271BA5  75 65                           jne 0x140271c0c
00271BA7  44 3B E2                        cmp r12d, edx
00271BAA  73 60                           jae 0x140271c0c
00271BAC  8B EA                           mov ebp, edx
00271BAE  48 8D 0D CB D9 D1 00            lea rcx, [rip + 0xd1d9cb]
00271BB5  41 2B EC                        sub ebp, r12d
00271BB8  41 BD 01 00 00 00               mov r13d, 1
00271BBE  C1 E5 12                        shl ebp, 0x12
00271BC1  41 8B F8                        mov edi, r8d
00271BC4  44 89 6C 24 38                  mov dword ptr [rsp + 0x38], r13d
00271BC9  E8 D2 C9 F9 FF                  call 0x14020e5a0
00271BCE  48 8B 1D EB D9 D1 00            mov rbx, qword ptr [rip + 0xd1d9eb]
00271BD5  48 8D 05 E4 D9 D1 00            lea rax, [rip + 0xd1d9e4]
00271BDC  48 3B D8                        cmp rbx, rax
00271BDF  0F 85 6B 01 00 00               jne 0x140271d50
00271BE5  48 8D 0D 94 D9 D1 00            lea rcx, [rip + 0xd1d994]
00271BEC  E8 CF FD FD FF                  call 0x1402519c0
00271BF1  8B 6C 24 28                     mov ebp, dword ptr [rsp + 0x28]
00271BF5  45 33 C0                        xor r8d, r8d
00271BF8  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
00271BFF  85 FF                           test edi, edi
00271C01  40 8A 7C 24 20                  mov dil, byte ptr [rsp + 0x20]
00271C06  0F 85 C7 FB FF FF               jne 0x1402717d3
00271C0C  F0 FF 05 A5 3F BF 00            lock inc dword ptr [rip + 0xbf3fa5]
00271C13  41 8B C7                        mov eax, r15d
00271C16  48 83 C4 68                     add rsp, 0x68
00271C1A  41 5F                           pop r15
00271C1C  41 5E                           pop r14
00271C1E  41 5D                           pop r13
00271C20  41 5C                           pop r12
00271C22  5F                              pop rdi
00271C23  5E                              pop rsi
00271C24  5D                              pop rbp
00271C25  5B                              pop rbx
00271C26  C3                              ret
00271C27  CC                              int3
00271C28  33 C0                           xor eax, eax
00271C2A  66 39 47 10                     cmp word ptr [rdi + 0x10], ax
00271C2E  0F 85 6C FC FF FF               jne 0x1402718a0
00271C34  48 39 07                        cmp qword ptr [rdi], rax
00271C37  0F 84 63 FC FF FF               je 0x1402718a0
00271C3D  48 85 FF                        test rdi, rdi
00271C40  0F 84 5C FC FF FF               je 0x1402718a2
00271C46  E9 D6 FC FF FF                  jmp 0x140271921
00271C4B  66 39 5F 10                     cmp word ptr [rdi + 0x10], bx
00271C4F  0F 85 EC FC FF FF               jne 0x140271941
00271C55  48 8B 0F                        mov rcx, qword ptr [rdi]
00271C58  48 85 C9                        test rcx, rcx
00271C5B  0F 84 E0 FC FF FF               je 0x140271941
00271C61  4D 85 F6                        test r14, r14
00271C64  0F 84 03 FD FF FF               je 0x14027196d
00271C6A  E9 EC FC FF FF                  jmp 0x14027195b
00271C6F  E8 38 7C 23 00                  call 0x1404a98ac
00271C74  48 8B F0                        mov rsi, rax
00271C77  45 33 C0                        xor r8d, r8d
00271C7A  E9 DA FB FF FF                  jmp 0x140271859
00271C7F  4D 89 01                        mov qword ptr [r9], r8
00271C82  C7 44 24 34 01 00 00 00         mov dword ptr [rsp + 0x34], 1
00271C8A  E9 2E FB FF FF                  jmp 0x1402717bd
00271C8F  BD 01 00 00 00                  mov ebp, 1
00271C94  8B 4C 24 30                     mov ecx, dword ptr [rsp + 0x30]
00271C98  83 C9 02                        or ecx, 2
00271C9B  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00271CA0  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00271CA4  E9 B7 FD FF FF                  jmp 0x140271a60
00271CA9  49 8B 06                        mov rax, qword ptr [r14]
00271CAC  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00271CB4  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
00271CB8  48 89 01                        mov qword ptr [rcx], rax
00271CBB  49 89 16                        mov qword ptr [r14], rdx
00271CBE  E9 B7 83 46 00                  jmp 0x1406da07a
00271CC3  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00271CC8  E9 AD 83 46 00                  jmp 0x1406da07a
00271CCD  48 8B D7                        mov rdx, rdi
00271CD0  41 8B CF                        mov ecx, r15d
00271CD3  E8 18 E1 06 00                  call 0x1402dfdf0
00271CD8  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
00271CDF  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00271CE4  E8 B7 3A 00 00                  call 0x1402757a0
00271CE9  48 8B CF                        mov rcx, rdi
00271CEC  E8 6B 9A 11 00                  call 0x14038b75c
00271CF1  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00271CF6  E8 E5 0F 0D 00                  call 0x140342ce0
00271CFB  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
00271D00  EB 2E                           jmp 0x140271d30
00271D02  48 8B D7                        mov rdx, rdi
00271D05  41 8B CF                        mov ecx, r15d
00271D08  E8 E3 E0 06 00                  call 0x1402dfdf0
00271D0D  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
00271D14  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00271D19  E8 82 3A 00 00                  call 0x1402757a0
00271D1E  48 8B CF                        mov rcx, rdi
00271D21  E8 36 9A 11 00                  call 0x14038b75c
00271D26  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00271D2B  E8 B0 0F 0D 00                  call 0x140342ce0
00271D30  44 8B 7C 24 24                  mov r15d, dword ptr [rsp + 0x24]
00271D35  E9 B0 FD FF FF                  jmp 0x140271aea
00271D3A  40 8A 7C 24 20                  mov dil, byte ptr [rsp + 0x20]
00271D3F  E9 70 FB FF FF                  jmp 0x1402718b4
00271D44  8B 94 24 B8 00 00 00            mov edx, dword ptr [rsp + 0xb8]
00271D4B  E9 36 FE FF FF                  jmp 0x140271b86
00271D50  4C 8D 3D 69 D8 D1 00            lea r15, [rip + 0xd1d869]
00271D57  E9 28 83 46 00                  jmp 0x1406da084
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcUnmapInactiveViewsInternal(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pB8;
    unsigned __int64 v_stack_pC8;

    v_stack_p20 = a4;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    a1 = 0;
    v_stack_m50 = 0;
    a3 = 0;
    v_stack_m84 = 0;
    v_stack_m70 = 0;
    v_stack_m74 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m60 = v_xmm0;
    if (a4 != 0) goto loc_00271C7F;
loc_002717BD:
    result = (unsigned int)(((unsigned int)(a3)) & (1));
    v_stack_p18 = (unsigned int)(result);
    v_rdi = (unsigned __int8)(((unsigned __int8)(result)) ^ (1));
    v_stack_m88 = (unsigned __int8)(v_rdi);
loc_002717D3:
    if (0 >= a2) goto loc_00271B86;
loc_002717DC:
    if (0 > (*(unsigned int *)(v_rip + 12534734))) goto loc_00271D44;
    if (0 != 0) goto loc_00271B50;
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
    v_stack_m7C = (unsigned int)(v_rbx);
    if ((unsigned __int8)(v_rdi) != 0) goto loc_00271C6F;
    result = KeAcquireQueuedSpinLock(0 + 4, a2, a3, a4);
loc_0027180E:
    result = CcReferenceVacbArray(0, a2, a3, a4);
    result = 0;
    if (0 != 0) goto loc_0027182D;
    v_rbx = (unsigned int)((0) + 1);
    if (((unsigned int)(v_rbx)) < 0x500ULL) goto loc_0027180E;
    goto loc_00271835;
loc_0027182D:
    result = CcRecalculateVacbArrayHighwaterMark(0, a2, a3, a4);
loc_00271835:
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rbp = (unsigned int)((0) + 1);
    a3 = 0;
    v_stack_m80 = (unsigned int)(v_rbp);
    if (0 == 0) goto loc_002717DC;
loc_00271859:
    if ((*(unsigned int *)(0 + 4)) == 1) goto loc_002718B4;
loc_0027185F:
    if ((unsigned __int8)(v_stack_m88) == 0) goto loc_002718D0;
loc_00271867:
    result = RtlRandom(v_rip + 12161066, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) + 1);
    result = (a2 * 4 + 2) + (0);
    result = (*(unsigned __int64 *)(0 + result * 8 + 8)) - 1;
    if (result <= -3) goto loc_00271C28;
    result = 0;
loc_002718A0:
    v_rbx = (unsigned int)((0) + 1);
loc_002718A2:
    if (((unsigned int)(v_rbx)) <= 16) goto loc_00271867;
    v_stack_m88 = 0;
loc_002718B4:
    a2 = 0;
    result = CcDereferenceVacbArray(0, a2, a3, a4);
    a3 = 0;
    goto loc_002717D3;
loc_002718D0:
    if (((unsigned int)(v_rbx)) == -1) {
        v_rbx = *(unsigned int *)(0 + 8);
        v_rbx = (unsigned int)((v_rbx) + 1);
        v_stack_m7C = (unsigned int)(v_rbx);
    }
    if ((unsigned int)(v_rbx) == 0) goto loc_002718B4;
loc_002718EC:
    v_rbx = (unsigned int)((v_rbx) - 1);
    v_rdi = ((unsigned int)((unsigned int)(v_rbx))) + (2);
    result = (*(unsigned __int64 *)(0 + v_rdi + v_rbx * 4 * 8 + 8)) - 1;
    if (result <= -3) goto loc_00271B07;
loc_0027190D:
    if ((unsigned int)(v_rbx) != 0) goto loc_002718EC;
loc_00271914:
    v_stack_m7C = (unsigned int)(v_rbx);
    if (0 == 0) goto loc_00271D3A;
loc_00271921:
    result = KeAcquireQueuedSpinLock(4, (unsigned int)(v_stack_p10), a3, a4);
    v_rbx = 0;
    a1 = (*(unsigned __int64 *)(0 + 8)) - 1;
    if (a1 <= -3) goto loc_00271C4B;
loc_00271941:
    v_stack_m68 = 0;
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    goto loc_00271AEF;
loc_0027195B:
    a1 = (4) ^ (0);
    if (((result) & (a1)) != 0) goto loc_00271941;
loc_0027196D:
    result = CcReferenceSharedCacheMapByVacb(0, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00271941;
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(0 + 8) + 152))) >> (9));
    v_r15 = (unsigned int)((v_r15) & (1));
    result = CcAcquireBcbLockAndVacbLock((unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(0 + 8), a3, a4);
    if (v_stack_p8 != (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 536))) goto loc_00271D02;
    a2 = 0;
    if (sign_flag) goto loc_00271D02;
    if ((*(unsigned __int64 *)(0 + 16)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 32))) goto loc_00271D02;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 32)) <= 0x2000000ULL) goto loc_00271B59;
    result = CcGetVacbLargeOffset(*(unsigned __int64 *)(0 + 8), *(unsigned __int64 *)(0 + 16), a3, a4);
    a2 = 0;
loc_002719F2:
    if (result == 0) goto loc_00271CCD;
    if ((*(unsigned __int16 *)(result + 16)) != 0) goto loc_00271CCD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 32)) > 0x2000000ULL) goto loc_00271B38;
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int64 *)(0 + 16)))) >> (18);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 88) + a1 * 8) = 0;
loc_00271A21:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 536) + 1248)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13752938))))) goto loc_00271C8F;
    if ((unsigned int)((unsigned int)(v_stack_m74)) != 0) goto loc_00271C94;
    a1 = (unsigned int)(((unsigned int)(v_stack_m78)) & (0xFFFFFFFDULL));
    v_stack_m78 = (unsigned int)(a1);
    if (v_stack_m68 == 0) goto loc_00271B6C;
loc_00271A60:
    result = CcUnmapVacb(result, *(unsigned __int64 *)(0 + 8), (unsigned int)((unsigned int)(a1)), a4);
    result = CcReleaseBcbLockAndVacbLock((unsigned int)((unsigned int)(v_r15)), *(unsigned __int64 *)(0 + 8), (unsigned int)((unsigned int)(a1)), a4);
    a2 = 0;
    if (0 != 0) goto loc_00271CC3;
    v_r12 = (unsigned int)((0) + 1);
    v_stack_m84 = (unsigned int)(a2 + 1);
    if ((unsigned int)((unsigned int)(v_stack_m74)) != 0) goto loc_00271CA9;
    result = KeAcquireQueuedSpinLock(4, a2, (unsigned int)((unsigned int)(a1)), a4);
    result = CcSetVacbInFreeList(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 536), result, 0, a4);
    result = KeReleaseQueuedSpinLock(4, (unsigned __int8)((unsigned __int8)(result)), 0, a4);
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(*(unsigned __int64 *)(0 + 8) + 536) + 768, v_stack_m60, 0, a4);
    result = CcDecrementOpenCount(*(unsigned __int64 *)(0 + 8), v_stack_m60, 0, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, 0, a4);
loc_00271AEA:
loc_00271AEF:
    a3 = 0;
    goto loc_002717D3;
loc_00271B07:
    if ((*(unsigned __int16 *)(v_stack_m88 + 16)) != 0) goto loc_0027190D;
    if (*(unsigned __int64 *)(v_stack_m88) == 0) goto loc_0027190D;
    if (v_stack_m68 == 0) goto loc_00271914;
    result = (*(unsigned __int64 *)(v_stack_m88)) ^ (v_stack_m68);
    if (((a4) & (result)) != 0) goto loc_0027190D;
    goto loc_00271914;
loc_00271B38:
    a4 = 0;
    a3 = 0;
    result = CcSetVacbLargeOffset(v_stack_m88, (unsigned __int8)(result), a3, a4);
    a2 = 0;
    goto loc_00271A21;
loc_00271B50:
    goto loc_0027185F;
loc_00271B59:
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m7C)))) >> (18);
    goto loc_002719F2;
loc_00271B6C:
    if (v_stack_p18 == 0) goto loc_00271A60;
    v_stack_m68 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 88) + a1 * 8));
    goto loc_00271A60;
loc_00271B86:
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 88) + a1 * 8));
    v_rsi = 0;
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = CcDereferenceVacbArray(a1, a2, a3, a4);
        a2 = v_stack_p10;
        a3 = 0;
        v_rsi = 0;
    }
    if ((unsigned int)((unsigned int)(v_stack_m70)) != 0) goto loc_00271C0C;
    if (((unsigned int)(v_r12)) >= a2) goto loc_00271C0C;
    v_rbp = (unsigned int)(((unsigned int)(a2)) - ((unsigned int)(v_r12)));
    v_rbp = (unsigned int)((v_rbp) << (18));
    v_stack_m70 = 1;
    result = ExAcquireFastMutex(v_rip + 13752779, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 13752811)) != (v_rip + 13752804)) goto loc_00271D50;
    result = ExReleaseFastMutex(v_rip + 13752724, a2, a3, a4);
    a3 = 0;
    if (0 != 0) goto loc_002717D3;
loc_00271C0C:
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)(a2 + 1));
loc_00271C28:
    result = 0;
    if ((*(unsigned __int16 *)(v_stack_m88 + 16)) != 0) goto loc_002718A0;
    if ((*(unsigned __int64 *)(v_stack_m88)) == 0) goto loc_002718A0;
    if (v_stack_m88 == 0) goto loc_002718A2;
    goto loc_00271921;
loc_00271C4B:
    if ((*(unsigned __int16 *)(v_stack_m88 + 16)) != ((unsigned __int16)(*(unsigned __int64 *)(v_rip + 13752811)))) goto loc_00271941;
    if (*(unsigned __int64 *)(v_stack_m88) == 0) goto loc_00271941;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 88) + a1 * 8) == 0) goto loc_0027196D;
    goto loc_0027195B;
loc_00271C6F:
    result = CcGetRandomVacbArrayWithReference(*(unsigned __int64 *)(v_stack_m88), (unsigned int)(v_stack_p10), a3, a4);
    a3 = 0;
    goto loc_00271859;
loc_00271C7F:
    *(unsigned __int64 *)(a4) = 0;
    v_stack_p34 = 1;
    goto loc_002717BD;
loc_00271C8F:
loc_00271C94:
    a1 = (unsigned int)(((unsigned int)(v_stack_p30)) | (2));
    v_stack_p40 = (unsigned int)(v_stack_p10);
    v_stack_p30 = (unsigned int)(a1);
    goto loc_00271A60;
loc_00271CA9:
    v_stack_p34 = (unsigned int)((unsigned int)(v_stack_p10));
    *(unsigned __int64 *)(v_stack_pC8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 88) + a1 * 8));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m88 + 88) + a1 * 8)) = (unsigned int)(v_stack_p10);
loc_00271CC3:
loc_00271CCD:
    result = CcReleaseBcbLockAndVacbLock((unsigned int)((unsigned int)((unsigned int)(v_stack_p24))), v_stack_m88, a3, a4);
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p48, a3, a4);
    result = CcDecrementOpenCount(v_stack_m88, v_stack_p48, a3, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, v_stack_p48, a3, a4);
    goto loc_00271D30;
loc_00271D02:
    result = CcReleaseBcbLockAndVacbLock((unsigned int)((unsigned int)((unsigned int)(v_stack_p24))), v_stack_m88, a3, a4);
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p48, a3, a4);
    result = CcDecrementOpenCount(v_stack_m88, v_stack_p48, a3, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, v_stack_p48, a3, a4);
loc_00271D30:
    goto loc_00271AEA;
loc_00271D3A:
    goto loc_002718B4;
loc_00271D44:
    goto loc_00271B86;
loc_00271D50:
}
```

## 5. (Beta) C Style

```c
int64_t CcUnmapInactiveViewsInternal(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint8_t v_stack_m88;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;
    uint32_t v_stack_pB8;
    uint64_t v_stack_pC8;

    v_stack_p20 = Arg4;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    Arg1 = 0;
    v_stack_m50 = 0;
    Arg3 = 0;
    v_stack_m84 = 0;
    v_stack_m70 = 0;
    v_stack_m74 = 0;
    v_stack_m78 = 0;
    v_stack_m68 = 0;
    v_stack_m80 = 0;
    v_stack_m60 = v_xmm0;
    if (Arg4 != 0) goto loc_00271C7F;
loc_002717BD:
    result = (uint32_t)(((uint32_t)(Arg3)) & (1));
    v_stack_p18 = (uint32_t)(result);
    local_rdi = (uint8_t)(((uint8_t)(result)) ^ (1));
    v_stack_m88 = (uint8_t)(local_rdi);
loc_002717D3:
    if (0 >= Arg2) goto loc_00271B86;
loc_002717DC:
    if (0 > (*(uint32_t *)(v_rip + 0xBF43CE))) goto loc_00271D44;
    if (0 != 0) goto loc_00271B50;
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
    v_stack_m7C = (uint32_t)(local_rbx);
    if ((uint8_t)(local_rdi) != 0) goto loc_00271C6F;
    result = KeAcquireQueuedSpinLock(0 + 4, Arg2, Arg3, Arg4);
loc_0027180E:
    result = CcReferenceVacbArray(0, Arg2, Arg3, Arg4);
    result = 0;
    if (0 != 0) goto loc_0027182D;
    local_rbx = (uint32_t)((0) + 1);
    if (((uint32_t)(local_rbx)) < 0x500ULL) goto loc_0027180E;
    goto loc_00271835;
loc_0027182D:
    result = CcRecalculateVacbArrayHighwaterMark(0, Arg2, Arg3, Arg4);
loc_00271835:
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    local_rbp = (uint32_t)((0) + 1);
    Arg3 = 0;
    v_stack_m80 = (uint32_t)(local_rbp);
    if (0 == 0) goto loc_002717DC;
loc_00271859:
    if ((*(uint32_t *)(0 + 0x4)) == 1) goto loc_002718B4;
loc_0027185F:
    if ((uint8_t)(v_stack_m88) == 0) goto loc_002718D0;
loc_00271867:
    result = RtlRandom(v_rip + 12161066, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    Arg2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) + 1);
    result = (Arg2 * 4 + 2) + (0);
    result = (*(uint64_t *)(0 + result * 8 + 0x8)) - 1;
    if (result <= -3) goto loc_00271C28;
    result = 0;
loc_002718A0:
    local_rbx = (uint32_t)((0) + 1);
loc_002718A2:
    if (((uint32_t)(local_rbx)) <= 16) goto loc_00271867;
    v_stack_m88 = 0;
loc_002718B4:
    Arg2 = 0;
    result = CcDereferenceVacbArray(0, Arg2, Arg3, Arg4);
    Arg3 = 0;
    goto loc_002717D3;
loc_002718D0:
    if (((uint32_t)(local_rbx)) == -1) {
        local_rbx = *(uint32_t *)(0 + 0x8);
        local_rbx = (uint32_t)((local_rbx) + 1);
        v_stack_m7C = (uint32_t)(local_rbx);
    }
    if ((uint32_t)(local_rbx) == 0) goto loc_002718B4;
loc_002718EC:
    local_rbx = (uint32_t)((local_rbx) - 1);
    local_rdi = ((uint32_t)((uint32_t)(local_rbx))) + (2);
    result = (*(uint64_t *)(0 + local_rdi + local_rbx * 4 * 8 + 0x8)) - 1;
    if (result <= -3) goto loc_00271B07;
loc_0027190D:
    if ((uint32_t)(local_rbx) != 0) goto loc_002718EC;
loc_00271914:
    v_stack_m7C = (uint32_t)(local_rbx);
    if (0 == 0) goto loc_00271D3A;
loc_00271921:
    result = KeAcquireQueuedSpinLock(4, (uint32_t)(v_stack_p10), Arg3, Arg4);
    local_rbx = 0;
    Arg1 = (*(uint64_t *)(0 + 0x8)) - 1;
    if (Arg1 <= -3) goto loc_00271C4B;
loc_00271941:
    v_stack_m68 = 0;
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    goto loc_00271AEF;
loc_0027195B:
    Arg1 = (4) ^ (0);
    if (((result) & (Arg1)) != 0) goto loc_00271941;
loc_0027196D:
    result = CcReferenceSharedCacheMapByVacb(0, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00271941;
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(0 + 0x8) + 0x98))) >> (9));
    local_r15 = (uint32_t)((local_r15) & (1));
    result = CcAcquireBcbLockAndVacbLock((uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(0 + 0x8), Arg3, Arg4);
    if (v_stack_p8 != (*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x218))) goto loc_00271D02;
    Arg2 = 0;
    if (sign_flag) goto loc_00271D02;
    if ((*(uint64_t *)(0 + 0x10)) >= (*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x20))) goto loc_00271D02;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x20)) <= 0x2000000ULL) goto loc_00271B59;
    result = CcGetVacbLargeOffset(*(uint64_t *)(0 + 0x8), *(uint64_t *)(0 + 0x10), Arg3, Arg4);
    Arg2 = 0;
loc_002719F2:
    if (result == 0) goto loc_00271CCD;
    if ((*(uint16_t *)(result + 0x10)) != 0) goto loc_00271CCD;
    if ((*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x20)) > 0x2000000ULL) goto loc_00271B38;
    Arg1 = ((uint32_t)((uint32_t)(*(uint64_t *)(0 + 0x10)))) >> (18);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x58) + Arg1 * 8) = 0;
loc_00271A21:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x218) + 0x4E0)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xD1DA6A))))) goto loc_00271C8F;
    if ((uint32_t)((uint32_t)(v_stack_m74)) != 0) goto loc_00271C94;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m78)) & (0xFFFFFFFDULL));
    v_stack_m78 = (uint32_t)(Arg1);
    if (v_stack_m68 == 0) goto loc_00271B6C;
loc_00271A60:
    result = CcUnmapVacb(result, *(uint64_t *)(0 + 0x8), (uint32_t)((uint32_t)(Arg1)), Arg4);
    result = CcReleaseBcbLockAndVacbLock((uint32_t)((uint32_t)(local_r15)), *(uint64_t *)(0 + 0x8), (uint32_t)((uint32_t)(Arg1)), Arg4);
    Arg2 = 0;
    if (0 != 0) goto loc_00271CC3;
    local_r12 = (uint32_t)((0) + 1);
    v_stack_m84 = (uint32_t)(Arg2 + 1);
    if ((uint32_t)((uint32_t)(v_stack_m74)) != 0) goto loc_00271CA9;
    result = KeAcquireQueuedSpinLock(4, Arg2, (uint32_t)((uint32_t)(Arg1)), Arg4);
    result = CcSetVacbInFreeList(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x218), result, 0, Arg4);
    result = KeReleaseQueuedSpinLock(4, (uint8_t)((uint8_t)(result)), 0, Arg4);
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(*(uint64_t *)(0 + 0x8) + 0x218) + 768, v_stack_m60, 0, Arg4);
    result = CcDecrementOpenCount(*(uint64_t *)(0 + 0x8), v_stack_m60, 0, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m60, v_stack_m60, 0, Arg4);
loc_00271AEA:
loc_00271AEF:
    Arg3 = 0;
    goto loc_002717D3;
loc_00271B07:
    if ((*(uint16_t *)(v_stack_m88 + 0x10)) != 0) goto loc_0027190D;
    if (*(uint64_t *)(v_stack_m88) == 0) goto loc_0027190D;
    if (v_stack_m68 == 0) goto loc_00271914;
    result = (*(uint64_t *)(v_stack_m88)) ^ (v_stack_m68);
    if (((Arg4) & (result)) != 0) goto loc_0027190D;
    goto loc_00271914;
loc_00271B38:
    Arg4 = 0;
    Arg3 = 0;
    result = CcSetVacbLargeOffset(v_stack_m88, (uint8_t)(result), Arg3, Arg4);
    Arg2 = 0;
    goto loc_00271A21;
loc_00271B50:
    goto loc_0027185F;
loc_00271B59:
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m7C)))) >> (18);
    goto loc_002719F2;
loc_00271B6C:
    if (v_stack_p18 == 0) goto loc_00271A60;
    v_stack_m68 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x58) + Arg1 * 8));
    goto loc_00271A60;
loc_00271B86:
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x58) + Arg1 * 8));
    local_rsi = 0;
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = CcDereferenceVacbArray(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_p10;
        Arg3 = 0;
        local_rsi = 0;
    }
    if ((uint32_t)((uint32_t)(v_stack_m70)) != 0) goto loc_00271C0C;
    if (((uint32_t)(local_r12)) >= Arg2) goto loc_00271C0C;
    local_rbp = (uint32_t)(((uint32_t)(Arg2)) - ((uint32_t)(local_r12)));
    local_rbp = (uint32_t)((local_rbp) << (18));
    v_stack_m70 = 1;
    result = ExAcquireFastMutex(v_rip + 13752779, Arg2, Arg3, Arg4);
    if ((*(uint64_t *)(v_rip + 0xD1D9EB)) != (v_rip + 13752804)) goto loc_00271D50;
    result = ExReleaseFastMutex(v_rip + 13752724, Arg2, Arg3, Arg4);
    Arg3 = 0;
    if (0 != 0) goto loc_002717D3;
loc_00271C0C:
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)(Arg2 + 1));
loc_00271C28:
    result = 0;
    if ((*(uint16_t *)(v_stack_m88 + 0x10)) != 0) goto loc_002718A0;
    if ((*(uint64_t *)(v_stack_m88)) == 0) goto loc_002718A0;
    if (v_stack_m88 == 0) goto loc_002718A2;
    goto loc_00271921;
loc_00271C4B:
    if ((*(uint16_t *)(v_stack_m88 + 0x10)) != ((uint16_t)(*(uint64_t *)(v_rip + 0xD1D9EB)))) goto loc_00271941;
    if (*(uint64_t *)(v_stack_m88) == 0) goto loc_00271941;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x58) + Arg1 * 8) == 0) goto loc_0027196D;
    goto loc_0027195B;
loc_00271C6F:
    result = CcGetRandomVacbArrayWithReference(*(uint64_t *)(v_stack_m88), (uint32_t)(v_stack_p10), Arg3, Arg4);
    Arg3 = 0;
    goto loc_00271859;
loc_00271C7F:
    *(uint64_t *)(Arg4) = 0;
    v_stack_p34 = 1;
    goto loc_002717BD;
loc_00271C8F:
loc_00271C94:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p30)) | (2));
    v_stack_p40 = (uint32_t)(v_stack_p10);
    v_stack_p30 = (uint32_t)(Arg1);
    goto loc_00271A60;
loc_00271CA9:
    v_stack_p34 = (uint32_t)((uint32_t)(v_stack_p10));
    *(uint64_t *)(v_stack_pC8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x58) + Arg1 * 8));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m88 + 0x58) + Arg1 * 8)) = (uint32_t)(v_stack_p10);
loc_00271CC3:
loc_00271CCD:
    result = CcReleaseBcbLockAndVacbLock((uint32_t)((uint32_t)((uint32_t)(v_stack_p24))), v_stack_m88, Arg3, Arg4);
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p48, Arg3, Arg4);
    result = CcDecrementOpenCount(v_stack_m88, v_stack_p48, Arg3, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, v_stack_p48, Arg3, Arg4);
    goto loc_00271D30;
loc_00271D02:
    result = CcReleaseBcbLockAndVacbLock((uint32_t)((uint32_t)((uint32_t)(v_stack_p24))), v_stack_m88, Arg3, Arg4);
    result = KeAcquireInStackQueuedSpinLock(1 + 768, v_stack_p48, Arg3, Arg4);
    result = CcDecrementOpenCount(v_stack_m88, v_stack_p48, Arg3, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_p48, v_stack_p48, Arg3, Arg4);
loc_00271D30:
    goto loc_00271AEA;
loc_00271D3A:
    goto loc_002718B4;
loc_00271D44:
    goto loc_00271B86;
loc_00271D50:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0027174C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
