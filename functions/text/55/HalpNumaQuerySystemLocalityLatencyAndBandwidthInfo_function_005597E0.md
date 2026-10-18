# HalpNumaQuerySystemLocalityLatencyAndBandwidthInfo

- RVA: `0x005597E0`–`0x00559D78` (길이 `1,432` bytes)
- VA: `0x00000001405597E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C46B0`
- 디코드: `404`개 명령, `1,432/1,432` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00559890` → [HalpNumaQueryProximityId](HalpNumaQueryProximityId_function_00559750.md) (function, `0x00559750`)
- `0x005598C7` → [HalpNumaQueryProximityId](HalpNumaQueryProximityId_function_00559750.md) (function, `0x00559750`)
- `0x00559918` → [HalpNumaSystemLocalityInfoIncludeQueryDataType](HalpNumaSystemLocalityInfoIncludeQueryDataType_function_0055A034.md) (function, `0x0055A034`)
- `0x00559942` → [HalpNumaSystemLocalityInfoFindTargetIndex](HalpNumaSystemLocalityInfoFindTargetIndex_function_00559FDC.md) (function, `0x00559FDC`)
- `0x00559968` → [HalpNumaSystemLocalityInfoFindInitiatorIndex](HalpNumaSystemLocalityInfoFindInitiatorIndex_function_00559F8C.md) (function, `0x00559F8C`)
- `0x00559982` → [HalpNumaSystemLocalityInfoFindTargetIndex](HalpNumaSystemLocalityInfoFindTargetIndex_function_00559FDC.md) (function, `0x00559FDC`)
- `0x00559991` → [HalpNumaSystemLocalityInfoFindInitiatorIndex](HalpNumaSystemLocalityInfoFindInitiatorIndex_function_00559F8C.md) (function, `0x00559F8C`)
- `0x00559A12` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00559A61` → [HalpNumaSystemLocalityInfoIncludeQueryDataType](HalpNumaSystemLocalityInfoIncludeQueryDataType_function_0055A034.md) (function, `0x0055A034`)
- `0x00559B5B` → [HalpNumaSystemLocalityInfoFindTargetIndex](HalpNumaSystemLocalityInfoFindTargetIndex_function_00559FDC.md) (function, `0x00559FDC`)
- `0x00559B8A` → [HalpNumaSystemLocalityInfoFindTargetIndex](HalpNumaSystemLocalityInfoFindTargetIndex_function_00559FDC.md) (function, `0x00559FDC`)
- `0x00559BA8` → [HalpNumaSystemLocalityInfoFindInitiatorIndex](HalpNumaSystemLocalityInfoFindInitiatorIndex_function_00559F8C.md) (function, `0x00559F8C`)
- `0x00559BB7` → [HalpNumaSystemLocalityInfoFindTargetIndex](HalpNumaSystemLocalityInfoFindTargetIndex_function_00559FDC.md) (function, `0x00559FDC`)
- `0x00559C67` → [HalpNumaQueryProximityNode](HalpNumaQueryProximityNode_function_00559790.md) (function, `0x00559790`)
- `0x00559C8E` → [HalpNumaQueryProximityNode](HalpNumaQueryProximityNode_function_00559790.md) (function, `0x00559790`)
- `0x00559D4F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00559806` → RVA `0x00F90640` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005597E0  48 8B C4                        mov rax, rsp
005597E3  48 89 58 08                     mov qword ptr [rax + 8], rbx
005597E7  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
005597EB  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
005597EF  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
005597F3  55                              push rbp
005597F4  41 54                           push r12
005597F6  41 55                           push r13
005597F8  41 56                           push r14
005597FA  41 57                           push r15
005597FC  48 8B EC                        mov rbp, rsp
005597FF  48 81 EC 80 00 00 00            sub rsp, 0x80
00559806  4C 8B 35 33 6E A3 00            mov r14, qword ptr [rip + 0xa36e33]
0055980D  45 33 C9                        xor r9d, r9d
00559810  66 44 89 4D A0                  mov word ptr [rbp - 0x60], r9w
00559815  41 8B F8                        mov edi, r8d
00559818  4C 89 75 C0                     mov qword ptr [rbp - 0x40], r14
0055981C  8B C2                           mov eax, edx
0055981E  4D 85 F6                        test r14, r14
00559821  75 0A                           jne 0x14055982d
00559823  BB E5 00 00 C0                  mov ebx, 0xc00000e5
00559828  E9 10 05 00 00                  jmp 0x140559d3d
0055982D  BA 01 00 00 00                  mov edx, 1
00559832  3B CA                           cmp ecx, edx
00559834  74 0A                           je 0x140559840
00559836  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0055983B  E9 FD 04 00 00                  jmp 0x140559d3d
00559840  4C 39 4D 68                     cmp qword ptr [rbp + 0x68], r9
00559844  74 F0                           je 0x140559836
00559846  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
0055984A  4D 85 E4                        test r12, r12
0055984D  75 10                           jne 0x14055985f
0055984F  44 39 4D 60                     cmp dword ptr [rbp + 0x60], r9d
00559853  74 0A                           je 0x14055985f
00559855  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0055985A  E9 F5 04 00 00                  jmp 0x140559d54
0055985F  41 BA FF FF FF FF               mov r10d, 0xffffffff
00559865  41 BF FF FF 00 00               mov r15d, 0xffff
0055986B  44 89 55 DC                     mov dword ptr [rbp - 0x24], r10d
0055986F  45 8B EA                        mov r13d, r10d
00559872  41 3B C2                        cmp eax, r10d
00559875  74 35                           je 0x1405598ac
00559877  41 3B C7                        cmp eax, r15d
0055987A  76 0A                           jbe 0x140559886
0055987C  BB 25 02 00 C0                  mov ebx, 0xc0000225
00559881  E9 B7 04 00 00                  jmp 0x140559d3d
00559886  45 33 C0                        xor r8d, r8d
00559889  48 8D 55 DC                     lea rdx, [rbp - 0x24]
0055988D  0F B7 C8                        movzx ecx, ax
00559890  E8 BB FE FF FF                  call 0x140559750
00559895  45 33 C9                        xor r9d, r9d
00559898  8B D8                           mov ebx, eax
0055989A  85 C0                           test eax, eax
0055989C  0F 88 9B 04 00 00               js 0x140559d3d
005598A2  44 8B 6D DC                     mov r13d, dword ptr [rbp - 0x24]
005598A6  41 BA FF FF FF FF               mov r10d, 0xffffffff
005598AC  44 89 55 A4                     mov dword ptr [rbp - 0x5c], r10d
005598B0  41 8B F2                        mov esi, r10d
005598B3  41 3B FA                        cmp edi, r10d
005598B6  74 2A                           je 0x1405598e2
005598B8  41 3B FF                        cmp edi, r15d
005598BB  77 BF                           ja 0x14055987c
005598BD  45 33 C0                        xor r8d, r8d
005598C0  48 8D 55 A4                     lea rdx, [rbp - 0x5c]
005598C4  0F B7 CF                        movzx ecx, di
005598C7  E8 84 FE FF FF                  call 0x140559750
005598CC  45 33 C9                        xor r9d, r9d
005598CF  8B D8                           mov ebx, eax
005598D1  85 C0                           test eax, eax
005598D3  0F 88 64 04 00 00               js 0x140559d3d
005598D9  8B 75 A4                        mov esi, dword ptr [rbp - 0x5c]
005598DC  41 BA FF FF FF FF               mov r10d, 0xffffffff
005598E2  41 8B 5E 10                     mov ebx, dword ptr [r14 + 0x10]
005598E6  45 8B F9                        mov r15d, r9d
005598E9  49 03 DE                        add rbx, r14
005598EC  45 8B F1                        mov r14d, r9d
005598EF  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
005598F3  41 83 79 04 00                  cmp dword ptr [r9 + 4], 0
005598F8  0F 86 D4 00 00 00               jbe 0x1405599d2
005598FE  44 8B 65 48                     mov r12d, dword ptr [rbp + 0x48]
00559902  41 83 FC 04                     cmp r12d, 4
00559906  74 0A                           je 0x140559912
00559908  44 3B 63 04                     cmp r12d, dword ptr [rbx + 4]
0055990C  0F 85 AA 00 00 00               jne 0x1405599bc
00559912  8B 55 50                        mov edx, dword ptr [rbp + 0x50]
00559915  48 8B CB                        mov rcx, rbx
00559918  E8 17 07 00 00                  call 0x14055a034
0055991D  84 C0                           test al, al
0055991F  0F 84 97 00 00 00               je 0x1405599bc
00559925  33 FF                           xor edi, edi
00559927  45 3B EA                        cmp r13d, r10d
0055992A  75 2E                           jne 0x14055995a
0055992C  41 3B F2                        cmp esi, r10d
0055992F  75 09                           jne 0x14055993a
00559931  8B 7B 10                        mov edi, dword ptr [rbx + 0x10]
00559934  0F AF 7B 0C                     imul edi, dword ptr [rbx + 0xc]
00559938  EB 72                           jmp 0x1405599ac
0055993A  45 33 C0                        xor r8d, r8d
0055993D  8B D6                           mov edx, esi
0055993F  48 8B CB                        mov rcx, rbx
00559942  E8 95 06 00 00                  call 0x140559fdc
00559947  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
0055994B  41 BA FF FF FF FF               mov r10d, 0xffffffff
00559951  85 C0                           test eax, eax
00559953  78 57                           js 0x1405599ac
00559955  8B 7B 0C                        mov edi, dword ptr [rbx + 0xc]
00559958  EB 52                           jmp 0x1405599ac
0055995A  45 33 C0                        xor r8d, r8d
0055995D  48 8B CB                        mov rcx, rbx
00559960  41 3B F2                        cmp esi, r10d
00559963  75 1B                           jne 0x140559980
00559965  41 8B D5                        mov edx, r13d
00559968  E8 1F 06 00 00                  call 0x140559f8c
0055996D  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
00559971  41 BA FF FF FF FF               mov r10d, 0xffffffff
00559977  85 C0                           test eax, eax
00559979  78 31                           js 0x1405599ac
0055997B  8B 7B 10                        mov edi, dword ptr [rbx + 0x10]
0055997E  EB 2C                           jmp 0x1405599ac
00559980  8B D6                           mov edx, esi
00559982  E8 55 06 00 00                  call 0x140559fdc
00559987  85 C0                           test eax, eax
00559989  78 17                           js 0x1405599a2
0055998B  41 8B D5                        mov edx, r13d
0055998E  48 8B CB                        mov rcx, rbx
00559991  E8 F6 05 00 00                  call 0x140559f8c
00559996  85 C0                           test eax, eax
00559998  41 B8 01 00 00 00               mov r8d, 1
0055999E  41 0F 49 F8                     cmovns edi, r8d
005599A2  4C 8B 4D C0                     mov r9, qword ptr [rbp - 0x40]
005599A6  41 BA FF FF FF FF               mov r10d, 0xffffffff
005599AC  8A 43 09                        mov al, byte ptr [rbx + 9]
005599AF  84 C0                           test al, al
005599B1  74 04                           je 0x1405599b7
005599B3  3C 03                           cmp al, 3
005599B5  75 02                           jne 0x1405599b9
005599B7  03 FF                           add edi, edi
005599B9  44 03 FF                        add r15d, edi
005599BC  8B 03                           mov eax, dword ptr [rbx]
005599BE  41 FF C6                        inc r14d
005599C1  48 03 D8                        add rbx, rax
005599C4  45 3B 71 04                     cmp r14d, dword ptr [r9 + 4]
005599C8  0F 82 34 FF FF FF               jb 0x140559902
005599CE  4C 8B 65 58                     mov r12, qword ptr [rbp + 0x58]
005599D2  41 8B C7                        mov eax, r15d
005599D5  48 C1 E0 05                     shl rax, 5
005599D9  49 3B C2                        cmp rax, r10
005599DC  0F 87 56 03 00 00               ja 0x140559d38
005599E2  44 8D 70 08                     lea r14d, [rax + 8]
005599E6  41 83 FE 08                     cmp r14d, 8
005599EA  0F 82 48 03 00 00               jb 0x140559d38
005599F0  33 DB                           xor ebx, ebx
005599F2  44 39 75 60                     cmp dword ptr [rbp + 0x60], r14d
005599F6  73 11                           jae 0x140559a09
005599F8  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
005599FC  BB 23 00 00 C0                  mov ebx, 0xc0000023
00559A01  44 89 30                        mov dword ptr [rax], r14d
00559A04  E9 34 03 00 00                  jmp 0x140559d3d
00559A09  44 8B 45 60                     mov r8d, dword ptr [rbp + 0x60]
00559A0D  33 D2                           xor edx, edx
00559A0F  49 8B CC                        mov rcx, r12
00559A12  E8 29 D2 16 00                  call 0x1406c6c40
00559A17  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00559A1B  45 33 DB                        xor r11d, r11d
00559A1E  45 89 3C 24                     mov dword ptr [r12], r15d
00559A22  45 32 FF                        xor r15b, r15b
00559A25  44 89 5D B0                     mov dword ptr [rbp - 0x50], r11d
00559A29  8B 78 10                        mov edi, dword ptr [rax + 0x10]
00559A2C  48 03 3D 0D 6C A3 00            add rdi, qword ptr [rip + 0xa36c0d]
00559A33  45 33 D2                        xor r10d, r10d
00559A36  44 89 55 A4                     mov dword ptr [rbp - 0x5c], r10d
00559A3A  44 3B 50 04                     cmp r10d, dword ptr [rax + 4]
00559A3E  0F 83 EB 02 00 00               jae 0x140559d2f
00559A44  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
00559A47  41 B9 04 00 00 00               mov r9d, 4
00559A4D  41 3B C1                        cmp eax, r9d
00559A50  74 09                           je 0x140559a5b
00559A52  3B 47 04                        cmp eax, dword ptr [rdi + 4]
00559A55  0F 85 AD 02 00 00               jne 0x140559d08
00559A5B  8B 55 50                        mov edx, dword ptr [rbp + 0x50]
00559A5E  48 8B CF                        mov rcx, rdi
00559A61  E8 CE 05 00 00                  call 0x14055a034
00559A66  84 C0                           test al, al
00559A68  0F 84 9A 02 00 00               je 0x140559d08
00559A6E  0F B6 4F 09                     movzx ecx, byte ptr [rdi + 9]
00559A72  BA 01 00 00 00                  mov edx, 1
00559A77  44 89 4D B8                     mov dword ptr [rbp - 0x48], r9d
00559A7B  44 8B E2                        mov r12d, edx
00559A7E  44 89 4D BC                     mov dword ptr [rbp - 0x44], r9d
00559A82  89 55 D8                        mov dword ptr [rbp - 0x28], edx
00559A85  85 C9                           test ecx, ecx
00559A87  74 41                           je 0x140559aca
00559A89  2B CA                           sub ecx, edx
00559A8B  74 37                           je 0x140559ac4
00559A8D  2B CA                           sub ecx, edx
00559A8F  74 2A                           je 0x140559abb
00559A91  2B CA                           sub ecx, edx
00559A93  74 1A                           je 0x140559aaf
00559A95  2B CA                           sub ecx, edx
00559A97  74 11                           je 0x140559aaa
00559A99  3B CA                           cmp ecx, edx
00559A9B  0F 85 80 02 00 00               jne 0x140559d21
00559AA1  C7 45 B8 03 00 00 00            mov dword ptr [rbp - 0x48], 3
00559AA8  EB 35                           jmp 0x140559adf
00559AAA  89 55 B8                        mov dword ptr [rbp - 0x48], edx
00559AAD  EB 30                           jmp 0x140559adf
00559AAF  89 55 B8                        mov dword ptr [rbp - 0x48], edx
00559AB2  C7 45 BC 03 00 00 00            mov dword ptr [rbp - 0x44], 3
00559AB9  EB 1A                           jmp 0x140559ad5
00559ABB  C7 45 B8 02 00 00 00            mov dword ptr [rbp - 0x48], 2
00559AC2  EB 1B                           jmp 0x140559adf
00559AC4  83 65 B8 00                     and dword ptr [rbp - 0x48], 0
00559AC8  EB 15                           jmp 0x140559adf
00559ACA  83 65 B8 00                     and dword ptr [rbp - 0x48], 0
00559ACE  C7 45 BC 02 00 00 00            mov dword ptr [rbp - 0x44], 2
00559AD5  41 BC 02 00 00 00               mov r12d, 2
00559ADB  44 89 65 D8                     mov dword ptr [rbp - 0x28], r12d
00559ADF  8B 57 0C                        mov edx, dword ptr [rdi + 0xc]
00559AE2  41 BA FF FF FF FF               mov r10d, 0xffffffff
00559AE8  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
00559AEC  48 8D 42 08                     lea rax, [rdx + 8]
00559AF0  48 8D 0C 95 00 00 00 00         lea rcx, [rdx*4]
00559AF8  48 8D 04 87                     lea rax, [rdi + rax*4]
00559AFC  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00559B00  49 3B CA                        cmp rcx, r10
00559B03  0F 87 2F 02 00 00               ja 0x140559d38
00559B09  44 8B 4F 10                     mov r9d, dword ptr [rdi + 0x10]
00559B0D  41 8B C1                        mov eax, r9d
00559B10  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
00559B14  48 C1 E0 02                     shl rax, 2
00559B18  49 3B C2                        cmp rax, r10
00559B1B  0F 87 17 02 00 00               ja 0x140559d38
00559B21  44 8D 04 08                     lea r8d, [rax + rcx]
00559B25  44 3B C0                        cmp r8d, eax
00559B28  0F 82 0A 02 00 00               jb 0x140559d38
00559B2E  33 DB                           xor ebx, ebx
00559B30  41 8B C0                        mov eax, r8d
00559B33  21 5D A8                        and dword ptr [rbp - 0x58], ebx
00559B36  48 83 C0 20                     add rax, 0x20
00559B3A  21 5D AC                        and dword ptr [rbp - 0x54], ebx
00559B3D  48 03 C7                        add rax, rdi
00559B40  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00559B44  45 3B EA                        cmp r13d, r10d
00559B47  75 32                           jne 0x140559b7b
00559B49  41 3B F2                        cmp esi, r10d
00559B4C  0F 84 99 00 00 00               je 0x140559beb
00559B52  4C 8D 45 AC                     lea r8, [rbp - 0x54]
00559B56  8B D6                           mov edx, esi
00559B58  48 8B CF                        mov rcx, rdi
00559B5B  E8 7C 04 00 00                  call 0x140559fdc
00559B60  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00559B64  85 C0                           test eax, eax
00559B66  78 72                           js 0x140559bda
00559B68  44 8B 4D AC                     mov r9d, dword ptr [rbp - 0x54]
00559B6C  41 FF C1                        inc r9d
00559B6F  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
00559B73  41 BF 01 00 00 00               mov r15d, 1
00559B79  EB 63                           jmp 0x140559bde
00559B7B  4C 8D 45 A8                     lea r8, [rbp - 0x58]
00559B7F  41 8B D5                        mov edx, r13d
00559B82  48 8B CF                        mov rcx, rdi
00559B85  41 3B F2                        cmp esi, r10d
00559B88  75 1E                           jne 0x140559ba8
00559B8A  E8 4D 04 00 00                  call 0x140559fdc
00559B8F  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
00559B93  85 C0                           test eax, eax
00559B95  78 0B                           js 0x140559ba2
00559B97  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
00559B9A  FF C2                           inc edx
00559B9C  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
00559BA0  EB D1                           jmp 0x140559b73
00559BA2  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00559BA6  EB 36                           jmp 0x140559bde
00559BA8  E8 DF 03 00 00                  call 0x140559f8c
00559BAD  85 C0                           test eax, eax
00559BAF  78 25                           js 0x140559bd6
00559BB1  4C 8D 45 AC                     lea r8, [rbp - 0x54]
00559BB5  8B D6                           mov edx, esi
00559BB7  E8 20 04 00 00                  call 0x140559fdc
00559BBC  85 C0                           test eax, eax
00559BBE  78 16                           js 0x140559bd6
00559BC0  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
00559BC3  44 8B 4D AC                     mov r9d, dword ptr [rbp - 0x54]
00559BC7  FF C2                           inc edx
00559BC9  41 FF C1                        inc r9d
00559BCC  48 89 55 D0                     mov qword ptr [rbp - 0x30], rdx
00559BD0  4C 89 4D C8                     mov qword ptr [rbp - 0x38], r9
00559BD4  EB 11                           jmp 0x140559be7
00559BD6  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00559BDA  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
00559BDE  45 84 FF                        test r15b, r15b
00559BE1  0F 84 1D 01 00 00               je 0x140559d04
00559BE7  44 8B 5D B0                     mov r11d, dword ptr [rbp - 0x50]
00559BEB  45 33 ED                        xor r13d, r13d
00559BEE  41 8D 4D 01                     lea ecx, [r13 + 1]
00559BF2  45 3B EC                        cmp r13d, r12d
00559BF5  0F 83 06 01 00 00               jae 0x140559d01
00559BFB  44 8B 65 A8                     mov r12d, dword ptr [rbp - 0x58]
00559BFF  41 8B C5                        mov eax, r13d
00559C02  44 3B E2                        cmp r12d, edx
00559C05  0F 83 EA 00 00 00               jae 0x140559cf5
00559C0B  44 8B 7D AC                     mov r15d, dword ptr [rbp - 0x54]
00559C0F  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00559C13  45 3B F9                        cmp r15d, r9d
00559C16  0F 83 CD 00 00 00               jae 0x140559ce9
00559C1C  8B 44 85 B8                     mov eax, dword ptr [rbp + rax*4 - 0x48]
00559C20  41 8B DB                        mov ebx, r11d
00559C23  48 C1 E3 05                     shl rbx, 5
00559C27  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00559C2B  89 44 13 14                     mov dword ptr [rbx + rdx + 0x14], eax
00559C2F  8A 44 13 18                     mov al, byte ptr [rbx + rdx + 0x18]
00559C33  8A C8                           mov cl, al
00559C35  32 4F 08                        xor cl, byte ptr [rdi + 8]
00559C38  80 E1 01                        and cl, 1
00559C3B  32 C8                           xor cl, al
00559C3D  88 4C 13 18                     mov byte ptr [rbx + rdx + 0x18], cl
00559C41  8A C1                           mov al, cl
00559C43  32 47 08                        xor al, byte ptr [rdi + 8]
00559C46  24 02                           and al, 2
00559C48  32 C1                           xor al, cl
00559C4A  41 8B CC                        mov ecx, r12d
00559C4D  88 44 13 18                     mov byte ptr [rbx + rdx + 0x18], al
00559C51  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
00559C54  88 44 13 19                     mov byte ptr [rbx + rdx + 0x19], al
00559C58  8B 47 04                        mov eax, dword ptr [rdi + 4]
00559C5B  89 44 13 10                     mov dword ptr [rbx + rdx + 0x10], eax
00559C5F  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00559C63  8B 4C 8F 20                     mov ecx, dword ptr [rdi + rcx*4 + 0x20]
00559C67  E8 24 FB FF FF                  call 0x140559790
00559C6C  85 C0                           test eax, eax
00559C6E  0F 88 B4 00 00 00               js 0x140559d28
00559C74  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
00559C78  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00559C7C  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00559C80  89 44 0B 08                     mov dword ptr [rbx + rcx + 8], eax
00559C84  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00559C88  41 8B CF                        mov ecx, r15d
00559C8B  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
00559C8E  E8 FD FA FF FF                  call 0x140559790
00559C93  8B D8                           mov ebx, eax
00559C95  85 C0                           test eax, eax
00559C97  0F 88 8B 00 00 00               js 0x140559d28
00559C9D  0F B7 45 A0                     movzx eax, word ptr [rbp - 0x60]
00559CA1  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
00559CA5  4C 8B 45 E8                     mov r8, qword ptr [rbp - 0x18]
00559CA9  44 8B 5D B0                     mov r11d, dword ptr [rbp - 0x50]
00559CAD  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
00559CB1  4C 8B 4D C8                     mov r9, qword ptr [rbp - 0x38]
00559CB5  41 89 44 10 0C                  mov dword ptr [r8 + rdx + 0xc], eax
00559CBA  41 8B C4                        mov eax, r12d
00559CBD  0F AF 47 10                     imul eax, dword ptr [rdi + 0x10]
00559CC1  41 03 C7                        add eax, r15d
00559CC4  0F B7 0C 41                     movzx ecx, word ptr [rcx + rax*2]
00559CC8  48 0F AF 4F 18                  imul rcx, qword ptr [rdi + 0x18]
00559CCD  41 8B C5                        mov eax, r13d
00559CD0  49 89 4C 10 20                  mov qword ptr [r8 + rdx + 0x20], rcx
00559CD5  B9 01 00 00 00                  mov ecx, 1
00559CDA  44 03 D9                        add r11d, ecx
00559CDD  44 89 5D B0                     mov dword ptr [rbp - 0x50], r11d
00559CE1  44 03 F9                        add r15d, ecx
00559CE4  E9 2A FF FF FF                  jmp 0x140559c13
00559CE9  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
00559CED  44 03 E1                        add r12d, ecx
00559CF0  E9 0D FF FF FF                  jmp 0x140559c02
00559CF5  44 8B 65 D8                     mov r12d, dword ptr [rbp - 0x28]
00559CF9  44 03 E9                        add r13d, ecx
00559CFC  E9 F1 FE FF FF                  jmp 0x140559bf2
00559D01  45 32 FF                        xor r15b, r15b
00559D04  44 8B 55 A4                     mov r10d, dword ptr [rbp - 0x5c]
00559D08  8B 07                           mov eax, dword ptr [rdi]
00559D0A  44 8B 6D DC                     mov r13d, dword ptr [rbp - 0x24]
00559D0E  48 03 F8                        add rdi, rax
00559D11  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
00559D15  41 FF C2                        inc r10d
00559D18  44 8B 5D B0                     mov r11d, dword ptr [rbp - 0x50]
00559D1C  E9 15 FD FF FF                  jmp 0x140559a36
00559D21  BB 60 02 00 C0                  mov ebx, 0xc0000260
00559D26  EB 15                           jmp 0x140559d3d
00559D28  BB 0F 00 14 C0                  mov ebx, 0xc014000f
00559D2D  EB 0E                           jmp 0x140559d3d
00559D2F  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
00559D33  44 89 30                        mov dword ptr [rax], r14d
00559D36  EB 1C                           jmp 0x140559d54
00559D38  BB 95 00 00 C0                  mov ebx, 0xc0000095
00559D3D  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
00559D41  48 85 C0                        test rax, rax
00559D44  74 0E                           je 0x140559d54
00559D46  44 8B 45 60                     mov r8d, dword ptr [rbp + 0x60]
00559D4A  33 D2                           xor edx, edx
00559D4C  48 8B C8                        mov rcx, rax
00559D4F  E8 EC CE 16 00                  call 0x1406c6c40
00559D54  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00559D5C  8B C3                           mov eax, ebx
00559D5E  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00559D62  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00559D66  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00559D6A  49 8B E3                        mov rsp, r11
00559D6D  41 5F                           pop r15
00559D6F  41 5E                           pop r14
00559D71  41 5D                           pop r13
00559D73  41 5C                           pop r12
00559D75  5D                              pop rbp
00559D76  C3                              ret
00559D77  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpNumaQuerySystemLocalityLatencyAndBandwidthInfo(int a1, int a2, int a3, int a4, unsigned int a5, __int64 a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned __int16 v_stack_m88;
    unsigned int v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (128);
    a4 = 0;
    v_stack_m88 = 0;
    v_stack_m68 = *(unsigned __int64 *)(v_rip + 10710579);
    if (*(unsigned __int64 *)(v_rip + 10710579) != 0) goto loc_0055982D;
    goto loc_00559D3D;
loc_0055982D:
    if (a1 == 1) goto loc_00559840;
loc_00559836:
    goto loc_00559D3D;
loc_00559840:
    if (a8 == 0) goto loc_00559836;
    if (a6 != 0) goto loc_0055985F;
    if (a7 == 0) goto loc_0055985F;
    goto loc_00559D54;
loc_0055985F:
    v_stack_m4C = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(a2))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_005598AC;
    if (((unsigned int)((unsigned int)(a2))) <= ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_00559886;
loc_0055987C:
    goto loc_00559D3D;
loc_00559886:
    a3 = 0;
    result = HalpNumaQueryProximityId((unsigned __int16)((unsigned int)(a2)), v_stack_m4C, a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_00559D3D;
loc_005598AC:
    v_stack_m84 = (unsigned int)((unsigned int)(0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(a3))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_005598E2;
    if (((unsigned int)((unsigned int)(a3))) > ((unsigned int)((unsigned int)(0xFFFFULL)))) goto loc_0055987C;
    a3 = 0;
    result = HalpNumaQueryProximityId((unsigned __int16)((unsigned int)(a3)), v_stack_m84, a3, a4);
    a4 = 0;
    if (sign_flag) goto loc_00559D3D;
loc_005598E2:
    v_rbx = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 10710579) + 16))) + (*(unsigned __int64 *)(v_rip + 10710579));
    if ((*(unsigned int *)(v_stack_m68 + 4)) <= 0) goto loc_005599D2;
loc_00559902:
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 4) goto loc_00559912;
    if (((unsigned int)((unsigned int)(v_stack_p20))) != (*(unsigned int *)(v_rbx + 4))) goto loc_005599BC;
loc_00559912:
    result = HalpNumaSystemLocalityInfoIncludeQueryDataType(v_rbx, (unsigned int)(a5), a3, v_stack_m68);
    if ((unsigned __int8)(result) == 0) goto loc_005599BC;
    v_rdi = 0;
    if (((unsigned int)((unsigned int)(v_stack_m4C))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0055995A;
    if (((unsigned int)((unsigned int)(v_stack_m84))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_0055993A;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + 16))) * (*(unsigned int *)(v_rbx + 12)));
    goto loc_005599AC;
loc_0055993A:
    a3 = 0;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(v_rbx, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), a3, v_stack_m68);
    if (sign_flag) goto loc_005599AC;
    goto loc_005599AC;
loc_0055995A:
    a3 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m84))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00559980;
    result = HalpNumaSystemLocalityInfoFindInitiatorIndex(v_rbx, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))), a3, v_stack_m68);
    if (sign_flag) goto loc_005599AC;
    goto loc_005599AC;
loc_00559980:
    result = HalpNumaSystemLocalityInfoFindTargetIndex(v_rbx, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), a3, v_stack_m68);
    v_rdi = (unsigned int)(*(unsigned int *)(v_rbx + 16));
    if (!(sign_flag)) {
        a2 = (unsigned int)((unsigned int)(v_stack_m4C));
        a1 = v_rbx;
        result = HalpNumaSystemLocalityInfoFindInitiatorIndex(a1, a2, a3, v_stack_m68);
        a3 = 1;
        v_rdi = (unsigned int)(*(unsigned int *)(v_rbx + 16));
        if (!sign_flag) { v_rdi = a3; }
    }
loc_005599AC:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 9)) == 0) goto loc_005599B7;
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 9))) == 3) {
        v_rdi = (unsigned int)((v_rdi) + ((unsigned int)(v_rdi)));
    }
    v_r15 = (unsigned int)((0) + ((unsigned int)(v_rdi)));
loc_005599BC:
    v_r14 = (unsigned int)((0) + 1);
    v_rbx = (v_rbx) + ((unsigned int)(*(unsigned int *)(v_rbx)));
    if (((unsigned int)(v_r14)) < (*(unsigned int *)(v_stack_m68 + 4))) goto loc_00559902;
loc_005599D2:
    result = ((unsigned int)((unsigned int)(v_r15))) << (5);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00559D38;
    if (((unsigned int)(result + 8)) < 8) goto loc_00559D38;
    v_rbx = 0;
    if (a7 >= ((unsigned int)(result + 8))) goto loc_00559A09;
    *(unsigned int *)(a8) = (unsigned int)(result + 8);
    goto loc_00559D3D;
loc_00559A09:
    a2 = 0;
    result = memset(a6, a2, (unsigned int)(a7), v_stack_m68);
    v_r11 = 0;
    *(unsigned int *)(a6) = (unsigned int)(v_r15);
    v_r15 = 0;
    v_stack_m78 = 0;
    v_rdi = ((unsigned int)(*(unsigned int *)(v_stack_m68 + 16))) + (*(unsigned __int64 *)(v_rip + 10710029));
    v_r10 = 0;
loc_00559A36:
    v_stack_m84 = 0;
    if (0 >= (*(unsigned int *)(v_stack_m68 + 4))) goto loc_00559D2F;
    if (((unsigned int)((unsigned int)(v_stack_p20))) == 4) goto loc_00559A5B;
    if (((unsigned int)((unsigned int)(v_stack_p20))) != (*(unsigned int *)(v_rdi + 4))) goto loc_00559D08;
loc_00559A5B:
    result = HalpNumaSystemLocalityInfoIncludeQueryDataType(v_rdi, (unsigned int)(a5), (unsigned int)(a7), 4);
    if ((unsigned __int8)(result) == 0) goto loc_00559D08;
    v_stack_m70 = 4;
    v_stack_m6C = 4;
    v_stack_m50 = 1;
    if ((unsigned int)(*(unsigned __int8 *)(v_rdi + 9)) == 0) goto loc_00559ACA;
    a1 = (unsigned int)((*(unsigned __int8 *)(v_rdi + 9)) - (1));
    if (condition_is_equal) goto loc_00559AC4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00559ABB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00559AAF;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00559AAA;
    if (a1 != 1) goto loc_00559D21;
    v_stack_m70 = 3;
    goto loc_00559ADF;
loc_00559AAA:
    v_stack_m70 = 1;
    goto loc_00559ADF;
loc_00559AAF:
    v_stack_m70 = 1;
    v_stack_m6C = 3;
    goto loc_00559AD5;
loc_00559ABB:
    v_stack_m70 = 2;
    goto loc_00559ADF;
loc_00559AC4:
    goto loc_00559ADF;
loc_00559ACA:
    v_stack_m6C = 2;
loc_00559AD5:
    v_stack_m50 = 2;
loc_00559ADF:
    v_stack_m58 = (unsigned int)(*(unsigned int *)(v_rdi + 12));
    v_stack_m48 = v_rdi + (unsigned int)(*(unsigned int *)(v_rdi + 12)) + 8 * 4;
    if (((unsigned int)(*(unsigned int *)(v_rdi + 12)) * 4) > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00559D38;
    v_stack_m60 = (unsigned int)(*(unsigned int *)(v_rdi + 16));
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 16))))) << (2);
    if (result > ((unsigned int)(0xFFFFFFFFULL))) goto loc_00559D38;
    if (((unsigned int)(result + (unsigned int)(*(unsigned int *)(v_rdi + 12)) * 4 * 1)) < ((unsigned int)(result))) goto loc_00559D38;
    v_rbx = 0;
    result = ((unsigned int)((unsigned int)(result + (unsigned int)(*(unsigned int *)(v_rdi + 12)) * 4 * 1))) + (32);
    result = (result) + (v_rdi);
    v_stack_m38 = result;
    if (((unsigned int)((unsigned int)(v_stack_m4C))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00559B7B;
    if (((unsigned int)((unsigned int)(v_stack_m84))) == ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00559BEB;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), v_stack_m7C, (unsigned int)(*(unsigned int *)(v_rdi + 16)));
    if (sign_flag) goto loc_00559BDA;
    a4 = (unsigned int)(((unsigned int)(v_stack_m7C)) + 1);
    v_stack_m60 = a4;
loc_00559B73:
    goto loc_00559BDE;
loc_00559B7B:
    if (((unsigned int)((unsigned int)(v_stack_m84))) != ((unsigned int)((unsigned int)(0xFFFFFFFFULL)))) goto loc_00559BA8;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_m4C))), v_stack_m80, a4);
    if (sign_flag) goto loc_00559BA2;
    a2 = (unsigned int)(((unsigned int)(v_stack_m80)) + 1);
    v_stack_m58 = a2;
    goto loc_00559B73;
loc_00559BA2:
    goto loc_00559BDE;
loc_00559BA8:
    result = HalpNumaSystemLocalityInfoFindInitiatorIndex(v_rdi, v_stack_m58, v_stack_m80, v_stack_m60);
    if (sign_flag) goto loc_00559BD6;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(v_rdi, (unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559BD6;
    a2 = (unsigned int)(((unsigned int)(v_stack_m80)) + 1);
    a4 = (unsigned int)(((unsigned int)(v_stack_m7C)) + 1);
    v_stack_m58 = a2;
    v_stack_m60 = a4;
    goto loc_00559BE7;
loc_00559BD6:
loc_00559BDA:
loc_00559BDE:
    if (1 == 0) goto loc_00559D04;
loc_00559BE7:
loc_00559BEB:
    v_r13 = 0;
loc_00559BF2:
    if (0 >= 2) goto loc_00559D01;
loc_00559C02:
    if (((unsigned int)((unsigned int)(v_stack_m80))) >= ((unsigned int)(v_stack_m58))) goto loc_00559CF5;
loc_00559C13:
    if (((unsigned int)((unsigned int)(v_stack_m7C))) >= ((unsigned int)(v_stack_m60))) goto loc_00559CE9;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m78)))) << (5);
    v_stack_m40 = v_rbx;
    *(unsigned int *)(v_rbx + a6 * 1 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 0 * 4 - 72)));
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rbx + a6 * 1 + 24))) ^ (*(unsigned __int8 *)(v_rdi + 8)));
    a1 = (unsigned __int8)((a1) & (1));
    a1 = (unsigned __int8)((a1) ^ ((unsigned __int8)(*(unsigned __int8 *)(v_rbx + a6 * 1 + 24))));
    *(unsigned __int8 *)(v_rbx + a6 * 1 + 24) = (unsigned __int8)(a1);
    result = (unsigned __int8)(((unsigned __int8)(a1)) ^ (*(unsigned __int8 *)(v_rdi + 8)));
    result = (unsigned __int8)((result) & (2));
    result = (unsigned __int8)((result) ^ ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(v_rbx + a6 * 1 + 24) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rbx + a6 * 1 + 25) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi + 10));
    *(unsigned int *)(v_rbx + a6 * 1 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    result = HalpNumaQueryProximityNode((unsigned int)(*(unsigned int *)(v_rdi + (unsigned int)((unsigned int)((unsigned int)(v_stack_m80))) * 4 + 32)), v_stack_m88, v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559D28;
    *(unsigned int *)(v_rbx + a6 * 1 + 8) = (unsigned int)(v_stack_m88);
    result = HalpNumaQueryProximityNode((unsigned int)(*(unsigned int *)(v_stack_m48 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m7C))) * 4)), v_stack_m88, v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559D28;
    *(unsigned int *)(v_stack_m40 + a6 * 1 + 12) = (unsigned int)(v_stack_m88);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m80)))) * (*(unsigned int *)(v_rdi + 16)));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(v_stack_m7C))));
    a1 = (*(unsigned __int16 *)(v_stack_m38 + result * 2)) * (*(unsigned __int64 *)(v_rdi + 24));
    *(unsigned __int64 *)(v_stack_m40 + a6 * 1 + 32) = a1;
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m78)) + (1));
    v_stack_m78 = (unsigned int)(v_r11);
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m7C)) + (1));
    goto loc_00559C13;
loc_00559CE9:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m80)) + (1));
    goto loc_00559C02;
loc_00559CF5:
    v_r13 = (unsigned int)((v_r13) + (1));
    goto loc_00559BF2;
loc_00559D01:
    v_r15 = 0;
loc_00559D04:
loc_00559D08:
    v_rdi = (v_rdi) + ((unsigned int)(*(unsigned int *)(v_rdi)));
    v_r10 = (unsigned int)(((unsigned int)(v_stack_m84)) + 1);
    goto loc_00559A36;
loc_00559D21:
    goto loc_00559D3D;
loc_00559D28:
    goto loc_00559D3D;
loc_00559D2F:
    *(unsigned int *)(a8) = (unsigned int)(result + 8);
    goto loc_00559D54;
loc_00559D38:
loc_00559D3D:
    result = a6;
    if (a6 != 0) {
        a3 = a7;
        a2 = 0;
        a1 = a6;
        result = memset(a1, a2, a3, v_stack_m60);
    }
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000095ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t HalpNumaQuerySystemLocalityLatencyAndBandwidthInfo(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, int64_t Arg6, uint32_t Arg7, void *Arg8)
{
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint16_t v_stack_m88;
    uint32_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (128);
    Arg4 = 0;
    v_stack_m88 = 0;
    v_stack_m68 = *(uint64_t *)(v_rip + 0xA36E33);
    if (*(uint64_t *)(v_rip + 0xA36E33) != 0) goto loc_0055982D;
    goto loc_00559D3D;
loc_0055982D:
    if (Arg1 == 1) goto loc_00559840;
loc_00559836:
    goto loc_00559D3D;
loc_00559840:
    if (Arg8 == NULL) goto loc_00559836;
    if (Arg6 != 0) goto loc_0055985F;
    if (Arg7 == 0) goto loc_0055985F;
    goto loc_00559D54;
loc_0055985F:
    v_stack_m4C = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(Arg2))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_005598AC;
    if (((uint32_t)((uint32_t)(Arg2))) <= ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_00559886;
loc_0055987C:
    goto loc_00559D3D;
loc_00559886:
    Arg3 = 0;
    result = HalpNumaQueryProximityId((uint16_t)((uint32_t)(Arg2)), v_stack_m4C, Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00559D3D;
loc_005598AC:
    v_stack_m84 = (uint32_t)((uint32_t)(0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(Arg3))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_005598E2;
    if (((uint32_t)((uint32_t)(Arg3))) > ((uint32_t)((uint32_t)(0xFFFFULL)))) goto loc_0055987C;
    Arg3 = 0;
    result = HalpNumaQueryProximityId((uint16_t)((uint32_t)(Arg3)), v_stack_m84, Arg3, Arg4);
    Arg4 = 0;
    if (sign_flag) goto loc_00559D3D;
loc_005598E2:
    local_rbx = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xA36E33) + 0x10))) + (*(uint64_t *)(v_rip + 0xA36E33));
    if ((*(uint32_t *)(v_stack_m68 + 0x4)) <= 0) goto loc_005599D2;
loc_00559902:
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 4) goto loc_00559912;
    if (((uint32_t)((uint32_t)(v_stack_p20))) != (*(uint32_t *)(local_rbx + 0x4))) goto loc_005599BC;
loc_00559912:
    result = HalpNumaSystemLocalityInfoIncludeQueryDataType(local_rbx, (uint32_t)(Arg5), Arg3, v_stack_m68);
    if ((uint8_t)(result) == 0) goto loc_005599BC;
    local_rdi = 0;
    if (((uint32_t)((uint32_t)(v_stack_m4C))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0055995A;
    if (((uint32_t)((uint32_t)(v_stack_m84))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_0055993A;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + 0x10))) * (*(uint32_t *)(local_rbx + 0xC)));
    goto loc_005599AC;
loc_0055993A:
    Arg3 = 0;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(local_rbx, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), Arg3, v_stack_m68);
    if (sign_flag) goto loc_005599AC;
    goto loc_005599AC;
loc_0055995A:
    Arg3 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m84))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00559980;
    result = HalpNumaSystemLocalityInfoFindInitiatorIndex(local_rbx, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))), Arg3, v_stack_m68);
    if (sign_flag) goto loc_005599AC;
    goto loc_005599AC;
loc_00559980:
    result = HalpNumaSystemLocalityInfoFindTargetIndex(local_rbx, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), Arg3, v_stack_m68);
    local_rdi = (uint32_t)(*(uint32_t *)(local_rbx + 0x10));
    if (!(sign_flag)) {
        Arg2 = (uint32_t)((uint32_t)(v_stack_m4C));
        Arg1 = local_rbx;
        result = HalpNumaSystemLocalityInfoFindInitiatorIndex(Arg1, Arg2, Arg3, v_stack_m68);
        Arg3 = 1;
        local_rdi = (uint32_t)(*(uint32_t *)(local_rbx + 0x10));
        if (!sign_flag) { local_rdi = Arg3; }
    }
loc_005599AC:
    if ((uint8_t)(*(uint8_t *)(local_rbx + 0x9)) == 0) goto loc_005599B7;
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x9))) == 3) {
        local_rdi = (uint32_t)((local_rdi) + ((uint32_t)(local_rdi)));
    }
    local_r15 = (uint32_t)((0) + ((uint32_t)(local_rdi)));
loc_005599BC:
    local_r14 = (uint32_t)((0) + 1);
    local_rbx = (local_rbx) + ((uint32_t)(*(uint32_t *)(local_rbx)));
    if (((uint32_t)(local_r14)) < (*(uint32_t *)(v_stack_m68 + 0x4))) goto loc_00559902;
loc_005599D2:
    result = ((uint32_t)((uint32_t)(local_r15))) << (5);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00559D38;
    if (((uint32_t)(result + 8)) < 8) goto loc_00559D38;
    local_rbx = 0;
    if (Arg7 >= ((uint32_t)(result + 8))) goto loc_00559A09;
    *(uint32_t *)(arg8) = (uint32_t)(result + 8);
    goto loc_00559D3D;
loc_00559A09:
    Arg2 = 0;
    result = memset(Arg6, Arg2, (uint32_t)(Arg7), v_stack_m68);
    local_r11 = 0;
    *(uint32_t *)(Arg6) = (uint32_t)(local_r15);
    local_r15 = 0;
    v_stack_m78 = 0;
    local_rdi = ((uint32_t)(*(uint32_t *)(v_stack_m68 + 0x10))) + (*(uint64_t *)(v_rip + 0xA36C0D));
    local_r10 = 0;
loc_00559A36:
    v_stack_m84 = 0;
    if (0 >= (*(uint32_t *)(v_stack_m68 + 0x4))) goto loc_00559D2F;
    if (((uint32_t)((uint32_t)(v_stack_p20))) == 4) goto loc_00559A5B;
    if (((uint32_t)((uint32_t)(v_stack_p20))) != (*(uint32_t *)(local_rdi + 0x4))) goto loc_00559D08;
loc_00559A5B:
    result = HalpNumaSystemLocalityInfoIncludeQueryDataType(local_rdi, (uint32_t)(Arg5), (uint32_t)(Arg7), 4);
    if ((uint8_t)(result) == 0) goto loc_00559D08;
    v_stack_m70 = 4;
    v_stack_m6C = 4;
    v_stack_m50 = 1;
    if ((uint32_t)(*(uint8_t *)(local_rdi + 0x9)) == 0) goto loc_00559ACA;
    Arg1 = (uint32_t)((*(uint8_t *)(local_rdi + 0x9)) - (1));
    if (condition_is_equal) goto loc_00559AC4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00559ABB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00559AAF;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00559AAA;
    if (Arg1 != 1) goto loc_00559D21;
    v_stack_m70 = 3;
    goto loc_00559ADF;
loc_00559AAA:
    v_stack_m70 = 1;
    goto loc_00559ADF;
loc_00559AAF:
    v_stack_m70 = 1;
    v_stack_m6C = 3;
    goto loc_00559AD5;
loc_00559ABB:
    v_stack_m70 = 2;
    goto loc_00559ADF;
loc_00559AC4:
    goto loc_00559ADF;
loc_00559ACA:
    v_stack_m6C = 2;
loc_00559AD5:
    v_stack_m50 = 2;
loc_00559ADF:
    v_stack_m58 = (uint32_t)(*(uint32_t *)(local_rdi + 0xC));
    v_stack_m48 = local_rdi + (uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 8 * 4;
    if (((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) * 4) > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00559D38;
    v_stack_m60 = (uint32_t)(*(uint32_t *)(local_rdi + 0x10));
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x10))))) << (2);
    if (result > ((uint32_t)(0xFFFFFFFFULL))) goto loc_00559D38;
    if (((uint32_t)(result + (uint32_t)(*(uint32_t *)(local_rdi + 0xC)) * 4 * 1)) < ((uint32_t)(result))) goto loc_00559D38;
    local_rbx = 0;
    result = ((uint32_t)((uint32_t)(result + (uint32_t)(*(uint32_t *)(local_rdi + 0xC)) * 4 * 1))) + (32);
    result = (result) + (local_rdi);
    v_stack_m38 = result;
    if (((uint32_t)((uint32_t)(v_stack_m4C))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00559B7B;
    if (((uint32_t)((uint32_t)(v_stack_m84))) == ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00559BEB;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), v_stack_m7C, (uint32_t)(*(uint32_t *)(local_rdi + 0x10)));
    if (sign_flag) goto loc_00559BDA;
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m7C)) + 1);
    v_stack_m60 = Arg4;
loc_00559B73:
    goto loc_00559BDE;
loc_00559B7B:
    if (((uint32_t)((uint32_t)(v_stack_m84))) != ((uint32_t)((uint32_t)(0xFFFFFFFFULL)))) goto loc_00559BA8;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_m4C))), v_stack_m80, Arg4);
    if (sign_flag) goto loc_00559BA2;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m80)) + 1);
    v_stack_m58 = Arg2;
    goto loc_00559B73;
loc_00559BA2:
    goto loc_00559BDE;
loc_00559BA8:
    result = HalpNumaSystemLocalityInfoFindInitiatorIndex(local_rdi, v_stack_m58, v_stack_m80, v_stack_m60);
    if (sign_flag) goto loc_00559BD6;
    result = HalpNumaSystemLocalityInfoFindTargetIndex(local_rdi, (uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559BD6;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m80)) + 1);
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m7C)) + 1);
    v_stack_m58 = Arg2;
    v_stack_m60 = Arg4;
    goto loc_00559BE7;
loc_00559BD6:
loc_00559BDA:
loc_00559BDE:
    if (1 == 0) goto loc_00559D04;
loc_00559BE7:
loc_00559BEB:
    local_r13 = 0;
loc_00559BF2:
    if (0 >= 2) goto loc_00559D01;
loc_00559C02:
    if (((uint32_t)((uint32_t)(v_stack_m80))) >= ((uint32_t)(v_stack_m58))) goto loc_00559CF5;
loc_00559C13:
    if (((uint32_t)((uint32_t)(v_stack_m7C))) >= ((uint32_t)(v_stack_m60))) goto loc_00559CE9;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m78)))) << (5);
    v_stack_m40 = local_rbx;
    *(uint32_t *)(local_rbx + Arg6 * 1 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x0 * 4 - 0x48)));
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(local_rbx + Arg6 * 1 + 0x18))) ^ (*(uint8_t *)(local_rdi + 0x8)));
    Arg1 = (uint8_t)((Arg1) & (1));
    Arg1 = (uint8_t)((Arg1) ^ ((uint8_t)(*(uint8_t *)(local_rbx + Arg6 * 1 + 0x18))));
    *(uint8_t *)(local_rbx + Arg6 * 1 + 0x18) = (uint8_t)(Arg1);
    result = (uint8_t)(((uint8_t)(Arg1)) ^ (*(uint8_t *)(local_rdi + 0x8)));
    result = (uint8_t)((result) & (2));
    result = (uint8_t)((result) ^ ((uint8_t)(Arg1)));
    *(uint8_t *)(local_rbx + Arg6 * 1 + 0x18) = (uint8_t)(result);
    *(uint8_t *)(local_rbx + Arg6 * 1 + 0x19) = (uint8_t)(*(uint8_t *)(local_rdi + 0xA));
    *(uint32_t *)(local_rbx + Arg6 * 1 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    result = HalpNumaQueryProximityNode((uint32_t)(*(uint32_t *)(local_rdi + (uint32_t)((uint32_t)((uint32_t)(v_stack_m80))) * 4 + 0x20)), v_stack_m88, v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559D28;
    *(uint32_t *)(local_rbx + Arg6 * 1 + 0x8) = (uint32_t)(v_stack_m88);
    result = HalpNumaQueryProximityNode((uint32_t)(*(uint32_t *)(v_stack_m48 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m7C))) * 4)), v_stack_m88, v_stack_m7C, v_stack_m60);
    if (sign_flag) goto loc_00559D28;
    *(uint32_t *)(v_stack_m40 + Arg6 * 1 + 0xC) = (uint32_t)(v_stack_m88);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m80)))) * (*(uint32_t *)(local_rdi + 0x10)));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(v_stack_m7C))));
    Arg1 = (*(uint16_t *)(v_stack_m38 + result * 2)) * (*(uint64_t *)(local_rdi + 0x18));
    *(uint64_t *)(v_stack_m40 + Arg6 * 1 + 0x20) = Arg1;
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m78)) + (1));
    v_stack_m78 = (uint32_t)(local_r11);
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m7C)) + (1));
    goto loc_00559C13;
loc_00559CE9:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m80)) + (1));
    goto loc_00559C02;
loc_00559CF5:
    local_r13 = (uint32_t)((local_r13) + (1));
    goto loc_00559BF2;
loc_00559D01:
    local_r15 = 0;
loc_00559D04:
loc_00559D08:
    local_rdi = (local_rdi) + ((uint32_t)(*(uint32_t *)(local_rdi)));
    local_r10 = (uint32_t)(((uint32_t)(v_stack_m84)) + 1);
    goto loc_00559A36;
loc_00559D21:
    goto loc_00559D3D;
loc_00559D28:
    goto loc_00559D3D;
loc_00559D2F:
    *(uint32_t *)(arg8) = (uint32_t)(result + 8);
    goto loc_00559D54;
loc_00559D38:
loc_00559D3D:
    result = Arg6;
    if (Arg6 != 0) {
        Arg3 = Arg7;
        Arg2 = 0;
        Arg1 = Arg6;
        result = memset(Arg1, Arg2, Arg3, v_stack_m60);
    }
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000095ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg8` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005597E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
