# MiReplenishPageSlist

- RVA: `0x003BADE0`–`0x003BB4D3` (길이 `1,779` bytes)
- VA: `0x00000001403BADE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008CC00`
- 디코드: `416`개 명령, `1,779/1,779` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x003BAEAB` → [MiNodeFreeZeroPages](MiNodeFreeZeroPages_function_003BBF60.md) (function, `0x003BBF60`)
- `0x003BAECD` → [MiGetColorHeadBase](MiGetColorHeadBase_function_003BB8B0.md) (function, `0x003BB8B0`)
- `0x003BAF28` → [MiDecreaseAvailablePages](MiDecreaseAvailablePages_function_003BB570.md) (function, `0x003BB570`)
- `0x003BAFBB` → [MiSetPfnBlink](MiSetPfnBlink_function_003BC790.md) (function, `0x003BC790`)
- `0x003BAFE5` → [ExpInterlockedPushEntrySList](../6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x003BB0A7` → [MiUpdateZeroFreeBitmap](MiUpdateZeroFreeBitmap_function_003BCE50.md) (function, `0x003BCE50`)
- `0x003BB0DE` → [MiNodeFreeZeroPages](MiNodeFreeZeroPages_function_003BBF60.md) (function, `0x003BBF60`)
- `0x003BB107` → [InterlockedPushListSList](../6B/InterlockedPushListSList_function_006BA620.md) (function, `0x006BA620`)
- `0x003BB202` → [MiIsFreeZeroPfnCold](../31/MiIsFreeZeroPfnCold_function_0031E5E4.md) (function, `0x0031E5E4`)
- `0x003BB252` → [MiUpdateLargePageCandidateValue](../33/MiUpdateLargePageCandidateValue_function_0033EF80.md) (function, `0x0033EF80`)
- `0x003BB29D` → [MiSetPfnSlist](MiSetPfnSlist_function_003BB4DC.md) (function, `0x003BB4DC`)
- `0x003BB325` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x003BB449` → [MiPageListCollision](../43/MiPageListCollision_function_00436B48.md) (function, `0x00436B48`)
- `0x003BB474` → [MiAddPageToHeatList](../44/MiAddPageToHeatList_function_0044603C.md) (function, `0x0044603C`)
- `0x003BB499` → [MiIncreaseAvailablePages](MiIncreaseAvailablePages_function_003BCC10.md) (function, `0x003BCC10`)
- `0x003BB4B2` → [MiIssuePageHeatList](../44/MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)

### Direct callers
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x00289FDB`

### Static image references
- `0x003BAE74` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)
- `0x003BAFFE` → RVA `0x00E2DCCC` (`.data`; read)
- `0x003BB06F` → RVA `0x00FC5002` (`ALMOSTRO`; read)
- `0x003BB145` → RVA `0x00E3014C` (`.data`; read)
- `0x003BB195` → RVA `0x00E30088` (`.data`; read)
- `0x003BB32B` → RVA `0x00FC6A88` (`ALMOSTRO`; read)
- `0x003BB404` → RVA `0x00E301A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003BB339` → [sub_006E7B34](../6E/Unknown_function_006E7B34.md) (`tail-transfer`)
  - `0x003BB42D` → [sub_006E7B34 + 0x53](../6E/Unknown_function_006E7B34.md) (`tail-transfer`)
  - `0x003BB441` → [sub_006E7B34 + 0xC9](../6E/Unknown_function_006E7B34.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003BADE0  48 8B C4                        mov rax, rsp
003BADE3  48 89 58 18                     mov qword ptr [rax + 0x18], rbx
003BADE7  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
003BADEB  89 50 10                        mov dword ptr [rax + 0x10], edx
003BADEE  55                              push rbp
003BADEF  56                              push rsi
003BADF0  57                              push rdi
003BADF1  41 54                           push r12
003BADF3  41 55                           push r13
003BADF5  41 56                           push r14
003BADF7  41 57                           push r15
003BADF9  48 81 EC A0 00 00 00            sub rsp, 0xa0
003BAE00  4C 8B A9 88 3A 00 00            mov r13, qword ptr [rcx + 0x3a88]
003BAE07  0F 57 C0                        xorps xmm0, xmm0
003BAE0A  0F 11 40 B0                     movups xmmword ptr [rax - 0x50], xmm0
003BAE0E  41 8B D8                        mov ebx, r8d
003BAE11  48 8B F1                        mov rsi, rcx
003BAE14  4C 63 F2                        movsxd r14, edx
003BAE17  41 8B 45 04                     mov eax, dword ptr [r13 + 4]
003BAE1B  A8 10                           test al, 0x10
003BAE1D  0F 85 62 02 00 00               jne 0x1403bb085
003BAE23  4A 8B 84 F6 60 3A 00 00         mov rax, qword ptr [rsi + r14*8 + 0x3a60]
003BAE2B  44 8B FB                        mov r15d, ebx
003BAE2E  44 0F B6 E3                     movzx r12d, bl
003BAE32  41 C1 EF 12                     shr r15d, 0x12
003BAE36  41 8B CC                        mov ecx, r12d
003BAE39  48 C1 E1 04                     shl rcx, 4
003BAE3D  41 83 E7 03                     and r15d, 3
003BAE41  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
003BAE46  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
003BAE4B  4C 89 A4 24 80 00 00 00         mov qword ptr [rsp + 0x80], r12
003BAE53  0F B7 0C 08                     movzx ecx, word ptr [rax + rcx]
003BAE57  41 8B 85 50 42 00 00            mov eax, dword ptr [r13 + 0x4250]
003BAE5E  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
003BAE63  48 3B C8                        cmp rcx, rax
003BAE66  0F 83 19 02 00 00               jae 0x1403bb085
003BAE6C  48 63 E8                        movsxd rbp, eax
003BAE6F  33 D2                           xor edx, edx
003BAE71  48 2B E9                        sub rbp, rcx
003BAE74  F7 05 3A BC C0 00 00 00 20 00   test dword ptr [rip + 0xc0bc3a], 0x200000
003BAE7E  0F 85 53 05 00 00               jne 0x1403bb3d7
003BAE84  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
003BAE88  8B C3                           mov eax, ebx
003BAE8A  48 8D 7D 40                     lea rdi, [rbp + 0x40]
003BAE8E  C1 E8 08                        shr eax, 8
003BAE91  48 8B CE                        mov rcx, rsi
003BAE94  24 01                           and al, 1
003BAE96  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
003BAE9A  8A D0                           mov dl, al
003BAE9C  45 85 F6                        test r14d, r14d
003BAE9F  0F 84 33 02 00 00               je 0x1403bb0d8
003BAEA5  41 B8 00 00 08 00               mov r8d, 0x80000
003BAEAB  E8 B0 10 00 00                  call 0x1403bbf60
003BAEB0  48 3B C7                        cmp rax, rdi
003BAEB3  0F 82 CC 01 00 00               jb 0x1403bb085
003BAEB9  48 C7 44 24 60 C0 0B 00 00      mov qword ptr [rsp + 0x60], 0xbc0
003BAEC2  45 8B CF                        mov r9d, r15d
003BAEC5  45 8B C6                        mov r8d, r14d
003BAEC8  8B D3                           mov edx, ebx
003BAECA  48 8B CE                        mov rcx, rsi
003BAECD  E8 DE 09 00 00                  call 0x1403bb8b0
003BAED2  4D 6B F4 58                     imul r14, r12, 0x58
003BAED6  41 B8 20 04 00 00               mov r8d, 0x420
003BAEDC  4C 03 F0                        add r14, rax
003BAEDF  49 8B 0E                        mov rcx, qword ptr [r14]
003BAEE2  48 3B E9                        cmp rbp, rcx
003BAEE5  48 0F 47 E9                     cmova rbp, rcx
003BAEE9  49 8B 8D 00 49 00 00            mov rcx, qword ptr [r13 + 0x4900]
003BAEF0  48 2B CD                        sub rcx, rbp
003BAEF3  49 3B C8                        cmp rcx, r8
003BAEF6  0F 82 89 01 00 00               jb 0x1403bb085
003BAEFC  33 C9                           xor ecx, ecx
003BAEFE  48 89 6C 24 68                  mov qword ptr [rsp + 0x68], rbp
003BAF03  44 8B E1                        mov r12d, ecx
003BAF06  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
003BAF0B  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
003BAF10  8B F9                           mov edi, ecx
003BAF12  44 8B F9                        mov r15d, ecx
003BAF15  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
003BAF1A  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
003BAF1F  44 8B C9                        mov r9d, ecx
003BAF22  49 8B CD                        mov rcx, r13
003BAF25  48 8B D5                        mov rdx, rbp
003BAF28  E8 43 06 00 00                  call 0x1403bb570
003BAF2D  85 C0                           test eax, eax
003BAF2F  74 42                           je 0x1403baf73
003BAF31  4D 8B 7E 10                     mov r15, qword ptr [r14 + 0x10]
003BAF35  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
003BAF3A  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
003BAF44  4B 8D 3C 7F                     lea rdi, [r15 + r15*2]
003BAF48  48 C1 E7 04                     shl rdi, 4
003BAF4C  48 8B C1                        mov rax, rcx
003BAF4F  48 03 F8                        add rdi, rax
003BAF52  45 8D 54 24 01                  lea r10d, [r12 + 1]
003BAF57  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
003BAF5C  F0 48 0F BA 6F 18 3F            lock bts qword ptr [rdi + 0x18], 0x3f
003BAF63  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
003BAF6D  0F 83 BC 01 00 00               jae 0x1403bb12f
003BAF73  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
003BAF78  49 3B C4                        cmp rax, r12
003BAF7B  0F 85 0F 05 00 00               jne 0x1403bb490
003BAF81  45 33 F6                        xor r14d, r14d
003BAF84  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
003BAF8C  44 39 70 04                     cmp dword ptr [rax + 4], r14d
003BAF90  0F 85 19 05 00 00               jne 0x1403bb4af
003BAF96  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
003BAF9B  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
003BAFA5  45 33 C0                        xor r8d, r8d
003BAFA8  4C 89 7D 10                     mov qword ptr [rbp + 0x10], r15
003BAFAC  4C 3B F8                        cmp r15, rax
003BAFAF  0F 84 EC 00 00 00               je 0x1403bb0a1
003BAFB5  48 8B D0                        mov rdx, rax
003BAFB8  48 8B CF                        mov rcx, rdi
003BAFBB  E8 D0 17 00 00                  call 0x1403bc790
003BAFC0  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
003BAFC5  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
003BAFCA  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
003BAFCF  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
003BAFD4  48 03 8C FE 60 3A 00 00         add rcx, qword ptr [rsi + rdi*8 + 0x3a60]
003BAFDC  48 85 C0                        test rax, rax
003BAFDF  0F 85 1C 01 00 00               jne 0x1403bb101
003BAFE5  E8 C6 F5 2F 00                  call 0x1406ba5b0
003BAFEA  41 BF 01 00 00 00               mov r15d, 1
003BAFF0  48 85 C0                        test rax, rax
003BAFF3  75 4E                           jne 0x1403bb043
003BAFF5  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
003BAFFC  33 D2                           xor edx, edx
003BAFFE  F7 35 C8 2C A7 00               div dword ptr [rip + 0xa72cc8]
003BB004  48 8B C7                        mov rax, rdi
003BB007  45 8B CF                        mov r9d, r15d
003BB00A  48 03 C0                        add rax, rax
003BB00D  44 8B D2                        mov r10d, edx
003BB010  41 83 E2 1F                     and r10d, 0x1f
003BB014  8B CA                           mov ecx, edx
003BB016  48 C1 E9 05                     shr rcx, 5
003BB01A  44 8B DA                        mov r11d, edx
003BB01D  48 8B 84 C6 08 3A 00 00         mov rax, qword ptr [rsi + rax*8 + 0x3a08]
003BB025  4C 8D 04 88                     lea r8, [rax + rcx*4]
003BB029  49 8D 42 01                     lea rax, [r10 + 1]
003BB02D  48 83 F8 20                     cmp rax, 0x20
003BB031  0F 87 88 00 00 00               ja 0x1403bb0bf
003BB037  41 8B CA                        mov ecx, r10d
003BB03A  41 8B C7                        mov eax, r15d
003BB03D  D3 E0                           shl eax, cl
003BB03F  F0 41 09 00                     lock or dword ptr [r8], eax
003BB043  49 8B D4                        mov rdx, r12
003BB046  48 F7 DA                        neg rdx
003BB049  F0 48 01 55 00                  lock add qword ptr [rbp], rdx
003BB04E  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
003BB053  4D 85 C0                        test r8, r8
003BB056  0F 85 B5 00 00 00               jne 0x1403bb111
003BB05C  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
003BB061  F0 4A 01 14 28                  lock add qword ptr [rax + r13], rdx
003BB066  F0 48 01 94 FE 08 0F 00 00      lock add qword ptr [rsi + rdi*8 + 0xf08], rdx
003BB06F  44 38 3D 8C 9F C0 00            cmp byte ptr [rip + 0xc09f8c], r15b
003BB076  0F 87 40 04 00 00               ja 0x1403bb4bc
003BB07C  4D 85 E4                        test r12, r12
003BB07F  0F 85 B9 02 00 00               jne 0x1403bb33e
003BB085  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
003BB08D  48 81 C4 A0 00 00 00            add rsp, 0xa0
003BB094  41 5F                           pop r15
003BB096  41 5E                           pop r14
003BB098  41 5D                           pop r13
003BB09A  41 5C                           pop r12
003BB09C  5F                              pop rdi
003BB09D  5E                              pop rsi
003BB09E  5D                              pop rbp
003BB09F  C3                              ret
003BB0A0  CC                              int3
003BB0A1  48 8B D5                        mov rdx, rbp
003BB0A4  48 8B CE                        mov rcx, rsi
003BB0A7  E8 A4 1D 00 00                  call 0x1403bce50
003BB0AC  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
003BB0B6  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
003BB0BA  E9 01 FF FF FF                  jmp 0x1403bafc0
003BB0BF  4D 85 D2                        test r10, r10
003BB0C2  0F 85 B5 02 00 00               jne 0x1403bb37d
003BB0C8  49 8B C9                        mov rcx, r9
003BB0CB  41 8B C7                        mov eax, r15d
003BB0CE  D3 E0                           shl eax, cl
003BB0D0  41 2B C7                        sub eax, r15d
003BB0D3  E9 67 FF FF FF                  jmp 0x1403bb03f
003BB0D8  41 B8 10 00 08 00               mov r8d, 0x80010
003BB0DE  E8 7D 0E 00 00                  call 0x1403bbf60
003BB0E3  48 3B C7                        cmp rax, rdi
003BB0E6  72 9D                           jb 0x1403bb085
003BB0E8  33 FF                           xor edi, edi
003BB0EA  41 38 BD E5 3E 00 00            cmp byte ptr [r13 + 0x3ee5], dil
003BB0F1  75 92                           jne 0x1403bb085
003BB0F3  48 C7 44 24 60 40 0B 00 00      mov qword ptr [rsp + 0x60], 0xb40
003BB0FC  E9 C1 FD FF FF                  jmp 0x1403baec2
003BB101  45 8B CC                        mov r9d, r12d
003BB104  4C 8B C0                        mov r8, rax
003BB107  E8 14 F5 2F 00                  call 0x1406ba620
003BB10C  E9 D9 FE FF FF                  jmp 0x1403bafea
003BB111  48 8B C3                        mov rax, rbx
003BB114  0F B6 CB                        movzx ecx, bl
003BB117  48 C1 E8 12                     shr rax, 0x12
003BB11B  83 E0 03                        and eax, 3
003BB11E  48 8B 84 C6 00 14 00 00         mov rax, qword ptr [rsi + rax*8 + 0x1400]
003BB126  4C 29 04 C8                     sub qword ptr [rax + rcx*8], r8
003BB12A  E9 2D FF FF FF                  jmp 0x1403bb05c
003BB12F  44 8B B4 24 E8 00 00 00         mov r14d, dword ptr [rsp + 0xe8]
003BB137  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
003BB13C  45 85 F6                        test r14d, r14d
003BB13F  0F 84 E6 01 00 00               je 0x1403bb32b
003BB145  44 39 15 00 50 A7 00            cmp dword ptr [rip + 0xa75000], r10d
003BB14C  0F 84 A6 02 00 00               je 0x1403bb3f8
003BB152  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
003BB155  66 85 C9                        test cx, cx
003BB158  0F 85 95 01 00 00               jne 0x1403bb2f3
003BB15E  44 8B C1                        mov r8d, ecx
003BB161  41 C1 E8 10                     shr r8d, 0x10
003BB165  41 F6 C0 20                     test r8b, 0x20
003BB169  0F 85 84 01 00 00               jne 0x1403bb2f3
003BB16F  41 F6 C0 10                     test r8b, 0x10
003BB173  0F 85 7A 01 00 00               jne 0x1403bb2f3
003BB179  41 8A C0                        mov al, r8b
003BB17C  24 07                           and al, 7
003BB17E  41 3A C2                        cmp al, r10b
003BB181  0F 87 6C 01 00 00               ja 0x1403bb2f3
003BB187  41 F6 C0 08                     test r8b, 8
003BB18B  0F 85 59 01 00 00               jne 0x1403bb2ea
003BB191  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
003BB195  48 8B 15 EC 4E A7 00            mov rdx, qword ptr [rip + 0xa74eec]
003BB19C  48 C1 E8 2B                     shr rax, 0x2b
003BB1A0  25 FF 03 00 00                  and eax, 0x3ff
003BB1A5  4C 39 2C C2                     cmp qword ptr [rdx + rax*8], r13
003BB1A9  0F 85 44 01 00 00               jne 0x1403bb2f3
003BB1AF  8B 47 20                        mov eax, dword ptr [rdi + 0x20]
003BB1B2  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
003BB1B9  C1 E8 10                        shr eax, 0x10
003BB1BC  24 FD                           and al, 0xfd
003BB1BE  0C 05                           or al, 5
003BB1C0  88 84 24 E2 00 00 00            mov byte ptr [rsp + 0xe2], al
003BB1C7  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
003BB1CE  89 47 20                        mov dword ptr [rdi + 0x20], eax
003BB1D1  41 F6 C0 08                     test r8b, 8
003BB1D5  0F 85 6B 02 00 00               jne 0x1403bb446
003BB1DB  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
003BB1DF  48 B9 00 00 00 00 00 FF FF FF   movabs rcx, 0xffffff0000000000
003BB1E9  48 23 C1                        and rax, rcx
003BB1EC  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
003BB1F0  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003BB1FA  F0 48 21 47 18                  lock and qword ptr [rdi + 0x18], rax
003BB1FF  48 8B CF                        mov rcx, rdi
003BB202  E8 DD 33 F6 FF                  call 0x14031e5e4
003BB207  33 C9                           xor ecx, ecx
003BB209  85 C0                           test eax, eax
003BB20B  0F 85 48 02 00 00               jne 0x1403bb459
003BB211  45 85 F6                        test r14d, r14d
003BB214  75 05                           jne 0x1403bb21b
003BB216  4C 01 54 24 50                  add qword ptr [rsp + 0x50], r10
003BB21B  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003BB225  48 8B C0                        mov rax, rax
003BB228  45 33 C9                        xor r9d, r9d
003BB22B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003BB230  4C 8B F7                        mov r14, rdi
003BB233  49 8B CD                        mov rcx, r13
003BB236  4C 2B F0                        sub r14, rax
003BB239  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
003BB243  49 C1 FE 04                     sar r14, 4
003BB247  4C 0F AF F0                     imul r14, rax
003BB24B  45 8D 41 03                     lea r8d, [r9 + 3]
003BB24F  49 8B D6                        mov rdx, r14
003BB252  E8 29 3D F8 FF                  call 0x14033ef80
003BB257  4C 8B 3F                        mov r15, qword ptr [rdi]
003BB25A  48 B8 FF FF FF FF FF 00 00 00   movabs rax, 0xffffffffff
003BB264  4C 23 F8                        and r15, rax
003BB267  48 B8 FF FF FF FF 3F 00 00 00   movabs rax, 0x3fffffffff
003BB271  4C 3B F8                        cmp r15, rax
003BB274  74 70                           je 0x1403bb2e6
003BB276  4B 8D 3C 7F                     lea rdi, [r15 + r15*2]
003BB27A  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003BB284  48 C1 E7 04                     shl rdi, 4
003BB288  48 8B C0                        mov rax, rax
003BB28B  48 03 F8                        add rdi, rax
003BB28E  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
003BB293  8B 94 24 E8 00 00 00            mov edx, dword ptr [rsp + 0xe8]
003BB29A  49 8B CA                        mov rcx, r10
003BB29D  E8 3A 02 00 00                  call 0x1403bb4dc
003BB2A2  41 B9 00 00 03 00               mov r9d, 0x30000
003BB2A8  49 89 3A                        mov qword ptr [r10], rdi
003BB2AB  33 D2                           xor edx, edx
003BB2AD  41 BA 01 00 00 00               mov r10d, 1
003BB2B3  8B C3                           mov eax, ebx
003BB2B5  4D 03 E2                        add r12, r10
003BB2B8  41 23 C1                        and eax, r9d
003BB2BB  8B CA                           mov ecx, edx
003BB2BD  41 3B C1                        cmp eax, r9d
003BB2C0  0F 85 BA 01 00 00               jne 0x1403bb480
003BB2C6  4C 01 94 CC 88 00 00 00         add qword ptr [rsp + rcx*8 + 0x88], r10
003BB2CE  49 2B EA                        sub rbp, r10
003BB2D1  0F 84 9C FC FF FF               je 0x1403baf73
003BB2D7  48 B9 00 00 00 00 00 DE FF FF   movabs rcx, 0xffffde0000000000
003BB2E1  E9 76 FC FF FF                  jmp 0x1403baf5c
003BB2E6  33 FF                           xor edi, edi
003BB2E8  EB A4                           jmp 0x1403bb28e
003BB2EA  41 3A C2                        cmp al, r10b
003BB2ED  0F 84 9E FE FF FF               je 0x1403bb191
003BB2F3  4C 8B C9                        mov r9, rcx
003BB2F6  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
003BB300  48 8B C0                        mov rax, rax
003BB303  48 2B F8                        sub rdi, rax
003BB306  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
003BB30B  48 C1 FF 04                     sar rdi, 4
003BB30F  BA 98 00 00 00                  mov edx, 0x98
003BB314  49 B8 AB AA AA AA AA AA AA AA   movabs r8, 0xaaaaaaaaaaaaaaab
003BB31E  4C 0F AF C7                     imul r8, rdi
003BB322  8D 4A B6                        lea ecx, [rdx - 0x4a]
003BB325  E8 36 23 14 00                  call 0x1404fd660
003BB32A  CC                              int3
003BB32B  8A 05 57 B7 C0 00               mov al, byte ptr [rip + 0xc0b757]
003BB331  84 C0                           test al, al
003BB333  0F 89 0C FE FF FF               jns 0x1403bb145
003BB339  E9 F6 C7 32 00                  jmp 0x1406e7b34
003BB33E  44 8B 5C 24 38                  mov r11d, dword ptr [rsp + 0x38]
003BB343  4C 8D 94 24 88 00 00 00         lea r10, [rsp + 0x88]
003BB34B  45 8B C6                        mov r8d, r14d
003BB34E  4D 8B 0A                        mov r9, qword ptr [r10]
003BB351  4D 85 C9                        test r9, r9
003BB354  75 12                           jne 0x1403bb368
003BB356  45 03 C7                        add r8d, r15d
003BB359  49 83 C2 08                     add r10, 8
003BB35D  41 83 F8 02                     cmp r8d, 2
003BB361  72 EB                           jb 0x1403bb34e
003BB363  E9 1D FD FF FF                  jmp 0x1403bb085
003BB368  49 63 C8                        movsxd rcx, r8d
003BB36B  49 F7 D9                        neg r9
003BB36E  49 8D 14 8B                     lea rdx, [r11 + rcx*4]
003BB372  F0 4C 01 8C D6 18 0F 00 00      lock add qword ptr [rsi + rdx*8 + 0xf18], r9
003BB37B  EB D9                           jmp 0x1403bb356
003BB37D  41 83 E3 1F                     and r11d, 0x1f
003BB381  BA 20 00 00 00                  mov edx, 0x20
003BB386  41 2B D3                        sub edx, r11d
003BB389  41 8B C7                        mov eax, r15d
003BB38C  8B CA                           mov ecx, edx
003BB38E  D3 E0                           shl eax, cl
003BB390  49 8B CA                        mov rcx, r10
003BB393  41 2B C7                        sub eax, r15d
003BB396  D3 E0                           shl eax, cl
003BB398  F0 41 09 00                     lock or dword ptr [r8], eax
003BB39C  8B C2                           mov eax, edx
003BB39E  49 83 C0 04                     add r8, 4
003BB3A2  4C 2B C8                        sub r9, rax
003BB3A5  49 83 F9 20                     cmp r9, 0x20
003BB3A9  72 1E                           jb 0x1403bb3c9
003BB3AB  49 8B C9                        mov rcx, r9
003BB3AE  48 C1 E9 05                     shr rcx, 5
003BB3B2  48 6B C1 E0                     imul rax, rcx, -0x20
003BB3B6  4C 03 C8                        add r9, rax
003BB3B9  41 C7 00 FF FF FF FF            mov dword ptr [r8], 0xffffffff
003BB3C0  49 83 C0 04                     add r8, 4
003BB3C4  49 2B CF                        sub rcx, r15
003BB3C7  75 F0                           jne 0x1403bb3b9
003BB3C9  4D 85 C9                        test r9, r9
003BB3CC  0F 84 71 FC FF FF               je 0x1403bb043
003BB3D2  E9 F1 FC FF FF                  jmp 0x1403bb0c8
003BB3D7  41 8B 09                        mov ecx, dword ptr [r9]
003BB3DA  C1 E9 03                        shr ecx, 3
003BB3DD  41 2B 49 04                     sub ecx, dword ptr [r9 + 4]
003BB3E1  48 3B E9                        cmp rbp, rcx
003BB3E4  C7 44 24 30 01 00 00 00         mov dword ptr [rsp + 0x30], 1
003BB3EC  48 0F 42 CD                     cmovb rcx, rbp
003BB3F0  48 8B E9                        mov rbp, rcx
003BB3F3  E9 90 FA FF FF                  jmp 0x1403bae88
003BB3F8  4D 8B CA                        mov r9, r10
003BB3FB  48 8B C1                        mov rax, rcx
003BB3FE  4C 8B D7                        mov r10, rdi
003BB401  4C 2B D0                        sub r10, rax
003BB404  48 8B 05 9D 4D A7 00            mov rax, qword ptr [rip + 0xa74d9d]
003BB40B  49 C1 FA 04                     sar r10, 4
003BB40F  4D 0F AF D0                     imul r10, r8
003BB413  4D 8B DA                        mov r11, r10
003BB416  49 8B CA                        mov rcx, r10
003BB419  48 C1 E9 05                     shr rcx, 5
003BB41D  41 83 E3 1F                     and r11d, 0x1f
003BB421  4C 8D 04 88                     lea r8, [rax + rcx*4]
003BB425  49 8D 43 01                     lea rax, [r11 + 1]
003BB429  48 83 F8 20                     cmp rax, 0x20
003BB42D  0F 87 54 C7 32 00               ja 0x1406e7b87
003BB433  41 BA 01 00 00 00               mov r10d, 1
003BB439  41 8B CB                        mov ecx, r11d
003BB43C  41 8B C2                        mov eax, r10d
003BB43F  D3 E0                           shl eax, cl
003BB441  E9 B7 C7 32 00                  jmp 0x1406e7bfd
003BB446  48 8B CF                        mov rcx, rdi
003BB449  E8 FA B6 07 00                  call 0x140436b48
003BB44E  41 BA 01 00 00 00               mov r10d, 1
003BB454  E9 82 FD FF FF                  jmp 0x1403bb1db
003BB459  39 4C 24 30                     cmp dword ptr [rsp + 0x30], ecx
003BB45D  0F 84 B8 FD FF FF               je 0x1403bb21b
003BB463  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
003BB46B  41 B8 03 00 00 00               mov r8d, 3
003BB471  49 8B D7                        mov rdx, r15
003BB474  E8 C3 AB 08 00                  call 0x14044603c
003BB479  33 C9                           xor ecx, ecx
003BB47B  E9 9B FD FF FF                  jmp 0x1403bb21b
003BB480  49 81 FE 00 00 10 00            cmp r14, 0x100000
003BB487  49 0F 42 CA                     cmovb rcx, r10
003BB48B  E9 36 FE FF FF                  jmp 0x1403bb2c6
003BB490  49 2B C4                        sub rax, r12
003BB493  49 8B CD                        mov rcx, r13
003BB496  48 8B D0                        mov rdx, rax
003BB499  E8 72 17 00 00                  call 0x1403bcc10
003BB49E  45 33 F6                        xor r14d, r14d
003BB4A1  4D 85 E4                        test r12, r12
003BB4A4  0F 84 DB FB FF FF               je 0x1403bb085
003BB4AA  E9 D5 FA FF FF                  jmp 0x1403baf84
003BB4AF  48 8B C8                        mov rcx, rax
003BB4B2  E8 A5 AC 08 00                  call 0x14044615c
003BB4B7  E9 DA FA FF FF                  jmp 0x1403baf96
003BB4BC  0F B6 44 24 34                  movzx eax, byte ptr [rsp + 0x34]
003BB4C1  48 8D 0C 47                     lea rcx, [rdi + rax*2]
003BB4C5  F0 48 01 94 CE 30 3B 00 00      lock add qword ptr [rsi + rcx*8 + 0x3b30], rdx
003BB4CE  E9 A9 FB FF FF                  jmp 0x1403bb07c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReplenishPageSlist(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned __int8 v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_pE0;
    unsigned __int8 v_stack_pE2;
    unsigned int v_stack_pE8;
    unsigned __int64 v_stack_pF8;

    *(unsigned __int64 *)(v_rsp + 24) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (160);
    *(unsigned __int64 *)(v_rsp - 80) = v_xmm0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14984) + 4)))) & (16)) != 0) goto loc_003BB085;
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (18));
    a1 = ((unsigned int)((unsigned int)((unsigned __int8)((unsigned int)(a3))))) << (4);
    v_r15 = (unsigned int)((v_r15) & (3));
    v_stack_m60 = a1;
    v_stack_mA0 = (unsigned int)(v_r15);
    v_stack_m58 = (unsigned __int8)((unsigned int)(a3));
    v_stack_m68 = (int)(a2);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 14944) + a1 * 1)) >= ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14984) + 16976)))) goto loc_003BB085;
    a2 = 0;
    v_rbp = ((int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 14984) + 16976))))) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + (int)(a2) * 8 + 14944) + a1 * 1));
    if (((*(unsigned int *)(v_rip + 12631098)) & (0x200000ULL)) != 0) goto loc_003BB3D7;
    v_stack_mA8 = 0;
loc_003BAE88:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) >> (8));
    result = (unsigned __int8)((result) & (1));
    v_stack_mA4 = (unsigned int)(result);
    if ((unsigned int)((int)(a2)) == 0) goto loc_003BB0D8;
    result = MiNodeFreeZeroPages(a1, (unsigned __int8)(result), (unsigned int)(0x80000ULL), a4);
    if (result < (v_rbp + 64)) goto loc_003BB085;
    v_stack_m78 = 0xBC0ULL;
loc_003BAEC2:
    result = MiGetColorHeadBase(a1, (unsigned int)((unsigned int)((unsigned int)(a3))), (unsigned int)((unsigned int)((int)(a2))), (unsigned int)((unsigned int)(v_r15)));
    v_r14 = ((int)(a2)) * ((unsigned __int8)((unsigned int)(a3)));
    v_r14 = (v_r14) + (result);
    if (v_rbp > (*(unsigned __int64 *)(v_r14))) { v_rbp = *(unsigned __int64 *)(v_r14); }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 14984) + 18688)) - (v_rbp);
    if (a1 < ((unsigned int)(0x420ULL))) goto loc_003BB085;
    a1 = 0;
    v_stack_m70 = v_rbp;
    v_stack_m88 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    result = MiDecreaseAvailablePages(*(unsigned __int64 *)(a1 + 14984), v_rbp, (unsigned int)(0x420ULL), 0);
    if ((unsigned int)(result) == 0) goto loc_003BAF73;
    v_stack_m80 = v_r14;
    v_rdi = (*(unsigned __int64 *)(v_r14 + 16) + *(unsigned __int64 *)(v_r14 + 16) * 2) << (4);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(a1 + 14984));
    v_stack_m90 = v_rdi;
loc_003BAF5C:
    if (condition_is_above_or_equal) goto loc_003BB12F;
loc_003BAF73:
    if (v_stack_m70 != 0) goto loc_003BB490;
    v_r14 = 0;
loc_003BAF84:
    if ((*(unsigned int *)(v_stack_p20 + 4)) != 0) goto loc_003BB4AF;
loc_003BAF96:
    a3 = 0;
    *(unsigned __int64 *)(v_stack_m80 + 16) = *(unsigned __int64 *)(v_r14 + 16);
    if ((*(unsigned __int64 *)(v_r14 + 16)) == v_stack_p20) goto loc_003BB0A1;
    result = MiSetPfnBlink(v_rdi, v_stack_p20, a3, 0);
loc_003BAFC0:
    a1 = (v_stack_m60) + (*(unsigned __int64 *)(a1 + v_stack_m68 * 8 + 14944));
    if (v_stack_m98 != 0) goto loc_003BB101;
    result = ExpInterlockedPushEntrySList(a1, v_stack_m90, a3, 0);
loc_003BAFEA:
    if (result != 0) goto loc_003BB043;
    a2 = 0;
    result = (v_stack_m68) + (v_stack_m68);
    v_r10 = (unsigned int)((0) & (31));
    a1 = (0) >> (5);
    if ((v_r10 + 1) > 32) goto loc_003BB0BF;
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
loc_003BB03F:
loc_003BB043:
    a2 = -(0);
    if (v_stack_m88 != 0) goto loc_003BB111;
loc_003BB05C:
    if ((*(unsigned __int8 *)(v_rip + 12623756)) > 1) goto loc_003BB4BC;
loc_003BB07C:
    if (0 != 0) goto loc_003BB33E;
loc_003BB085:
    v_rsp = (v_rsp) + (160);
    return v_stack_m78;
loc_003BB0A1:
    result = MiUpdateZeroFreeBitmap(a1, v_stack_m80, v_stack_m88, 1);
    *(unsigned __int64 *)(v_stack_m80 + 24) = result;
    goto loc_003BAFC0;
loc_003BB0BF:
    if (v_r10 != 0) goto loc_003BB37D;
loc_003BB0C8:
    result = (unsigned int)((1) << (1));
    result = (unsigned int)((result) - (1));
    goto loc_003BB03F;
loc_003BB0D8:
    result = MiNodeFreeZeroPages(1, v_stack_m80, (unsigned int)(0x80010ULL), 1);
    if (result < v_stack_m68) goto loc_003BB085;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 14984) + 16101)) != 0) goto loc_003BB085;
    v_stack_p60 = 0xB40ULL;
    goto loc_003BAEC2;
loc_003BB101:
    result = InterlockedPushListSList(1, v_stack_m80, result, 0);
    goto loc_003BAFEA;
loc_003BB111:
    result = (v_stack_p18) >> (18);
    result = (unsigned int)((result) & (3));
    goto loc_003BB05C;
loc_003BB12F:
    v_stack_p40 = 0;
    if ((unsigned int)((unsigned int)(v_stack_pE8)) == 0) goto loc_003BB32B;
loc_003BB145:
    if ((*(unsigned int *)(v_rip + 10964992)) == ((unsigned int)(v_r10))) goto loc_003BB3F8;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_rdi + 32))) != 0) goto loc_003BB2F3;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32))))) >> (16));
    if ((((unsigned __int8)(a3)) & (32)) != 0) goto loc_003BB2F3;
    if ((((unsigned __int8)(a3)) & (16)) != 0) goto loc_003BB2F3;
    result = (unsigned __int8)(((unsigned __int8)(a3)) & (7));
    if (((unsigned __int8)(result)) > ((unsigned __int8)(v_r10))) goto loc_003BB2F3;
    if ((((unsigned __int8)(a3)) & (8)) != 0) goto loc_003BB2EA;
loc_003BB191:
    result = (*(unsigned __int64 *)(v_rdi + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10964716) + result * 8)) != (*(unsigned __int64 *)(a1 + 14984))) goto loc_003BB2F3;
    v_stack_pE0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    v_stack_pE2 = (unsigned __int8)(result);
    *(unsigned int *)(v_rdi + 32) = (unsigned int)((unsigned int)(v_stack_pE0));
    if ((((unsigned __int8)(a3)) & (8)) != 0) goto loc_003BB446;
loc_003BB1DB:
    result = (*(unsigned __int64 *)(v_rdi + 24)) & ((unsigned int)(*(unsigned int *)(v_rdi + 32)));
    *(unsigned __int64 *)(v_rdi + 24) = result;
    result = MiIsFreeZeroPfnCold(0, *(unsigned __int64 *)(v_rip + 10964716), a3, 0);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_003BB459;
    if ((unsigned int)((unsigned int)(v_stack_pE8)) == 0) {
    }
    a4 = 0;
    v_stack_p20 = 0;
    v_r14 = (0) - (result);
    v_r14 = (v_r14) >> (4);
    v_r14 = (v_r14) * (result);
    result = MiUpdateLargePageCandidateValue(*(unsigned __int64 *)(a1 + 14984), v_r14, a4 + 3, a4);
    v_r15 = (*(unsigned __int64 *)(v_rdi)) & (result);
    if (v_r15 == result) goto loc_003BB2E6;
    v_rdi = (v_r15 + v_r15 * 2) << (4);
    v_rdi = (v_rdi) + (result);
loc_003BB28E:
    result = MiSetPfnSlist(v_stack_p40, (unsigned int)(v_stack_pE8), a4 + 3, a4);
    *(unsigned __int64 *)(v_stack_p40) = v_rdi;
    a2 = 0;
    v_r12 = (0) + (1);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & ((unsigned int)((unsigned int)(0x30000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x30000ULL)))) goto loc_003BB480;
loc_003BB2C6:
    v_rbp = (v_stack_m80) - (1);
    if (condition_is_equal) goto loc_003BAF73;
    goto loc_003BAF5C;
loc_003BB2E6:
    v_rdi = 0;
    goto loc_003BB28E;
loc_003BB2EA:
    if (((unsigned __int8)(result)) == 1) goto loc_003BB191;
loc_003BB2F3:
    v_rdi = (v_rdi) - (result);
    v_stack_p20 = v_r15;
    v_rdi = (v_rdi) >> (4);
    a3 = (a4 + 3) * (v_rdi);
    result = KeBugCheckEx(152 - 74, 152, a3, 0);
loc_003BB32B:
    if (!sign_flag) goto loc_003BB145;
loc_003BB33E:
loc_003BB34E:
    if (*(unsigned __int64 *)(v_stack_p88) != 0) goto loc_003BB368;
loc_003BB356:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) + ((unsigned int)(v_r15)));
    v_r10 = (v_stack_p88) + (8);
    if (a3 < 2) goto loc_003BB34E;
    goto loc_003BB085;
loc_003BB368:
    a4 = -(*(unsigned __int64 *)(v_stack_p88));
    goto loc_003BB356;
loc_003BB37D:
    v_r11 = (unsigned int)(((unsigned int)(v_stack_p38)) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(v_r11)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - ((unsigned int)(v_r15)));
    result = (unsigned int)((result) << ((unsigned __int8)(v_r10)));
    a3 = (a3) + (4);
    a4 = (a4) - ((unsigned int)(a2));
    if (a4 < 32) goto loc_003BB3C9;
    a1 = (a4) >> (5);
    result = ((unsigned int)(a2)) * (a1);
    a4 = (a4) + (result);
loc_003BB3B9:
    *(unsigned int *)(a3) = 0xFFFFFFFFULL;
    a3 = (a3) + (4);
    a1 = (a1) - (v_r15);
    if (condition_is_not_equal) goto loc_003BB3B9;
loc_003BB3C9:
    if (a4 == 0) goto loc_003BB043;
    goto loc_003BB0C8;
loc_003BB3D7:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) >> (3));
    a1 = (unsigned int)((a1) - (*(unsigned int *)(a4 + 4)));
    v_stack_p30 = 1;
    if (v_rbp < a1) { a1 = v_rbp; }
    goto loc_003BAE88;
loc_003BB3F8:
    v_r10 = (v_rdi) - (a1);
    v_r10 = (v_r10) >> (4);
    v_r10 = (v_r10) * (a3);
    a1 = (v_r10) >> (5);
    v_r11 = (unsigned int)((v_r10) & (31));
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r11)))));
loc_003BB446:
    result = MiPageListCollision(v_rdi, a2, *(unsigned __int64 *)(v_rip + 10964381) + a1 * 4, v_r10);
    goto loc_003BB1DB;
loc_003BB459:
    if (v_stack_p30 == ((unsigned int)(v_rdi))) goto loc_003BB21B;
    result = MiAddPageToHeatList(v_stack_pF8, v_r15, 3, v_r10);
    a1 = 0;
    goto loc_003BB21B;
loc_003BB480:
    if (v_r14 < 0x100000ULL) { a1 = 1; }
    goto loc_003BB2C6;
loc_003BB490:
    result = (result) - (v_r12);
    result = MiIncreaseAvailablePages(*(unsigned __int64 *)(a1 + 14984), result, 3, v_r10);
    v_r14 = 0;
    if (v_r12 == 0) goto loc_003BB085;
    goto loc_003BAF84;
loc_003BB4AF:
    result = MiIssuePageHeatList(result, result, 3, v_r10);
    goto loc_003BAF96;
loc_003BB4BC:
    goto loc_003BB07C;
}
```

## 5. (Beta) C Style

```c
int64_t MiReplenishPageSlist(void *Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint8_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p88;
    uint32_t v_stack_pE0;
    uint8_t v_stack_pE2;
    uint32_t v_stack_pE8;
    uint64_t v_stack_pF8;

    *(uint64_t *)(local_rsp + 0x18) = local_rbx;
    *(void **)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (160);
    *(uint64_t *)(local_rsp - 0x50) = v_xmm0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x3A88) + 0x4)))) & (16)) != 0) goto loc_003BB085;
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (18));
    Arg1 = ((uint32_t)((uint32_t)((uint8_t)((uint32_t)(Arg3))))) << (4);
    local_r15 = (uint32_t)((local_r15) & (3));
    v_stack_m60 = Arg1;
    v_stack_mA0 = (uint32_t)(local_r15);
    v_stack_m58 = (uint8_t)((uint32_t)(Arg3));
    v_stack_m68 = (int32_t)(Arg2);
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x3A60) + arg1 * 1)) >= ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x3A88) + 0x4250)))) goto loc_003BB085;
    Arg2 = 0;
    local_rbp = ((int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x3A88) + 0x4250))))) - (*(uint16_t *)(*(uint64_t *)(arg1 + (int32_t)(Arg2) * 8 + 0x3A60) + arg1 * 1));
    if (((*(uint32_t *)(v_rip + 0xC0BC3A)) & (0x200000ULL)) != 0) goto loc_003BB3D7;
    v_stack_mA8 = 0;
loc_003BAE88:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) >> (8));
    result = (uint8_t)((result) & (1));
    v_stack_mA4 = (uint32_t)(result);
    if ((uint32_t)((int32_t)(Arg2)) == 0) goto loc_003BB0D8;
    result = MiNodeFreeZeroPages(Arg1, (uint8_t)(result), (uint32_t)(0x80000ULL), Arg4);
    if (result < (local_rbp + 64)) goto loc_003BB085;
    v_stack_m78 = 0xBC0ULL;
loc_003BAEC2:
    result = MiGetColorHeadBase(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg3))), (uint32_t)((uint32_t)((int32_t)(Arg2))), (uint32_t)((uint32_t)(local_r15)));
    local_r14 = ((int32_t)(Arg2)) * ((uint8_t)((uint32_t)(Arg3)));
    local_r14 = (local_r14) + (result);
    if (local_rbp > (*(uint64_t *)(local_r14))) { local_rbp = *(uint64_t *)(local_r14); }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x3A88) + 0x4900)) - (local_rbp);
    if (Arg1 < ((uint32_t)(0x420ULL))) goto loc_003BB085;
    Arg1 = 0;
    v_stack_m70 = local_rbp;
    v_stack_m88 = 0;
    v_stack_m98 = 0;
    v_stack_m90 = 0;
    v_stack_m80 = 0;
    result = MiDecreaseAvailablePages(*(uint64_t *)(arg1 + 0x3A88), local_rbp, (uint32_t)(0x420ULL), 0);
    if ((uint32_t)(result) == 0) goto loc_003BAF73;
    v_stack_m80 = local_r14;
    local_rdi = (*(uint64_t *)(local_r14 + 0x10) + *(uint64_t *)(local_r14 + 0x10) * 2) << (4);
    local_rdi = (local_rdi) + (*(uint64_t *)(arg1 + 0x3A88));
    v_stack_m90 = local_rdi;
loc_003BAF5C:
    if (condition_is_above_or_equal) goto loc_003BB12F;
loc_003BAF73:
    if (v_stack_m70 != 0) goto loc_003BB490;
    local_r14 = 0;
loc_003BAF84:
    if ((*(uint32_t *)(v_stack_p20 + 0x4)) != 0) goto loc_003BB4AF;
loc_003BAF96:
    Arg3 = 0;
    *(uint64_t *)(v_stack_m80 + 0x10) = *(uint64_t *)(local_r14 + 0x10);
    if ((*(uint64_t *)(local_r14 + 0x10)) == v_stack_p20) goto loc_003BB0A1;
    result = MiSetPfnBlink(local_rdi, v_stack_p20, Arg3, 0);
loc_003BAFC0:
    Arg1 = (v_stack_m60) + (*(uint64_t *)(arg1 + v_stack_m68 * 8 + 0x3A60));
    if (v_stack_m98 != 0) goto loc_003BB101;
    result = ExpInterlockedPushEntrySList(Arg1, v_stack_m90, Arg3, 0);
loc_003BAFEA:
    if (result != 0) goto loc_003BB043;
    Arg2 = 0;
    result = (v_stack_m68) + (v_stack_m68);
    local_r10 = (uint32_t)((0) & (31));
    Arg1 = (0) >> (5);
    if ((local_r10 + 1) > 32) goto loc_003BB0BF;
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
loc_003BB03F:
loc_003BB043:
    Arg2 = -(0);
    if (v_stack_m88 != 0) goto loc_003BB111;
loc_003BB05C:
    if ((*(uint8_t *)(v_rip + 0xC09F8C)) > 1) goto loc_003BB4BC;
loc_003BB07C:
    if (0 != 0) goto loc_003BB33E;
loc_003BB085:
    local_rsp = (local_rsp) + (160);
    return v_stack_m78;
loc_003BB0A1:
    result = MiUpdateZeroFreeBitmap(Arg1, v_stack_m80, v_stack_m88, 1);
    *(uint64_t *)(v_stack_m80 + 0x18) = result;
    goto loc_003BAFC0;
loc_003BB0BF:
    if (local_r10 != 0) goto loc_003BB37D;
loc_003BB0C8:
    result = (uint32_t)((1) << (1));
    result = (uint32_t)((result) - (1));
    goto loc_003BB03F;
loc_003BB0D8:
    result = MiNodeFreeZeroPages(1, v_stack_m80, (uint32_t)(0x80010ULL), 1);
    if (result < v_stack_m68) goto loc_003BB085;
    local_rdi = 0;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x3A88) + 0x3EE5)) != 0) goto loc_003BB085;
    v_stack_p60 = 0xB40ULL;
    goto loc_003BAEC2;
loc_003BB101:
    result = InterlockedPushListSList(1, v_stack_m80, result, 0);
    goto loc_003BAFEA;
loc_003BB111:
    result = (v_stack_p18) >> (18);
    result = (uint32_t)((result) & (3));
    goto loc_003BB05C;
loc_003BB12F:
    v_stack_p40 = 0;
    if ((uint32_t)((uint32_t)(v_stack_pE8)) == 0) goto loc_003BB32B;
loc_003BB145:
    if ((*(uint32_t *)(v_rip + 0xA75000)) == ((uint32_t)(local_r10))) goto loc_003BB3F8;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) != 0) goto loc_003BB2F3;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20))))) >> (16));
    if ((((uint8_t)(Arg3)) & (32)) != 0) goto loc_003BB2F3;
    if ((((uint8_t)(Arg3)) & (16)) != 0) goto loc_003BB2F3;
    result = (uint8_t)(((uint8_t)(Arg3)) & (7));
    if (((uint8_t)(result)) > ((uint8_t)(local_r10))) goto loc_003BB2F3;
    if ((((uint8_t)(Arg3)) & (8)) != 0) goto loc_003BB2EA;
loc_003BB191:
    result = (*(uint64_t *)(local_rdi + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA74EEC) + result * 8)) != (*(uint64_t *)(arg1 + 0x3A88))) goto loc_003BB2F3;
    v_stack_pE0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    v_stack_pE2 = (uint8_t)(result);
    *(uint32_t *)(local_rdi + 0x20) = (uint32_t)((uint32_t)(v_stack_pE0));
    if ((((uint8_t)(Arg3)) & (8)) != 0) goto loc_003BB446;
loc_003BB1DB:
    result = (*(uint64_t *)(local_rdi + 0x18)) & ((uint32_t)(*(uint32_t *)(local_rdi + 0x20)));
    *(uint64_t *)(local_rdi + 0x18) = result;
    result = MiIsFreeZeroPfnCold(0, *(uint64_t *)(v_rip + 0xA74EEC), Arg3, 0);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_003BB459;
    if ((uint32_t)((uint32_t)(v_stack_pE8)) == 0) {
    }
    Arg4 = 0;
    v_stack_p20 = 0;
    local_r14 = (0) - (result);
    local_r14 = (local_r14) >> (4);
    local_r14 = (local_r14) * (result);
    result = MiUpdateLargePageCandidateValue(*(uint64_t *)(arg1 + 0x3A88), local_r14, Arg4 + 3, Arg4);
    local_r15 = (*(uint64_t *)(local_rdi)) & (result);
    if (local_r15 == result) goto loc_003BB2E6;
    local_rdi = (local_r15 + local_r15 * 2) << (4);
    local_rdi = (local_rdi) + (result);
loc_003BB28E:
    result = MiSetPfnSlist(v_stack_p40, (uint32_t)(v_stack_pE8), Arg4 + 3, Arg4);
    *(uint64_t *)(v_stack_p40) = local_rdi;
    Arg2 = 0;
    local_r12 = (0) + (1);
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & ((uint32_t)((uint32_t)(0x30000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x30000ULL)))) goto loc_003BB480;
loc_003BB2C6:
    local_rbp = (v_stack_m80) - (1);
    if (condition_is_equal) goto loc_003BAF73;
    goto loc_003BAF5C;
loc_003BB2E6:
    local_rdi = 0;
    goto loc_003BB28E;
loc_003BB2EA:
    if (((uint8_t)(result)) == 1) goto loc_003BB191;
loc_003BB2F3:
    local_rdi = (local_rdi) - (result);
    v_stack_p20 = local_r15;
    local_rdi = (local_rdi) >> (4);
    Arg3 = (Arg4 + 3) * (local_rdi);
    result = KeBugCheckEx(152 - 74, 152, Arg3, 0);
loc_003BB32B:
    if (!sign_flag) goto loc_003BB145;
loc_003BB33E:
loc_003BB34E:
    if (*(uint64_t *)(v_stack_p88) != 0) goto loc_003BB368;
loc_003BB356:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) + ((uint32_t)(local_r15)));
    local_r10 = (v_stack_p88) + (8);
    if (Arg3 < 2) goto loc_003BB34E;
    goto loc_003BB085;
loc_003BB368:
    Arg4 = -(*(uint64_t *)(v_stack_p88));
    goto loc_003BB356;
loc_003BB37D:
    local_r11 = (uint32_t)(((uint32_t)(v_stack_p38)) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(local_r11)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - ((uint32_t)(local_r15)));
    result = (uint32_t)((result) << ((uint8_t)(local_r10)));
    Arg3 = (Arg3) + (4);
    Arg4 = (Arg4) - ((uint32_t)(Arg2));
    if (Arg4 < 32) goto loc_003BB3C9;
    Arg1 = (Arg4) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg1);
    Arg4 = (Arg4) + (result);
loc_003BB3B9:
    *(uint32_t *)(Arg3) = 0xFFFFFFFFULL;
    Arg3 = (Arg3) + (4);
    Arg1 = (Arg1) - (local_r15);
    if (condition_is_not_equal) goto loc_003BB3B9;
loc_003BB3C9:
    if (Arg4 == NULL) goto loc_003BB043;
    goto loc_003BB0C8;
loc_003BB3D7:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) >> (3));
    Arg1 = (uint32_t)((Arg1) - (*(uint32_t *)(arg4 + 0x4)));
    v_stack_p30 = 1;
    if (local_rbp < Arg1) { Arg1 = local_rbp; }
    goto loc_003BAE88;
loc_003BB3F8:
    local_r10 = (local_rdi) - (Arg1);
    local_r10 = (local_r10) >> (4);
    local_r10 = (local_r10) * (Arg3);
    Arg1 = (local_r10) >> (5);
    local_r11 = (uint32_t)((local_r10) & (31));
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(local_r11)))));
loc_003BB446:
    result = MiPageListCollision(local_rdi, Arg2, *(uint64_t *)(v_rip + 0xA74D9D) + Arg1 * 4, local_r10);
    goto loc_003BB1DB;
loc_003BB459:
    if (v_stack_p30 == ((uint32_t)(local_rdi))) goto loc_003BB21B;
    result = MiAddPageToHeatList(v_stack_pF8, local_r15, 3, local_r10);
    Arg1 = 0;
    goto loc_003BB21B;
loc_003BB480:
    if (local_r14 < 0x100000ULL) { Arg1 = 1; }
    goto loc_003BB2C6;
loc_003BB490:
    result = (result) - (local_r12);
    result = MiIncreaseAvailablePages(*(uint64_t *)(arg1 + 0x3A88), result, 3, local_r10);
    local_r14 = 0;
    if (local_r12 == 0) goto loc_003BB085;
    goto loc_003BAF84;
loc_003BB4AF:
    result = MiIssuePageHeatList(result, result, 3, local_r10);
    goto loc_003BAF96;
loc_003BB4BC:
    goto loc_003BB07C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF08 + rdi*8` | `64` | `R/W` |
| `Arg1` | `+ 0xF18 + rdx*8` | `64` | `R/W` |
| `Arg1` | `+ 0x1400 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x3A08 + rax*8` | `64` | `R` |
| `Arg1` | `+ 0x3A60 + r14*8` | `64` | `R` |
| `Arg1` | `+ 0x3A60 + rdi*8` | `64` | `R` |
| `Arg1` | `+ 0x3A88` | `64` | `R` |
| `Arg1` | `+ 0x3B30 + rcx*8` | `64` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BADE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
