# KiCancelTimer

- RVA: `0x003D3A80`–`0x003D3F0A` (길이 `1,162` bytes)
- VA: `0x00000001403D3A80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00091904`
- 디코드: `284`개 명령, `1,162/1,162` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x003D3BFF` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x003D3D67` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3D76` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3E04` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3E0F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3E24` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3E33` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3E4B` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3E5A` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3E72` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3E81` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3E99` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003D3EA8` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003D3EF1` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)

### Direct callers
- [KiSwapThread](../35/KiSwapThread_function_00355640.md) at `0x003559B2`
- [ExpTimerPause](ExpTimerPause_function_003D38C4.md) at `0x003D3911`
- [KeCancelTimerInternal](KeCancelTimerInternal_function_003D39E4.md) at `0x003D3A07`
- [KiSuspendThread](../46/KiSuspendThread_function_0046B964.md) at `0x0046BB28`

### Static image references
- `0x003D3A8B` → RVA `0x00E0A740` (`.data`; read)
- `0x003D3ABC` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x003D3B1C` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x003D3BC6` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x003D3C7A` → RVA `0x00FC5030` (`ALMOSTRO`; read)
- `0x003D3D59` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003D3A80  4C 8B DC                        mov r11, rsp
003D3A83  53                              push rbx
003D3A84  55                              push rbp
003D3A85  56                              push rsi
003D3A86  57                              push rdi
003D3A87  48 83 EC 78                     sub rsp, 0x78
003D3A8B  48 8B 05 AE 6C A3 00            mov rax, qword ptr [rip + 0xa36cae]
003D3A92  48 33 C4                        xor rax, rsp
003D3A95  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
003D3A9A  4D 89 63 10                     mov qword ptr [r11 + 0x10], r12
003D3A9E  48 8B F9                        mov rdi, rcx
003D3AA1  4D 89 6B 18                     mov qword ptr [r11 + 0x18], r13
003D3AA5  40 32 ED                        xor bpl, bpl
003D3AA8  4D 89 73 20                     mov qword ptr [r11 + 0x20], r14
003D3AAC  4D 89 7B D8                     mov qword ptr [r11 - 0x28], r15
003D3AB0  88 54 24 30                     mov byte ptr [rsp + 0x30], dl
003D3AB4  49 C7 43 A0 00 00 00 00         mov qword ptr [r11 - 0x60], 0
003D3ABC  4C 8D 1D 3D C5 C2 FF            lea r11, [rip - 0x3d3ac3]
003D3AC3  33 DB                           xor ebx, ebx
003D3AC5  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
003D3ACA  0F 82 E1 01 00 00               jb 0x1403d3cb1
003D3AD0  F6 47 03 C0                     test byte ptr [rdi + 3], 0xc0
003D3AD4  0F 84 B0 00 00 00               je 0x1403d3b8a
003D3ADA  0F B7 47 38                     movzx eax, word ptr [rdi + 0x38]
003D3ADE  44 0F B6 4F 02                  movzx r9d, byte ptr [rdi + 2]
003D3AE3  45 8B E9                        mov r13d, r9d
003D3AE6  4D 8B 94 C3 40 8C FC 00         mov r10, qword ptr [r11 + rax*8 + 0xfc8c40]
003D3AEE  0F B7 47 3A                     movzx eax, word ptr [rdi + 0x3a]
003D3AF2  49 8D 59 10                     lea rbx, [r9 + 0x10]
003D3AF6  48 C1 E0 08                     shl rax, 8
003D3AFA  48 03 D8                        add rbx, rax
003D3AFD  4C 89 54 24 48                  mov qword ptr [rsp + 0x48], r10
003D3B02  48 C1 E3 05                     shl rbx, 5
003D3B06  4D 8D A2 00 41 00 00            lea r12, [r10 + 0x4100]
003D3B0D  49 03 DC                        add rbx, r12
003D3B10  33 F6                           xor esi, esi
003D3B12  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
003D3B18  73 1A                           jae 0x1403d3b34
003D3B1A  FF C6                           inc esi
003D3B1C  85 35 8A 17 BF 00               test dword ptr [rip + 0xbf178a], esi
003D3B22  0F 84 31 02 00 00               je 0x1403d3d59
003D3B28  F3 90                           pause
003D3B2A  48 8B 03                        mov rax, qword ptr [rbx]
003D3B2D  48 85 C0                        test rax, rax
003D3B30  74 E0                           je 0x1403d3b12
003D3B32  EB E6                           jmp 0x1403d3b1a
003D3B34  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003D3B38  84 C0                           test al, al
003D3B3A  0F 88 61 02 00 00               js 0x1403d3da1
003D3B40  44 0F B7 47 3A                  movzx r8d, word ptr [rdi + 0x3a]
003D3B45  48 8D 57 20                     lea rdx, [rdi + 0x20]
003D3B49  48 8B 0A                        mov rcx, qword ptr [rdx]
003D3B4C  45 8B F8                        mov r15d, r8d
003D3B4F  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
003D3B53  49 83 F7 01                     xor r15, 1
003D3B57  49 C1 E7 08                     shl r15, 8
003D3B5B  45 8B F0                        mov r14d, r8d
003D3B5E  49 C1 E6 08                     shl r14, 8
003D3B62  49 83 C7 10                     add r15, 0x10
003D3B66  49 83 C6 10                     add r14, 0x10
003D3B6A  4D 03 FD                        add r15, r13
003D3B6D  4D 03 F5                        add r14, r13
003D3B70  49 C1 E7 05                     shl r15, 5
003D3B74  49 C1 E6 05                     shl r14, 5
003D3B78  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
003D3B7C  75 05                           jne 0x1403d3b83
003D3B7E  48 39 10                        cmp qword ptr [rax], rdx
003D3B81  74 17                           je 0x1403d3b9a
003D3B83  B9 03 00 00 00                  mov ecx, 3
003D3B88  CD 29                           int 0x29
003D3B8A  40 38 6C 24 30                  cmp byte ptr [rsp + 0x30], bpl
003D3B8F  74 35                           je 0x1403d3bc6
003D3B91  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
003D3B98  EB 2C                           jmp 0x1403d3bc6
003D3B9A  48 89 08                        mov qword ptr [rax], rcx
003D3B9D  48 89 41 08                     mov qword ptr [rcx + 8], rax
003D3BA1  48 3B C1                        cmp rax, rcx
003D3BA4  74 68                           je 0x1403d3c0e
003D3BA6  F0 48 83 23 00                  lock and qword ptr [rbx], 0
003D3BAB  B8 7F FF FF BF                  mov eax, 0xbfffff7f
003D3BB0  BA FF FF FF BF                  mov edx, 0xbfffffff
003D3BB5  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
003D3BBA  48 8B CF                        mov rcx, rdi
003D3BBD  40 B5 01                        mov bpl, 1
003D3BC0  0F 44 C2                        cmove eax, edx
003D3BC3  F0 21 01                        lock and dword ptr [rcx], eax
003D3BC6  F7 05 38 2F BF 00 00 00 02 00   test dword ptr [rip + 0xbf2f38], 0x20000
003D3BD0  0F 85 DC 02 00 00               jne 0x1403d3eb2
003D3BD6  4C 8B 7C 24 70                  mov r15, qword ptr [rsp + 0x70]
003D3BDB  40 0F B6 C5                     movzx eax, bpl
003D3BDF  4C 8B B4 24 B8 00 00 00         mov r14, qword ptr [rsp + 0xb8]
003D3BE7  4C 8B AC 24 B0 00 00 00         mov r13, qword ptr [rsp + 0xb0]
003D3BEF  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
003D3BF7  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
003D3BFC  48 33 CC                        xor rcx, rsp
003D3BFF  E8 3C 8A 2D 00                  call 0x1406ac640
003D3C04  48 83 C4 78                     add rsp, 0x78
003D3C08  5F                              pop rdi
003D3C09  5E                              pop rsi
003D3C0A  5D                              pop rbp
003D3C0B  5B                              pop rbx
003D3C0C  C3                              ret
003D3C0D  CC                              int3
003D3C0E  43 C7 44 26 1C FF FF FF FF      mov dword ptr [r14 + r12 + 0x1c], 0xffffffff
003D3C17  66 45 85 C0                     test r8w, r8w
003D3C1B  0F 85 B9 00 00 00               jne 0x1403d3cda
003D3C21  49 8D B5 10 01 00 00            lea rsi, [r13 + 0x110]
003D3C28  48 C1 E6 05                     shl rsi, 5
003D3C2C  49 03 F4                        add rsi, r12
003D3C2F  33 ED                           xor ebp, ebp
003D3C31  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
003D3C37  73 1A                           jae 0x1403d3c53
003D3C39  FF C5                           inc ebp
003D3C3B  85 2D 6B 16 BF 00               test dword ptr [rip + 0xbf166b], ebp
003D3C41  0F 84 CF 01 00 00               je 0x1403d3e16
003D3C47  F3 90                           pause
003D3C49  48 8B 06                        mov rax, qword ptr [rsi]
003D3C4C  48 85 C0                        test rax, rax
003D3C4F  74 E0                           je 0x1403d3c31
003D3C51  EB E6                           jmp 0x1403d3c39
003D3C53  43 83 7C 26 1C FF               cmp dword ptr [r14 + r12 + 0x1c], -1
003D3C59  75 4C                           jne 0x1403d3ca7
003D3C5B  43 83 7C 27 1C FF               cmp dword ptr [r15 + r12 + 0x1c], -1
003D3C61  75 44                           jne 0x1403d3ca7
003D3C63  4C 8B 54 24 48                  mov r10, qword ptr [rsp + 0x48]
003D3C68  48 8D 0D 91 C3 C2 FF            lea rcx, [rip - 0x3d3c6f]
003D3C6F  41 0F B6 82 D0 00 00 00         movzx eax, byte ptr [r10 + 0xd0]
003D3C77  48 03 C0                        add rax, rax
003D3C7A  83 3D AF 13 BF 00 00            cmp dword ptr [rip + 0xbf13af], 0
003D3C81  48 8B 8C C1 28 85 FC 00         mov rcx, qword ptr [rcx + rax*8 + 0xfc8528]
003D3C89  0F 84 F1 00 00 00               je 0x1403d3d80
003D3C8F  45 8B CD                        mov r9d, r13d
003D3C92  49 C1 ED 06                     shr r13, 6
003D3C96  41 83 E1 3F                     and r9d, 0x3f
003D3C9A  41 8B C1                        mov eax, r9d
003D3C9D  F0 4A 0F B3 04 E9               lock btr qword ptr [rcx + r13*8], rax
003D3CA3  4A 8D 0C E9                     lea rcx, [rcx + r13*8]
003D3CA7  F0 48 83 26 00                  lock and qword ptr [rsi], 0
003D3CAC  E9 F5 FE FF FF                  jmp 0x1403d3ba6
003D3CB1  FF C3                           inc ebx
003D3CB3  85 1D F3 15 BF 00               test dword ptr [rip + 0xbf15f3], ebx
003D3CB9  0F 84 7E 01 00 00               je 0x1403d3e3d
003D3CBF  F3 90                           pause
003D3CC1  8B 07                           mov eax, dword ptr [rdi]
003D3CC3  84 C0                           test al, al
003D3CC5  78 EA                           js 0x1403d3cb1
003D3CC7  F0 0F BA 2F 07                  lock bts dword ptr [rdi], 7
003D3CCC  72 E3                           jb 0x1403d3cb1
003D3CCE  4C 8D 1D 2B C3 C2 FF            lea r11, [rip - 0x3d3cd5]
003D3CD5  E9 F6 FD FF FF                  jmp 0x1403d3ad0
003D3CDA  49 8D 75 10                     lea rsi, [r13 + 0x10]
003D3CDE  48 C1 E6 05                     shl rsi, 5
003D3CE2  49 03 F4                        add rsi, r12
003D3CE5  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
003D3CEB  73 04                           jae 0x1403d3cf1
003D3CED  F3 90                           pause
003D3CEF  EB 09                           jmp 0x1403d3cfa
003D3CF1  48 85 F6                        test rsi, rsi
003D3CF4  0F 85 59 FF FF FF               jne 0x1403d3c53
003D3CFA  F0 48 83 23 00                  lock and qword ptr [rbx], 0
003D3CFF  33 DB                           xor ebx, ebx
003D3D01  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
003D3D07  73 1A                           jae 0x1403d3d23
003D3D09  FF C3                           inc ebx
003D3D0B  85 1D 9B 15 BF 00               test dword ptr [rip + 0xbf159b], ebx
003D3D11  0F 84 4D 01 00 00               je 0x1403d3e64
003D3D17  F3 90                           pause
003D3D19  48 8B 06                        mov rax, qword ptr [rsi]
003D3D1C  48 85 C0                        test rax, rax
003D3D1F  74 E0                           je 0x1403d3d01
003D3D21  EB E6                           jmp 0x1403d3d09
003D3D23  49 8D 9D 10 01 00 00            lea rbx, [r13 + 0x110]
003D3D2A  48 C1 E3 05                     shl rbx, 5
003D3D2E  49 03 DC                        add rbx, r12
003D3D31  33 ED                           xor ebp, ebp
003D3D33  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
003D3D39  0F 83 14 FF FF FF               jae 0x1403d3c53
003D3D3F  FF C5                           inc ebp
003D3D41  85 2D 65 15 BF 00               test dword ptr [rip + 0xbf1565], ebp
003D3D47  0F 84 3E 01 00 00               je 0x1403d3e8b
003D3D4D  F3 90                           pause
003D3D4F  48 8B 03                        mov rax, qword ptr [rbx]
003D3D52  48 85 C0                        test rax, rax
003D3D55  74 DC                           je 0x1403d3d33
003D3D57  EB E6                           jmp 0x1403d3d3f
003D3D59  8B 05 59 2D BF 00               mov eax, dword ptr [rip + 0xbf2d59]
003D3D5F  A8 40                           test al, 0x40
003D3D61  0F 84 C1 FD FF FF               je 0x1403d3b28
003D3D67  E8 24 B7 F3 FF                  call 0x14030f490
003D3D6C  84 C0                           test al, al
003D3D6E  0F 84 B4 FD FF FF               je 0x1403d3b28
003D3D74  8B CE                           mov ecx, esi
003D3D76  E8 E5 B6 F3 FF                  call 0x14030f460
003D3D7B  E9 AA FD FF FF                  jmp 0x1403d3b2a
003D3D80  45 0F B6 8A D1 00 00 00         movzx r9d, byte ptr [r10 + 0xd1]
003D3D88  49 C1 E5 06                     shl r13, 6
003D3D8C  49 03 CD                        add rcx, r13
003D3D8F  41 8B C1                        mov eax, r9d
003D3D92  F0 48 0F B3 01                  lock btr qword ptr [rcx], rax
003D3D97  F0 48 83 26 00                  lock and qword ptr [rsi], 0
003D3D9C  E9 05 FE FF FF                  jmp 0x1403d3ba6
003D3DA1  F0 48 83 23 00                  lock and qword ptr [rbx], 0
003D3DA6  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003D3DAA  33 C9                           xor ecx, ecx
003D3DAC  83 E0 3F                        and eax, 0x3f
003D3DAF  49 87 0C C4                     xchg qword ptr [r12 + rax*8], rcx
003D3DB3  48 85 C9                        test rcx, rcx
003D3DB6  0F 85 3F 01 00 00               jne 0x1403d3efb
003D3DBC  F0 81 27 7F FF FF FF            lock and dword ptr [rdi], 0xffffff7f
003D3DC3  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003D3DC7  4C 8D 1D 32 C2 C2 FF            lea r11, [rip - 0x3d3dce]
003D3DCE  33 DB                           xor ebx, ebx
003D3DD0  84 C0                           test al, al
003D3DD2  0F 89 EB FC FF FF               jns 0x1403d3ac3
003D3DD8  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
003D3DE0  FF C3                           inc ebx
003D3DE2  85 1D C4 14 BF 00               test dword ptr [rip + 0xbf14c4], ebx
003D3DE8  74 10                           je 0x1403d3dfa
003D3DEA  F3 90                           pause
003D3DEC  0F B6 47 03                     movzx eax, byte ptr [rdi + 3]
003D3DF0  84 C0                           test al, al
003D3DF2  0F 89 C4 FC FF FF               jns 0x1403d3abc
003D3DF8  EB E6                           jmp 0x1403d3de0
003D3DFA  8B 05 B8 2C BF 00               mov eax, dword ptr [rip + 0xbf2cb8]
003D3E00  A8 40                           test al, 0x40
003D3E02  74 E6                           je 0x1403d3dea
003D3E04  E8 87 B6 F3 FF                  call 0x14030f490
003D3E09  84 C0                           test al, al
003D3E0B  74 DD                           je 0x1403d3dea
003D3E0D  8B CB                           mov ecx, ebx
003D3E0F  E8 4C B6 F3 FF                  call 0x14030f460
003D3E14  EB D6                           jmp 0x1403d3dec
003D3E16  8B 05 9C 2C BF 00               mov eax, dword ptr [rip + 0xbf2c9c]
003D3E1C  A8 40                           test al, 0x40
003D3E1E  0F 84 23 FE FF FF               je 0x1403d3c47
003D3E24  E8 67 B6 F3 FF                  call 0x14030f490
003D3E29  84 C0                           test al, al
003D3E2B  0F 84 16 FE FF FF               je 0x1403d3c47
003D3E31  8B CD                           mov ecx, ebp
003D3E33  E8 28 B6 F3 FF                  call 0x14030f460
003D3E38  E9 0C FE FF FF                  jmp 0x1403d3c49
003D3E3D  8B 05 75 2C BF 00               mov eax, dword ptr [rip + 0xbf2c75]
003D3E43  A8 40                           test al, 0x40
003D3E45  0F 84 74 FE FF FF               je 0x1403d3cbf
003D3E4B  E8 40 B6 F3 FF                  call 0x14030f490
003D3E50  84 C0                           test al, al
003D3E52  0F 84 67 FE FF FF               je 0x1403d3cbf
003D3E58  8B CB                           mov ecx, ebx
003D3E5A  E8 01 B6 F3 FF                  call 0x14030f460
003D3E5F  E9 5D FE FF FF                  jmp 0x1403d3cc1
003D3E64  8B 05 4E 2C BF 00               mov eax, dword ptr [rip + 0xbf2c4e]
003D3E6A  A8 40                           test al, 0x40
003D3E6C  0F 84 A5 FE FF FF               je 0x1403d3d17
003D3E72  E8 19 B6 F3 FF                  call 0x14030f490
003D3E77  84 C0                           test al, al
003D3E79  0F 84 98 FE FF FF               je 0x1403d3d17
003D3E7F  8B CB                           mov ecx, ebx
003D3E81  E8 DA B5 F3 FF                  call 0x14030f460
003D3E86  E9 8E FE FF FF                  jmp 0x1403d3d19
003D3E8B  8B 05 27 2C BF 00               mov eax, dword ptr [rip + 0xbf2c27]
003D3E91  A8 40                           test al, 0x40
003D3E93  0F 84 B4 FE FF FF               je 0x1403d3d4d
003D3E99  E8 F2 B5 F3 FF                  call 0x14030f490
003D3E9E  84 C0                           test al, al
003D3EA0  0F 84 A7 FE FF FF               je 0x1403d3d4d
003D3EA6  8B CD                           mov ecx, ebp
003D3EA8  E8 B3 B5 F3 FF                  call 0x14030f460
003D3EAD  E9 9D FE FF FF                  jmp 0x1403d3d4f
003D3EB2  40 84 ED                        test bpl, bpl
003D3EB5  0F 84 1B FD FF FF               je 0x1403d3bd6
003D3EBB  48 8D 44 24 38                  lea rax, [rsp + 0x38]
003D3EC0  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
003D3EC5  41 B9 55 0F 00 00               mov r9d, 0xf55
003D3ECB  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
003D3ED0  BA 01 00 00 00                  mov edx, 1
003D3ED5  48 C7 44 24 58 08 00 00 00      mov qword ptr [rsp + 0x58], 8
003D3EDE  41 B8 00 00 02 40               mov r8d, 0x40020000
003D3EE4  C7 44 24 20 02 06 00 00         mov dword ptr [rsp + 0x20], 0x602
003D3EEC  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
003D3EF1  E8 5A 14 E6 FF                  call 0x140235350
003D3EF6  E9 DB FC FF FF                  jmp 0x1403d3bd6
003D3EFB  B8 7F FF FF 00                  mov eax, 0xffff7f
003D3F00  BA FF FF FF 00                  mov edx, 0xffffff
003D3F05  E9 AB FC FF FF                  jmp 0x1403d3bb5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiCancelTimer(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m50;
    unsigned __int8 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 10710190)) ^ (v_rsp);
    v_stack_m38 = result;
    *(unsigned __int64 *)(v_rsp + 16) = v_r12;
    *(unsigned __int64 *)(v_rsp + 24) = v_r13;
    v_rbp = 0;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    *(unsigned __int64 *)(v_rsp - 40) = v_r15;
    v_stack_m68 = a2;
    *(unsigned __int64 *)(v_rsp - 96) = 0;
loc_003D3ABC:
loc_003D3AC3:
    v_rbx = 0;
    if (condition_is_below) goto loc_003D3CB1;
loc_003D3AD0:
    if (((*(unsigned __int8 *)(a1 + 3)) & (192)) == 0) goto loc_003D3B8A;
    result = (*(unsigned __int16 *)(a1 + 58)) << (8);
    v_rbx = (*(unsigned __int8 *)(a1 + 2) + 16) + (result);
    v_stack_m50 = *(unsigned __int64 *)(v_rip - 4012739 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976);
    v_rbx = (v_rbx) << (5);
    v_rbx = (v_rbx) + (*(unsigned __int64 *)(v_rip - 4012739 + *(unsigned __int16 *)(a1 + 56) * 8 + 16550976) + 16640);
    v_rsi = 0;
loc_003D3B12:
    if (condition_is_above_or_equal) goto loc_003D3B34;
loc_003D3B1A:
    v_rsi = (unsigned int)((v_rsi) + 1);
    if (((*(unsigned int *)(v_rip + 12523402)) & ((unsigned int)(v_rsi))) == 0) goto loc_003D3D59;
loc_003D3B28:
loc_003D3B2A:
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_003D3B12;
    goto loc_003D3B1A;
loc_003D3B34:
    if (sign_flag) goto loc_003D3DA1;
    v_r15 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) ^ (1);
    v_r15 = (v_r15) << (8);
    v_r14 = ((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + 58)))) << (8);
    v_r15 = (v_r15) + (16);
    v_r14 = (v_r14) + (16);
    v_r15 = (v_r15) + ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 2))));
    v_r14 = (v_r14) + ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a1 + 2))));
    v_r15 = (v_r15) << (5);
    v_r14 = (v_r14) << (5);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 8)) != (a1 + 32)) goto loc_003D3B83;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8))) == (a1 + 32)) goto loc_003D3B9A;
loc_003D3B83:
loc_003D3B8A:
    if (v_stack_m68 == 0) goto loc_003D3BC6;
    goto loc_003D3BC6;
loc_003D3B9A:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32 + 8)) = 3;
    *(unsigned __int64 *)(3 + 8) = *(unsigned __int64 *)(a1 + 32 + 8);
    if ((*(unsigned __int64 *)(a1 + 32 + 8)) == 3) goto loc_003D3C0E;
loc_003D3BA6:
loc_003D3BB5:
    result = (unsigned int)(0xBFFFFF7FULL);
    if (v_stack_m68 == 0) { result = (unsigned int)((unsigned int)(0xBFFFFFFFULL)); }
loc_003D3BC6:
    if (((*(unsigned int *)(v_rip + 12529464)) & (0x20000ULL)) != 0) goto loc_003D3EB2;
loc_003D3BD6:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(a1 + 2));
    v_rsp = (v_rsp) + (120);
    return result;
loc_003D3C0E:
    *(unsigned int *)(v_stack_p20 + v_stack_p10 * 1 + 28) = 0xFFFFFFFFULL;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 58)) != 0) goto loc_003D3CDA;
    v_rsi = (v_stack_p18 + 272) << (5);
    v_rsi = (v_rsi) + (v_stack_p10);
    v_rbp = 0;
loc_003D3C31:
    if (condition_is_above_or_equal) goto loc_003D3C53;
loc_003D3C39:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 12523115)) & ((unsigned int)(v_rbp))) == 0) goto loc_003D3E16;
loc_003D3C47:
loc_003D3C49:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_003D3C31;
    goto loc_003D3C39;
loc_003D3C53:
    if ((*(unsigned int *)(v_stack_p20 + v_stack_p10 * 1 + 28)) != -1) goto loc_003D3CA7;
    if ((*(unsigned int *)(v_stack_m28 + v_stack_p10 * 1 + 28)) != -1) goto loc_003D3CA7;
    result = (*(unsigned __int8 *)(v_stack_p48 + 208)) + (*(unsigned __int8 *)(v_stack_p48 + 208));
    if ((*(unsigned int *)(v_rip + 12522415)) == 0) goto loc_003D3D80;
    v_r13 = (v_stack_p18) >> (6);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p18))) & (63));
loc_003D3CA7:
    goto loc_003D3BA6;
loc_003D3CB1:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 12522995)) & ((unsigned int)(v_rbx))) == 0) goto loc_003D3E3D;
loc_003D3CBF:
loc_003D3CC1:
    if (sign_flag) goto loc_003D3CB1;
    if (condition_is_below) goto loc_003D3CB1;
    goto loc_003D3AD0;
loc_003D3CDA:
    v_rsi = (v_r13 + 16) << (5);
    v_rsi = (v_rsi) + (v_stack_p10);
    if (condition_is_above_or_equal) goto loc_003D3CF1;
    goto loc_003D3CFA;
loc_003D3CF1:
    if (v_rsi != 0) goto loc_003D3C53;
loc_003D3CFA:
    v_rbx = 0;
loc_003D3D01:
    if (condition_is_above_or_equal) goto loc_003D3D23;
loc_003D3D09:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 12522907)) & ((unsigned int)(v_rbx))) == 0) goto loc_003D3E64;
loc_003D3D17:
loc_003D3D19:
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_003D3D01;
    goto loc_003D3D09;
loc_003D3D23:
    v_rbx = (v_r13 + 272) << (5);
    v_rbx = (v_rbx) + (v_stack_p10);
    v_rbp = 0;
loc_003D3D33:
    if (condition_is_above_or_equal) goto loc_003D3C53;
loc_003D3D3F:
    v_rbp = (unsigned int)((v_rbp) + 1);
    if (((*(unsigned int *)(v_rip + 12522853)) & ((unsigned int)(v_rbp))) == 0) goto loc_003D3E8B;
loc_003D3D4D:
loc_003D3D4F:
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_003D3D33;
    goto loc_003D3D3F;
loc_003D3D59:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528985)))) & (64)) == 0) goto loc_003D3B28;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(unsigned __int64 *)(v_rip - 4013167 + result * 8 + 16549160) + v_r13 * 8, (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), a4);
    if ((unsigned __int8)(result) == 0) goto loc_003D3B28;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rsi)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), a4);
    goto loc_003D3B2A;
loc_003D3D80:
    v_r13 = (v_r13) << (6);
    a1 = ((unsigned int)((unsigned int)(v_rsi))) + (v_r13);
    goto loc_003D3BA6;
loc_003D3DA1:
    a1 = 0;
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 3)) & (63));
    if (0 != 0) goto loc_003D3EFB;
    v_rbx = 0;
    if (!sign_flag) goto loc_003D3AC3;
loc_003D3DE0:
    v_rbx = (unsigned int)((v_rbx) + 1);
    if (((*(unsigned int *)(v_rip + 12522692)) & ((unsigned int)(v_rbx))) == 0) goto loc_003D3DFA;
loc_003D3DEA:
loc_003D3DEC:
    if (!sign_flag) goto loc_003D3ABC;
    goto loc_003D3DE0;
loc_003D3DFA:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528824)))) & (64)) == 0) goto loc_003D3DEA;
    result = KiCheckVpBackingLongSpinWaitHypercall(a1, (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    if ((unsigned __int8)(result) == 0) goto loc_003D3DEA;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    goto loc_003D3DEC;
loc_003D3E16:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528796)))) & (64)) == 0) goto loc_003D3C47;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    if ((unsigned __int8)(result) == 0) goto loc_003D3C47;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    goto loc_003D3C49;
loc_003D3E3D:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528757)))) & (64)) == 0) goto loc_003D3CBF;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    if ((unsigned __int8)(result) == 0) goto loc_003D3CBF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    goto loc_003D3CC1;
loc_003D3E64:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528718)))) & (64)) == 0) goto loc_003D3D17;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    if ((unsigned __int8)(result) == 0) goto loc_003D3D17;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    goto loc_003D3D19;
loc_003D3E8B:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12528679)))) & (64)) == 0) goto loc_003D3D4D;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    if ((unsigned __int8)(result) == 0) goto loc_003D3D4D;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), (unsigned int)(0xBFFFFFFFULL), *(unsigned __int16 *)(a1 + 58), *(unsigned __int8 *)(v_stack_p48 + 209));
    goto loc_003D3D4F;
loc_003D3EB2:
    if ((unsigned __int8)(v_rbp) == 0) goto loc_003D3BD6;
    v_stack_p38 = 0;
    v_stack_p50 = v_stack_p38;
    v_stack_p58 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p50, 1, (unsigned int)(0x40020000ULL), (unsigned int)(0xF55ULL));
    goto loc_003D3BD6;
loc_003D3EFB:
    goto loc_003D3BB5;
}
```

## 5. (Beta) C Style

```c
int64_t KiCancelTimer(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m50;
    uint8_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0xA36CAE)) ^ (local_rsp);
    v_stack_m38 = result;
    *(uint64_t *)(local_rsp + 0x10) = local_r12;
    *(uint64_t *)(local_rsp + 0x18) = local_r13;
    local_rbp = 0;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    *(uint64_t *)(local_rsp - 0x28) = local_r15;
    v_stack_m68 = Arg2;
    *(uint64_t *)(local_rsp - 0x60) = 0;
loc_003D3ABC:
loc_003D3AC3:
    local_rbx = 0;
    if (condition_is_below) goto loc_003D3CB1;
loc_003D3AD0:
    if (((*(uint8_t *)(arg1 + 0x3)) & (192)) == 0) goto loc_003D3B8A;
    result = (*(uint16_t *)(arg1 + 0x3A)) << (8);
    local_rbx = (*(uint8_t *)(arg1 + 0x2) + 16) + (result);
    v_stack_m50 = *(uint64_t *)(v_rip - 0x3D3AC3 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40);
    local_rbx = (local_rbx) << (5);
    local_rbx = (local_rbx) + (*(uint64_t *)(v_rip - 0x3D3AC3 + *(uint16_t *)(arg1 + 0x38) * 8 + 0xFC8C40) + 16640);
    local_rsi = 0;
loc_003D3B12:
    if (condition_is_above_or_equal) goto loc_003D3B34;
loc_003D3B1A:
    local_rsi = (uint32_t)((local_rsi) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF178A)) & ((uint32_t)(local_rsi))) == 0) goto loc_003D3D59;
loc_003D3B28:
loc_003D3B2A:
    if (*(uint64_t *)(local_rbx) == 0) goto loc_003D3B12;
    goto loc_003D3B1A;
loc_003D3B34:
    if (sign_flag) goto loc_003D3DA1;
    local_r15 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) ^ (1);
    local_r15 = (local_r15) << (8);
    local_r14 = ((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + 0x3A)))) << (8);
    local_r15 = (local_r15) + (16);
    local_r14 = (local_r14) + (16);
    local_r15 = (local_r15) + ((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x2))));
    local_r14 = (local_r14) + ((uint32_t)((uint32_t)(*(uint8_t *)(arg1 + 0x2))));
    local_r15 = (local_r15) << (5);
    local_r14 = (local_r14) << (5);
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x8)) != (Arg1 + 32)) goto loc_003D3B83;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8))) == (Arg1 + 32)) goto loc_003D3B9A;
loc_003D3B83:
loc_003D3B8A:
    if (v_stack_m68 == 0) goto loc_003D3BC6;
    goto loc_003D3BC6;
loc_003D3B9A:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x20 + 0x8)) = 3;
    *(uint64_t *)(3 + 0x8) = *(uint64_t *)(arg1 + 0x20 + 0x8);
    if ((*(uint64_t *)(arg1 + 0x20 + 0x8)) == 3) goto loc_003D3C0E;
loc_003D3BA6:
loc_003D3BB5:
    result = (uint32_t)(0xBFFFFF7FULL);
    if (v_stack_m68 == 0) { result = (uint32_t)((uint32_t)(0xBFFFFFFFULL)); }
loc_003D3BC6:
    if (((*(uint32_t *)(v_rip + 0xBF2F38)) & (0x20000ULL)) != 0) goto loc_003D3EB2;
loc_003D3BD6:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(arg1 + 0x2));
    local_rsp = (local_rsp) + (120);
    return result;
loc_003D3C0E:
    *(uint32_t *)(v_stack_p20 + v_stack_p10 * 1 + 0x1C) = 0xFFFFFFFFULL;
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x3A)) != 0) goto loc_003D3CDA;
    local_rsi = (v_stack_p18 + 272) << (5);
    local_rsi = (local_rsi) + (v_stack_p10);
    local_rbp = 0;
loc_003D3C31:
    if (condition_is_above_or_equal) goto loc_003D3C53;
loc_003D3C39:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF166B)) & ((uint32_t)(local_rbp))) == 0) goto loc_003D3E16;
loc_003D3C47:
loc_003D3C49:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_003D3C31;
    goto loc_003D3C39;
loc_003D3C53:
    if ((*(uint32_t *)(v_stack_p20 + v_stack_p10 * 1 + 0x1C)) != -1) goto loc_003D3CA7;
    if ((*(uint32_t *)(v_stack_m28 + v_stack_p10 * 1 + 0x1C)) != -1) goto loc_003D3CA7;
    result = (*(uint8_t *)(v_stack_p48 + 0xD0)) + (*(uint8_t *)(v_stack_p48 + 0xD0));
    if ((*(uint32_t *)(v_rip + 0xBF13AF)) == 0) goto loc_003D3D80;
    local_r13 = (v_stack_p18) >> (6);
    a4 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p18))) & (63));
loc_003D3CA7:
    goto loc_003D3BA6;
loc_003D3CB1:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF15F3)) & ((uint32_t)(local_rbx))) == 0) goto loc_003D3E3D;
loc_003D3CBF:
loc_003D3CC1:
    if (sign_flag) goto loc_003D3CB1;
    if (condition_is_below) goto loc_003D3CB1;
    goto loc_003D3AD0;
loc_003D3CDA:
    local_rsi = (local_r13 + 16) << (5);
    local_rsi = (local_rsi) + (v_stack_p10);
    if (condition_is_above_or_equal) goto loc_003D3CF1;
    goto loc_003D3CFA;
loc_003D3CF1:
    if (local_rsi != 0) goto loc_003D3C53;
loc_003D3CFA:
    local_rbx = 0;
loc_003D3D01:
    if (condition_is_above_or_equal) goto loc_003D3D23;
loc_003D3D09:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF159B)) & ((uint32_t)(local_rbx))) == 0) goto loc_003D3E64;
loc_003D3D17:
loc_003D3D19:
    if (*(uint64_t *)(local_rsi) == 0) goto loc_003D3D01;
    goto loc_003D3D09;
loc_003D3D23:
    local_rbx = (local_r13 + 272) << (5);
    local_rbx = (local_rbx) + (v_stack_p10);
    local_rbp = 0;
loc_003D3D33:
    if (condition_is_above_or_equal) goto loc_003D3C53;
loc_003D3D3F:
    local_rbp = (uint32_t)((local_rbp) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF1565)) & ((uint32_t)(local_rbp))) == 0) goto loc_003D3E8B;
loc_003D3D4D:
loc_003D3D4F:
    if (*(uint64_t *)(local_rbx) == 0) goto loc_003D3D33;
    goto loc_003D3D3F;
loc_003D3D59:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2D59)))) & (64)) == 0) goto loc_003D3B28;
    result = KiCheckVpBackingLongSpinWaitHypercall(*(uint64_t *)(v_rip - 0x3D3C6F + result * 8 + 0xFC8528) + local_r13 * 8, (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), a4);
    if ((uint8_t)(result) == 0) goto loc_003D3B28;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rsi)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), a4);
    goto loc_003D3B2A;
loc_003D3D80:
    local_r13 = (local_r13) << (6);
    Arg1 = ((uint32_t)((uint32_t)(local_rsi))) + (local_r13);
    goto loc_003D3BA6;
loc_003D3DA1:
    Arg1 = 0;
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x3)) & (63));
    if (0 != 0) goto loc_003D3EFB;
    local_rbx = 0;
    if (!sign_flag) goto loc_003D3AC3;
loc_003D3DE0:
    local_rbx = (uint32_t)((local_rbx) + 1);
    if (((*(uint32_t *)(v_rip + 0xBF14C4)) & ((uint32_t)(local_rbx))) == 0) goto loc_003D3DFA;
loc_003D3DEA:
loc_003D3DEC:
    if (!sign_flag) goto loc_003D3ABC;
    goto loc_003D3DE0;
loc_003D3DFA:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2CB8)))) & (64)) == 0) goto loc_003D3DEA;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg1, (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    if ((uint8_t)(result) == 0) goto loc_003D3DEA;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    goto loc_003D3DEC;
loc_003D3E16:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2C9C)))) & (64)) == 0) goto loc_003D3C47;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    if ((uint8_t)(result) == 0) goto loc_003D3C47;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    goto loc_003D3C49;
loc_003D3E3D:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2C75)))) & (64)) == 0) goto loc_003D3CBF;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    if ((uint8_t)(result) == 0) goto loc_003D3CBF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    goto loc_003D3CC1;
loc_003D3E64:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2C4E)))) & (64)) == 0) goto loc_003D3D17;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    if ((uint8_t)(result) == 0) goto loc_003D3D17;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    goto loc_003D3D19;
loc_003D3E8B:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBF2C27)))) & (64)) == 0) goto loc_003D3D4D;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    if ((uint8_t)(result) == 0) goto loc_003D3D4D;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), (uint32_t)(0xBFFFFFFFULL), *(uint16_t *)(arg1 + 0x3A), *(uint8_t *)(v_stack_p48 + 0xD1));
    goto loc_003D3D4F;
loc_003D3EB2:
    if ((uint8_t)(local_rbp) == 0) goto loc_003D3BD6;
    v_stack_p38 = 0;
    v_stack_p50 = v_stack_p38;
    v_stack_p58 = 8;
    v_stack_p20 = 0x602ULL;
    result = EtwTraceKernelEvent(v_stack_p50, 1, (uint32_t)(0x40020000ULL), (uint32_t)(0xF55ULL));
    goto loc_003D3BD6;
loc_003D3EFB:
    goto loc_003D3BB5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x2` | `8` | `R` |
| `Arg1` | `+ 0x3` | `8` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x38` | `16` | `R` |
| `Arg1` | `+ 0x3A` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D3A80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
