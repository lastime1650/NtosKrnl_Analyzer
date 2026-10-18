# ExpWorkerThread

- RVA: `0x004ECAF0`–`0x004ED1F7` (길이 `1,799` bytes)
- VA: `0x00000001404ECAF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D54BC`
- 디코드: `441`개 명령, `1,799/1,799` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **15**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x004ECB39` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004ECBC6` → [KeRemovePriQueue](../3C/KeRemovePriQueue_function_003C5090.md) (function, `0x003C5090`)
- `0x004ECC68` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x004ECC82` → [Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline](../65/Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline_function_0065AA88.md) (function, `0x0065AA88`)
- `0x004ECD65` → [EtwTraceThreadWorkItem](../4D/EtwTraceThreadWorkItem_function_004DC3D0.md) (function, `0x004DC3D0`)
- `0x004ECD70` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004ECD7D` → [EtwTraceThreadWorkItem](../4D/EtwTraceThreadWorkItem_function_004DC3D0.md) (function, `0x004DC3D0`)
- `0x004ECD8A` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004ECD9B` → [KxReenterRetpolinedCode](../44/KxReenterRetpolinedCode_function_0044EE64.md) (function, `0x0044EE64`)
- `0x004ECEC9` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x004ECEDB` → [KeRevertToUserGroupAffinityThread](../39/KeRevertToUserGroupAffinityThread_function_00398EC0.md) (function, `0x00398EC0`)
- `0x004ECEF6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004ECF0B` → [KeQueryNodeActiveAffinityEx](../25/KeQueryNodeActiveAffinityEx_function_00256740.md) (function, `0x00256740`)
- `0x004ECF8D` → [KeSetUserAffinityThread](../2C/KeSetUserAffinityThread_function_002CFA2C.md) (function, `0x002CFA2C`)
- `0x004ECFB4` → [DbgPrintEx](../35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x004ED078` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x004ED088` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004ED0C3` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED0CC` → [PsGetIoPriorityThread](../34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x004ED0E4` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED102` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED121` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED12A` → [PsGetPagePriorityThread](../3C/PsGetPagePriorityThread_function_003C3E80.md) (function, `0x003C3E80`)
- `0x004ED142` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED15B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED181` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED19A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED1B8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED1D8` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004ED1F1` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004ECB0F` → RVA `0x00E0A740` (`.data`; read)
- `0x004ECB8E` → RVA `0x00EFA958` (`.data`; read)
- `0x004ECC8F` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)
- `0x004ECCBC` → RVA `0x000110F8` (`.rdata`; read)
- `0x004ECCE9` → RVA `0x00E0EBDC` (`.data`; read)
- `0x004ECD0B` → RVA `0x00EFA910` (`.data`; read)
- `0x004ECD51` → RVA `0x00FC6B08` (`ALMOSTRO`; read)
- `0x004ECEB6` → RVA `0x00B4DB40` (`ExpWorkerSystemAffinityActiveMessage`; read)
- `0x004ECFA1` → RVA `0x00B4DA80` (`ExpWorkerActivityIdSetMessage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004ECAF0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
004ECAF5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
004ECAFA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
004ECAFF  57                              push rdi
004ECB00  41 54                           push r12
004ECB02  41 55                           push r13
004ECB04  41 56                           push r14
004ECB06  41 57                           push r15
004ECB08  48 81 EC 80 01 00 00            sub rsp, 0x180
004ECB0F  48 8B 05 2A DC 91 00            mov rax, qword ptr [rip + 0x91dc2a]
004ECB16  48 33 C4                        xor rax, rsp
004ECB19  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
004ECB21  48 8B E9                        mov rbp, rcx
004ECB24  0F 57 C0                        xorps xmm0, xmm0
004ECB27  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
004ECB2C  33 D2                           xor edx, edx
004ECB2E  41 B8 08 01 00 00               mov r8d, 0x108
004ECB34  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
004ECB39  E8 02 A1 1D 00                  call 0x1406c6c40
004ECB3E  65 48 8B 34 25 88 01 00 00      mov rsi, qword ptr gs:[0x188]
004ECB47  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
004ECB4C  4C 8B BD B8 02 00 00            mov r15, qword ptr [rbp + 0x2b8]
004ECB53  33 C0                           xor eax, eax
004ECB55  4C 8B AD B0 02 00 00            mov r13, qword ptr [rbp + 0x2b0]
004ECB5C  41 B4 01                        mov r12b, 1
004ECB5F  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004ECB64  8B 86 A4 05 00 00               mov eax, dword ptr [rsi + 0x5a4]
004ECB6A  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
004ECB6F  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
004ECB74  41 84 C4                        test r12b, al
004ECB77  74 07                           je 0x1404ecb80
004ECB79  B9 38 00 00 00                  mov ecx, 0x38
004ECB7E  CD 29                           int 0x29
004ECB80  83 C8 01                        or eax, 1
004ECB83  89 86 A4 05 00 00               mov dword ptr [rsi + 0x5a4], eax
004ECB89  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
004ECB8E  80 3D C3 DD A0 00 00            cmp byte ptr [rip + 0xa0ddc3], 0
004ECB95  75 1A                           jne 0x1404ecbb1
004ECB97  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004ECBA0  8B 41 78                        mov eax, dword ptr [rcx + 0x78]
004ECBA3  C1 E8 06                        shr eax, 6
004ECBA6  41 84 C4                        test r12b, al
004ECBA9  74 06                           je 0x1404ecbb1
004ECBAB  F0 0F BA 71 78 06               lock btr dword ptr [rcx + 0x78], 6
004ECBB1  48 8D 9D C8 02 00 00            lea rbx, [rbp + 0x2c8]
004ECBB8  4C 8B CA                        mov r9, rdx
004ECBBB  45 33 C0                        xor r8d, r8d
004ECBBE  33 D2                           xor edx, edx
004ECBC0  48 8B CD                        mov rcx, rbp
004ECBC3  48 8B FB                        mov rdi, rbx
004ECBC6  E8 C5 84 ED FF                  call 0x1403c5090
004ECBCB  4C 8B F0                        mov r14, rax
004ECBCE  45 84 E4                        test r12b, r12b
004ECBD1  74 2F                           je 0x1404ecc02
004ECBD3  45 32 E4                        xor r12b, r12b
004ECBD6  48 8D 9D C8 02 00 00            lea rbx, [rbp + 0x2c8]
004ECBDD  44 88 A5 D0 02 00 00            mov byte ptr [rbp + 0x2d0], r12b
004ECBE4  F0 81 23 FF BF FF FF            lock and dword ptr [rbx], 0xffffbfff
004ECBEB  33 C0                           xor eax, eax
004ECBED  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004ECBF2  8B D0                           mov edx, eax
004ECBF4  49 81 FE 02 01 00 00            cmp r14, 0x102
004ECBFB  74 BB                           je 0x1404ecbb8
004ECBFD  48 8B C3                        mov rax, rbx
004ECC00  EB 13                           jmp 0x1404ecc15
004ECC02  48 8B C3                        mov rax, rbx
004ECC05  48 8B DF                        mov rbx, rdi
004ECC08  49 81 FE 02 01 00 00            cmp r14, 0x102
004ECC0F  0F 84 CA 03 00 00               je 0x1404ecfdf
004ECC15  48 8B D8                        mov rbx, rax
004ECC18  49 81 FE 80 00 00 00            cmp r14, 0x80
004ECC1F  0F 84 BA 03 00 00               je 0x1404ecfdf
004ECC25  8B 85 CC 02 00 00               mov eax, dword ptr [rbp + 0x2cc]
004ECC2B  8B 0B                           mov ecx, dword ptr [rbx]
004ECC2D  0F B6 95 D0 02 00 00            movzx edx, byte ptr [rbp + 0x2d0]
004ECC34  3B C8                           cmp ecx, eax
004ECC36  7C 1B                           jl 0x1404ecc53
004ECC38  3B 8D D4 02 00 00               cmp ecx, dword ptr [rbp + 0x2d4]
004ECC3E  7D 2D                           jge 0x1404ecc6d
004ECC40  48 8D 45 08                     lea rax, [rbp + 8]
004ECC44  48 39 00                        cmp qword ptr [rax], rax
004ECC47  75 24                           jne 0x1404ecc6d
004ECC49  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
004ECC4D  75 04                           jne 0x1404ecc53
004ECC4F  84 D2                           test dl, dl
004ECC51  74 1A                           je 0x1404ecc6d
004ECC53  41 0F B7 0F                     movzx ecx, word ptr [r15]
004ECC57  45 33 C0                        xor r8d, r8d
004ECC5A  49 8B 45 10                     mov rax, qword ptr [r13 + 0x10]
004ECC5E  33 D2                           xor edx, edx
004ECC60  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
004ECC64  48 83 C1 10                     add rcx, 0x10
004ECC68  E8 A3 26 E5 FF                  call 0x14033f310
004ECC6D  F0 FF 85 C0 02 00 00            lock inc dword ptr [rbp + 0x2c0]
004ECC74  49 8B 7E 10                     mov rdi, qword ptr [r14 + 0x10]
004ECC78  4D 8B 7E 18                     mov r15, qword ptr [r14 + 0x18]
004ECC7C  8B 9D D8 02 00 00               mov ebx, dword ptr [rbp + 0x2d8]
004ECC82  E8 01 DE 16 00                  call 0x14065aa88
004ECC87  85 C0                           test eax, eax
004ECC89  0F 84 C0 00 00 00               je 0x1404ecd4f
004ECC8F  48 8B 05 0A A2 AD 00            mov rax, qword ptr [rip + 0xada20a]
004ECC96  49 39 45 00                     cmp qword ptr [r13], rax
004ECC9A  0F 85 AF 00 00 00               jne 0x1404ecd4f
004ECCA0  83 FB 01                        cmp ebx, 1
004ECCA3  0F 85 A6 00 00 00               jne 0x1404ecd4f
004ECCA9  49 63 46 54                     movsxd rax, dword ptr [r14 + 0x54]
004ECCAD  4C 8B 95 E8 02 00 00            mov r10, qword ptr [rbp + 0x2e8]
004ECCB4  83 F8 07                        cmp eax, 7
004ECCB7  73 10                           jae 0x1404eccc9
004ECCB9  0F AE E8                        lfence
004ECCBC  48 8D 0D 35 44 B2 FF            lea rcx, [rip - 0x4dbbcb]
004ECCC3  44 8B 0C 81                     mov r9d, dword ptr [rcx + rax*4]
004ECCC7  EB 04                           jmp 0x1404ecccd
004ECCC9  44 8D 48 E0                     lea r9d, [rax - 0x20]
004ECCCD  49 63 C1                        movsxd rax, r9d
004ECCD0  33 DB                           xor ebx, ebx
004ECCD2  F0 49 FF 4C C2 10               lock dec qword ptr [r10 + rax*8 + 0x10]
004ECCD8  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
004ECCE2  49 8B 4E 58                     mov rcx, qword ptr [r14 + 0x58]
004ECCE6  48 8B D0                        mov rdx, rax
004ECCE9  44 8B 05 EC 1E 92 00            mov r8d, dword ptr [rip + 0x921eec]
004ECCF0  48 2B D1                        sub rdx, rcx
004ECCF3  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
004ECCFD  48 F7 E2                        mul rdx
004ECD00  8B C3                           mov eax, ebx
004ECD02  48 C1 EA 0B                     shr rdx, 0xb
004ECD06  45 85 C0                        test r8d, r8d
004ECD09  74 1E                           je 0x1404ecd29
004ECD0B  48 8B 0D FE DB A0 00            mov rcx, qword ptr [rip + 0xa0dbfe]
004ECD12  48 3B 11                        cmp rdx, qword ptr [rcx]
004ECD15  72 0D                           jb 0x1404ecd24
004ECD17  FF C0                           inc eax
004ECD19  48 83 C1 08                     add rcx, 8
004ECD1D  41 3B C0                        cmp eax, r8d
004ECD20  72 F0                           jb 0x1404ecd12
004ECD22  EB 05                           jmp 0x1404ecd29
004ECD24  41 3B C0                        cmp eax, r8d
004ECD27  72 04                           jb 0x1404ecd2d
004ECD29  41 8D 40 FF                     lea eax, [r8 - 1]
004ECD2D  45 0F AF C8                     imul r9d, r8d
004ECD31  44 03 C8                        add r9d, eax
004ECD34  49 8B 02                        mov rax, qword ptr [r10]
004ECD37  4A 8D 14 CD 00 00 00 00         lea rdx, [r9*8]
004ECD3F  48 8B 0C 02                     mov rcx, qword ptr [rdx + rax]
004ECD43  49 8B 02                        mov rax, qword ptr [r10]
004ECD46  48 FF C1                        inc rcx
004ECD49  48 89 0C 02                     mov qword ptr [rdx + rax], rcx
004ECD4D  EB 02                           jmp 0x1404ecd51
004ECD4F  33 DB                           xor ebx, ebx
004ECD51  F7 05 AD 9D AD 00 00 00 00 08   test dword ptr [rip + 0xad9dad], 0x8000000
004ECD5B  74 27                           je 0x1404ecd84
004ECD5D  BA 40 05 00 00                  mov edx, 0x540
004ECD62  48 8B CF                        mov rcx, rdi
004ECD65  E8 66 F6 FE FF                  call 0x1404dc3d0
004ECD6A  49 8B CF                        mov rcx, r15
004ECD6D  48 8B C7                        mov rax, rdi
004ECD70  E8 5B DD 1C 00                  call 0x1406baad0
004ECD75  BA 41 05 00 00                  mov edx, 0x541
004ECD7A  48 8B CF                        mov rcx, rdi
004ECD7D  E8 4E F6 FE FF                  call 0x1404dc3d0
004ECD82  EB 0B                           jmp 0x1404ecd8f
004ECD84  49 8B CF                        mov rcx, r15
004ECD87  48 8B C7                        mov rax, rdi
004ECD8A  E8 41 DD 1C 00                  call 0x1406baad0
004ECD8F  65 8A 04 25 5E 08 00 00         mov al, byte ptr gs:[0x85e]
004ECD97  A8 01                           test al, 1
004ECD99  74 05                           je 0x1404ecda0
004ECD9B  E8 C4 20 F6 FF                  call 0x14044ee64
004ECDA0  48 8D 86 08 03 00 00            lea rax, [rsi + 0x308]
004ECDA7  48 39 00                        cmp qword ptr [rax], rax
004ECDAA  0F 85 2E 04 00 00               jne 0x1404ed1de
004ECDB0  8B 86 E4 01 00 00               mov eax, dword ptr [rsi + 0x1e4]
004ECDB6  85 C0                           test eax, eax
004ECDB8  0F 85 00 04 00 00               jne 0x1404ed1be
004ECDBE  44 0F 20 C0                     mov rax, cr8
004ECDC2  84 C0                           test al, al
004ECDC4  0F 85 D6 03 00 00               jne 0x1404ed1a0
004ECDCA  8B 86 A0 05 00 00               mov eax, dword ptr [rsi + 0x5a0]
004ECDD0  A8 08                           test al, 8
004ECDD2  0F 85 AF 03 00 00               jne 0x1404ed187
004ECDD8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004ECDE1  80 B8 4A 02 00 00 01            cmp byte ptr [rax + 0x24a], 1
004ECDE8  0F 84 73 03 00 00               je 0x1404ed161
004ECDEE  48 8B 86 98 06 00 00            mov rax, qword ptr [rsi + 0x698]
004ECDF5  48 83 F8 FD                     cmp rax, -3
004ECDF9  0F 85 49 03 00 00               jne 0x1404ed148
004ECDFF  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
004ECE06  8B 8E A0 05 00 00               mov ecx, dword ptr [rsi + 0x5a0]
004ECE0C  C1 E9 09                        shr ecx, 9
004ECE0F  83 E1 07                        and ecx, 7
004ECE12  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
004ECE19  48 85 C0                        test rax, rax
004ECE1C  74 0B                           je 0x1404ece29
004ECE1E  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
004ECE24  3B C8                           cmp ecx, eax
004ECE26  0F 4D C8                        cmovge ecx, eax
004ECE29  83 F9 02                        cmp ecx, 2
004ECE2C  7D 21                           jge 0x1404ece4f
004ECE2E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004ECE37  48 3B F0                        cmp rsi, rax
004ECE3A  0F 85 89 02 00 00               jne 0x1404ed0c9
004ECE40  83 BE E0 05 00 00 00            cmp dword ptr [rsi + 0x5e0], 0
004ECE47  0F 84 7C 02 00 00               je 0x1404ed0c9
004ECE4D  EB 06                           jmp 0x1404ece55
004ECE4F  0F 85 74 02 00 00               jne 0x1404ed0c9
004ECE55  48 8B 86 20 02 00 00            mov rax, qword ptr [rsi + 0x220]
004ECE5C  8B 8E A0 05 00 00               mov ecx, dword ptr [rsi + 0x5a0]
004ECE62  C1 E9 0C                        shr ecx, 0xc
004ECE65  83 E1 07                        and ecx, 7
004ECE68  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
004ECE6F  48 85 C0                        test rax, rax
004ECE72  74 0B                           je 0x1404ece7f
004ECE74  8B 80 44 04 00 00               mov eax, dword ptr [rax + 0x444]
004ECE7A  3B C8                           cmp ecx, eax
004ECE7C  0F 43 C8                        cmovae ecx, eax
004ECE7F  83 F9 05                        cmp ecx, 5
004ECE82  0F 85 9F 02 00 00               jne 0x1404ed127
004ECE88  8B 86 A8 05 00 00               mov eax, dword ptr [rsi + 0x5a8]
004ECE8E  0F BA E0 08                     bt eax, 8
004ECE92  0F 82 70 02 00 00               jb 0x1404ed108
004ECE98  44 8B 86 A4 05 00 00            mov r8d, dword ptr [rsi + 0x5a4]
004ECE9F  41 0F BA E0 0B                  bt r8d, 0xb
004ECEA4  0F 82 40 02 00 00               jb 0x1404ed0ea
004ECEAA  8B 46 74                        mov eax, dword ptr [rsi + 0x74]
004ECEAD  A8 08                           test al, 8
004ECEAF  74 2F                           je 0x1404ecee0
004ECEB1  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
004ECEB6  4C 8D 05 83 0C 66 00            lea r8, [rip + 0x660c83]
004ECEBD  4C 8B CF                        mov r9, rdi
004ECEC0  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
004ECEC5  33 D2                           xor edx, edx
004ECEC7  33 C9                           xor ecx, ecx
004ECEC9  E8 C2 C3 E6 FF                  call 0x140359290
004ECECE  0F 57 C0                        xorps xmm0, xmm0
004ECED1  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
004ECED6  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
004ECEDB  E8 E0 BF EA FF                  call 0x140398ec0
004ECEE0  33 D2                           xor edx, edx
004ECEE2  48 C7 44 24 60 01 00 20 00      mov qword ptr [rsp + 0x60], 0x200001
004ECEEB  41 B8 00 01 00 00               mov r8d, 0x100
004ECEF1  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
004ECEF6  E8 45 9D 1D 00                  call 0x1406c6c40
004ECEFB  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
004ECF00  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
004ECF05  45 33 C0                        xor r8d, r8d
004ECF08  0F B7 09                        movzx ecx, word ptr [rcx]
004ECF0B  E8 30 98 D6 FF                  call 0x140256740
004ECF10  4C 8B 8E 28 02 00 00            mov r9, qword ptr [rsi + 0x228]
004ECF17  44 0F B7 44 24 60               movzx r8d, word ptr [rsp + 0x60]
004ECF1D  41 0F B7 01                     movzx eax, word ptr [r9]
004ECF21  66 44 3B C0                     cmp r8w, ax
004ECF25  73 05                           jae 0x1404ecf2c
004ECF27  4D 8B D1                        mov r10, r9
004ECF2A  EB 09                           jmp 0x1404ecf35
004ECF2C  4C 8D 54 24 60                  lea r10, [rsp + 0x60]
004ECF31  44 0F B7 C0                     movzx r8d, ax
004ECF35  0F B7 C3                        movzx eax, bx
004ECF38  66 41 3B D8                     cmp bx, r8w
004ECF3C  73 22                           jae 0x1404ecf60
004ECF3E  66 90                           nop
004ECF40  0F B7 C8                        movzx ecx, ax
004ECF43  48 8D 14 CD 00 00 00 00         lea rdx, [rcx*8]
004ECF4B  49 8B 4C C9 08                  mov rcx, qword ptr [r9 + rcx*8 + 8]
004ECF50  48 39 4C 14 68                  cmp qword ptr [rsp + rdx + 0x68], rcx
004ECF55  75 2E                           jne 0x1404ecf85
004ECF57  66 FF C0                        inc ax
004ECF5A  66 41 3B C0                     cmp ax, r8w
004ECF5E  72 E0                           jb 0x1404ecf40
004ECF60  41 0F B7 12                     movzx edx, word ptr [r10]
004ECF64  66 3B C2                        cmp ax, dx
004ECF67  73 29                           jae 0x1404ecf92
004ECF69  0F 1F 80 00 00 00 00            nop dword ptr [rax]
004ECF70  0F B7 C8                        movzx ecx, ax
004ECF73  49 83 7C CA 08 00               cmp qword ptr [r10 + rcx*8 + 8], 0
004ECF79  75 0A                           jne 0x1404ecf85
004ECF7B  66 FF C0                        inc ax
004ECF7E  66 3B C2                        cmp ax, dx
004ECF81  72 ED                           jb 0x1404ecf70
004ECF83  EB 0D                           jmp 0x1404ecf92
004ECF85  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
004ECF8A  48 8B CE                        mov rcx, rsi
004ECF8D  E8 9A 2A DE FF                  call 0x1402cfa2c
004ECF92  48 83 BE 30 06 00 00 00         cmp qword ptr [rsi + 0x630], 0
004ECF9A  74 2D                           je 0x1404ecfc9
004ECF9C  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
004ECFA1  4C 8D 05 D8 0A 66 00            lea r8, [rip + 0x660ad8]
004ECFA8  4C 8B CF                        mov r9, rdi
004ECFAB  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
004ECFB0  33 D2                           xor edx, edx
004ECFB2  33 C9                           xor ecx, ecx
004ECFB4  E8 D7 C2 E6 FF                  call 0x140359290
004ECFB9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004ECFC2  48 89 98 30 06 00 00            mov qword ptr [rax + 0x630], rbx
004ECFC9  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
004ECFCE  48 8D 9D C8 02 00 00            lea rbx, [rbp + 0x2c8]
004ECFD5  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
004ECFDA  E9 D9 FB FF FF                  jmp 0x1404ecbb8
004ECFDF  8B 03                           mov eax, dword ptr [rbx]
004ECFE1  0F BA E0 0F                     bt eax, 0xf
004ECFE5  72 12                           jb 0x1404ecff9
004ECFE7  48 8D 86 40 05 00 00            lea rax, [rsi + 0x540]
004ECFEE  48 39 00                        cmp qword ptr [rax], rax
004ECFF1  75 E2                           jne 0x1404ecfd5
004ECFF3  83 7D 04 00                     cmp dword ptr [rbp + 4], 0
004ECFF7  75 DC                           jne 0x1404ecfd5
004ECFF9  0F 0D 0B                        prefetchw byte ptr [rbx]
004ECFFC  8B 85 C8 02 00 00               mov eax, dword ptr [rbp + 0x2c8]
004ED002  8B D0                           mov edx, eax
004ED004  44 8B C0                        mov r8d, eax
004ED007  81 E2 FF 3F 00 00               and edx, 0x3fff
004ED00D  FF CA                           dec edx
004ED00F  0F BA E0 0F                     bt eax, 0xf
004ED013  72 0E                           jb 0x1404ed023
004ED015  0F BA E0 0E                     bt eax, 0xe
004ED019  72 BA                           jb 0x1404ecfd5
004ED01B  3B 95 CC 02 00 00               cmp edx, dword ptr [rbp + 0x2cc]
004ED021  7C B2                           jl 0x1404ecfd5
004ED023  8B C8                           mov ecx, eax
004ED025  81 E1 00 C0 FF FF               and ecx, 0xffffc000
004ED02B  0B D1                           or edx, ecx
004ED02D  F0 0F B1 13                     lock cmpxchg dword ptr [rbx], edx
004ED031  41 3B C0                        cmp eax, r8d
004ED034  75 CC                           jne 0x1404ed002
004ED036  48 8D 86 40 05 00 00            lea rax, [rsi + 0x540]
004ED03D  48 39 00                        cmp qword ptr [rax], rax
004ED040  75 6D                           jne 0x1404ed0af
004ED042  83 A6 A4 05 00 00 FE            and dword ptr [rsi + 0x5a4], 0xfffffffe
004ED049  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
004ED052  41 8B 40 78                     mov eax, dword ptr [r8 + 0x78]
004ED056  C1 E8 06                        shr eax, 6
004ED059  A8 01                           test al, 1
004ED05B  75 07                           jne 0x1404ed064
004ED05D  F0 41 0F BA 68 78 06            lock bts dword ptr [r8 + 0x78], 6
004ED064  81 FA 00 80 00 00               cmp edx, 0x8000
004ED06A  75 11                           jne 0x1404ed07d
004ED06C  48 8B 8D E0 02 00 00            mov rcx, qword ptr [rbp + 0x2e0]
004ED073  45 33 C0                        xor r8d, r8d
004ED076  33 D2                           xor edx, edx
004ED078  E8 93 22 E5 FF                  call 0x14033f310
004ED07D  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
004ED085  48 33 CC                        xor rcx, rsp
004ED088  E8 B3 F5 1B 00                  call 0x1406ac640
004ED08D  4C 8D 9C 24 80 01 00 00         lea r11, [rsp + 0x180]
004ED095  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
004ED099  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
004ED09D  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
004ED0A1  49 8B E3                        mov rsp, r11
004ED0A4  41 5F                           pop r15
004ED0A6  41 5E                           pop r14
004ED0A8  41 5D                           pop r13
004ED0AA  41 5C                           pop r12
004ED0AC  5F                              pop rdi
004ED0AD  C3                              ret
004ED0AE  CC                              int3
004ED0AF  33 C0                           xor eax, eax
004ED0B1  45 33 C9                        xor r9d, r9d
004ED0B4  4C 8B C6                        mov r8, rsi
004ED0B7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004ED0BC  33 D2                           xor edx, edx
004ED0BE  B9 D2 01 00 00                  mov ecx, 0x1d2
004ED0C3  E8 98 05 01 00                  call 0x1404fd660
004ED0C8  CC                              int3
004ED0C9  48 8B CE                        mov rcx, rsi
004ED0CC  E8 5F 68 E5 FF                  call 0x140343930
004ED0D1  4C 63 C0                        movsxd r8, eax
004ED0D4  48 8B D7                        mov rdx, rdi
004ED0D7  B9 28 01 00 00                  mov ecx, 0x128
004ED0DC  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004ED0E1  4D 8B CF                        mov r9, r15
004ED0E4  E8 77 05 01 00                  call 0x1404fd660
004ED0E9  CC                              int3
004ED0EA  49 C1 E8 0B                     shr r8, 0xb
004ED0EE  4D 8B CF                        mov r9, r15
004ED0F1  41 83 E0 01                     and r8d, 1
004ED0F5  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004ED0FA  48 8B D7                        mov rdx, rdi
004ED0FD  B9 D6 01 00 00                  mov ecx, 0x1d6
004ED102  E8 59 05 01 00                  call 0x1404fd660
004ED107  CC                              int3
004ED108  C1 E8 09                        shr eax, 9
004ED10B  4D 8B CF                        mov r9, r15
004ED10E  83 E0 07                        and eax, 7
004ED111  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004ED116  44 8B C0                        mov r8d, eax
004ED119  48 8B D7                        mov rdx, rdi
004ED11C  B9 5B 01 00 00                  mov ecx, 0x15b
004ED121  E8 3A 05 01 00                  call 0x1404fd660
004ED126  CC                              int3
004ED127  48 8B CE                        mov rcx, rsi
004ED12A  E8 51 6D ED FF                  call 0x1403c3e80
004ED12F  44 8B C0                        mov r8d, eax
004ED132  B9 29 01 00 00                  mov ecx, 0x129
004ED137  4D 8B CF                        mov r9, r15
004ED13A  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004ED13F  48 8B D7                        mov rdx, rdi
004ED142  E8 19 05 01 00                  call 0x1404fd660
004ED147  CC                              int3
004ED148  4D 8B CE                        mov r9, r14
004ED14B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED150  4D 8B C7                        mov r8, r15
004ED153  48 8B D7                        mov rdx, rdi
004ED156  B9 9A 01 00 00                  mov ecx, 0x19a
004ED15B  E8 00 05 01 00                  call 0x1404fd660
004ED160  CC                              int3
004ED161  44 0F B6 8E 4A 02 00 00         movzx r9d, byte ptr [rsi + 0x24a]
004ED169  B9 05 00 00 00                  mov ecx, 5
004ED16E  4C 8B 86 B8 00 00 00            mov r8, qword ptr [rsi + 0xb8]
004ED175  48 8B 96 20 02 00 00            mov rdx, qword ptr [rsi + 0x220]
004ED17C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
004ED181  E8 DA 04 01 00                  call 0x1404fd660
004ED186  CC                              int3
004ED187  4D 8B CE                        mov r9, r14
004ED18A  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED18F  4D 8B C7                        mov r8, r15
004ED192  48 8B D7                        mov rdx, rdi
004ED195  B9 DF 00 00 00                  mov ecx, 0xdf
004ED19A  E8 C1 04 01 00                  call 0x1404fd660
004ED19F  CC                              int3
004ED1A0  44 0F 20 C0                     mov rax, cr8
004ED1A4  44 0F B6 C0                     movzx r8d, al
004ED1A8  4D 8B CF                        mov r9, r15
004ED1AB  48 8B D7                        mov rdx, rdi
004ED1AE  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004ED1B3  B9 E1 00 00 00                  mov ecx, 0xe1
004ED1B8  E8 A3 04 01 00                  call 0x1404fd660
004ED1BD  CC                              int3
004ED1BE  44 0F B6 86 4A 02 00 00         movzx r8d, byte ptr [rsi + 0x24a]
004ED1C6  4C 8B C8                        mov r9, rax
004ED1C9  B8 01 00 00 00                  mov eax, 1
004ED1CE  48 8B D7                        mov rdx, rdi
004ED1D1  8B C8                           mov ecx, eax
004ED1D3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004ED1D8  E8 83 04 01 00                  call 0x1404fd660
004ED1DD  CC                              int3
004ED1DE  4D 8B CE                        mov r9, r14
004ED1E1  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004ED1E6  4D 8B C7                        mov r8, r15
004ED1E9  48 8B D7                        mov rdx, rdi
004ED1EC  B9 39 00 00 00                  mov ecx, 0x39
004ED1F1  E8 6A 04 01 00                  call 0x1404fd660
004ED1F6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWorkerThread(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (384);
    result = (*(unsigned __int64 *)(v_rip + 9559082)) ^ (v_rsp);
    v_stack_m38 = result;
    a2 = 0;
    v_stack_m160 = v_xmm0;
    result = memset(v_stack_m148, a2, 264, a4);
    result = 0;
    v_stack_m168 = 0;
    v_stack_m178 = v_stack_m168;
    v_stack_m170 = *(unsigned __int64 *)(a1 + 696);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))))) != 0) {
        a1 = 56;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))) | (1));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444) = (unsigned int)(result);
    if ((*(unsigned __int8 *)(v_rip + 10542531)) != 0) goto loc_004ECBB1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120))) >> (6));
    if (((1) & ((unsigned __int8)(result))) != 0) {
    }
loc_004ECBB8:
    a3 = 0;
    a2 = 0;
    result = KeRemovePriQueue(a1, a2, a3, v_stack_m168);
    if (1 == 0) goto loc_004ECC02;
    v_r12 = 0;
    *(unsigned __int8 *)(a1 + 720) = 0;
    result = 0;
    v_stack_m178 = 0;
    if (0 == 258) goto loc_004ECBB8;
    goto loc_004ECC15;
loc_004ECC02:
    if (0 == 258) goto loc_004ECFDF;
loc_004ECC15:
    if (0 == 128) goto loc_004ECFDF;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712)))) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 716))))) goto loc_004ECC53;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712)))) >= (*(unsigned int *)(a1 + 724))) goto loc_004ECC6D;
    if ((*(unsigned __int64 *)(a1 + 8)) != (a1 + 8)) goto loc_004ECC6D;
    if ((*(unsigned int *)(a1 + 4)) != 0) goto loc_004ECC53;
    result = a1 + 8;
    if ((unsigned __int8)(*(unsigned __int8 *)(a1 + 720)) != 0) {
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 696));
        a3 = 0;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 688) + 16);
        a2 = 0;
        a1 = *(unsigned __int64 *)(result + a1 * 8);
        a1 = (a1) + (16);
        result = KeSetEvent(a1, a2, a3, v_stack_m168);
    }
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline(a1, a2, a3, v_stack_m168);
    if ((unsigned int)(result) == 0) goto loc_004ECD4F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 688))) != (*(unsigned __int64 *)(v_rip + 11379210))) goto loc_004ECD4F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 728)))) != 1) goto loc_004ECD4F;
    if (((unsigned int)((int)(*(unsigned int *)(result + 84)))) >= 7) goto loc_004ECCC9;
    goto loc_004ECCCD;
loc_004ECCC9:
loc_004ECCCD:
    v_rbx = 0;
    a2 = ((int)((unsigned int)((int)(*(unsigned int *)(result + 84)) - 32))) - (*(unsigned __int64 *)(result + 88));
    a2 = (a2) >> (11);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9576172))) == 0) goto loc_004ECD29;
loc_004ECD12:
    if (a2 < (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10542078)))) goto loc_004ECD24;
    result = (unsigned int)((0) + 1);
    a1 = (*(unsigned __int64 *)(v_rip + 10542078)) + (8);
    if (((unsigned int)(result)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9576172))))) goto loc_004ECD12;
    goto loc_004ECD29;
loc_004ECD24:
    if (((unsigned int)(result)) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9576172))))) {
        result = (unsigned int)(*(unsigned int *)(v_rip + 9576172)) - 1;
    }
    a4 = (unsigned int)(((int)(*(unsigned int *)(result + 84)) - 32) * ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9576172)))));
    a4 = (unsigned int)((a4) + ((unsigned int)(result)));
    a1 = (*(unsigned __int64 *)(a4 * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 744)) * 1)) + 1;
    *(unsigned __int64 *)(a4 * 8 + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 744)) * 1) = a1;
    goto loc_004ECD51;
loc_004ECD4F:
    v_rbx = 0;
loc_004ECD51:
    if (((*(unsigned int *)(v_rip + 11378093)) & (0x8000000ULL)) == 0) goto loc_004ECD84;
    result = EtwTraceThreadWorkItem(*(unsigned __int64 *)(result + 16), (unsigned int)(0x540ULL), (unsigned int)(*(unsigned int *)(v_rip + 9576172)), a4);
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 24), (unsigned int)(0x540ULL), (unsigned int)(*(unsigned int *)(v_rip + 9576172)), a4);
    result = EtwTraceThreadWorkItem(*(unsigned __int64 *)(result + 16), (unsigned int)(0x541ULL), (unsigned int)(*(unsigned int *)(v_rip + 9576172)), a4);
    goto loc_004ECD8F;
loc_004ECD84:
    result = guard_dispatch_icall(*(unsigned __int64 *)(result + 24), (unsigned int)(0x541ULL), (unsigned int)(*(unsigned int *)(v_rip + 9576172)), a4);
loc_004ECD8F:
    result = *(unsigned __int8 *)(gs_base + (0 + 2142));
    if ((((unsigned __int8)(*(unsigned __int8 *)(gs_base + (0 + 2142)))) & (1)) != 0) {
        result = KxReenterRetpolinedCode(*(unsigned __int64 *)(result + 24), (unsigned int)(0x541ULL), (unsigned int)(*(unsigned int *)(v_rip + 9576172)), a4);
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 776)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 776)) goto loc_004ED1DE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484))) != 0) goto loc_004ED1BE;
    if ((unsigned __int8)(v_cr8) != 0) goto loc_004ED1A0;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) goto loc_004ED187;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_004ED161;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1688)) != -3) goto loc_004ED148;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (9));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1084);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    if (((unsigned int)(a1)) >= 2) goto loc_004ECE4F;
    if ((*(unsigned __int64 *)(gs_base + (0 + 392))) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_004ED0C9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1504)) == 0) goto loc_004ED0C9;
    goto loc_004ECE55;
loc_004ECE4F:
    if ((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1504)) != 0) goto loc_004ED0C9;
loc_004ECE55:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440))) >> (12));
    a1 = (unsigned int)((a1) & (7));
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 672) + 1092);
        if (((unsigned int)(a1)) >= ((unsigned int)(result))) { a1 = (unsigned int)(result); }
    }
    if (((unsigned int)(a1)) != 5) goto loc_004ED127;
    if (((unsigned int)(a1)) < 5) goto loc_004ED108;
    if (((unsigned int)(a1)) < 5) goto loc_004ED0EA;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)))) & (8)) != 0) {
        v_stack_m180 = result;
        a3 = v_rip + 6687875;
        a4 = *(unsigned __int64 *)(result + 16);
        v_stack_m188 = *(unsigned __int64 *)(result + 24);
        a2 = 0;
        a1 = 0;
        result = DbgPrintEx(a1, a2, a3, a4);
        a1 = v_stack_m160;
        v_stack_m160 = v_xmm0;
        result = KeRevertToUserGroupAffinityThread(a1, a2, a3, a4);
    }
    a2 = 0;
    v_stack_m148 = 0x200001ULL;
    result = memset(v_stack_m140, a2, 256, a4);
    a3 = 0;
    result = KeQueryNodeActiveAffinityEx(*(unsigned __int16 *)(v_stack_m170), v_stack_m148, a3, a4);
    if (((unsigned __int16)(v_stack_m148)) >= ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552))))) goto loc_004ECF2C;
    goto loc_004ECF35;
loc_004ECF2C:
loc_004ECF35:
    if (0 >= ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552)))))) goto loc_004ECF60;
loc_004ECF40:
    if ((*(unsigned __int64 *)(v_rsp + 0 * 8 * 1 + 104)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552) + 0 * 8 + 8))) goto loc_004ECF85;
    result = (unsigned __int16)((0) + 1);
    if (((unsigned __int16)(result)) < ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552)))))) goto loc_004ECF40;
loc_004ECF60:
    if (((unsigned __int16)(result)) >= ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m148)))) goto loc_004ECF92;
loc_004ECF70:
    if ((*(unsigned __int64 *)(v_stack_m148 + (unsigned __int16)(result) * 8 + 8)) != 0) goto loc_004ECF85;
    result = (unsigned __int16)((result) + 1);
    if (((unsigned __int16)(result)) < ((unsigned __int16)(*(unsigned __int16 *)(v_stack_m148)))) goto loc_004ECF70;
    goto loc_004ECF92;
loc_004ECF85:
    result = KeSetUserAffinityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_m148, (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552))), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 552));
loc_004ECF92:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1584)) != 0) {
        v_stack_m180 = result;
        a3 = v_rip + 6687448;
        a4 = *(unsigned __int64 *)(result + 16);
        v_stack_m188 = *(unsigned __int64 *)(result + 24);
        a2 = 0;
        a1 = 0;
        result = DbgPrintEx(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        *(unsigned __int64 *)(result + 1584) = 0;
    }
loc_004ECFD5:
    goto loc_004ECBB8;
loc_004ECFDF:
    if (condition_is_below) goto loc_004ECFF9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1344)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1344)) goto loc_004ECFD5;
    if ((*(unsigned int *)(a1 + 4)) != 0) goto loc_004ECFD5;
loc_004ECFF9:
loc_004ED002:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712))))) & (0x3FFFULL));
    a2 = (unsigned int)((a2) - 1);
    if (condition_is_below) goto loc_004ED023;
    if (condition_is_below) goto loc_004ECFD5;
    if (a2 < (*(unsigned int *)(a1 + 716))) goto loc_004ECFD5;
loc_004ED023:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712))))) & (0xFFFFC000ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712)))) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 712))))))) goto loc_004ED002;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1344)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 1344)) goto loc_004ED0AF;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 120))) >> (6));
    if ((((unsigned __int8)(result)) & (1)) == 0) {
    }
    if (a2 == 0x8000ULL) {
        a1 = *(unsigned __int64 *)(a1 + 736);
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_004ED0AF:
    result = 0;
    a4 = 0;
    v_stack_m160 = 0;
    a2 = 0;
    result = KeBugCheckEx(466, a2, *(unsigned __int64 *)(v_stack_m28 + 72), a4);
loc_004ED0C9:
    result = PsGetIoPriorityThread(*(unsigned __int64 *)(v_stack_m28 + 72), a2, *(unsigned __int64 *)(v_stack_m28 + 72), a4);
    v_stack_m160 = result;
    result = KeBugCheckEx(296, *(unsigned __int64 *)(result + 16), (int)((unsigned int)(result)), v_stack_m170);
loc_004ED0EA:
    a3 = ((int)((unsigned int)(result))) >> (11);
    a3 = (unsigned int)((a3) & (1));
    v_stack_m160 = result;
    result = KeBugCheckEx(470, *(unsigned __int64 *)(result + 16), a3, v_stack_m170);
loc_004ED108:
    result = (unsigned int)((result) >> (9));
    result = (unsigned int)((result) & (7));
    v_stack_m160 = result;
    result = KeBugCheckEx(347, *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)(result)), v_stack_m170);
loc_004ED127:
    result = PsGetPagePriorityThread(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)(result)), v_stack_m170);
    v_stack_m160 = result;
    result = KeBugCheckEx(297, *(unsigned __int64 *)(result + 16), (unsigned int)((unsigned int)(result)), v_stack_m170);
loc_004ED148:
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(410, *(unsigned __int64 *)(result + 16), v_stack_m170, result);
loc_004ED161:
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m28 + 72);
    result = KeBugCheckEx(5, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 544), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 184), *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 586));
loc_004ED187:
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(223, *(unsigned __int64 *)(result + 16), v_stack_m170, result);
loc_004ED1A0:
    v_stack_m160 = result;
    result = KeBugCheckEx(225, *(unsigned __int64 *)(result + 16), (unsigned __int8)(v_cr8), v_stack_m170);
loc_004ED1BE:
    v_stack_m160 = 1;
    result = KeBugCheckEx(1, *(unsigned __int64 *)(result + 16), *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 586), result);
loc_004ED1DE:
    v_stack_m160 = *(unsigned __int64 *)(v_stack_m28 + 56);
    result = KeBugCheckEx(57, *(unsigned __int64 *)(result + 16), v_stack_m170, result);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWorkerThread(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (384);
    result = (*(uint64_t *)(v_rip + 0x91DC2A)) ^ (local_rsp);
    v_stack_m38 = result;
    Arg2 = 0;
    v_stack_m160 = v_xmm0;
    result = memset(v_stack_m148, Arg2, 264, a4);
    result = 0;
    v_stack_m168 = 0;
    v_stack_m178 = v_stack_m168;
    v_stack_m170 = *(uint64_t *)(arg1 + 0x2B8);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))))) != 0) {
        Arg1 = 56;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))) | (1));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4) = (uint32_t)(result);
    if ((*(uint8_t *)(v_rip + 0xA0DDC3)) != 0) goto loc_004ECBB1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78))) >> (6));
    if (((1) & ((uint8_t)(result))) != 0) {
    }
loc_004ECBB8:
    a3 = 0;
    Arg2 = 0;
    result = KeRemovePriQueue(Arg1, Arg2, a3, v_stack_m168);
    if (1 == 0) goto loc_004ECC02;
    local_r12 = 0;
    *(uint8_t *)(arg1 + 0x2D0) = 0;
    result = 0;
    v_stack_m178 = 0;
    if (0 == 258) goto loc_004ECBB8;
    goto loc_004ECC15;
loc_004ECC02:
    if (0 == 258) goto loc_004ECFDF;
loc_004ECC15:
    if (0 == 128) goto loc_004ECFDF;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8)))) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2CC))))) goto loc_004ECC53;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8)))) >= (*(uint32_t *)(arg1 + 0x2D4))) goto loc_004ECC6D;
    if ((*(uint64_t *)(arg1 + 0x8)) != (Arg1 + 8)) goto loc_004ECC6D;
    if ((*(uint32_t *)(arg1 + 0x4)) != 0) goto loc_004ECC53;
    result = Arg1 + 8;
    if ((uint8_t)(*(uint8_t *)(arg1 + 0x2D0)) != 0) {
        Arg1 = *(uint16_t *)(*(uint64_t *)(arg1 + 0x2B8));
        a3 = 0;
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x2B0) + 0x10);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(result + arg1 * 8);
        Arg1 = (Arg1) + (16);
        result = KeSetEvent(Arg1, Arg2, a3, v_stack_m168);
    }
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline(Arg1, Arg2, a3, v_stack_m168);
    if ((uint32_t)(result) == 0) goto loc_004ECD4F;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x2B0))) != (*(uint64_t *)(v_rip + 0xADA20A))) goto loc_004ECD4F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2D8)))) != 1) goto loc_004ECD4F;
    if (((uint32_t)((int32_t)(*(uint32_t *)(result + 0x54)))) >= 7) goto loc_004ECCC9;
    goto loc_004ECCCD;
loc_004ECCC9:
loc_004ECCCD:
    local_rbx = 0;
    Arg2 = ((int32_t)((uint32_t)((int32_t)(*(uint32_t *)(result + 0x54)) - 32))) - (*(uint64_t *)(result + 0x58));
    Arg2 = (Arg2) >> (11);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921EEC))) == 0) goto loc_004ECD29;
loc_004ECD12:
    if (Arg2 < (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA0DBFE)))) goto loc_004ECD24;
    result = (uint32_t)((0) + 1);
    Arg1 = (*(uint64_t *)(v_rip + 0xA0DBFE)) + (8);
    if (((uint32_t)(result)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921EEC))))) goto loc_004ECD12;
    goto loc_004ECD29;
loc_004ECD24:
    if (((uint32_t)(result)) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921EEC))))) {
        result = (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)) - 1;
    }
    a4 = (uint32_t)(((int32_t)(*(uint32_t *)(result + 0x54)) - 32) * ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)))));
    a4 = (uint32_t)((a4) + ((uint32_t)(result)));
    Arg1 = (*(uint64_t *)(a4 * 8 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x2E8)) * 1)) + 1;
    *(void **)(a4 * 8 + *(uint64_t *)(*(uint64_t *)(arg1 + 0x2E8)) * 1) = Arg1;
    goto loc_004ECD51;
loc_004ECD4F:
    local_rbx = 0;
loc_004ECD51:
    if (((*(uint32_t *)(v_rip + 0xAD9DAD)) & (0x8000000ULL)) == 0) goto loc_004ECD84;
    result = EtwTraceThreadWorkItem(*(uint64_t *)(result + 0x10), (uint32_t)(0x540ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)), a4);
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x18), (uint32_t)(0x540ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)), a4);
    result = EtwTraceThreadWorkItem(*(uint64_t *)(result + 0x10), (uint32_t)(0x541ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)), a4);
    goto loc_004ECD8F;
loc_004ECD84:
    result = guard_dispatch_icall(*(uint64_t *)(result + 0x18), (uint32_t)(0x541ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)), a4);
loc_004ECD8F:
    result = *(uint8_t *)(gs_base + (0 + 0x85E));
    if ((((uint8_t)(*(uint8_t *)(gs_base + (0 + 0x85E)))) & (1)) != 0) {
        result = KxReenterRetpolinedCode(*(uint64_t *)(result + 0x18), (uint32_t)(0x541ULL), (uint32_t)(*(uint32_t *)(v_rip + 0x921EEC)), a4);
    }
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x308)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 776)) goto loc_004ED1DE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4))) != 0) goto loc_004ED1BE;
    if ((uint8_t)(v_cr8) != 0) goto loc_004ED1A0;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) goto loc_004ED187;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_004ED161;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x698)) != -3) goto loc_004ED148;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (9));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x43C);
        if (((uint32_t)(Arg1)) >= ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    }
    if (((uint32_t)(Arg1)) >= 2) goto loc_004ECE4F;
    if ((*(uint64_t *)(gs_base + (0 + 0x188))) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_004ED0C9;
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5E0)) == 0) goto loc_004ED0C9;
    goto loc_004ECE55;
loc_004ECE4F:
    if ((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5E0)) != 0) goto loc_004ED0C9;
loc_004ECE55:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0))) >> (12));
    Arg1 = (uint32_t)((Arg1) & (7));
    result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0);
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x2A0) + 0x444);
        if (((uint32_t)(Arg1)) >= ((uint32_t)(result))) { Arg1 = (uint32_t)(result); }
    }
    if (((uint32_t)(Arg1)) != 5) goto loc_004ED127;
    if (((uint32_t)(Arg1)) < 5) goto loc_004ED108;
    if (((uint32_t)(Arg1)) < 5) goto loc_004ED0EA;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)))) & (8)) != 0) {
        v_stack_m180 = result;
        a3 = v_rip + 6687875;
        a4 = *(uint64_t *)(result + 0x10);
        v_stack_m188 = *(uint64_t *)(result + 0x18);
        Arg2 = 0;
        Arg1 = 0;
        result = DbgPrintEx(Arg1, Arg2, a3, a4);
        Arg1 = v_stack_m160;
        v_stack_m160 = v_xmm0;
        result = KeRevertToUserGroupAffinityThread(Arg1, Arg2, a3, a4);
    }
    Arg2 = 0;
    v_stack_m148 = 0x200001ULL;
    result = memset(v_stack_m140, Arg2, 256, a4);
    a3 = 0;
    result = KeQueryNodeActiveAffinityEx(*(uint16_t *)(v_stack_m170), v_stack_m148, a3, a4);
    if (((uint16_t)(v_stack_m148)) >= ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228))))) goto loc_004ECF2C;
    goto loc_004ECF35;
loc_004ECF2C:
loc_004ECF35:
    if (0 >= ((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228)))))) goto loc_004ECF60;
loc_004ECF40:
    if ((*(uint64_t *)(local_rsp + 0x0 * 8 * 1 + 0x68)) != (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228) + 0x0 * 8 + 0x8))) goto loc_004ECF85;
    result = (uint16_t)((0) + 1);
    if (((uint16_t)(result)) < ((uint16_t)((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228)))))) goto loc_004ECF40;
loc_004ECF60:
    if (((uint16_t)(result)) >= ((uint16_t)(*(uint16_t *)(v_stack_m148)))) goto loc_004ECF92;
loc_004ECF70:
    if ((*(uint64_t *)(v_stack_m148 + (uint16_t)(result) * 8 + 0x8)) != 0) goto loc_004ECF85;
    result = (uint16_t)((result) + 1);
    if (((uint16_t)(result)) < ((uint16_t)(*(uint16_t *)(v_stack_m148)))) goto loc_004ECF70;
    goto loc_004ECF92;
loc_004ECF85:
    result = KeSetUserAffinityThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_m148, (uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228))), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x228));
loc_004ECF92:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x630)) != 0) {
        v_stack_m180 = result;
        a3 = v_rip + 6687448;
        a4 = *(uint64_t *)(result + 0x10);
        v_stack_m188 = *(uint64_t *)(result + 0x18);
        Arg2 = 0;
        Arg1 = 0;
        result = DbgPrintEx(Arg1, Arg2, a3, a4);
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        *(uint64_t *)(result + 0x630) = 0;
    }
loc_004ECFD5:
    goto loc_004ECBB8;
loc_004ECFDF:
    if (condition_is_below) goto loc_004ECFF9;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x540)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 1344)) goto loc_004ECFD5;
    if ((*(uint32_t *)(arg1 + 0x4)) != 0) goto loc_004ECFD5;
loc_004ECFF9:
loc_004ED002:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8))))) & (0x3FFFULL));
    Arg2 = (uint32_t)((Arg2) - 1);
    if (condition_is_below) goto loc_004ED023;
    if (condition_is_below) goto loc_004ECFD5;
    if (Arg2 < (*(uint32_t *)(arg1 + 0x2CC))) goto loc_004ECFD5;
loc_004ED023:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8))))) & (0xFFFFC000ULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8)))) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x2C8))))))) goto loc_004ED002;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x540)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 1344)) goto loc_004ED0AF;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x78))) >> (6));
    if ((((uint8_t)(result)) & (1)) == 0) {
    }
    if (Arg2 == 0x8000ULL) {
        Arg1 = *(uint64_t *)(arg1 + 0x2E0);
        a3 = 0;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    return result;
loc_004ED0AF:
    result = 0;
    a4 = 0;
    v_stack_m160 = 0;
    Arg2 = 0;
    result = KeBugCheckEx(466, Arg2, *(uint64_t *)(v_stack_m28 + 0x48), a4);
loc_004ED0C9:
    result = PsGetIoPriorityThread(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, *(uint64_t *)(v_stack_m28 + 0x48), a4);
    v_stack_m160 = result;
    result = KeBugCheckEx(296, *(uint64_t *)(result + 0x10), (int32_t)((uint32_t)(result)), v_stack_m170);
loc_004ED0EA:
    a3 = ((int32_t)((uint32_t)(result))) >> (11);
    a3 = (uint32_t)((a3) & (1));
    v_stack_m160 = result;
    result = KeBugCheckEx(470, *(uint64_t *)(result + 0x10), a3, v_stack_m170);
loc_004ED108:
    result = (uint32_t)((result) >> (9));
    result = (uint32_t)((result) & (7));
    v_stack_m160 = result;
    result = KeBugCheckEx(347, *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)(result)), v_stack_m170);
loc_004ED127:
    result = PsGetPagePriorityThread(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)(result)), v_stack_m170);
    v_stack_m160 = result;
    result = KeBugCheckEx(297, *(uint64_t *)(result + 0x10), (uint32_t)((uint32_t)(result)), v_stack_m170);
loc_004ED148:
    v_stack_m160 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(410, *(uint64_t *)(result + 0x10), v_stack_m170, result);
loc_004ED161:
    v_stack_m160 = *(uint64_t *)(v_stack_m28 + 0x48);
    result = KeBugCheckEx(5, *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x220), *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB8), *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x24A));
loc_004ED187:
    v_stack_m160 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(223, *(uint64_t *)(result + 0x10), v_stack_m170, result);
loc_004ED1A0:
    v_stack_m160 = result;
    result = KeBugCheckEx(225, *(uint64_t *)(result + 0x10), (uint8_t)(v_cr8), v_stack_m170);
loc_004ED1BE:
    v_stack_m160 = 1;
    result = KeBugCheckEx(1, *(uint64_t *)(result + 0x10), *(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x24A), result);
loc_004ED1DE:
    v_stack_m160 = *(uint64_t *)(v_stack_m28 + 0x38);
    result = KeBugCheckEx(57, *(uint64_t *)(result + 0x10), v_stack_m170, result);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x2B0` | `64` | `R` |
| `Arg1` | `+ 0x2B8` | `64` | `R` |
| `Arg1` | `+ 0x2C0` | `32` | `R/W` |
| `Arg1` | `+ 0x2C8` | `32` | `R` |
| `Arg1` | `+ 0x2C8` | `64` | `R` |
| `Arg1` | `+ 0x2CC` | `32` | `R` |
| `Arg1` | `+ 0x2D0` | `8` | `R` |
| `Arg1` | `+ 0x2D0` | `8` | `W` |
| `Arg1` | `+ 0x2D4` | `32` | `R` |
| `Arg1` | `+ 0x2D8` | `32` | `R` |
| `Arg1` | `+ 0x2E0` | `64` | `R` |
| `Arg1` | `+ 0x2E8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004ECAF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
