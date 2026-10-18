# RtlpDeCommitFreeBlock

- RVA: `0x005EA158`–`0x005EA701` (길이 `1,449` bytes)
- VA: `0x00000001405EA158`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5BB4`
- 디코드: `359`개 명령, `1,449/1,449` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **23**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x005EA1E9` → [RtlpCoalesceFreeBlocks](RtlpCoalesceFreeBlocks_function_005E952C.md) (function, `0x005E952C`)
- `0x005EA237` → [RtlpRemoveUCRBlock](RtlpRemoveUCRBlock_function_005EB8B0.md) (function, `0x005EB8B0`)
- `0x005EA306` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005EA30B` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x005EA345` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005EA34A` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x005EA36D` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x005EA37E` → [RtlpUpdateHeapRates](RtlpUpdateHeapRates_function_005EBC98.md) (function, `0x005EBC98`)
- `0x005EA3A5` → [RtlpCreateUCREntry](RtlpCreateUCREntry_function_005EA010.md) (function, `0x005EA010`)
- `0x005EA3CE` → [RtlpRemoveUCRBlock](RtlpRemoveUCRBlock_function_005EB8B0.md) (function, `0x005EB8B0`)
- `0x005EA3E2` → [RtlpInsertUCRBlock](RtlpInsertUCRBlock_function_005EB7E8.md) (function, `0x005EB7E8`)
- `0x005EA47F` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005EA484` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x005EA4C2` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EA58F` → [ZwFreeVirtualMemory](../6A/ZwFreeVirtualMemory_function_006AD490.md) (function, `0x006AD490`)
- `0x005EA607` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005EA60C` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x005EA64A` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x005EA661` → [RtlpInsertFreeBlock](RtlpInsertFreeBlock_function_005EB4C0.md) (function, `0x005EB4C0`)
- `0x005EA6A7` → [RtlpCreateUCREntry](RtlpCreateUCREntry_function_005EA010.md) (function, `0x005EA010`)
- `0x005EA6D2` → [DbgPrint](../35/DbgPrint_function_00358CB0.md) (function, `0x00358CB0`)
- `0x005EA6D7` → [RtlpHeapHandleError](../5F/RtlpHeapHandleError_function_005F12AC.md) (function, `0x005F12AC`)
- `0x005EA6E3` → [RtlpInsertFreeBlock](RtlpInsertFreeBlock_function_005EB4C0.md) (function, `0x005EB4C0`)

### Direct callers
- [RtlpFreeHeap](RtlpFreeHeap_function_005EABC0.md) at `0x005EAD3F`

### Static image references
- `0x005EA17D` → RVA `0x00E67B30` (`.data`; read)
- `0x005EA2EF` → RVA `0x00E67B60` (`.data`; read)
- `0x005EA2FF` → RVA `0x006CC9A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x005EA33E` → RVA `0x006CC990` (` ?? ::FNODOBFM::`string'`; read)
- `0x005EA478` → RVA `0x006CC970` (` ?? ::FNODOBFM::`string'`; read)
- `0x005EA600` → RVA `0x006CCAF0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005EA158  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005EA15D  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
005EA162  55                              push rbp
005EA163  56                              push rsi
005EA164  57                              push rdi
005EA165  41 54                           push r12
005EA167  41 55                           push r13
005EA169  41 56                           push r14
005EA16B  41 57                           push r15
005EA16D  48 8B EC                        mov rbp, rsp
005EA170  48 83 EC 50                     sub rsp, 0x50
005EA174  48 8B 81 68 01 00 00            mov rax, qword ptr [rcx + 0x168]
005EA17B  33 FF                           xor edi, edi
005EA17D  48 33 05 AC D9 87 00            xor rax, qword ptr [rip + 0x87d9ac]
005EA184  4C 8B F2                        mov r14, rdx
005EA187  48 8B D9                        mov rbx, rcx
005EA18A  48 89 7D 40                     mov qword ptr [rbp + 0x40], rdi
005EA18E  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
005EA192  44 8A FF                        mov r15b, dil
005EA195  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
005EA199  0F 85 44 05 00 00               jne 0x1405ea6e3
005EA19F  4C 3B 81 B0 00 00 00            cmp r8, qword ptr [rcx + 0xb0]
005EA1A6  0F 82 37 05 00 00               jb 0x1405ea6e3
005EA1AC  48 8B 91 C0 00 00 00            mov rdx, qword ptr [rcx + 0xc0]
005EA1B3  49 03 D0                        add rdx, r8
005EA1B6  48 3B 91 B8 00 00 00            cmp rdx, qword ptr [rcx + 0xb8]
005EA1BD  0F 82 1A 05 00 00               jb 0x1405ea6dd
005EA1C3  8B 89 B8 02 00 00               mov ecx, dword ptr [rcx + 0x2b8]
005EA1C9  48 8B 83 40 02 00 00            mov rax, qword ptr [rbx + 0x240]
005EA1D0  83 C1 04                        add ecx, 4
005EA1D3  48 D3 E8                        shr rax, cl
005EA1D6  48 3B D0                        cmp rdx, rax
005EA1D9  0F 82 FE 04 00 00               jb 0x1405ea6dd
005EA1DF  4C 8D 45 50                     lea r8, [rbp + 0x50]
005EA1E3  49 8B D6                        mov rdx, r14
005EA1E6  48 8B CB                        mov rcx, rbx
005EA1E9  E8 3E F3 FF FF                  call 0x1405e952c
005EA1EE  4C 8B E8                        mov r13, rax
005EA1F1  41 0F B6 46 0E                  movzx eax, byte ptr [r14 + 0xe]
005EA1F6  84 C0                           test al, al
005EA1F8  74 19                           je 0x1405ea213
005EA1FA  49 81 E6 00 00 FF FF            and r14, 0xffffffffffff0000
005EA201  8B C8                           mov ecx, eax
005EA203  48 C1 E1 10                     shl rcx, 0x10
005EA207  4C 2B F1                        sub r14, rcx
005EA20A  49 81 C6 00 00 01 00            add r14, 0x10000
005EA211  EB 03                           jmp 0x1405ea216
005EA213  4C 8B F3                        mov r14, rbx
005EA216  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
005EA21A  41 B9 01 00 00 00               mov r9d, 1
005EA220  4C 8B E6                        mov r12, rsi
005EA223  49 C1 E4 04                     shl r12, 4
005EA227  4D 03 E5                        add r12, r13
005EA22A  41 80 7C 24 0F 03               cmp byte ptr [r12 + 0xf], 3
005EA230  75 7C                           jne 0x1405ea2ae
005EA232  49 8D 54 24 10                  lea rdx, [r12 + 0x10]
005EA237  E8 74 16 00 00                  call 0x1405eb8b0
005EA23C  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
005EA241  49 8B 44 24 30                  mov rax, qword ptr [r12 + 0x30]
005EA246  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
005EA24A  48 89 4D F0                     mov qword ptr [rbp - 0x10], rcx
005EA24E  83 C9 FF                        or ecx, 0xffffffff
005EA251  41 01 4E 54                     add dword ptr [r14 + 0x54], ecx
005EA255  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
005EA25A  48 C1 E8 0C                     shr rax, 0xc
005EA25E  41 29 46 50                     sub dword ptr [r14 + 0x50], eax
005EA262  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
005EA267  48 03 83 40 02 00 00            add rax, qword ptr [rbx + 0x240]
005EA26E  01 8B 64 02 00 00               add dword ptr [rbx + 0x264], ecx
005EA274  48 89 83 40 02 00 00            mov qword ptr [rbx + 0x240], rax
005EA27B  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
005EA280  48 3D 00 F0 0F 00               cmp rax, 0xff000
005EA286  72 07                           jb 0x1405ea28f
005EA288  48 29 83 48 02 00 00            sub qword ptr [rbx + 0x248], rax
005EA28F  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
005EA294  48 83 C6 40                     add rsi, 0x40
005EA298  48 C1 E8 04                     shr rax, 4
005EA29C  41 B9 01 00 00 00               mov r9d, 1
005EA2A2  48 03 F0                        add rsi, rax
005EA2A5  45 8A F9                        mov r15b, r9b
005EA2A8  48 89 75 50                     mov qword ptr [rbp + 0x50], rsi
005EA2AC  EB 04                           jmp 0x1405ea2b2
005EA2AE  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
005EA2B2  41 0F B7 45 0C                  movzx eax, word ptr [r13 + 0xc]
005EA2B7  66 39 83 8C 00 00 00            cmp word ptr [rbx + 0x8c], ax
005EA2BE  0F 85 3F 02 00 00               jne 0x1405ea503
005EA2C4  49 8D 56 60                     lea rdx, [r14 + 0x60]
005EA2C8  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
005EA2CC  48 8B 0A                        mov rcx, qword ptr [rdx]
005EA2CF  48 3B D1                        cmp rdx, rcx
005EA2D2  74 18                           je 0x1405ea2ec
005EA2D4  4C 8D 61 F0                     lea r12, [rcx - 0x10]
005EA2D8  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
005EA2DD  49 03 44 24 20                  add rax, qword ptr [r12 + 0x20]
005EA2E2  49 3B C5                        cmp rax, r13
005EA2E5  74 08                           je 0x1405ea2ef
005EA2E7  48 8B 09                        mov rcx, qword ptr [rcx]
005EA2EA  EB E3                           jmp 0x1405ea2cf
005EA2EC  4C 8B E7                        mov r12, rdi
005EA2EF  8B 15 6B D8 87 00               mov edx, dword ptr [rip + 0x87d86b]
005EA2F5  41 3B D1                        cmp edx, r9d
005EA2F8  7C 17                           jl 0x1405ea311
005EA2FA  4D 85 E4                        test r12, r12
005EA2FD  75 12                           jne 0x1405ea311
005EA2FF  48 8D 0D 9A 26 0E 00            lea rcx, [rip + 0xe269a]
005EA306  E8 A5 E9 D6 FF                  call 0x140358cb0
005EA30B  E8 9C 6F 00 00                  call 0x1405f12ac
005EA310  CC                              int3
005EA311  48 8B CE                        mov rcx, rsi
005EA314  48 C1 E1 04                     shl rcx, 4
005EA318  45 84 FF                        test r15b, r15b
005EA31B  75 04                           jne 0x1405ea321
005EA31D  48 83 C1 E0                     add rcx, -0x20
005EA321  49 03 CD                        add rcx, r13
005EA324  48 81 E1 00 F0 FF FF            and rcx, 0xfffffffffffff000
005EA32B  49 2B CD                        sub rcx, r13
005EA32E  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
005EA332  75 27                           jne 0x1405ea35b
005EA334  41 3B D1                        cmp edx, r9d
005EA337  7C 17                           jl 0x1405ea350
005EA339  45 84 FF                        test r15b, r15b
005EA33C  74 12                           je 0x1405ea350
005EA33E  48 8D 0D 4B 26 0E 00            lea rcx, [rip + 0xe264b]
005EA345  E8 66 E9 D6 FF                  call 0x140358cb0
005EA34A  E8 5D 6F 00 00                  call 0x1405f12ac
005EA34F  CC                              int3
005EA350  4C 8B C6                        mov r8, rsi
005EA353  49 8B D5                        mov rdx, r13
005EA356  E9 85 03 00 00                  jmp 0x1405ea6e0
005EA35B  41 B9 00 40 00 00               mov r9d, 0x4000
005EA361  4C 8D 45 40                     lea r8, [rbp + 0x40]
005EA365  48 8D 55 E0                     lea rdx, [rbp - 0x20]
005EA369  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005EA36D  E8 1E 31 0C 00                  call 0x1406ad490
005EA372  85 C0                           test eax, eax
005EA374  79 3A                           jns 0x1405ea3b0
005EA376  BA 03 00 00 00                  mov edx, 3
005EA37B  48 8B CB                        mov rcx, rbx
005EA37E  E8 15 19 00 00                  call 0x1405ebc98
005EA383  45 84 FF                        test r15b, r15b
005EA386  74 C8                           je 0x1405ea350
005EA388  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
005EA38C  48 8D 45 50                     lea rax, [rbp + 0x50]
005EA390  4C 8B 4D F0                     mov r9, qword ptr [rbp - 0x10]
005EA394  49 83 C0 D0                     add r8, -0x30
005EA398  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005EA39D  49 8B D6                        mov rdx, r14
005EA3A0  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
005EA3A5  E8 66 FC FF FF                  call 0x1405ea010
005EA3AA  48 8B 75 50                     mov rsi, qword ptr [rbp + 0x50]
005EA3AE  EB A0                           jmp 0x1405ea350
005EA3B0  FF 83 6C 02 00 00               inc dword ptr [rbx + 0x26c]
005EA3B6  49 8B 4C 24 28                  mov rcx, qword ptr [r12 + 0x28]
005EA3BB  48 81 F9 00 F0 0F 00            cmp rcx, 0xff000
005EA3C2  72 07                           jb 0x1405ea3cb
005EA3C4  48 29 8B 48 02 00 00            sub qword ptr [rbx + 0x248], rcx
005EA3CB  49 8B D4                        mov rdx, r12
005EA3CE  E8 DD 14 00 00                  call 0x1405eb8b0
005EA3D3  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
005EA3D7  49 8B D4                        mov rdx, r12
005EA3DA  49 01 44 24 28                  add qword ptr [r12 + 0x28], rax
005EA3DF  48 8B CB                        mov rcx, rbx
005EA3E2  E8 01 14 00 00                  call 0x1405eb7e8
005EA3E7  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
005EA3EB  48 C1 E8 0C                     shr rax, 0xc
005EA3EF  41 01 46 50                     add dword ptr [r14 + 0x50], eax
005EA3F3  48 8B 83 40 02 00 00            mov rax, qword ptr [rbx + 0x240]
005EA3FA  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
005EA3FE  48 2B C1                        sub rax, rcx
005EA401  48 89 83 40 02 00 00            mov qword ptr [rbx + 0x240], rax
005EA408  49 8B 44 24 28                  mov rax, qword ptr [r12 + 0x28]
005EA40D  48 3D 00 F0 0F 00               cmp rax, 0xff000
005EA413  72 07                           jb 0x1405ea41c
005EA415  48 01 83 48 02 00 00            add qword ptr [rbx + 0x248], rax
005EA41C  45 84 FF                        test r15b, r15b
005EA41F  0F 85 C3 02 00 00               jne 0x1405ea6e8
005EA425  4C 8B 7D E0                     mov r15, qword ptr [rbp - 0x20]
005EA429  0F B7 83 8C 00 00 00            movzx eax, word ptr [rbx + 0x8c]
005EA430  4C 03 F9                        add r15, rcx
005EA433  48 C1 E6 04                     shl rsi, 4
005EA437  66 41 89 47 0C                  mov word ptr [r15 + 0xc], ax
005EA43C  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
005EA440  4A 8D 14 2E                     lea rdx, [rsi + r13]
005EA444  48 03 4D 40                     add rcx, qword ptr [rbp + 0x40]
005EA448  48 3B D1                        cmp rdx, rcx
005EA44B  0F 84 8A 00 00 00               je 0x1405ea4db
005EA451  41 88 7F 0F                     mov byte ptr [r15 + 0xf], dil
005EA455  B8 01 00 00 00                  mov eax, 1
005EA45A  41 88 7F 0A                     mov byte ptr [r15 + 0xa], dil
005EA45E  48 2B 75 40                     sub rsi, qword ptr [rbp + 0x40]
005EA462  48 C1 EE 04                     shr rsi, 4
005EA466  39 05 F4 D6 87 00               cmp dword ptr [rip + 0x87d6f4], eax
005EA46C  66 41 89 77 08                  mov word ptr [r15 + 8], si
005EA471  7C 17                           jl 0x1405ea48a
005EA473  66 3B F0                        cmp si, ax
005EA476  77 12                           ja 0x1405ea48a
005EA478  48 8D 0D F1 24 0E 00            lea rcx, [rip + 0xe24f1]
005EA47F  E8 2C E8 D6 FF                  call 0x140358cb0
005EA484  E8 23 6E 00 00                  call 0x1405f12ac
005EA489  CC                              int3
005EA48A  41 88 7F 0B                     mov byte ptr [r15 + 0xb], dil
005EA48E  49 8B 56 28                     mov rdx, qword ptr [r14 + 0x28]
005EA492  49 3B D6                        cmp rdx, r14
005EA495  74 33                           je 0x1405ea4ca
005EA497  49 8B F7                        mov rsi, r15
005EA49A  49 2B F6                        sub rsi, r14
005EA49D  48 C1 EE 10                     shr rsi, 0x10
005EA4A1  48 FF C6                        inc rsi
005EA4A4  48 81 FE FE 00 00 00            cmp rsi, 0xfe
005EA4AB  72 1A                           jb 0x1405ea4c7
005EA4AD  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
005EA4B2  4D 8B CE                        mov r9, r14
005EA4B5  4D 8B C7                        mov r8, r15
005EA4B8  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005EA4BD  B9 03 00 00 00                  mov ecx, 3
005EA4C2  E8 F5 12 D7 FF                  call 0x14035b7bc
005EA4C7  40 8A FE                        mov dil, sil
005EA4CA  45 0F B7 47 08                  movzx r8d, word ptr [r15 + 8]
005EA4CF  49 8B D7                        mov rdx, r15
005EA4D2  41 88 7F 0E                     mov byte ptr [r15 + 0xe], dil
005EA4D6  E9 05 02 00 00                  jmp 0x1405ea6e0
005EA4DB  39 7B 7C                        cmp dword ptr [rbx + 0x7c], edi
005EA4DE  0F 84 04 02 00 00               je 0x1405ea6e8
005EA4E4  41 8A 4F 0A                     mov cl, byte ptr [r15 + 0xa]
005EA4E8  41 32 4F 09                     xor cl, byte ptr [r15 + 9]
005EA4EC  41 32 4F 08                     xor cl, byte ptr [r15 + 8]
005EA4F0  41 88 4F 0B                     mov byte ptr [r15 + 0xb], cl
005EA4F4  8B 83 88 00 00 00               mov eax, dword ptr [rbx + 0x88]
005EA4FA  41 31 47 08                     xor dword ptr [r15 + 8], eax
005EA4FE  E9 E5 01 00 00                  jmp 0x1405ea6e8
005EA503  49 8D 95 3F 10 00 00            lea rdx, [r13 + 0x103f]
005EA50A  49 C7 C0 00 F0 FF FF            mov r8, 0xfffffffffffff000
005EA511  49 23 D0                        and rdx, r8
005EA514  49 8D 45 50                     lea rax, [r13 + 0x50]
005EA518  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
005EA51C  48 3B D0                        cmp rdx, rax
005EA51F  75 0B                           jne 0x1405ea52c
005EA521  48 81 C2 00 10 00 00            add rdx, 0x1000
005EA528  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
005EA52C  48 8B CE                        mov rcx, rsi
005EA52F  48 C1 E1 04                     shl rcx, 4
005EA533  45 84 FF                        test r15b, r15b
005EA536  75 04                           jne 0x1405ea53c
005EA538  48 83 C1 E0                     add rcx, -0x20
005EA53C  49 03 CD                        add rcx, r13
005EA53F  49 23 C8                        and rcx, r8
005EA542  48 3B CA                        cmp rcx, rdx
005EA545  0F 82 6A 01 00 00               jb 0x1405ea6b5
005EA54B  48 2B CA                        sub rcx, rdx
005EA54E  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
005EA552  41 80 7C 24 0F 03               cmp byte ptr [r12 + 0xf], 3
005EA558  74 17                           je 0x1405ea571
005EA55A  48 85 C9                        test rcx, rcx
005EA55D  0F 84 ED FD FF FF               je 0x1405ea350
005EA563  48 3B 8B B0 00 00 00            cmp rcx, qword ptr [rbx + 0xb0]
005EA56A  73 0A                           jae 0x1405ea576
005EA56C  E9 DF FD FF FF                  jmp 0x1405ea350
005EA571  48 85 C9                        test rcx, rcx
005EA574  74 26                           je 0x1405ea59c
005EA576  44 01 8B 6C 02 00 00            add dword ptr [rbx + 0x26c], r9d
005EA57D  4C 8D 45 40                     lea r8, [rbp + 0x40]
005EA581  41 B9 00 40 00 00               mov r9d, 0x4000
005EA587  48 8D 55 E0                     lea rdx, [rbp - 0x20]
005EA58B  48 83 C9 FF                     or rcx, 0xffffffffffffffff
005EA58F  E8 FC 2E 0C 00                  call 0x1406ad490
005EA594  85 C0                           test eax, eax
005EA596  0F 88 DA FD FF FF               js 0x1405ea376
005EA59C  45 84 FF                        test r15b, r15b
005EA59F  0F 85 E2 00 00 00               jne 0x1405ea687
005EA5A5  4C 8B 7D 40                     mov r15, qword ptr [rbp + 0x40]
005EA5A9  4C 03 7D E0                     add r15, qword ptr [rbp - 0x20]
005EA5AD  0F B7 83 8C 00 00 00            movzx eax, word ptr [rbx + 0x8c]
005EA5B4  48 C1 E6 04                     shl rsi, 4
005EA5B8  66 41 89 47 0C                  mov word ptr [r15 + 0xc], ax
005EA5BD  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
005EA5C1  48 03 4D 40                     add rcx, qword ptr [rbp + 0x40]
005EA5C5  4A 8D 14 2E                     lea rdx, [rsi + r13]
005EA5C9  48 3B D1                        cmp rdx, rcx
005EA5CC  0F 84 96 00 00 00               je 0x1405ea668
005EA5D2  41 88 7F 0F                     mov byte ptr [r15 + 0xf], dil
005EA5D6  B8 01 00 00 00                  mov eax, 1
005EA5DB  41 88 7F 0A                     mov byte ptr [r15 + 0xa], dil
005EA5DF  48 2B 75 40                     sub rsi, qword ptr [rbp + 0x40]
005EA5E3  48 2B 75 E0                     sub rsi, qword ptr [rbp - 0x20]
005EA5E7  49 03 F5                        add rsi, r13
005EA5EA  48 C1 EE 04                     shr rsi, 4
005EA5EE  39 05 6C D5 87 00               cmp dword ptr [rip + 0x87d56c], eax
005EA5F4  66 41 89 77 08                  mov word ptr [r15 + 8], si
005EA5F9  7C 17                           jl 0x1405ea612
005EA5FB  66 3B F0                        cmp si, ax
005EA5FE  77 12                           ja 0x1405ea612
005EA600  48 8D 0D E9 24 0E 00            lea rcx, [rip + 0xe24e9]
005EA607  E8 A4 E6 D6 FF                  call 0x140358cb0
005EA60C  E8 9B 6C 00 00                  call 0x1405f12ac
005EA611  CC                              int3
005EA612  41 88 7F 0B                     mov byte ptr [r15 + 0xb], dil
005EA616  49 8B 56 28                     mov rdx, qword ptr [r14 + 0x28]
005EA61A  49 3B D6                        cmp rdx, r14
005EA61D  74 33                           je 0x1405ea652
005EA61F  49 8B F7                        mov rsi, r15
005EA622  49 2B F6                        sub rsi, r14
005EA625  48 C1 EE 10                     shr rsi, 0x10
005EA629  48 FF C6                        inc rsi
005EA62C  48 81 FE FE 00 00 00            cmp rsi, 0xfe
005EA633  72 1A                           jb 0x1405ea64f
005EA635  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
005EA63A  4D 8B CE                        mov r9, r14
005EA63D  4D 8B C7                        mov r8, r15
005EA640  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
005EA645  B9 03 00 00 00                  mov ecx, 3
005EA64A  E8 6D 11 D7 FF                  call 0x14035b7bc
005EA64F  40 8A FE                        mov dil, sil
005EA652  45 0F B7 47 08                  movzx r8d, word ptr [r15 + 8]
005EA657  49 8B D7                        mov rdx, r15
005EA65A  48 8B CB                        mov rcx, rbx
005EA65D  41 88 7F 0E                     mov byte ptr [r15 + 0xe], dil
005EA661  E8 5A 0E 00 00                  call 0x1405eb4c0
005EA666  EB 1F                           jmp 0x1405ea687
005EA668  39 7B 7C                        cmp dword ptr [rbx + 0x7c], edi
005EA66B  74 1A                           je 0x1405ea687
005EA66D  41 8A 4F 0A                     mov cl, byte ptr [r15 + 0xa]
005EA671  41 32 4F 09                     xor cl, byte ptr [r15 + 9]
005EA675  41 32 4F 08                     xor cl, byte ptr [r15 + 8]
005EA679  41 88 4F 0B                     mov byte ptr [r15 + 0xb], cl
005EA67D  8B 83 88 00 00 00               mov eax, dword ptr [rbx + 0x88]
005EA683  41 31 47 08                     xor dword ptr [r15 + 8], eax
005EA687  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
005EA68B  48 8D 45 F8                     lea rax, [rbp - 8]
005EA68F  4C 8B 4D 40                     mov r9, qword ptr [rbp + 0x40]
005EA693  49 83 C0 D0                     add r8, -0x30
005EA697  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005EA69C  49 8B D6                        mov rdx, r14
005EA69F  48 8B CB                        mov rcx, rbx
005EA6A2  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
005EA6A7  E8 64 F9 FF FF                  call 0x1405ea010
005EA6AC  4C 8B 45 F8                     mov r8, qword ptr [rbp - 8]
005EA6B0  E9 9E FC FF FF                  jmp 0x1405ea353
005EA6B5  44 39 0D A4 D4 87 00            cmp dword ptr [rip + 0x87d4a4], r9d
005EA6BC  0F 8C 8E FC FF FF               jl 0x1405ea350
005EA6C2  45 84 FF                        test r15b, r15b
005EA6C5  0F 84 85 FC FF FF               je 0x1405ea350
005EA6CB  48 8D 0D BE 22 0E 00            lea rcx, [rip + 0xe22be]
005EA6D2  E8 D9 E5 D6 FF                  call 0x140358cb0
005EA6D7  E8 D0 6B 00 00                  call 0x1405f12ac
005EA6DC  CC                              int3
005EA6DD  49 8B D6                        mov rdx, r14
005EA6E0  48 8B CB                        mov rcx, rbx
005EA6E3  E8 D8 0D 00 00                  call 0x1405eb4c0
005EA6E8  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
005EA6F0  48 83 C4 50                     add rsp, 0x50
005EA6F4  41 5F                           pop r15
005EA6F6  41 5E                           pop r14
005EA6F8  41 5D                           pop r13
005EA6FA  41 5C                           pop r12
005EA6FC  5F                              pop rdi
005EA6FD  5E                              pop rsi
005EA6FE  5D                              pop rbp
005EA6FF  C3                              ret
005EA700  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpDeCommitFreeBlock(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (80);
    v_rdi = 0;
    result = (*(unsigned __int64 *)(a1 + 360)) ^ (*(unsigned __int64 *)(v_rip + 8903084));
    v_stack_p8 = 0;
    v_stack_m40 = 0;
    v_stack_m50 = 0;
    if (condition_is_not_equal) goto loc_005EA6E3;
    if (a3 < (*(unsigned __int64 *)(a1 + 176))) goto loc_005EA6E3;
    a2 = (*(unsigned __int64 *)(a1 + 192)) + (a3);
    if (a2 < (*(unsigned __int64 *)(a1 + 184))) goto loc_005EA6DD;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 696))) + (4));
    result = (*(unsigned __int64 *)(a1 + 576)) >> ((unsigned __int8)(a1));
    if (a2 < result) goto loc_005EA6DD;
    result = RtlpCoalesceFreeBlocks(a1, a2, v_stack_p18, a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(a2 + 14)) == 0) goto loc_005EA213;
    v_r14 = (a2) & (0xFFFFFFFFFFFF0000ULL);
    a1 = ((unsigned int)((unsigned int)(*(unsigned __int8 *)(a2 + 14)))) << (16);
    v_r14 = (v_r14) - (a1);
    v_r14 = (v_r14) + (0x10000ULL);
    goto loc_005EA216;
loc_005EA213:
loc_005EA216:
    v_r12 = (v_stack_p18) << (4);
    v_r12 = (v_r12) + (result);
    if ((*(unsigned __int8 *)(v_r12 + 15)) != 3) goto loc_005EA2AE;
    result = RtlpRemoveUCRBlock(a1, v_r12 + 16, v_stack_p18, 1);
    v_stack_m50 = *(unsigned __int64 *)(v_r12 + 48);
    v_stack_m48 = *(unsigned __int64 *)(v_r12 + 56);
    a1 = (unsigned int)((*(unsigned __int64 *)(v_r12 + 56)) | (0xFFFFFFFFULL));
    result = (*(unsigned __int64 *)(v_r12 + 56)) >> (12);
    result = (*(unsigned __int64 *)(v_r12 + 56)) + (*(unsigned __int64 *)(a1 + 576));
    *(unsigned __int64 *)(a1 + 576) = result;
    if ((*(unsigned __int64 *)(v_r12 + 56)) >= 0xFF000ULL) {
    }
    v_rsi = (v_stack_p18) + (64);
    result = (*(unsigned __int64 *)(v_r12 + 56)) >> (4);
    v_rsi = (v_rsi) + (result);
    v_stack_p18 = v_rsi;
    goto loc_005EA2B2;
loc_005EA2AE:
    v_stack_m48 = 0;
loc_005EA2B2:
    if ((*(unsigned __int16 *)(a1 + 140)) != ((unsigned __int16)(*(unsigned __int16 *)(result + 12)))) goto loc_005EA503;
    v_stack_m58 = result;
loc_005EA2CF:
    if ((a1 + 96) == (*(unsigned __int64 *)(a1 + 96))) goto loc_005EA2EC;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96) - 16 + 40)) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 96) - 16 + 32));
    if (result == result) goto loc_005EA2EF;
    goto loc_005EA2CF;
loc_005EA2EC:
loc_005EA2EF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8902763)))) < 1) goto loc_005EA311;
    if (0 == 0) {
        a1 = v_rip + 927386;
        result = DbgPrint(a1, (unsigned int)(*(unsigned int *)(v_rip + 8902763)), v_stack_p18, 1);
        result = RtlpHeapHandleError(a1, (unsigned int)(*(unsigned int *)(v_rip + 8902763)), v_stack_p18, 1);
    }
    a1 = (v_rsi) << (4);
    if (1 == 0) {
        a1 = (a1) + (-32);
    }
    a1 = (a1) + (result);
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) - (result);
    v_stack_p8 = a1;
    if (condition_is_not_equal) goto loc_005EA35B;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8902763)))) < 1) goto loc_005EA350;
    if (1 != 0) {
        a1 = v_rip + 927307;
        result = DbgPrint(a1, (unsigned int)(*(unsigned int *)(v_rip + 8902763)), v_stack_p18, 1);
        result = RtlpHeapHandleError(a1, (unsigned int)(*(unsigned int *)(v_rip + 8902763)), v_stack_p18, 1);
    }
loc_005EA353:
    goto loc_005EA6E0;
loc_005EA35B:
    a1 = (a1) | (-1);
    result = ZwFreeVirtualMemory(a1, v_stack_m58, v_stack_p8, (unsigned int)(0x4000ULL));
    if (!sign_flag) goto loc_005EA3B0;
loc_005EA376:
    result = RtlpUpdateHeapRates(a1, 3, v_stack_p8, (unsigned int)(0x4000ULL));
    if (1 == 0) goto loc_005EA350;
    a3 = (v_stack_m50) + (-48);
    v_stack_m60 = v_stack_p18;
    v_stack_m68 = result;
    result = RtlpCreateUCREntry(a1, a1, a3, v_stack_m48);
    goto loc_005EA350;
loc_005EA3B0:
    if ((*(unsigned __int64 *)(0 + 40)) >= 0xFF000ULL) {
    }
    result = RtlpRemoveUCRBlock(*(unsigned __int64 *)(0 + 40), 0, a3, v_stack_m48);
    result = RtlpInsertUCRBlock(a1, 0, a3, v_stack_m48);
    result = (v_stack_p8) >> (12);
    result = (*(unsigned __int64 *)(a1 + 576)) - (v_stack_p8);
    *(unsigned __int64 *)(a1 + 576) = result;
    if ((*(unsigned __int64 *)(0 + 40)) >= 0xFF000ULL) {
    }
    if (1 != 0) goto loc_005EA6E8;
    v_r15 = (v_stack_m58) + (v_stack_p8);
    v_rsi = (v_stack_p18) << (4);
    *(unsigned __int16 *)(v_r15 + 12) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 140));
    a1 = (v_stack_m58) + (v_stack_p8);
    if ((v_rsi + result * 1) == a1) goto loc_005EA4DB;
    *(unsigned __int8 *)(v_r15 + 15) = 0;
    *(unsigned __int8 *)(v_r15 + 10) = 0;
    v_rsi = (v_rsi) - (v_stack_p8);
    v_rsi = (v_rsi) >> (4);
    *(unsigned __int16 *)(v_r15 + 8) = (unsigned __int16)(v_rsi);
    if ((*(unsigned int *)(v_rip + 8902388)) < 1) goto loc_005EA48A;
    result = 1;
    if (((unsigned __int16)(v_rsi)) <= 1) {
        a1 = v_rip + 926961;
        result = DbgPrint(a1, v_rsi + result * 1, a3, v_stack_m48);
        result = RtlpHeapHandleError(a1, v_rsi + result * 1, a3, v_stack_m48);
    }
    *(unsigned __int8 *)(v_r15 + 11) = 0;
    if ((*(unsigned __int64 *)(a1 + 40)) == a1) goto loc_005EA4CA;
    v_rsi = (v_r15) - (a1);
    v_rsi = (v_rsi) >> (16);
    v_rsi = (v_rsi) + 1;
    if (v_rsi >= 254) {
        v_stack_m60 = 0;
        a4 = a1;
        a3 = v_r15;
        v_stack_m68 = 0;
        a1 = 3;
        result = RtlpLogHeapFailure(a1, *(unsigned __int64 *)(a1 + 40), a3, a4);
    }
loc_005EA4CA:
    *(unsigned __int8 *)(v_r15 + 14) = (unsigned __int8)((unsigned __int8)(v_rsi));
    goto loc_005EA6E0;
loc_005EA4DB:
    if ((*(unsigned int *)(a1 + 124)) == ((unsigned int)((unsigned __int8)(v_rsi)))) goto loc_005EA6E8;
    a1 = (unsigned __int8)((*(unsigned __int8 *)(v_r15 + 10)) ^ (*(unsigned __int8 *)(v_r15 + 9)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_r15 + 8)));
    *(unsigned __int8 *)(v_r15 + 11) = (unsigned __int8)(a1);
    goto loc_005EA6E8;
loc_005EA503:
    a2 = (result + 4159) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m58 = a2;
    if (a2 == (result + 80)) {
        a2 = (a2) + (0x1000ULL);
        v_stack_m58 = a2;
    }
    a1 = (v_rsi) << (4);
    if ((unsigned __int8)(v_r15) == 0) {
        a1 = (a1) + (-32);
    }
    a1 = (a1) + (result);
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    if (a1 < a2) goto loc_005EA6B5;
    a1 = (a1) - (a2);
    v_stack_p8 = a1;
    if ((*(unsigned __int8 *)(0 + 15)) == 3) goto loc_005EA571;
    if (a1 == 0) goto loc_005EA350;
    if (a1 >= (*(unsigned __int64 *)(a1 + 176))) goto loc_005EA576;
    goto loc_005EA350;
loc_005EA571:
    if (a1 == 0) goto loc_005EA59C;
loc_005EA576:
    a1 = (a1) | (-1);
    result = ZwFreeVirtualMemory(a1, v_stack_m58, v_stack_p8, (unsigned int)(0x4000ULL));
    if (sign_flag) goto loc_005EA376;
loc_005EA59C:
    if ((unsigned __int8)(v_r15) != 0) goto loc_005EA687;
    v_r15 = (v_stack_p8) + (v_stack_m58);
    v_rsi = (v_rsi) << (4);
    *(unsigned __int16 *)(v_r15 + 12) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 140));
    a1 = (v_stack_m58) + (v_stack_p8);
    if ((v_rsi + result * 1) == a1) goto loc_005EA668;
    *(unsigned __int8 *)(v_r15 + 15) = (unsigned __int8)((unsigned __int8)(v_rsi));
    *(unsigned __int8 *)(v_r15 + 10) = (unsigned __int8)((unsigned __int8)(v_rsi));
    v_rsi = (v_rsi) - (v_stack_p8);
    v_rsi = (v_rsi) - (v_stack_m58);
    v_rsi = (v_rsi) + (result);
    v_rsi = (v_rsi) >> (4);
    *(unsigned __int16 *)(v_r15 + 8) = (unsigned __int16)(v_rsi);
    if ((*(unsigned int *)(v_rip + 8901996)) < 1) goto loc_005EA612;
    result = 1;
    if (((unsigned __int16)(v_rsi)) <= 1) {
        a1 = v_rip + 926953;
        result = DbgPrint(a1, v_rsi + result * 1, v_stack_p8, (unsigned int)(0x4000ULL));
        result = RtlpHeapHandleError(a1, v_rsi + result * 1, v_stack_p8, (unsigned int)(0x4000ULL));
    }
    *(unsigned __int8 *)(v_r15 + 11) = (unsigned __int8)((unsigned __int8)(v_rsi));
    if ((*(unsigned __int64 *)(a1 + 40)) == a1) goto loc_005EA652;
    v_rsi = (v_r15) - (a1);
    v_rsi = (v_rsi) >> (16);
    v_rsi = (v_rsi) + 1;
    if (v_rsi >= 254) {
        v_stack_m60 = (unsigned __int8)(v_rsi);
        a4 = a1;
        a3 = v_r15;
        v_stack_m68 = (unsigned __int8)(v_rsi);
        a1 = 3;
        result = RtlpLogHeapFailure(a1, *(unsigned __int64 *)(a1 + 40), a3, a4);
    }
loc_005EA652:
    *(unsigned __int8 *)(v_r15 + 14) = (unsigned __int8)((unsigned __int8)(v_rsi));
    result = RtlpInsertFreeBlock(a1, v_r15, *(unsigned __int16 *)(v_r15 + 8), a4);
    goto loc_005EA687;
loc_005EA668:
    if ((*(unsigned int *)(a1 + 124)) != ((unsigned int)((unsigned __int8)(v_rsi)))) {
        a1 = *(unsigned __int8 *)(v_r15 + 10);
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_r15 + 9)));
        a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_r15 + 8)));
        *(unsigned __int8 *)(v_r15 + 11) = (unsigned __int8)(a1);
        result = *(unsigned int *)(a1 + 136);
    }
    a3 = (v_stack_m58) + (-48);
    v_stack_m60 = v_stack_m40;
    v_stack_m68 = result;
    result = RtlpCreateUCREntry(a1, a1, a3, v_stack_p8);
    goto loc_005EA353;
loc_005EA6B5:
    if ((*(unsigned int *)(v_rip + 8901796)) < ((unsigned int)(v_stack_p8))) goto loc_005EA350;
    if ((unsigned __int8)(v_r15) == 0) goto loc_005EA350;
    result = DbgPrint(v_rip + 926398, a1, v_stack_m40, v_stack_p8);
    result = RtlpHeapHandleError(v_rip + 926398, a1, v_stack_m40, v_stack_p8);
loc_005EA6DD:
loc_005EA6E0:
loc_005EA6E3:
    result = RtlpInsertFreeBlock(a1, a1, v_stack_m40, v_stack_p8);
loc_005EA6E8:
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpDeCommitFreeBlock(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (80);
    local_rdi = 0;
    result = (*(uint64_t *)(arg1 + 0x168)) ^ (*(uint64_t *)(v_rip + 0x87D9AC));
    v_stack_p8 = 0;
    v_stack_m40 = 0;
    v_stack_m50 = 0;
    if (condition_is_not_equal) goto loc_005EA6E3;
    if (Arg3 < (*(uint64_t *)(arg1 + 0xB0))) goto loc_005EA6E3;
    Arg2 = (*(uint64_t *)(arg1 + 0xC0)) + (Arg3);
    if (Arg2 < (*(uint64_t *)(arg1 + 0xB8))) goto loc_005EA6DD;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x2B8))) + (4));
    result = (*(uint64_t *)(arg1 + 0x240)) >> ((uint8_t)(Arg1));
    if (Arg2 < result) goto loc_005EA6DD;
    result = RtlpCoalesceFreeBlocks(Arg1, Arg2, v_stack_p18, a4);
    if ((uint8_t)(*(uint8_t *)(arg2 + 0xE)) == 0) goto loc_005EA213;
    local_r14 = (Arg2) & (0xFFFFFFFFFFFF0000ULL);
    Arg1 = ((uint32_t)((uint32_t)(*(uint8_t *)(arg2 + 0xE)))) << (16);
    local_r14 = (local_r14) - (Arg1);
    local_r14 = (local_r14) + (0x10000ULL);
    goto loc_005EA216;
loc_005EA213:
loc_005EA216:
    local_r12 = (v_stack_p18) << (4);
    local_r12 = (local_r12) + (result);
    if ((*(uint8_t *)(local_r12 + 0xF)) != 3) goto loc_005EA2AE;
    result = RtlpRemoveUCRBlock(Arg1, local_r12 + 16, v_stack_p18, 1);
    v_stack_m50 = *(uint64_t *)(local_r12 + 0x30);
    v_stack_m48 = *(uint64_t *)(local_r12 + 0x38);
    Arg1 = (uint32_t)((*(uint64_t *)(local_r12 + 0x38)) | (0xFFFFFFFFULL));
    result = (*(uint64_t *)(local_r12 + 0x38)) >> (12);
    result = (*(uint64_t *)(local_r12 + 0x38)) + (*(uint64_t *)(arg1 + 0x240));
    *(uint64_t *)(arg1 + 0x240) = result;
    if ((*(uint64_t *)(local_r12 + 0x38)) >= 0xFF000ULL) {
    }
    local_rsi = (v_stack_p18) + (64);
    result = (*(uint64_t *)(local_r12 + 0x38)) >> (4);
    local_rsi = (local_rsi) + (result);
    v_stack_p18 = local_rsi;
    goto loc_005EA2B2;
loc_005EA2AE:
    v_stack_m48 = 0;
loc_005EA2B2:
    if ((*(uint16_t *)(arg1 + 0x8C)) != ((uint16_t)(*(uint16_t *)(result + 0xC)))) goto loc_005EA503;
    v_stack_m58 = result;
loc_005EA2CF:
    if ((Arg1 + 96) == (*(uint64_t *)(arg1 + 0x60))) goto loc_005EA2EC;
    result = (*(uint64_t *)(*(uint64_t *)(arg1 + 0x60) - 0x10 + 0x28)) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x60) - 0x10 + 0x20));
    if (result == result) goto loc_005EA2EF;
    goto loc_005EA2CF;
loc_005EA2EC:
loc_005EA2EF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)))) < 1) goto loc_005EA311;
    if (0 == 0) {
        Arg1 = v_rip + 927386;
        result = DbgPrint(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)), v_stack_p18, 1);
        result = RtlpHeapHandleError(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)), v_stack_p18, 1);
    }
    Arg1 = (local_rsi) << (4);
    if (1 == 0) {
        Arg1 = (Arg1) + (-32);
    }
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) - (result);
    v_stack_p8 = Arg1;
    if (condition_is_not_equal) goto loc_005EA35B;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)))) < 1) goto loc_005EA350;
    if (1 != 0) {
        Arg1 = v_rip + 927307;
        result = DbgPrint(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)), v_stack_p18, 1);
        result = RtlpHeapHandleError(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x87D86B)), v_stack_p18, 1);
    }
loc_005EA353:
    goto loc_005EA6E0;
loc_005EA35B:
    Arg1 = (Arg1) | (-1);
    result = ZwFreeVirtualMemory(Arg1, v_stack_m58, v_stack_p8, (uint32_t)(0x4000ULL));
    if (!sign_flag) goto loc_005EA3B0;
loc_005EA376:
    result = RtlpUpdateHeapRates(Arg1, 3, v_stack_p8, (uint32_t)(0x4000ULL));
    if (1 == 0) goto loc_005EA350;
    Arg3 = (v_stack_m50) + (-48);
    v_stack_m60 = v_stack_p18;
    v_stack_m68 = result;
    result = RtlpCreateUCREntry(Arg1, Arg1, Arg3, v_stack_m48);
    goto loc_005EA350;
loc_005EA3B0:
    if ((*(uint64_t *)(0 + 0x28)) >= 0xFF000ULL) {
    }
    result = RtlpRemoveUCRBlock(*(uint64_t *)(0 + 0x28), 0, Arg3, v_stack_m48);
    result = RtlpInsertUCRBlock(Arg1, 0, Arg3, v_stack_m48);
    result = (v_stack_p8) >> (12);
    result = (*(uint64_t *)(arg1 + 0x240)) - (v_stack_p8);
    *(uint64_t *)(arg1 + 0x240) = result;
    if ((*(uint64_t *)(0 + 0x28)) >= 0xFF000ULL) {
    }
    if (1 != 0) goto loc_005EA6E8;
    local_r15 = (v_stack_m58) + (v_stack_p8);
    local_rsi = (v_stack_p18) << (4);
    *(uint16_t *)(local_r15 + 0xC) = (uint16_t)(*(uint16_t *)(arg1 + 0x8C));
    Arg1 = (v_stack_m58) + (v_stack_p8);
    if ((local_rsi + result * 1) == Arg1) goto loc_005EA4DB;
    *(uint8_t *)(local_r15 + 0xF) = 0;
    *(uint8_t *)(local_r15 + 0xA) = 0;
    local_rsi = (local_rsi) - (v_stack_p8);
    local_rsi = (local_rsi) >> (4);
    *(uint16_t *)(local_r15 + 0x8) = (uint16_t)(local_rsi);
    if ((*(uint32_t *)(v_rip + 0x87D6F4)) < 1) goto loc_005EA48A;
    result = 1;
    if (((uint16_t)(local_rsi)) <= 1) {
        Arg1 = v_rip + 926961;
        result = DbgPrint(Arg1, local_rsi + result * 1, Arg3, v_stack_m48);
        result = RtlpHeapHandleError(Arg1, local_rsi + result * 1, Arg3, v_stack_m48);
    }
    *(uint8_t *)(local_r15 + 0xB) = 0;
    if ((*(uint64_t *)(arg1 + 0x28)) == Arg1) goto loc_005EA4CA;
    local_rsi = (local_r15) - (Arg1);
    local_rsi = (local_rsi) >> (16);
    local_rsi = (local_rsi) + 1;
    if (local_rsi >= 254) {
        v_stack_m60 = 0;
        a4 = Arg1;
        Arg3 = local_r15;
        v_stack_m68 = 0;
        Arg1 = 3;
        result = RtlpLogHeapFailure(Arg1, *(uint64_t *)(arg1 + 0x28), Arg3, a4);
    }
loc_005EA4CA:
    *(uint8_t *)(local_r15 + 0xE) = (uint8_t)((uint8_t)(local_rsi));
    goto loc_005EA6E0;
loc_005EA4DB:
    if ((*(uint32_t *)(arg1 + 0x7C)) == ((uint32_t)((uint8_t)(local_rsi)))) goto loc_005EA6E8;
    Arg1 = (uint8_t)((*(uint8_t *)(local_r15 + 0xA)) ^ (*(uint8_t *)(local_r15 + 0x9)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(local_r15 + 0x8)));
    *(uint8_t *)(local_r15 + 0xB) = (uint8_t)(Arg1);
    goto loc_005EA6E8;
loc_005EA503:
    Arg2 = (result + 4159) & (0xFFFFFFFFFFFFF000ULL);
    v_stack_m58 = Arg2;
    if (Arg2 == (result + 80)) {
        Arg2 = (Arg2) + (0x1000ULL);
        v_stack_m58 = Arg2;
    }
    Arg1 = (local_rsi) << (4);
    if ((uint8_t)(local_r15) == 0) {
        Arg1 = (Arg1) + (-32);
    }
    Arg1 = (Arg1) + (result);
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    if (Arg1 < Arg2) goto loc_005EA6B5;
    Arg1 = (Arg1) - (Arg2);
    v_stack_p8 = Arg1;
    if ((*(uint8_t *)(0 + 0xF)) == 3) goto loc_005EA571;
    if (Arg1 == NULL) goto loc_005EA350;
    if (Arg1 >= (*(uint64_t *)(arg1 + 0xB0))) goto loc_005EA576;
    goto loc_005EA350;
loc_005EA571:
    if (Arg1 == NULL) goto loc_005EA59C;
loc_005EA576:
    Arg1 = (Arg1) | (-1);
    result = ZwFreeVirtualMemory(Arg1, v_stack_m58, v_stack_p8, (uint32_t)(0x4000ULL));
    if (sign_flag) goto loc_005EA376;
loc_005EA59C:
    if ((uint8_t)(local_r15) != 0) goto loc_005EA687;
    local_r15 = (v_stack_p8) + (v_stack_m58);
    local_rsi = (local_rsi) << (4);
    *(uint16_t *)(local_r15 + 0xC) = (uint16_t)(*(uint16_t *)(arg1 + 0x8C));
    Arg1 = (v_stack_m58) + (v_stack_p8);
    if ((local_rsi + result * 1) == Arg1) goto loc_005EA668;
    *(uint8_t *)(local_r15 + 0xF) = (uint8_t)((uint8_t)(local_rsi));
    *(uint8_t *)(local_r15 + 0xA) = (uint8_t)((uint8_t)(local_rsi));
    local_rsi = (local_rsi) - (v_stack_p8);
    local_rsi = (local_rsi) - (v_stack_m58);
    local_rsi = (local_rsi) + (result);
    local_rsi = (local_rsi) >> (4);
    *(uint16_t *)(local_r15 + 0x8) = (uint16_t)(local_rsi);
    if ((*(uint32_t *)(v_rip + 0x87D56C)) < 1) goto loc_005EA612;
    result = 1;
    if (((uint16_t)(local_rsi)) <= 1) {
        Arg1 = v_rip + 926953;
        result = DbgPrint(Arg1, local_rsi + result * 1, v_stack_p8, (uint32_t)(0x4000ULL));
        result = RtlpHeapHandleError(Arg1, local_rsi + result * 1, v_stack_p8, (uint32_t)(0x4000ULL));
    }
    *(uint8_t *)(local_r15 + 0xB) = (uint8_t)((uint8_t)(local_rsi));
    if ((*(uint64_t *)(arg1 + 0x28)) == Arg1) goto loc_005EA652;
    local_rsi = (local_r15) - (Arg1);
    local_rsi = (local_rsi) >> (16);
    local_rsi = (local_rsi) + 1;
    if (local_rsi >= 254) {
        v_stack_m60 = (uint8_t)(local_rsi);
        a4 = Arg1;
        Arg3 = local_r15;
        v_stack_m68 = (uint8_t)(local_rsi);
        Arg1 = 3;
        result = RtlpLogHeapFailure(Arg1, *(uint64_t *)(arg1 + 0x28), Arg3, a4);
    }
loc_005EA652:
    *(uint8_t *)(local_r15 + 0xE) = (uint8_t)((uint8_t)(local_rsi));
    result = RtlpInsertFreeBlock(Arg1, local_r15, *(uint16_t *)(local_r15 + 0x8), a4);
    goto loc_005EA687;
loc_005EA668:
    if ((*(uint32_t *)(arg1 + 0x7C)) != ((uint32_t)((uint8_t)(local_rsi)))) {
        Arg1 = *(uint8_t *)(local_r15 + 0xA);
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(local_r15 + 0x9)));
        Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(local_r15 + 0x8)));
        *(uint8_t *)(local_r15 + 0xB) = (uint8_t)(Arg1);
        result = *(uint32_t *)(arg1 + 0x88);
    }
    Arg3 = (v_stack_m58) + (-48);
    v_stack_m60 = v_stack_m40;
    v_stack_m68 = result;
    result = RtlpCreateUCREntry(Arg1, Arg1, Arg3, v_stack_p8);
    goto loc_005EA353;
loc_005EA6B5:
    if ((*(uint32_t *)(v_rip + 0x87D4A4)) < ((uint32_t)(v_stack_p8))) goto loc_005EA350;
    if ((uint8_t)(local_r15) == 0) goto loc_005EA350;
    result = DbgPrint(v_rip + 926398, Arg1, v_stack_m40, v_stack_p8);
    result = RtlpHeapHandleError(v_rip + 926398, Arg1, v_stack_m40, v_stack_p8);
loc_005EA6DD:
loc_005EA6E0:
loc_005EA6E3:
    result = RtlpInsertFreeBlock(Arg1, Arg1, v_stack_m40, v_stack_p8);
loc_005EA6E8:
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x8C` | `16` | `R` |
| `Arg1` | `+ 0xB0` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0x168` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `W` |
| `Arg1` | `+ 0x248` | `64` | `R/W` |
| `Arg1` | `+ 0x264` | `32` | `R/W` |
| `Arg1` | `+ 0x26C` | `32` | `R/W` |
| `Arg1` | `+ 0x2B8` | `32` | `R` |
| `Arg2` | `+ 0xE` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005EA158&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
