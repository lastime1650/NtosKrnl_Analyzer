# KiTimerWaitTest

- RVA: `0x002337D0`–`0x00233BD2` (길이 `1,026` bytes)
- VA: `0x00000001402337D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060514`
- 디코드: `275`개 명령, `1,026/1,026` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00233940` → [PsTimerResolutionActive](../3A/PsTimerResolutionActive_function_003A3010.md) (function, `0x003A3010`)
- `0x00233997` → [KiInsertTimerTable](KiInsertTimerTable_function_00233400.md) (function, `0x00233400`)
- `0x00233A1E` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00233A46` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00233A76` → [KiInsertQueueDpc](../20/KiInsertQueueDpc_function_00207C70.md) (function, `0x00207C70`)
- `0x00233A89` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00233AB9` → [KiInsertQueueInternal](../21/KiInsertQueueInternal_function_00219B30.md) (function, `0x00219B30`)
- `0x00233ADF` → [KiInsertQueueDpc](../20/KiInsertQueueDpc_function_00207C70.md) (function, `0x00207C70`)
- `0x00233AF5` → [KiTryUnwaitThread](../35/KiTryUnwaitThread_function_003506D0.md) (function, `0x003506D0`)
- `0x00233BC9` → [KiInsertQueueDpc](../20/KiInsertQueueDpc_function_00207C70.md) (function, `0x00207C70`)

### Direct callers
- [KiResumeThread](../20/KiResumeThread_function_00203644.md) at `0x00203A09`
- [KiCommitThreadWait](../20/KiCommitThreadWait_function_0020DFE0.md) at `0x0020E37E`
- [ExpSetTimerObject](ExpSetTimerObject_function_00231730.md) at `0x00231E77`
- [KiSetTimerEx](KiSetTimerEx_function_00232CB0.md) at `0x00232F76`
- [KeSetTimer](KeSetTimer_function_00233BE0.md) at `0x00233E88`
- [KiProcessExpiredTimerList](KiProcessExpiredTimerList_function_00234200.md) at `0x002342BA`
- [KiProcessExpiredTimerList](KiProcessExpiredTimerList_function_00234200.md) at `0x00234683`
- [KiAdjustTimerDueTimes](../4E/KiAdjustTimerDueTimes_function_004E8CD4.md) at `0x004E8F53`

### Static image references
- `0x002337FF` → RVA `0x00FC6F78` (`ALMOSTRO`; read)
- `0x0023381F` → RVA `0x00FC7250` (`ALMOSTRO`; read)
- `0x00233880` → RVA `0x00FC6B7C` (`ALMOSTRO`; read)
- `0x00233912` → RVA `0x00FC6C48` (`ALMOSTRO`; read)
- `0x00233B22` → RVA `0x00FC5030` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002337D0  4C 8B DC                        mov r11, rsp
002337D3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
002337D7  49 89 6B 18                     mov qword ptr [r11 + 0x18], rbp
002337DB  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
002337DF  57                              push rdi
002337E0  41 54                           push r12
002337E2  41 55                           push r13
002337E4  41 56                           push r14
002337E6  41 57                           push r15
002337E8  48 83 EC 50                     sub rsp, 0x50
002337EC  48 8B 72 30                     mov rsi, qword ptr [rdx + 0x30]
002337F0  33 C0                           xor eax, eax
002337F2  44 8A 22                        mov r12b, byte ptr [rdx]
002337F5  45 33 D2                        xor r10d, r10d
002337F8  48 8B E9                        mov rbp, rcx
002337FB  4D 89 53 10                     mov qword ptr [r11 + 0x10], r10
002337FF  48 8B 0D 72 37 D9 00            mov rcx, qword ptr [rip + 0xd93772]
00233806  0F 57 C0                        xorps xmm0, xmm0
00233809  48 33 F1                        xor rsi, rcx
0023380C  41 80 E4 7F                     and r12b, 0x7f
00233810  48 D3 C6                        rol rsi, cl
00233813  4D 8B F8                        mov r15, r8
00233816  48 33 F2                        xor rsi, rdx
00233819  48 8B FA                        mov rdi, rdx
0023381C  48 0F CE                        bswap rsi
0023381F  48 33 35 2A 3A D9 00            xor rsi, qword ptr [rip + 0xd93a2a]
00233826  41 B5 FF                        mov r13b, 0xff
00233829  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0023382E  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00233832  45 8D 5A 01                     lea r11d, [r10 + 1]
00233836  48 63 42 3C                     movsxd rax, dword ptr [rdx + 0x3c]
0023383A  85 C0                           test eax, eax
0023383C  0F 84 65 01 00 00               je 0x1402339a7
00233842  48 69 D8 F0 D8 FF FF            imul rbx, rax, -0x2710
00233849  8A 85 BA 38 00 00               mov al, byte ptr [rbp + 0x38ba]
0023384F  45 8A EA                        mov r13b, r10b
00233852  84 C0                           test al, al
00233854  74 3F                           je 0x140233895
00233856  8B 85 64 86 00 00               mov eax, dword ptr [rbp + 0x8664]
0023385C  FF C0                           inc eax
0023385E  89 85 64 86 00 00               mov dword ptr [rbp + 0x8664], eax
00233864  3D B8 0B 00 00                  cmp eax, 0xbb8
00233869  72 21                           jb 0x14023388c
0023386B  8B 8D 68 86 00 00               mov ecx, dword ptr [rbp + 0x8668]
00233871  44 89 95 64 86 00 00            mov dword ptr [rbp + 0x8664], r10d
00233878  81 F9 00 E1 F5 05               cmp ecx, 0x5f5e100
0023387E  73 0C                           jae 0x14023388c
00233880  03 0D F6 32 D9 00               add ecx, dword ptr [rip + 0xd932f6]
00233886  89 8D 68 86 00 00               mov dword ptr [rbp + 0x8668], ecx
0023388C  8B 85 68 86 00 00               mov eax, dword ptr [rbp + 0x8668]
00233892  48 2B D8                        sub rbx, rax
00233895  48 B9 08 00 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000008
0023389F  48 8B C3                        mov rax, rbx
002338A2  48 8B 09                        mov rcx, qword ptr [rcx]
002338A5  48 2B 42 18                     sub rax, qword ptr [rdx + 0x18]
002338A9  48 03 C1                        add rax, rcx
002338AC  78 04                           js 0x1402338b2
002338AE  48 89 4A 18                     mov qword ptr [rdx + 0x18], rcx
002338B2  44 8B 0A                        mov r9d, dword ptr [rdx]
002338B5  4D 8B F2                        mov r14, r10
002338B8  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
002338BD  41 C1 F9 08                     sar r9d, 8
002338C1  41 C0 E9 02                     shr r9b, 2
002338C5  45 84 C9                        test r9b, r9b
002338C8  74 48                           je 0x140233912
002338CA  41 8A C1                        mov al, r9b
002338CD  C0 E8 03                        shr al, 3
002338D0  04 02                           add al, 2
002338D2  0F B6 C8                        movzx ecx, al
002338D5  41 80 F9 08                     cmp r9b, 8
002338D9  41 8A C1                        mov al, r9b
002338DC  66 45 1B C0                     sbb r8w, r8w
002338E0  24 07                           and al, 7
002338E2  0F B6 D0                        movzx edx, al
002338E5  66 41 F7 D0                     not r8w
002338E9  66 41 83 E0 08                  and r8w, 8
002338EE  41 8D 04 0B                     lea eax, [r11 + rcx]
002338F2  66 44 0B C2                     or r8w, dx
002338F6  0F B6 C0                        movzx eax, al
002338F9  41 80 F9 08                     cmp r9b, 8
002338FD  0F 42 C8                        cmovb ecx, eax
00233900  66 41 D3 E0                     shl r8w, cl
00233904  41 0F B7 C0                     movzx eax, r8w
00233908  C1 E8 03                        shr eax, 3
0023390B  44 69 F0 10 27 00 00            imul r14d, eax, 0x2710
00233912  44 39 15 2F 33 D9 00            cmp dword ptr [rip + 0xd9332f], r10d
00233919  75 35                           jne 0x140233950
0023391B  4C 8D 47 08                     lea r8, [rdi + 8]
0023391F  66 44 89 5F 3A                  mov word ptr [rdi + 0x3a], r11w
00233924  49 8B 10                        mov rdx, qword ptr [r8]
00233927  EB 20                           jmp 0x140233949
00233929  48 8D 0A                        lea rcx, [rdx]
0023392C  48 8B 12                        mov rdx, qword ptr [rdx]
0023392F  44 38 59 10                     cmp byte ptr [rcx + 0x10], r11b
00233933  77 14                           ja 0x140233949
00233935  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00233939  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
00233940  E8 CB F6 16 00                  call 0x1403a3010
00233945  84 C0                           test al, al
00233947  75 07                           jne 0x140233950
00233949  49 3B D0                        cmp rdx, r8
0023394C  75 DB                           jne 0x140233929
0023394E  EB 05                           jmp 0x140233955
00233950  66 44 89 57 3A                  mov word ptr [rdi + 0x3a], r10w
00233955  80 64 24 31 FE                  and byte ptr [rsp + 0x31], 0xfe
0023395A  C6 44 24 33 40                  mov byte ptr [rsp + 0x33], 0x40
0023395F  48 29 5F 18                     sub qword ptr [rdi + 0x18], rbx
00233963  48 83 CA FF                     or rdx, 0xffffffffffffffff
00233967  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0023396B  4C 8B C6                        mov r8, rsi
0023396E  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
00233973  4A 8D 04 31                     lea rax, [rcx + r14]
00233977  48 3B C1                        cmp rax, rcx
0023397A  48 8B CD                        mov rcx, rbp
0023397D  48 0F 43 D0                     cmovae rdx, rax
00233981  48 C1 EA 12                     shr rdx, 0x12
00233985  44 0F B6 CA                     movzx r9d, dl
00233989  48 8B D7                        mov rdx, rdi
0023398C  44 88 4C 24 32                  mov byte ptr [rsp + 0x32], r9b
00233991  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00233995  89 07                           mov dword ptr [rdi], eax
00233997  E8 64 FA FF FF                  call 0x140233400
0023399C  45 33 D2                        xor r10d, r10d
0023399F  84 C0                           test al, al
002339A1  74 BC                           je 0x14023395f
002339A3  45 8D 5A 01                     lea r11d, [r10 + 1]
002339A7  44 89 5F 04                     mov dword ptr [rdi + 4], r11d
002339AB  48 8D 5F 08                     lea rbx, [rdi + 8]
002339AF  4C 8B 33                        mov r14, qword ptr [rbx]
002339B2  41 80 FC 08                     cmp r12b, 8
002339B6  0F 85 DB 00 00 00               jne 0x140233a97
002339BC  4C 3B F3                        cmp r14, rbx
002339BF  0F 84 4C 01 00 00               je 0x140233b11
002339C5  49 8B C6                        mov rax, r14
002339C8  4D 8B 36                        mov r14, qword ptr [r14]
002339CB  8A 48 10                        mov cl, byte ptr [rax + 0x10]
002339CE  41 3A CB                        cmp cl, r11b
002339D1  0F 85 D2 00 00 00               jne 0x140233aa9
002339D7  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
002339DC  E9 0B 01 00 00                  jmp 0x140233aec
002339E1  49 8B 0E                        mov rcx, qword ptr [r14]
002339E4  49 8B C6                        mov rax, r14
002339E7  4C 8B F1                        mov r14, rcx
002339EA  48 39 41 08                     cmp qword ptr [rcx + 8], rax
002339EE  0F 85 AE 00 00 00               jne 0x140233aa2
002339F4  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
002339F8  48 39 02                        cmp qword ptr [rdx], rax
002339FB  0F 85 A1 00 00 00               jne 0x140233aa2
00233A01  48 89 0A                        mov qword ptr [rdx], rcx
00233A04  48 89 51 08                     mov qword ptr [rcx + 8], rdx
00233A08  8A 48 10                        mov cl, byte ptr [rax + 0x10]
00233A0B  41 3A CB                        cmp cl, r11b
00233A0E  75 26                           jne 0x140233a36
00233A10  44 0F B7 40 12                  movzx r8d, word ptr [rax + 0x12]
00233A15  45 33 C9                        xor r9d, r9d
00233A18  48 8B D0                        mov rdx, rax
00233A1B  48 8B CD                        mov rcx, rbp
00233A1E  E8 AD CC 11 00                  call 0x1403506d0
00233A23  45 33 D2                        xor r10d, r10d
00233A26  84 C0                           test al, al
00233A28  74 67                           je 0x140233a91
00233A2A  83 6F 04 01                     sub dword ptr [rdi + 4], 1
00233A2E  0F 84 E4 00 00 00               je 0x140233b18
00233A34  EB 5B                           jmp 0x140233a91
00233A36  80 F9 02                        cmp cl, 2
00233A39  75 1C                           jne 0x140233a57
00233A3B  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00233A3F  48 8B D0                        mov rdx, rax
00233A42  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00233A46  E8 E5 60 FE FF                  call 0x140219b30
00233A4B  83 6F 04 01                     sub dword ptr [rdi + 4], 1
00233A4F  0F 84 C3 00 00 00               je 0x140233b18
00233A55  EB 37                           jmp 0x140233a8e
00233A57  45 33 C9                        xor r9d, r9d
00233A5A  80 F9 04                        cmp cl, 4
00233A5D  75 1E                           jne 0x140233a7d
00233A5F  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00233A63  4C 8B C0                        mov r8, rax
00233A66  44 89 57 04                     mov dword ptr [rdi + 4], r10d
00233A6A  48 8B D7                        mov rdx, rdi
00233A6D  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00233A71  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
00233A76  E8 F5 41 FD FF                  call 0x140207c70
00233A7B  EB 11                           jmp 0x140233a8e
00233A7D  41 B8 00 01 00 00               mov r8d, 0x100
00233A83  48 8B D0                        mov rdx, rax
00233A86  48 8B CD                        mov rcx, rbp
00233A89  E8 42 CC 11 00                  call 0x1403506d0
00233A8E  45 33 D2                        xor r10d, r10d
00233A91  41 BB 01 00 00 00               mov r11d, 1
00233A97  4C 3B F3                        cmp r14, rbx
00233A9A  0F 85 41 FF FF FF               jne 0x1402339e1
00233AA0  EB 76                           jmp 0x140233b18
00233AA2  B9 03 00 00 00                  mov ecx, 3
00233AA7  CD 29                           int 0x29
00233AA9  80 F9 02                        cmp cl, 2
00233AAC  75 12                           jne 0x140233ac0
00233AAE  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00233AB2  48 8B D0                        mov rdx, rax
00233AB5  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00233AB9  E8 72 60 FE FF                  call 0x140219b30
00233ABE  EB 3A                           jmp 0x140233afa
00233AC0  80 F9 04                        cmp cl, 4
00233AC3  75 21                           jne 0x140233ae6
00233AC5  C6 40 11 05                     mov byte ptr [rax + 0x11], 5
00233AC9  45 33 C9                        xor r9d, r9d
00233ACC  44 89 57 04                     mov dword ptr [rdi + 4], r10d
00233AD0  4C 8B C0                        mov r8, rax
00233AD3  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00233AD7  48 8B D7                        mov rdx, rdi
00233ADA  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
00233ADF  E8 8C 41 FD FF                  call 0x140207c70
00233AE4  EB 14                           jmp 0x140233afa
00233AE6  41 B8 00 01 00 00               mov r8d, 0x100
00233AEC  45 33 C9                        xor r9d, r9d
00233AEF  48 8B D0                        mov rdx, rax
00233AF2  48 8B CD                        mov rcx, rbp
00233AF5  E8 D6 CB 11 00                  call 0x1403506d0
00233AFA  41 BA 00 00 00 00               mov r10d, 0
00233B00  45 8D 5A 01                     lea r11d, [r10 + 1]
00233B04  4C 3B F3                        cmp r14, rbx
00233B07  0F 85 B8 FE FF FF               jne 0x1402339c5
00233B0D  48 8D 5F 08                     lea rbx, [rdi + 8]
00233B11  48 89 5B 08                     mov qword ptr [rbx + 8], rbx
00233B15  48 89 1B                        mov qword ptr [rbx], rbx
00233B18  48 85 F6                        test rsi, rsi
00233B1B  74 4B                           je 0x140233b68
00233B1D  4D 85 FF                        test r15, r15
00233B20  74 78                           je 0x140233b9a
00233B22  83 3D 07 15 D9 00 00            cmp dword ptr [rip + 0xd91507], 0
00233B29  74 0E                           je 0x140233b39
00233B2B  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
00233B2F  B9 00 08 00 00                  mov ecx, 0x800
00233B34  66 3B C1                        cmp ax, cx
00233B37  73 7E                           jae 0x140233bb7
00233B39  80 3E 1A                        cmp byte ptr [rsi], 0x1a
00233B3C  75 09                           jne 0x140233b47
00233B3E  80 BD B8 38 00 00 00            cmp byte ptr [rbp + 0x38b8], 0
00233B45  75 70                           jne 0x140233bb7
00233B47  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
00233B4E  48 89 B5 60 38 00 00            mov qword ptr [rbp + 0x3860], rsi
00233B55  48 85 46 10                     test qword ptr [rsi + 0x10], rax
00233B59  75 0D                           jne 0x140233b68
00233B5B  0F B6 85 D1 00 00 00            movzx eax, byte ptr [rbp + 0xd1]
00233B62  F0 48 0F AB 46 10               lock bts qword ptr [rsi + 0x10], rax
00233B68  41 0F B6 C5                     movzx eax, r13b
00233B6C  C1 E0 18                        shl eax, 0x18
00233B6F  0F BA E8 07                     bts eax, 7
00233B73  F7 D0                           not eax
00233B75  F0 21 07                        lock and dword ptr [rdi], eax
00233B78  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00233B7D  48 8B C6                        mov rax, rsi
00233B80  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00233B84  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
00233B88  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
00233B8C  49 8B E3                        mov rsp, r11
00233B8F  41 5F                           pop r15
00233B91  41 5E                           pop r14
00233B93  41 5D                           pop r13
00233B95  41 5C                           pop r12
00233B97  5F                              pop rdi
00233B98  C3                              ret
00233B99  CC                              int3
00233B9A  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
00233BA4  4C 8D BC 24 88 00 00 00         lea r15, [rsp + 0x88]
00233BAC  48 8B 00                        mov rax, qword ptr [rax]
00233BAF  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00233BB7  45 8B 47 04                     mov r8d, dword ptr [r15 + 4]
00233BBB  4C 8B CF                        mov r9, rdi
00233BBE  41 8B 17                        mov edx, dword ptr [r15]
00233BC1  48 8B CE                        mov rcx, rsi
00233BC4  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
00233BC9  E8 A2 40 FD FF                  call 0x140207c70
00233BCE  33 F6                           xor esi, esi
00233BD0  EB A6                           jmp 0x140233b78
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiTimerWaitTest(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int8 v_stack_m45;
    unsigned __int8 v_stack_m46;
    unsigned __int8 v_stack_m47;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p38;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp + 16) = 0;
    v_rsi = (*(unsigned __int64 *)(a2 + 48)) ^ (*(unsigned __int64 *)(v_rip + 14235506));
    v_r12 = (unsigned __int8)((*(unsigned __int8 *)(a2)) & (127));
    v_rsi = (v_rsi) ^ (a2);
    v_rsi = (v_rsi) ^ (*(unsigned __int64 *)(v_rip + 14236202));
    v_stack_m48 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    if ((unsigned int)((int)(*(unsigned int *)(a2 + 60))) == 0) goto loc_002339A7;
    v_rbx = (v_rbx) * ((int)(*(unsigned int *)(a2 + 60)));
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 14522)) == 0) goto loc_00233895;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 34404))) + 1);
    *(unsigned int *)(a1 + 34404) = (unsigned int)(result);
    if (((unsigned int)(result)) < 0xBB8ULL) goto loc_0023388C;
    *(unsigned int *)(a1 + 34404) = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 34408)))) < 0x5F5E100ULL) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 34408))) + (*(unsigned int *)(v_rip + 14234358)));
        *(unsigned int *)(a1 + 34408) = (unsigned int)(a1);
    }
    v_rbx = (v_rbx) - ((unsigned int)(*(unsigned int *)(a1 + 34408)));
loc_00233895:
    result = (v_rbx) - (*(unsigned __int64 *)(a2 + 24));
    result = (result) + (*(unsigned __int64 *)(a1));
    if (!(sign_flag)) {
        *(unsigned __int64 *)(a2 + 24) = *(unsigned __int64 *)(a1);
    }
    v_stack_m48 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) >> (8));
    a4 = (unsigned __int8)((a4) >> (2));
    v_r14 = 0;
    if ((unsigned __int8)(a4) != 0) {
        result = (unsigned __int8)(a4);
        result = (unsigned __int8)((result) >> (3));
        result = (unsigned __int8)((result) + (2));
        a1 = (unsigned __int8)(result);
        result = (unsigned __int8)(a4);
        result = (unsigned __int8)((result) & (7));
        a2 = (unsigned __int8)(result);
        a3 = (unsigned __int16)(~(a3));
        a3 = (unsigned __int16)((a3) & (8));
        result = v_r10 + 1 + a1 * 1;
        a3 = (unsigned __int16)((a3) | ((unsigned __int16)(a2)));
        result = (unsigned __int8)(result);
        if (((unsigned __int8)(a4)) < 8) { a1 = (unsigned int)(result); }
        a3 = (unsigned __int16)((a3) << ((unsigned __int8)(a1)));
        result = (unsigned __int16)(a3);
        result = (unsigned int)((result) >> (3));
        v_r14 = (unsigned int)((0) * ((unsigned int)(result)));
    }
    if ((*(unsigned int *)(v_rip + 14234415)) != 0) goto loc_00233950;
    *(unsigned __int16 *)(a2 + 58) = (unsigned __int16)(v_r10 + 1);
    goto loc_00233949;
loc_00233929:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 16)) > ((unsigned __int8)(v_r10 + 1))) goto loc_00233949;
    result = PsTimerResolutionActive(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8) + 24) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)), a2 + 8, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00233950;
loc_00233949:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) != (a2 + 8)) goto loc_00233929;
    goto loc_00233955;
loc_00233950:
    *(unsigned __int16 *)(a2 + 58) = 0;
loc_00233955:
    v_stack_m45 = 64;
loc_0023395F:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) | (-1);
    v_stack_m58 = 0;
    if ((*(unsigned __int64 *)(a2 + 24) + v_r14 * 1) >= (*(unsigned __int64 *)(a2 + 24))) { a2 = *(unsigned __int64 *)(a2 + 24) + v_r14 * 1; }
    a2 = (a2) >> (18);
    v_stack_m46 = (unsigned __int8)((unsigned __int8)(a2));
    *(unsigned int *)(a2) = (unsigned int)((unsigned int)(v_stack_m48));
    result = KiInsertTimerTable(a1, a2, v_rsi, (unsigned __int8)(a2));
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0023395F;
loc_002339A7:
    *(unsigned int *)(a2 + 4) = (unsigned int)(v_r10 + 1);
    if (((unsigned __int8)(v_r12)) != 8) goto loc_00233A97;
    if ((*(unsigned __int64 *)(a2 + 8)) == (a2 + 8)) goto loc_00233B11;
loc_002339C5:
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 8) + 16))) != ((unsigned __int8)(v_r10 + 1))) goto loc_00233AA9;
    goto loc_00233AEC;
loc_002339E1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) + 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)))) goto loc_00233AA2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 8))) != (*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)))) goto loc_00233AA2;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 8)) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 8);
    if (((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 16))) != ((unsigned __int8)(v_r10 + 1))) goto loc_00233A36;
    a4 = 0;
    result = KiTryUnwaitThread(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 18), a4);
    v_r10 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00233A91;
    if ((unsigned __int8)(result) == 0) goto loc_00233B18;
    goto loc_00233A91;
loc_00233A36:
    if (((unsigned __int8)(a1)) != 2) goto loc_00233A57;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) + 18), a4);
    if (((unsigned __int8)(a1)) == 2) goto loc_00233B18;
    goto loc_00233A8E;
loc_00233A57:
    a4 = 0;
    if (((unsigned __int8)(*(unsigned __int64 *)(result + 24))) != 4) goto loc_00233A7D;
    *(unsigned __int8 *)(result + 17) = 5;
    *(unsigned int *)(a2 + 4) = 0;
    v_stack_m58 = 0;
    result = KiInsertQueueDpc(*(unsigned __int64 *)(result + 24), a2, result, a4);
    goto loc_00233A8E;
loc_00233A7D:
    result = KiTryUnwaitThread(a1, result, 256, a4);
loc_00233A8E:
    v_r10 = 0;
loc_00233A91:
loc_00233A97:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)))) != (a2 + 8)) goto loc_002339E1;
    goto loc_00233B18;
loc_00233AA2:
loc_00233AA9:
    if (3 != 2) goto loc_00233AC0;
    *(unsigned __int8 *)(result + 17) = 5;
    result = KiInsertQueueInternal(*(unsigned __int64 *)(result + 24), result, 256, a4);
    goto loc_00233AFA;
loc_00233AC0:
    if (((unsigned __int8)(*(unsigned __int64 *)(result + 24))) != 4) goto loc_00233AE6;
    *(unsigned __int8 *)(result + 17) = 5;
    a4 = 0;
    *(unsigned int *)(a2 + 4) = 0;
    v_stack_m58 = 0;
    result = KiInsertQueueDpc(*(unsigned __int64 *)(result + 24), a2, result, a4);
    goto loc_00233AFA;
loc_00233AE6:
loc_00233AEC:
    a4 = 0;
    result = KiTryUnwaitThread(a1, result, 256, a4);
loc_00233AFA:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)))) != (a2 + 8)) goto loc_002339C5;
loc_00233B11:
    *(unsigned __int64 *)(a2 + 8 + 8) = a2 + 8;
    *(unsigned __int64 *)(a2 + 8) = a2 + 8;
loc_00233B18:
    if (v_rsi == 0) goto loc_00233B68;
    if (a3 == 0) goto loc_00233B9A;
    if ((*(unsigned int *)(v_rip + 14226695)) == 0) goto loc_00233B39;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rsi + 2))) >= ((unsigned __int16)((unsigned int)(0x800ULL)))) goto loc_00233BB7;
loc_00233B39:
    if ((*(unsigned __int8 *)(v_rsi)) != 26) goto loc_00233B47;
    if ((*(unsigned __int8 *)(a1 + 14520)) != 0) goto loc_00233BB7;
loc_00233B47:
    *(unsigned __int64 *)(a1 + 14432) = v_rsi;
    result = *(unsigned __int64 *)(a1 + 200);
    if (((*(unsigned __int64 *)(v_rsi + 16)) & (*(unsigned __int64 *)(a1 + 200))) == 0) {
        result = *(unsigned __int8 *)(a1 + 209);
    }
    result = (unsigned int)((0) << (24));
    result = (unsigned int)(~(result));
loc_00233B78:
    return v_rsi;
loc_00233B9A:
    v_stack_p38 = *(unsigned __int64 *)(v_rsi);
loc_00233BB7:
    v_stack_m30 = 0;
    result = KiInsertQueueDpc(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(*(unsigned int *)(v_stack_p38)), (unsigned int)(*(unsigned int *)(v_stack_p38 + 4)), a2);
    v_rsi = 0;
    goto loc_00233B78;
}
```

## 5. (Beta) C Style

```c
int64_t KiTimerWaitTest(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint8_t v_stack_m45;
    uint8_t v_stack_m46;
    uint8_t v_stack_m47;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p38;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    local_r10 = 0;
    *(uint64_t *)(local_rsp + 0x10) = 0;
    local_rsi = (*(uint64_t *)(arg2 + 0x30)) ^ (*(uint64_t *)(v_rip + 0xD93772));
    local_r12 = (uint8_t)((*(uint8_t *)(arg2)) & (127));
    local_rsi = (local_rsi) ^ (Arg2);
    local_rsi = (local_rsi) ^ (*(uint64_t *)(v_rip + 0xD93A2A));
    v_stack_m48 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    if ((uint32_t)((int32_t)(*(uint32_t *)(arg2 + 0x3C))) == 0) goto loc_002339A7;
    local_rbx = (local_rbx) * ((int32_t)(*(uint32_t *)(arg2 + 0x3C)));
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x38BA)) == 0) goto loc_00233895;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8664))) + 1);
    *(uint32_t *)(arg1 + 0x8664) = (uint32_t)(result);
    if (((uint32_t)(result)) < 0xBB8ULL) goto loc_0023388C;
    *(uint32_t *)(arg1 + 0x8664) = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8668)))) < 0x5F5E100ULL) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8668))) + (*(uint32_t *)(v_rip + 0xD932F6)));
        *(uint32_t *)(arg1 + 0x8668) = (uint32_t)(Arg1);
    }
    local_rbx = (local_rbx) - ((uint32_t)(*(uint32_t *)(arg1 + 0x8668)));
loc_00233895:
    result = (local_rbx) - (*(uint64_t *)(arg2 + 0x18));
    result = (result) + (*(uint64_t *)(arg1));
    if (!(sign_flag)) {
        *(uint64_t *)(arg2 + 0x18) = *(uint64_t *)(arg1);
    }
    v_stack_m48 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    a4 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) >> (8));
    a4 = (uint8_t)((a4) >> (2));
    local_r14 = 0;
    if ((uint8_t)(a4) != 0) {
        result = (uint8_t)(a4);
        result = (uint8_t)((result) >> (3));
        result = (uint8_t)((result) + (2));
        Arg1 = (uint8_t)(result);
        result = (uint8_t)(a4);
        result = (uint8_t)((result) & (7));
        Arg2 = (uint8_t)(result);
        Arg3 = (uint16_t)(~(Arg3));
        Arg3 = (uint16_t)((Arg3) & (8));
        result = local_r10 + 1 + Arg1 * 1;
        Arg3 = (uint16_t)((Arg3) | ((uint16_t)(Arg2)));
        result = (uint8_t)(result);
        if (((uint8_t)(a4)) < 8) { Arg1 = (uint32_t)(result); }
        Arg3 = (uint16_t)((Arg3) << ((uint8_t)(Arg1)));
        result = (uint16_t)(Arg3);
        result = (uint32_t)((result) >> (3));
        local_r14 = (uint32_t)((0) * ((uint32_t)(result)));
    }
    if ((*(uint32_t *)(v_rip + 0xD9332F)) != 0) goto loc_00233950;
    *(uint16_t *)(arg2 + 0x3A) = (uint16_t)(local_r10 + 1);
    goto loc_00233949;
loc_00233929:
    if ((*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10)) > ((uint8_t)(local_r10 + 1))) goto loc_00233949;
    result = PsTimerResolutionActive(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8) + 0x18) + 0x220), *(uint64_t *)(*(uint64_t *)(arg2 + 0x8)), Arg2 + 8, a4);
    if ((uint8_t)(result) != 0) goto loc_00233950;
loc_00233949:
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) != (Arg2 + 8)) goto loc_00233929;
    goto loc_00233955;
loc_00233950:
    *(uint16_t *)(arg2 + 0x3A) = 0;
loc_00233955:
    v_stack_m45 = 64;
loc_0023395F:
    Arg2 = (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) | (-1);
    v_stack_m58 = 0;
    if ((*(uint64_t *)(arg2 + 0x18) + local_r14 * 1) >= (*(uint64_t *)(arg2 + 0x18))) { Arg2 = *(uint64_t *)(arg2 + 0x18) + local_r14 * 1; }
    Arg2 = (Arg2) >> (18);
    v_stack_m46 = (uint8_t)((uint8_t)(Arg2));
    *(uint32_t *)(arg2) = (uint32_t)((uint32_t)(v_stack_m48));
    result = KiInsertTimerTable(Arg1, Arg2, local_rsi, (uint8_t)(Arg2));
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_0023395F;
loc_002339A7:
    *(uint32_t *)(arg2 + 0x4) = (uint32_t)(local_r10 + 1);
    if (((uint8_t)(local_r12)) != 8) goto loc_00233A97;
    if ((*(uint64_t *)(arg2 + 0x8)) == (Arg2 + 8)) goto loc_00233B11;
loc_002339C5:
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x8) + 0x10))) != ((uint8_t)(local_r10 + 1))) goto loc_00233AA9;
    goto loc_00233AEC;
loc_002339E1:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) + 0x8)) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)))) goto loc_00233AA2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x8))) != (*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)))) goto loc_00233AA2;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x8)) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)));
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) + 0x8) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x8);
    if (((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x10))) != ((uint8_t)(local_r10 + 1))) goto loc_00233A36;
    a4 = 0;
    result = KiTryUnwaitThread(Arg1, *(uint64_t *)(*(uint64_t *)(arg2 + 0x8)), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x12), a4);
    local_r10 = 0;
    if ((uint8_t)(result) == 0) goto loc_00233A91;
    if ((uint8_t)(result) == 0) goto loc_00233B18;
    goto loc_00233A91;
loc_00233A36:
    if (((uint8_t)(Arg1)) != 2) goto loc_00233A57;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) + 0x12), a4);
    if (((uint8_t)(Arg1)) == 2) goto loc_00233B18;
    goto loc_00233A8E;
loc_00233A57:
    a4 = 0;
    if (((uint8_t)(*(uint64_t *)(result + 0x18))) != 4) goto loc_00233A7D;
    *(uint8_t *)(result + 0x11) = 5;
    *(uint32_t *)(arg2 + 0x4) = 0;
    v_stack_m58 = 0;
    result = KiInsertQueueDpc(*(uint64_t *)(result + 0x18), Arg2, result, a4);
    goto loc_00233A8E;
loc_00233A7D:
    result = KiTryUnwaitThread(Arg1, result, 256, a4);
loc_00233A8E:
    local_r10 = 0;
loc_00233A91:
loc_00233A97:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)))) != (Arg2 + 8)) goto loc_002339E1;
    goto loc_00233B18;
loc_00233AA2:
loc_00233AA9:
    if (3 != 2) goto loc_00233AC0;
    *(uint8_t *)(result + 0x11) = 5;
    result = KiInsertQueueInternal(*(uint64_t *)(result + 0x18), result, 256, a4);
    goto loc_00233AFA;
loc_00233AC0:
    if (((uint8_t)(*(uint64_t *)(result + 0x18))) != 4) goto loc_00233AE6;
    *(uint8_t *)(result + 0x11) = 5;
    a4 = 0;
    *(uint32_t *)(arg2 + 0x4) = 0;
    v_stack_m58 = 0;
    result = KiInsertQueueDpc(*(uint64_t *)(result + 0x18), Arg2, result, a4);
    goto loc_00233AFA;
loc_00233AE6:
loc_00233AEC:
    a4 = 0;
    result = KiTryUnwaitThread(Arg1, result, 256, a4);
loc_00233AFA:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x8)))) != (Arg2 + 8)) goto loc_002339C5;
loc_00233B11:
    *(void **)(arg2 + 0x8 + 0x8) = Arg2 + 8;
    *(void **)(arg2 + 0x8) = Arg2 + 8;
loc_00233B18:
    if (local_rsi == 0) goto loc_00233B68;
    if (Arg3 == 0) goto loc_00233B9A;
    if ((*(uint32_t *)(v_rip + 0xD91507)) == 0) goto loc_00233B39;
    if (((uint16_t)(*(uint16_t *)(local_rsi + 0x2))) >= ((uint16_t)((uint32_t)(0x800ULL)))) goto loc_00233BB7;
loc_00233B39:
    if ((*(uint8_t *)(local_rsi)) != 26) goto loc_00233B47;
    if ((*(uint8_t *)(arg1 + 0x38B8)) != 0) goto loc_00233BB7;
loc_00233B47:
    *(uint64_t *)(arg1 + 0x3860) = local_rsi;
    result = *(uint64_t *)(arg1 + 0xC8);
    if (((*(uint64_t *)(local_rsi + 0x10)) & (*(uint64_t *)(arg1 + 0xC8))) == 0) {
        result = *(uint8_t *)(arg1 + 0xD1);
    }
    result = (uint32_t)((0) << (24));
    result = (uint32_t)(~(result));
loc_00233B78:
    return local_rsi;
loc_00233B9A:
    v_stack_p38 = *(uint64_t *)(local_rsi);
loc_00233BB7:
    v_stack_m30 = 0;
    result = KiInsertQueueDpc(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(*(uint32_t *)(v_stack_p38)), (uint32_t)(*(uint32_t *)(v_stack_p38 + 0x4)), Arg2);
    local_rsi = 0;
    goto loc_00233B78;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC8` | `64` | `R` |
| `Arg1` | `+ 0xD1` | `8` | `R` |
| `Arg1` | `+ 0x3860` | `64` | `W` |
| `Arg1` | `+ 0x38B8` | `8` | `R` |
| `Arg1` | `+ 0x38BA` | `8` | `R` |
| `Arg1` | `+ 0x8664` | `32` | `R` |
| `Arg1` | `+ 0x8664` | `32` | `W` |
| `Arg1` | `+ 0x8668` | `32` | `R` |
| `Arg1` | `+ 0x8668` | `32` | `W` |
| `Arg2` | `+ 0x0` | `8` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x4` | `32` | `R/W` |
| `Arg2` | `+ 0x4` | `32` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R/W` |
| `Arg2` | `+ 0x18` | `64` | `W` |
| `Arg2` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x3A` | `16` | `W` |
| `Arg2` | `+ 0x3C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002337D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
