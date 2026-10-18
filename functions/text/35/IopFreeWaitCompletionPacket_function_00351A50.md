# IopFreeWaitCompletionPacket

- RVA: `0x00351A50`–`0x00351EE2` (길이 `1,170` bytes)
- VA: `0x0000000140351A50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078EA0`
- 디코드: `270`개 명령, `1,170/1,170` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **29**; 고유 호출 대상: **12**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00351AB2` → [KiAcquireSpinLockInstrumented](../20/KiAcquireSpinLockInstrumented_function_002084F0.md) (function, `0x002084F0`)
- `0x00351AE7` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x00351B0D` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00351B4C` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00351B7D` → [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x00351BC3` → [KxWaitForSpinLockAndAcquire](../20/KxWaitForSpinLockAndAcquire_function_002085C0.md) (function, `0x002085C0`)
- `0x00351BF3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351C1F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351C4B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351C59` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00351CA0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351CDD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351D19` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00351D36` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00351D64` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x00351D6F` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00351D95` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x00351DB3` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00351DE2` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x00351DED` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00351E13` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x00351E31` → [KeAreInterruptsEnabled](../2F/KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)
- `0x00351E5F` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (function, `0x009D7F78`)
- `0x00351E6A` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (function, `0x00864A60`)
- `0x00351E90` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (function, `0x009D7E30`)
- `0x00351EAE` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)
- `0x00351EBC` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00351ECA` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)
- `0x00351ED8` → [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) (function, `0x003A2394`)

### Direct callers
- [IopDeleteIoCompletionInternal](IopDeleteIoCompletionInternal_function_00351438.md) at `0x003514F4`

### Static image references
- `0x00351A86` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x00351A93` → RVA `0x00FC6B06` (`ALMOSTRO`; read)
- `0x00351AA0` → RVA `0x00F0DE58` (`.data`; read)
- `0x00351AF4` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x00351B22` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00351C8E` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x00351D64` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x00351D6F` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00351D95` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x00351DE2` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x00351DED` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00351E13` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
  - `0x00351E5F` → [ObpDeregisterObject](../../page/9D/ObpDeregisterObject_function_009D7F78.md) (`.text` → `PAGE`)
  - `0x00351E6A` → [ObpRemoveObjectRoutine](../../page/86/ObpRemoveObjectRoutine_function_00864A60.md) (`.text` → `PAGE`)
  - `0x00351E90` → [ObpHandleRevocationBlockRemoveObject](../../page/9D/ObpHandleRevocationBlockRemoveObject_function_009D7E30.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00351A50  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00351A55  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00351A5A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00351A5F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00351A64  41 54                           push r12
00351A66  41 56                           push r14
00351A68  41 57                           push r15
00351A6A  48 83 EC 30                     sub rsp, 0x30
00351A6E  48 8B 69 50                     mov rbp, qword ptr [rcx + 0x50]
00351A72  4C 8B F2                        mov r14, rdx
00351A75  48 8B F1                        mov rsi, rcx
00351A78  44 0F 20 C7                     mov rdi, cr8
00351A7C  41 BC 02 00 00 00               mov r12d, 2
00351A82  45 0F 22 C4                     mov cr8, r12
00351A86  83 3D 93 52 C7 00 00            cmp dword ptr [rip + 0xc75293], 0
00351A8D  0F 85 BE 01 00 00               jne 0x140351c51
00351A93  F6 05 6C 50 C7 00 21            test byte ptr [rip + 0xc7506c], 0x21
00351A9A  0F 84 12 01 00 00               je 0x140351bb2
00351AA0  8B 05 B2 C3 BB 00               mov eax, dword ptr [rip + 0xbbc3b2]
00351AA6  85 C0                           test eax, eax
00351AA8  0F 85 04 01 00 00               jne 0x140351bb2
00351AAE  48 8D 4E 60                     lea rcx, [rsi + 0x60]
00351AB2  E8 39 6A EB FF                  call 0x1402084f0
00351AB7  C6 46 68 00                     mov byte ptr [rsi + 0x68], 0
00351ABB  48 C7 46 58 00 00 00 00         mov qword ptr [rsi + 0x58], 0
00351AC3  F6 05 3C 50 C7 00 01            test byte ptr [rip + 0xc7503c], 1
00351ACA  0F 85 C7 03 00 00               jne 0x140351e97
00351AD0  F0 48 83 66 60 00               lock and qword ptr [rsi + 0x60], 0
00351AD6  83 3D 43 52 C7 00 00            cmp dword ptr [rip + 0xc75243], 0
00351ADD  74 0D                           je 0x140351aec
00351ADF  44 0F 20 C1                     mov rcx, cr8
00351AE3  40 0F B6 D7                     movzx edx, dil
00351AE7  E8 AC 3B 1A 00                  call 0x1404f5698
00351AEC  40 0F B6 C7                     movzx eax, dil
00351AF0  44 0F 22 C0                     mov cr8, rax
00351AF4  83 3D 15 35 C7 00 00            cmp dword ptr [rip + 0xc73515], 0
00351AFB  74 15                           je 0x140351b12
00351AFD  33 D2                           xor edx, edx
00351AFF  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00351B03  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00351B09  44 8D 42 01                     lea r8d, [rdx + 1]
00351B0D  E8 D2 EE EB FF                  call 0x1402109e4
00351B12  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
00351B19  48 8B C3                        mov rax, rbx
00351B1C  F0 48 0F C1 45 D0               lock xadd qword ptr [rbp - 0x30], rax
00351B22  4C 8D 3D D7 E4 CA FF            lea r15, [rip - 0x351b29]
00351B29  48 83 E8 01                     sub rax, 1
00351B2D  0F 8E 9A 00 00 00               jle 0x140351bcd
00351B33  83 3D D6 34 C7 00 00            cmp dword ptr [rip + 0xc734d6], 0
00351B3A  74 15                           je 0x140351b51
00351B3C  33 D2                           xor edx, edx
00351B3E  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00351B42  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00351B48  44 8D 42 01                     lea r8d, [rdx + 1]
00351B4C  E8 93 EE EB FF                  call 0x1402109e4
00351B51  48 8B C3                        mov rax, rbx
00351B54  F0 49 0F C1 46 D0               lock xadd qword ptr [r14 - 0x30], rax
00351B5A  48 83 E8 01                     sub rax, 1
00351B5E  0F 8E 95 00 00 00               jle 0x140351bf9
00351B64  83 3D A5 34 C7 00 00            cmp dword ptr [rip + 0xc734a5], 0
00351B6B  74 15                           je 0x140351b82
00351B6D  33 D2                           xor edx, edx
00351B6F  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00351B73  41 B9 44 66 6C 74               mov r9d, 0x746c6644
00351B79  44 8D 42 01                     lea r8d, [rdx + 1]
00351B7D  E8 62 EE EB FF                  call 0x1402109e4
00351B82  F0 48 0F C1 5E D0               lock xadd qword ptr [rsi - 0x30], rbx
00351B88  48 83 EB 01                     sub rbx, 1
00351B8C  0F 8E 93 00 00 00               jle 0x140351c25
00351B92  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00351B97  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00351B9C  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00351BA1  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00351BA6  48 83 C4 30                     add rsp, 0x30
00351BAA  41 5F                           pop r15
00351BAC  41 5E                           pop r14
00351BAE  41 5C                           pop r12
00351BB0  C3                              ret
00351BB1  CC                              int3
00351BB2  F0 48 0F BA 6E 60 00            lock bts qword ptr [rsi + 0x60], 0
00351BB9  0F 83 F8 FE FF FF               jae 0x140351ab7
00351BBF  48 8D 4E 60                     lea rcx, [rsi + 0x60]
00351BC3  E8 F8 69 EB FF                  call 0x1402085c0
00351BC8  E9 EA FE FF FF                  jmp 0x140351ab7
00351BCD  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00351BD1  48 85 C9                        test rcx, rcx
00351BD4  0F 85 89 00 00 00               jne 0x140351c63
00351BDA  48 85 C0                        test rax, rax
00351BDD  0F 89 3C 01 00 00               jns 0x140351d1f
00351BE3  33 D2                           xor edx, edx
00351BE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00351BEA  4D 8B CC                        mov r9, r12
00351BED  4C 8B C5                        mov r8, rbp
00351BF0  8D 4A 18                        lea ecx, [rdx + 0x18]
00351BF3  E8 68 BA 1A 00                  call 0x1404fd660
00351BF8  CC                              int3
00351BF9  49 8B 4E D8                     mov rcx, qword ptr [r14 - 0x28]
00351BFD  48 85 C9                        test rcx, rcx
00351C00  0F 85 A0 00 00 00               jne 0x140351ca6
00351C06  48 85 C0                        test rax, rax
00351C09  0F 89 8D 01 00 00               jns 0x140351d9c
00351C0F  33 D2                           xor edx, edx
00351C11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00351C16  4D 8B CC                        mov r9, r12
00351C19  4D 8B C6                        mov r8, r14
00351C1C  8D 4A 18                        lea ecx, [rdx + 0x18]
00351C1F  E8 3C BA 1A 00                  call 0x1404fd660
00351C24  CC                              int3
00351C25  48 8B 4E D8                     mov rcx, qword ptr [rsi - 0x28]
00351C29  48 85 C9                        test rcx, rcx
00351C2C  0F 85 B1 00 00 00               jne 0x140351ce3
00351C32  48 85 DB                        test rbx, rbx
00351C35  0F 89 DF 01 00 00               jns 0x140351e1a
00351C3B  33 D2                           xor edx, edx
00351C3D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00351C42  4D 8B CC                        mov r9, r12
00351C45  4C 8B C6                        mov r8, rsi
00351C48  8D 4A 18                        lea ecx, [rdx + 0x18]
00351C4B  E8 10 BA 1A 00                  call 0x1404fd660
00351C50  CC                              int3
00351C51  41 0F B6 D4                     movzx edx, r12b
00351C55  40 0F B6 CF                     movzx ecx, dil
00351C59  E8 9E 3A 1A 00                  call 0x1404f56fc
00351C5E  E9 30 FE FF FF                  jmp 0x140351a93
00351C63  41 B9 01 00 00 00               mov r9d, 1
00351C69  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00351C6E  48 8D 45 D0                     lea rax, [rbp - 0x30]
00351C72  4C 8B C5                        mov r8, rbp
00351C75  48 C1 E8 08                     shr rax, 8
00351C79  4C 8D 3D 80 E3 CA FF            lea r15, [rip - 0x351c80]
00351C80  0F B6 D0                        movzx edx, al
00351C83  0F B6 45 E8                     movzx eax, byte ptr [rbp - 0x18]
00351C87  41 8D 49 17                     lea ecx, [r9 + 0x17]
00351C8B  48 33 D0                        xor rdx, rax
00351C8E  0F B6 05 B7 51 C7 00            movzx eax, byte ptr [rip + 0xc751b7]
00351C95  48 33 D0                        xor rdx, rax
00351C98  49 8B 94 D7 00 78 FC 00         mov rdx, qword ptr [r15 + rdx*8 + 0xfc7800]
00351CA0  E8 BB B9 1A 00                  call 0x1404fd660
00351CA5  CC                              int3
00351CA6  41 B9 01 00 00 00               mov r9d, 1
00351CAC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00351CB1  49 8D 46 D0                     lea rax, [r14 - 0x30]
00351CB5  4D 8B C6                        mov r8, r14
00351CB8  48 C1 E8 08                     shr rax, 8
00351CBC  0F B6 D0                        movzx edx, al
00351CBF  41 0F B6 46 E8                  movzx eax, byte ptr [r14 - 0x18]
00351CC4  41 8D 49 17                     lea ecx, [r9 + 0x17]
00351CC8  48 33 D0                        xor rdx, rax
00351CCB  0F B6 05 7A 51 C7 00            movzx eax, byte ptr [rip + 0xc7517a]
00351CD2  48 33 D0                        xor rdx, rax
00351CD5  49 8B 94 D7 00 78 FC 00         mov rdx, qword ptr [r15 + rdx*8 + 0xfc7800]
00351CDD  E8 7E B9 1A 00                  call 0x1404fd660
00351CE2  CC                              int3
00351CE3  41 B9 01 00 00 00               mov r9d, 1
00351CE9  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00351CEE  48 8D 46 D0                     lea rax, [rsi - 0x30]
00351CF2  4C 8B C6                        mov r8, rsi
00351CF5  48 C1 E8 08                     shr rax, 8
00351CF9  0F B6 D0                        movzx edx, al
00351CFC  0F B6 46 E8                     movzx eax, byte ptr [rsi - 0x18]
00351D00  41 8D 49 17                     lea ecx, [r9 + 0x17]
00351D04  48 33 D0                        xor rdx, rax
00351D07  0F B6 05 3E 51 C7 00            movzx eax, byte ptr [rip + 0xc7513e]
00351D0E  48 33 D0                        xor rdx, rax
00351D11  49 8B 94 D7 00 78 FC 00         mov rdx, qword ptr [r15 + rdx*8 + 0xfc7800]
00351D19  E8 42 B9 1A 00                  call 0x1404fd660
00351D1E  CC                              int3
00351D1F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00351D28  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
00351D30  0F 85 82 01 00 00               jne 0x140351eb8
00351D36  E8 25 63 FA FF                  call 0x1402f8060
00351D3B  84 C0                           test al, al
00351D3D  0F 84 75 01 00 00               je 0x140351eb8
00351D43  44 0F 20 C0                     mov rax, cr8
00351D47  3C 01                           cmp al, 1
00351D49  0F 83 69 01 00 00               jae 0x140351eb8
00351D4F  0F B6 45 EA                     movzx eax, byte ptr [rbp - 0x16]
00351D53  A8 40                           test al, 0x40
00351D55  75 22                           jne 0x140351d79
00351D57  83 3D B2 32 C7 00 00            cmp dword ptr [rip + 0xc732b2], 0
00351D5E  74 09                           je 0x140351d69
00351D60  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00351D64  E8 0F 62 68 00                  call 0x1409d7f78
00351D69  33 D2                           xor edx, edx
00351D6B  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00351D6F  E8 EC 2C 51 00                  call 0x140864a60
00351D74  E9 BA FD FF FF                  jmp 0x140351b33
00351D79  83 E0 7F                        and eax, 0x7f
00351D7C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00351D80  42 0F B6 84 38 80 FF F0 00      movzx eax, byte ptr [rax + r15 + 0xf0ff80]
00351D89  48 2B C8                        sub rcx, rax
00351D8C  48 8B 09                        mov rcx, qword ptr [rcx]
00351D8F  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
00351D93  74 C2                           je 0x140351d57
00351D95  E8 96 60 68 00                  call 0x1409d7e30
00351D9A  EB BB                           jmp 0x140351d57
00351D9C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00351DA5  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
00351DAD  0F 85 13 01 00 00               jne 0x140351ec6
00351DB3  E8 A8 62 FA FF                  call 0x1402f8060
00351DB8  84 C0                           test al, al
00351DBA  0F 84 06 01 00 00               je 0x140351ec6
00351DC0  44 0F 20 C0                     mov rax, cr8
00351DC4  3C 01                           cmp al, 1
00351DC6  0F 83 FA 00 00 00               jae 0x140351ec6
00351DCC  41 0F B6 46 EA                  movzx eax, byte ptr [r14 - 0x16]
00351DD1  A8 40                           test al, 0x40
00351DD3  75 22                           jne 0x140351df7
00351DD5  83 3D 34 32 C7 00 00            cmp dword ptr [rip + 0xc73234], 0
00351DDC  74 09                           je 0x140351de7
00351DDE  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00351DE2  E8 91 61 68 00                  call 0x1409d7f78
00351DE7  33 D2                           xor edx, edx
00351DE9  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00351DED  E8 6E 2C 51 00                  call 0x140864a60
00351DF2  E9 6D FD FF FF                  jmp 0x140351b64
00351DF7  83 E0 7F                        and eax, 0x7f
00351DFA  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00351DFE  42 0F B6 84 38 80 FF F0 00      movzx eax, byte ptr [rax + r15 + 0xf0ff80]
00351E07  48 2B C8                        sub rcx, rax
00351E0A  48 8B 09                        mov rcx, qword ptr [rcx]
00351E0D  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
00351E11  74 C2                           je 0x140351dd5
00351E13  E8 18 60 68 00                  call 0x1409d7e30
00351E18  EB BB                           jmp 0x140351dd5
00351E1A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00351E23  66 83 B8 E6 01 00 00 00         cmp word ptr [rax + 0x1e6], 0
00351E2B  0F 85 A3 00 00 00               jne 0x140351ed4
00351E31  E8 2A 62 FA FF                  call 0x1402f8060
00351E36  84 C0                           test al, al
00351E38  0F 84 96 00 00 00               je 0x140351ed4
00351E3E  44 0F 20 C0                     mov rax, cr8
00351E42  3C 01                           cmp al, 1
00351E44  0F 83 8A 00 00 00               jae 0x140351ed4
00351E4A  0F B6 46 EA                     movzx eax, byte ptr [rsi - 0x16]
00351E4E  A8 40                           test al, 0x40
00351E50  75 22                           jne 0x140351e74
00351E52  83 3D B7 31 C7 00 00            cmp dword ptr [rip + 0xc731b7], 0
00351E59  74 09                           je 0x140351e64
00351E5B  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00351E5F  E8 14 61 68 00                  call 0x1409d7f78
00351E64  33 D2                           xor edx, edx
00351E66  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00351E6A  E8 F1 2B 51 00                  call 0x140864a60
00351E6F  E9 1E FD FF FF                  jmp 0x140351b92
00351E74  83 E0 7F                        and eax, 0x7f
00351E77  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00351E7B  42 0F B6 84 38 80 FF F0 00      movzx eax, byte ptr [rax + r15 + 0xf0ff80]
00351E84  48 2B C8                        sub rcx, rax
00351E87  48 8B 09                        mov rcx, qword ptr [rcx]
00351E8A  80 79 18 00                     cmp byte ptr [rcx + 0x18], 0
00351E8E  74 C2                           je 0x140351e52
00351E90  E8 9B 5F 68 00                  call 0x1409d7e30
00351E95  EB BB                           jmp 0x140351e52
00351E97  8B 05 BB BF BB 00               mov eax, dword ptr [rip + 0xbbbfbb]
00351E9D  85 C0                           test eax, eax
00351E9F  0F 85 2B FC FF FF               jne 0x140351ad0
00351EA5  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
00351EAA  48 8D 4E 60                     lea rcx, [rsi + 0x60]
00351EAE  E8 3D 10 04 00                  call 0x140392ef0
00351EB3  E9 1E FC FF FF                  jmp 0x140351ad6
00351EB8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00351EBC  E8 D3 04 05 00                  call 0x1403a2394
00351EC1  E9 6D FC FF FF                  jmp 0x140351b33
00351EC6  49 8D 4E D0                     lea rcx, [r14 - 0x30]
00351ECA  E8 C5 04 05 00                  call 0x1403a2394
00351ECF  E9 90 FC FF FF                  jmp 0x140351b64
00351ED4  48 8D 4E D0                     lea rcx, [rsi - 0x30]
00351ED8  E8 B7 04 05 00                  call 0x1403a2394
00351EDD  E9 B0 FC FF FF                  jmp 0x140351b92
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopFreeWaitCompletionPacket(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (48);
    if ((*(unsigned int *)(v_rip + 13062803)) != 0) goto loc_00351C51;
loc_00351A93:
    if (((*(unsigned __int8 *)(v_rip + 13062252)) & (33)) == 0) goto loc_00351BB2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12305330))) != 0) goto loc_00351BB2;
    result = KiAcquireSpinLockInstrumented(a1 + 96, a2, a3, a4);
loc_00351AB7:
    *(unsigned __int8 *)(a1 + 104) = 0;
    *(unsigned __int64 *)(a1 + 88) = 0;
    if (((*(unsigned __int8 *)(v_rip + 13062204)) & (1)) != 0) goto loc_00351E97;
loc_00351AD0:
loc_00351AD6:
    if ((*(unsigned int *)(v_rip + 13062723)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    result = (unsigned __int8)(v_cr8);
    if ((*(unsigned int *)(v_rip + 13055253)) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 80) - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351BCD;
loc_00351B33:
    if ((*(unsigned int *)(v_rip + 13055190)) != 0) {
        a2 = 0;
        a1 = a2 - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351BF9;
loc_00351B64:
    if ((*(unsigned int *)(v_rip + 13055141)) != 0) {
        a2 = 0;
        a1 = a1 - 48;
        a4 = 0x746C6644ULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    v_rbx = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351C25;
loc_00351B92:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00351BB2:
    if (condition_is_above_or_equal) goto loc_00351AB7;
    result = KxWaitForSpinLockAndAcquire(v_stack_p18 + 96, a2, a3, a4);
    goto loc_00351AB7;
loc_00351BCD:
    if (*(unsigned __int64 *)(v_stack_p10 - 40) != 0) goto loc_00351C63;
    if (!sign_flag) goto loc_00351D1F;
    a2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p10, 2);
loc_00351BF9:
    if (*(unsigned __int64 *)(a2 - 40) != 0) goto loc_00351CA6;
    if (!sign_flag) goto loc_00351D9C;
    a2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, 0, 2);
loc_00351C25:
    if (*(unsigned __int64 *)(v_stack_p18 - 40) != 0) goto loc_00351CE3;
    if (!sign_flag) goto loc_00351E1A;
    a2 = 0;
    v_stack_p20 = v_stack_p8;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p18, 2);
loc_00351C51:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p20), 2, v_stack_p18, 2);
    goto loc_00351A93;
loc_00351C63:
    v_stack_p20 = (unsigned __int8)(v_stack_p20);
    result = (v_stack_p10 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p10 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13062583));
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3480704 + a2 * 8 + 16545792), v_stack_p10, 1);
loc_00351CA6:
    v_stack_p20 = 1 + 23;
    result = (a2 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13062522));
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3480704 + a2 * 8 + 16545792), a2, 1);
loc_00351CE3:
    v_stack_p20 = 1 + 23;
    result = (v_stack_p18 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_p18 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 13062462));
    result = KeBugCheckEx(1 + 23, *(unsigned __int64 *)(v_rip - 3480704 + a2 * 8 + 16545792), v_stack_p18, 1);
loc_00351D1F:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_00351EB8;
    result = KeAreInterruptsEnabled(1 + 23, *(unsigned __int64 *)(v_rip - 3480704 + a2 * 8 + 16545792), v_stack_p18, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00351EB8;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 1) goto loc_00351EB8;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p10 - 22))) & (64)) != 0) goto loc_00351D79;
loc_00351D57:
    result = *(unsigned __int8 *)(v_stack_p10 - 22);
    if ((*(unsigned int *)(v_rip + 13054642)) != 0) {
        a1 = v_stack_p10 - 48;
        result = ObpDeregisterObject(a1, *(unsigned __int64 *)(v_rip - 3480704 + a2 * 8 + 16545792), v_stack_p18, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p10 - 48, a2, v_stack_p18, 1);
    goto loc_00351B33;
loc_00351D79:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p10 - 48) - (*(unsigned __int8 *)(result + v_rip - 3480704 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00351D57;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p18, 1);
    goto loc_00351D57;
loc_00351D9C:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_00351EC6;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(a1), a2, v_stack_p18, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00351EC6;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 1) goto loc_00351EC6;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 - 22))) & (64)) != 0) goto loc_00351DF7;
loc_00351DD5:
    result = *(unsigned __int8 *)(a2 - 22);
    if ((*(unsigned int *)(v_rip + 13054516)) != 0) {
        a1 = a2 - 48;
        result = ObpDeregisterObject(a1, a2, v_stack_p18, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(a2 - 48, a2, v_stack_p18, 1);
    goto loc_00351B64;
loc_00351DF7:
    result = (unsigned int)((result) & (127));
    a1 = (a2 - 48) - (*(unsigned __int8 *)(result + v_rip - 3480704 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00351DD5;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p18, 1);
    goto loc_00351DD5;
loc_00351E1A:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 486)) != 0) goto loc_00351ED4;
    result = KeAreInterruptsEnabled(*(unsigned __int64 *)(a1), a2, v_stack_p18, 1);
    if ((unsigned __int8)(result) == 0) goto loc_00351ED4;
    if (((unsigned __int8)((unsigned __int8)(v_cr8))) >= 1) goto loc_00351ED4;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_p18 - 22))) & (64)) != 0) goto loc_00351E74;
loc_00351E52:
    result = *(unsigned __int8 *)(v_stack_p18 - 22);
    if ((*(unsigned int *)(v_rip + 13054391)) != 0) {
        a1 = v_stack_p18 - 48;
        result = ObpDeregisterObject(a1, a2, v_stack_p18, 1);
    }
    a2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p18 - 48, a2, v_stack_p18, 1);
    goto loc_00351B92;
loc_00351E74:
    result = (unsigned int)((result) & (127));
    a1 = (v_stack_p18 - 48) - (*(unsigned __int8 *)(result + v_rip - 3480704 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_00351E52;
    result = ObpHandleRevocationBlockRemoveObject(*(unsigned __int64 *)(a1), a2, v_stack_p18, 1);
    goto loc_00351E52;
loc_00351E97:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12304315))) != 0) goto loc_00351AD0;
    result = KiReleaseSpinLockInstrumented(v_stack_p18 + 96, v_stack_p48, v_stack_p18, 1);
    goto loc_00351AD6;
loc_00351EB8:
    result = ObpDeferObjectDeletion(v_stack_p10 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B33;
loc_00351EC6:
    result = ObpDeferObjectDeletion(a2 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B64;
loc_00351ED4:
    result = ObpDeferObjectDeletion(v_stack_p18 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B92;
}
```

## 5. (Beta) C Style

```c
int64_t IopFreeWaitCompletionPacket(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (48);
    if ((*(uint32_t *)(v_rip + 0xC75293)) != 0) goto loc_00351C51;
loc_00351A93:
    if (((*(uint8_t *)(v_rip + 0xC7506C)) & (33)) == 0) goto loc_00351BB2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBBC3B2))) != 0) goto loc_00351BB2;
    result = KiAcquireSpinLockInstrumented(Arg1 + 96, Arg2, a3, a4);
loc_00351AB7:
    *(uint8_t *)(arg1 + 0x68) = 0;
    *(uint64_t *)(arg1 + 0x58) = 0;
    if (((*(uint8_t *)(v_rip + 0xC7503C)) & (1)) != 0) goto loc_00351E97;
loc_00351AD0:
loc_00351AD6:
    if ((*(uint32_t *)(v_rip + 0xC75243)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, a3, a4);
    }
    result = (uint8_t)(v_cr8);
    if ((*(uint32_t *)(v_rip + 0xC73515)) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x50) - 48;
        a4 = 0x746C6644ULL;
        a3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351BCD;
loc_00351B33:
    if ((*(uint32_t *)(v_rip + 0xC734D6)) != 0) {
        Arg2 = 0;
        Arg1 = Arg2 - 48;
        a4 = 0x746C6644ULL;
        a3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, a3, a4);
    }
    result = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351BF9;
loc_00351B64:
    if ((*(uint32_t *)(v_rip + 0xC734A5)) != 0) {
        Arg2 = 0;
        Arg1 = Arg1 - 48;
        a4 = 0x746C6644ULL;
        a3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, a3, a4);
    }
    local_rbx = (-1) - (1);
    if (condition_is_less_or_equal) goto loc_00351C25;
loc_00351B92:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00351BB2:
    if (condition_is_above_or_equal) goto loc_00351AB7;
    result = KxWaitForSpinLockAndAcquire(v_stack_p18 + 96, Arg2, a3, a4);
    goto loc_00351AB7;
loc_00351BCD:
    if (*(uint64_t *)(v_stack_p10 - 0x28) != 0) goto loc_00351C63;
    if (!sign_flag) goto loc_00351D1F;
    Arg2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p10, 2);
loc_00351BF9:
    if (*(uint64_t *)(arg2 - 0x28) != 0) goto loc_00351CA6;
    if (!sign_flag) goto loc_00351D9C;
    Arg2 = 0;
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, 0, 2);
loc_00351C25:
    if (*(uint64_t *)(v_stack_p18 - 0x28) != 0) goto loc_00351CE3;
    if (!sign_flag) goto loc_00351E1A;
    Arg2 = 0;
    v_stack_p20 = v_stack_p8;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p18, 2);
loc_00351C51:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p20), 2, v_stack_p18, 2);
    goto loc_00351A93;
loc_00351C63:
    v_stack_p20 = (uint8_t)(v_stack_p20);
    result = (v_stack_p10 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p10 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC751B7));
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x351C80 + arg2 * 8 + 0xFC7800), v_stack_p10, 1);
loc_00351CA6:
    v_stack_p20 = 1 + 23;
    result = (Arg2 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC7517A));
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x351C80 + arg2 * 8 + 0xFC7800), Arg2, 1);
loc_00351CE3:
    v_stack_p20 = 1 + 23;
    result = (v_stack_p18 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_p18 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0xC7513E));
    result = KeBugCheckEx(1 + 23, *(uint64_t *)(v_rip - 0x351C80 + arg2 * 8 + 0xFC7800), v_stack_p18, 1);
loc_00351D1F:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_00351EB8;
    result = KeAreInterruptsEnabled(1 + 23, *(uint64_t *)(v_rip - 0x351C80 + arg2 * 8 + 0xFC7800), v_stack_p18, 1);
    if ((uint8_t)(result) == 0) goto loc_00351EB8;
    if (((uint8_t)((uint8_t)(v_cr8))) >= 1) goto loc_00351EB8;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p10 - 0x16))) & (64)) != 0) goto loc_00351D79;
loc_00351D57:
    result = *(uint8_t *)(v_stack_p10 - 0x16);
    if ((*(uint32_t *)(v_rip + 0xC732B2)) != 0) {
        Arg1 = v_stack_p10 - 48;
        result = ObpDeregisterObject(Arg1, *(uint64_t *)(v_rip - 0x351C80 + arg2 * 8 + 0xFC7800), v_stack_p18, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p10 - 48, Arg2, v_stack_p18, 1);
    goto loc_00351B33;
loc_00351D79:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p10 - 48) - (*(uint8_t *)(result + v_rip - 0x351C80 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x18)) == 0) goto loc_00351D57;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(arg1), Arg2, v_stack_p18, 1);
    goto loc_00351D57;
loc_00351D9C:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_00351EC6;
    result = KeAreInterruptsEnabled(*(uint64_t *)(arg1), Arg2, v_stack_p18, 1);
    if ((uint8_t)(result) == 0) goto loc_00351EC6;
    if (((uint8_t)((uint8_t)(v_cr8))) >= 1) goto loc_00351EC6;
    if ((((uint8_t)(*(uint8_t *)(arg2 - 0x16))) & (64)) != 0) goto loc_00351DF7;
loc_00351DD5:
    result = *(uint8_t *)(arg2 - 0x16);
    if ((*(uint32_t *)(v_rip + 0xC73234)) != 0) {
        Arg1 = Arg2 - 48;
        result = ObpDeregisterObject(Arg1, Arg2, v_stack_p18, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(Arg2 - 48, Arg2, v_stack_p18, 1);
    goto loc_00351B64;
loc_00351DF7:
    result = (uint32_t)((result) & (127));
    Arg1 = (Arg2 - 48) - (*(uint8_t *)(result + v_rip - 0x351C80 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x18)) == 0) goto loc_00351DD5;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(arg1), Arg2, v_stack_p18, 1);
    goto loc_00351DD5;
loc_00351E1A:
    if ((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E6)) != 0) goto loc_00351ED4;
    result = KeAreInterruptsEnabled(*(uint64_t *)(arg1), Arg2, v_stack_p18, 1);
    if ((uint8_t)(result) == 0) goto loc_00351ED4;
    if (((uint8_t)((uint8_t)(v_cr8))) >= 1) goto loc_00351ED4;
    if ((((uint8_t)(*(uint8_t *)(v_stack_p18 - 0x16))) & (64)) != 0) goto loc_00351E74;
loc_00351E52:
    result = *(uint8_t *)(v_stack_p18 - 0x16);
    if ((*(uint32_t *)(v_rip + 0xC731B7)) != 0) {
        Arg1 = v_stack_p18 - 48;
        result = ObpDeregisterObject(Arg1, Arg2, v_stack_p18, 1);
    }
    Arg2 = 0;
    result = ObpRemoveObjectRoutine(v_stack_p18 - 48, Arg2, v_stack_p18, 1);
    goto loc_00351B92;
loc_00351E74:
    result = (uint32_t)((result) & (127));
    Arg1 = (v_stack_p18 - 48) - (*(uint8_t *)(result + v_rip - 0x351C80 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(arg1) + 0x18)) == 0) goto loc_00351E52;
    result = ObpHandleRevocationBlockRemoveObject(*(uint64_t *)(arg1), Arg2, v_stack_p18, 1);
    goto loc_00351E52;
loc_00351E97:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBBBFBB))) != 0) goto loc_00351AD0;
    result = KiReleaseSpinLockInstrumented(v_stack_p18 + 96, v_stack_p48, v_stack_p18, 1);
    goto loc_00351AD6;
loc_00351EB8:
    result = ObpDeferObjectDeletion(v_stack_p10 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B33;
loc_00351EC6:
    result = ObpDeferObjectDeletion(Arg2 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B64;
loc_00351ED4:
    result = ObpDeferObjectDeletion(v_stack_p18 - 48, v_stack_p48, v_stack_p18, 1);
    goto loc_00351B92;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x30` | `64` | `R` |
| `Arg1` | `- 0x30` | `64` | `R/W` |
| `Arg1` | `- 0x28` | `64` | `R` |
| `Arg1` | `- 0x18` | `8` | `R` |
| `Arg1` | `- 0x16` | `8` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R/W` |
| `Arg1` | `+ 0x68` | `8` | `W` |
| `Arg2` | `- 0x30` | `64` | `R` |
| `Arg2` | `- 0x30` | `64` | `R/W` |
| `Arg2` | `- 0x28` | `64` | `R` |
| `Arg2` | `- 0x18` | `8` | `R` |
| `Arg2` | `- 0x16` | `8` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00351A50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
