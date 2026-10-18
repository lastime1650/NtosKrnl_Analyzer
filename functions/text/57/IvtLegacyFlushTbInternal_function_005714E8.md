# IvtLegacyFlushTbInternal

- RVA: `0x005714E8`–`0x00571C0D` (길이 `1,829` bytes)
- VA: `0x00000001405714E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5294`
- 디코드: `497`개 명령, `1,829/1,829` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00571721` → [IvtIommuSendCommand](../46/IvtIommuSendCommand_function_0046A6E4.md) (function, `0x0046A6E4`)
- `0x005717B1` → [HalpIommuGetNextFlushDevice](../4F/HalpIommuGetNextFlushDevice_function_004FB8E8.md) (function, `0x004FB8E8`)
- `0x00571835` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00571A59` → [IvtIommuSendCommand](../46/IvtIommuSendCommand_function_0046A6E4.md) (function, `0x0046A6E4`)
- `0x00571A9D` → [HalpIommuGetNextFlushDevice](../4F/HalpIommuGetNextFlushDevice_function_004FB8E8.md) (function, `0x004FB8E8`)
- `0x00571B3B` → [IvtIommuWaitCommand](../46/IvtIommuWaitCommand_function_0046A594.md) (function, `0x0046A594`)
- `0x00571B51` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00571B99` → [HalpIommuGetNextFlushDevice](../4F/HalpIommuGetNextFlushDevice_function_004FB8E8.md) (function, `0x004FB8E8`)
- `0x00571BD8` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00571BE6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IvtLegacyAttachDeviceDomainInternal](IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x00571119`
- [IvtLegacyAttachDeviceDomainInternal](IvtLegacyAttachDeviceDomainInternal_function_00570EDC.md) at `0x00571145`
- [IvtLegacyFlushDomainTb](IvtLegacyFlushDomainTb_function_00571420.md) at `0x00571471`
- [IvtLegacyFlushTb](IvtLegacyFlushTb_function_005714A0.md) at `0x005714D6`
- [IvtInitializeIommu](../../pagelk/B6/IvtInitializeIommu_function_00B61FE0.md) at `0x00B62104`

### Static image references
- `0x0057150B` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005714E8  48 8B C4                        mov rax, rsp
005714EB  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
005714EF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
005714F3  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
005714F7  55                              push rbp
005714F8  41 54                           push r12
005714FA  41 55                           push r13
005714FC  41 56                           push r14
005714FE  41 57                           push r15
00571500  48 8D 68 C1                     lea rbp, [rax - 0x3f]
00571504  48 81 EC D0 00 00 00            sub rsp, 0xd0
0057150B  48 8B 05 2E 92 89 00            mov rax, qword ptr [rip + 0x89922e]
00571512  48 33 C4                        xor rax, rsp
00571515  48 89 45 07                     mov qword ptr [rbp + 7], rax
00571519  48 8B 75 67                     mov rsi, qword ptr [rbp + 0x67]
0057151D  45 33 DB                        xor r11d, r11d
00571520  4C 8B 7D 6F                     mov r15, qword ptr [rbp + 0x6f]
00571524  0F 57 C0                        xorps xmm0, xmm0
00571527  44 88 4D 87                     mov byte ptr [rbp - 0x79], r9b
0057152B  4C 8B E9                        mov r13, rcx
0057152E  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00571532  45 8A D1                        mov r10b, r9b
00571535  48 89 4D D7                     mov qword ptr [rbp - 0x29], rcx
00571539  8B C2                           mov eax, edx
0057153B  89 55 C7                        mov dword ptr [rbp - 0x39], edx
0057153E  48 89 75 DF                     mov qword ptr [rbp - 0x21], rsi
00571542  4C 89 5D 9F                     mov qword ptr [rbp - 0x61], r11
00571546  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
0057154A  44 88 5D 89                     mov byte ptr [rbp - 0x77], r11b
0057154E  44 89 5D 8F                     mov dword ptr [rbp - 0x71], r11d
00571552  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
00571556  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
0057155A  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
0057155E  45 84 C9                        test r9b, r9b
00571561  75 58                           jne 0x1405715bb
00571563  83 F8 FF                        cmp eax, -1
00571566  75 2E                           jne 0x140571596
00571568  49 0F BA A5 D8 00 00 00 27      bt qword ptr [r13 + 0xd8], 0x27
00571571  44 88 5D 88                     mov byte ptr [rbp - 0x78], r11b
00571575  45 8A E3                        mov r12b, r11b
00571578  73 0B                           jae 0x140571585
0057157A  48 83 4D FF 40                  or qword ptr [rbp - 1], 0x40
0057157F  41 8D 5B 32                     lea ebx, [r11 + 0x32]
00571583  EB 05                           jmp 0x14057158a
00571585  BB 22 00 00 00                  mov ebx, 0x22
0057158A  48 81 CB C0 00 00 00            or rbx, 0xc0
00571591  E9 88 00 00 00                  jmp 0x14057161e
00571596  8B D8                           mov ebx, eax
00571598  81 E3 FF FF 0F 00               and ebx, 0xfffff
0057159E  48 C1 E3 20                     shl rbx, 0x20
005715A2  44 39 5D 77                     cmp dword ptr [rbp + 0x77], r11d
005715A6  75 06                           jne 0x1405715ae
005715A8  48 83 CB 26                     or rbx, 0x26
005715AC  EB 69                           jmp 0x140571617
005715AE  41 B4 01                        mov r12b, 1
005715B1  48 83 CB 36                     or rbx, 0x36
005715B5  44 88 65 88                     mov byte ptr [rbp - 0x78], r12b
005715B9  EB 63                           jmp 0x14057161e
005715BB  4D 85 C0                        test r8, r8
005715BE  74 52                           je 0x140571612
005715C0  44 39 5D 77                     cmp dword ptr [rbp + 0x77], r11d
005715C4  74 15                           je 0x1405715db
005715C6  49 0F BA A5 D8 00 00 00 27      bt qword ptr [r13 + 0xd8], 0x27
005715CF  73 0A                           jae 0x1405715db
005715D1  41 B4 01                        mov r12b, 1
005715D4  B9 32 00 00 00                  mov ecx, 0x32
005715D9  EB 08                           jmp 0x1405715e3
005715DB  45 8A E3                        mov r12b, r11b
005715DE  B9 22 00 00 00                  mov ecx, 0x22
005715E3  41 8B 40 30                     mov eax, dword ptr [r8 + 0x30]
005715E7  48 C1 E0 10                     shl rax, 0x10
005715EB  48 8B D8                        mov rbx, rax
005715EE  44 88 65 88                     mov byte ptr [rbp - 0x78], r12b
005715F2  48 33 D9                        xor rbx, rcx
005715F5  48 B9 FF FF 00 00 FF FF FF FF   movabs rcx, 0xffffffff0000ffff
005715FF  48 23 D9                        and rbx, rcx
00571602  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00571606  48 33 D8                        xor rbx, rax
00571609  48 81 CB C0 00 00 00            or rbx, 0xc0
00571610  EB 0C                           jmp 0x14057161e
00571612  BB 12 00 00 00                  mov ebx, 0x12
00571617  44 88 5D 88                     mov byte ptr [rbp - 0x78], r11b
0057161B  45 8A E3                        mov r12b, r11b
0057161E  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
00571622  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
00571626  48 85 F6                        test rsi, rsi
00571629  75 0E                           jne 0x140571639
0057162B  4D 85 FF                        test r15, r15
0057162E  75 09                           jne 0x140571639
00571630  41 8A FB                        mov dil, r11b
00571633  44 88 5D 8A                     mov byte ptr [rbp - 0x76], r11b
00571637  EB 10                           jmp 0x140571649
00571639  40 B7 01                        mov dil, 1
0057163C  40 8A C7                        mov al, dil
0057163F  40 88 7D 8A                     mov byte ptr [rbp - 0x76], dil
00571643  44 39 5D 77                     cmp dword ptr [rbp + 0x77], r11d
00571647  75 03                           jne 0x14057164c
00571649  41 8A C3                        mov al, r11b
0057164C  88 45 8B                        mov byte ptr [rbp - 0x75], al
0057164F  45 8B CB                        mov r9d, r11d
00571652  44 88 5D 8C                     mov byte ptr [rbp - 0x74], r11b
00571656  4C 89 5D CF                     mov qword ptr [rbp - 0x31], r11
0057165A  44 89 5D 93                     mov dword ptr [rbp - 0x6d], r11d
0057165E  44 89 5D 97                     mov dword ptr [rbp - 0x69], r11d
00571662  45 84 E4                        test r12b, r12b
00571665  75 04                           jne 0x14057166b
00571667  84 C0                           test al, al
00571669  74 5F                           je 0x1405716ca
0057166B  41 8B C1                        mov eax, r9d
0057166E  48 8B 14 C1                     mov rdx, qword ptr [rcx + rax*8]
00571672  48 8B C2                        mov rax, rdx
00571675  4C 8B C2                        mov r8, rdx
00571678  48 C1 E8 0A                     shr rax, 0xa
0057167C  83 E0 03                        and eax, 3
0057167F  49 C1 E8 0C                     shr r8, 0xc
00571683  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
00571687  8D 0C C0                        lea ecx, [rax + rax*8]
0057168A  89 4D 93                        mov dword ptr [rbp - 0x6d], ecx
0057168D  81 E2 FF 03 00 00               and edx, 0x3ff
00571693  74 30                           je 0x1405716c5
00571695  B8 01 00 00 00                  mov eax, 1
0057169A  48 D3 E0                        shl rax, cl
0057169D  48 0F AF C2                     imul rax, rdx
005716A1  49 03 C0                        add rax, r8
005716A4  49 33 C0                        xor rax, r8
005716A7  48 0F BD C8                     bsr rcx, rax
005716AB  B8 01 00 00 00                  mov eax, 1
005716B0  FF C1                           inc ecx
005716B2  48 D3 E0                        shl rax, cl
005716B5  48 FF C8                        dec rax
005716B8  89 4D 93                        mov dword ptr [rbp - 0x6d], ecx
005716BB  48 F7 D0                        not rax
005716BE  4C 23 C0                        and r8, rax
005716C1  4C 89 45 CF                     mov qword ptr [rbp - 0x31], r8
005716C5  45 84 E4                        test r12b, r12b
005716C8  75 07                           jne 0x1405716d1
005716CA  45 85 C9                        test r9d, r9d
005716CD  75 6A                           jne 0x140571739
005716CF  EB 46                           jmp 0x140571717
005716D1  45 84 D2                        test r10b, r10b
005716D4  74 24                           je 0x1405716fa
005716D6  41 0F B7 85 DE 00 00 00         movzx eax, word ptr [r13 + 0xde]
005716DE  83 E0 3F                        and eax, 0x3f
005716E1  3B C8                           cmp ecx, eax
005716E3  76 15                           jbe 0x1405716fa
005716E5  48 83 E3 EF                     and rbx, 0xffffffffffffffef
005716E9  44 88 5D 88                     mov byte ptr [rbp - 0x78], r11b
005716ED  48 83 CB 20                     or rbx, 0x20
005716F1  45 8A E3                        mov r12b, r11b
005716F4  48 89 5D F7                     mov qword ptr [rbp - 9], rbx
005716F8  EB 1D                           jmp 0x140571717
005716FA  48 8B 45 FF                     mov rax, qword ptr [rbp - 1]
005716FE  83 E1 3F                        and ecx, 0x3f
00571701  25 C0 0F 00 00                  and eax, 0xfc0
00571706  48 0B C8                        or rcx, rax
00571709  49 8B C0                        mov rax, r8
0057170C  48 C1 E0 0C                     shl rax, 0xc
00571710  48 0B C8                        or rcx, rax
00571713  48 89 4D FF                     mov qword ptr [rbp - 1], rcx
00571717  45 33 C0                        xor r8d, r8d
0057171A  48 8D 55 F7                     lea rdx, [rbp - 9]
0057171E  49 8B CD                        mov rcx, r13
00571721  E8 BE 8F EF FF                  call 0x14046a6e4
00571726  48 8B 5D F7                     mov rbx, qword ptr [rbp - 9]
0057172A  45 33 DB                        xor r11d, r11d
0057172D  44 8B 4D 97                     mov r9d, dword ptr [rbp - 0x69]
00571731  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
00571735  48 89 5D BF                     mov qword ptr [rbp - 0x41], rbx
00571739  40 84 FF                        test dil, dil
0057173C  0F 84 D5 03 00 00               je 0x140571b17
00571742  4C 89 7D B7                     mov qword ptr [rbp - 0x49], r15
00571746  48 85 F6                        test rsi, rsi
00571749  74 37                           je 0x140571782
0057174B  48 8B 7E 30                     mov rdi, qword ptr [rsi + 0x30]
0057174F  44 8B 76 3C                     mov r14d, dword ptr [rsi + 0x3c]
00571753  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
00571757  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
0057175B  45 84 D2                        test r10b, r10b
0057175E  75 0F                           jne 0x14057176f
00571760  48 8B 46 60                     mov rax, qword ptr [rsi + 0x60]
00571764  8B 48 30                        mov ecx, dword ptr [rax + 0x30]
00571767  C1 E9 0B                        shr ecx, 0xb
0057176A  80 E1 01                        and cl, 1
0057176D  EB 03                           jmp 0x140571772
0057176F  41 8A CB                        mov cl, r11b
00571772  48 8D 46 40                     lea rax, [rsi + 0x40]
00571776  88 4D 89                        mov byte ptr [rbp - 0x77], cl
00571779  48 8D 75 8C                     lea rsi, [rbp - 0x74]
0057177D  E9 96 00 00 00                  jmp 0x140571818
00571782  45 84 D2                        test r10b, r10b
00571785  75 4C                           jne 0x1405717d3
00571787  48 8D 45 A7                     lea rax, [rbp - 0x59]
0057178B  49 8B CF                        mov rcx, r15
0057178E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00571793  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00571797  48 8D 45 9F                     lea rax, [rbp - 0x61]
0057179B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005717A0  4C 8D 45 AF                     lea r8, [rbp - 0x51]
005717A4  48 8D 45 89                     lea rax, [rbp - 0x77]
005717A8  48 8D 55 B7                     lea rdx, [rbp - 0x49]
005717AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005717B1  E8 32 A1 F8 FF                  call 0x1404fb8e8
005717B6  45 33 DB                        xor r11d, r11d
005717B9  84 C0                           test al, al
005717BB  0F 84 52 03 00 00               je 0x140571b13
005717C1  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
005717C5  44 8B 75 8F                     mov r14d, dword ptr [rbp - 0x71]
005717C9  48 8B 7D AF                     mov rdi, qword ptr [rbp - 0x51]
005717CD  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
005717D1  EB 4D                           jmp 0x140571820
005717D3  49 8B 37                        mov rsi, qword ptr [r15]
005717D6  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
005717DA  44 88 5D 89                     mov byte ptr [rbp - 0x77], r11b
005717DE  49 3B F7                        cmp rsi, r15
005717E1  75 19                           jne 0x1405717fc
005717E3  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
005717E7  4C 89 5D AF                     mov qword ptr [rbp - 0x51], r11
005717EB  44 89 5D 8F                     mov dword ptr [rbp - 0x71], r11d
005717EF  4C 89 5D 9F                     mov qword ptr [rbp - 0x61], r11
005717F3  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
005717F7  E9 1B 03 00 00                  jmp 0x140571b17
005717FC  48 8B 46 D8                     mov rax, qword ptr [rsi - 0x28]
00571800  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
00571804  44 8B 70 3C                     mov r14d, dword ptr [rax + 0x3c]
00571808  48 83 C0 40                     add rax, 0x40
0057180C  48 83 C6 2C                     add rsi, 0x2c
00571810  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
00571814  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
00571818  48 89 75 A7                     mov qword ptr [rbp - 0x59], rsi
0057181C  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00571820  44 8B 4D 93                     mov r9d, dword ptr [rbp - 0x6d]
00571824  4C 8B 65 CF                     mov r12, qword ptr [rbp - 0x31]
00571828  41 8D 59 FF                     lea ebx, [r9 - 1]
0057182C  44 38 1E                        cmp byte ptr [rsi], r11b
0057182F  75 1F                           jne 0x140571850
00571831  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00571835  E8 E6 4D CA FF                  call 0x140216620
0057183A  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
0057183E  45 33 DB                        xor r11d, r11d
00571841  84 C0                           test al, al
00571843  0F 84 1C 02 00 00               je 0x140571a65
00571849  44 8B 4D 93                     mov r9d, dword ptr [rbp - 0x6d]
0057184D  C6 06 01                        mov byte ptr [rsi], 1
00571850  0F 57 C0                        xorps xmm0, xmm0
00571853  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
00571857  45 84 D2                        test r10b, r10b
0057185A  0F 85 3E 01 00 00               jne 0x14057199e
00571860  8B 45 C7                        mov eax, dword ptr [rbp - 0x39]
00571863  83 F8 FF                        cmp eax, -1
00571866  75 68                           jne 0x1405718d0
00571868  44 38 5D 89                     cmp byte ptr [rbp - 0x77], r11b
0057186C  75 57                           jne 0x1405718c5
0057186E  44 39 5D 97                     cmp dword ptr [rbp - 0x69], r11d
00571872  0F 85 ED 01 00 00               jne 0x140571a65
00571878  0F B7 D7                        movzx edx, di
0057187B  48 C1 E2 20                     shl rdx, 0x20
0057187F  48 83 CA 03                     or rdx, 3
00571883  49 0F BA A5 E0 00 00 00 29      bt qword ptr [r13 + 0xe0], 0x29
0057188C  73 18                           jae 0x1405718a6
0057188E  48 8B C7                        mov rax, rdi
00571891  83 E7 0F                        and edi, 0xf
00571894  48 83 E0 F0                     and rax, 0xfffffffffffffff0
00571898  48 C1 E0 24                     shl rax, 0x24
0057189C  48 0B C7                        or rax, rdi
0057189F  48 C1 E0 0C                     shl rax, 0xc
005718A3  48 0B D0                        or rdx, rax
005718A6  41 8B CE                        mov ecx, r14d
005718A9  48 C1 E1 10                     shl rcx, 0x10
005718AD  48 8B C1                        mov rax, rcx
005718B0  48 33 C2                        xor rax, rdx
005718B3  48 25 FF FF E0 FF               and rax, 0xffffffffffe0ffff
005718B9  48 33 C1                        xor rax, rcx
005718BC  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
005718C0  E9 8A 01 00 00                  jmp 0x140571a4f
005718C5  48 8B 45 E7                     mov rax, qword ptr [rbp - 0x19]
005718C9  BA 01 00 00 00                  mov edx, 1
005718CE  EB 0D                           jmp 0x1405718dd
005718D0  48 8B 55 EF                     mov rdx, qword ptr [rbp - 0x11]
005718D4  25 FF FF 0F 00                  and eax, 0xfffff
005718D9  48 C1 E0 20                     shl rax, 0x20
005718DD  44 0F B7 C7                     movzx r8d, di
005718E1  48 B9 F8 FF 00 00 FF FF FF FF   movabs rcx, 0xffffffff0000fff8
005718EB  49 C1 E0 10                     shl r8, 0x10
005718EF  48 23 C1                        and rax, rcx
005718F2  4C 0B C0                        or r8, rax
005718F5  49 83 C8 08                     or r8, 8
005718F9  49 0F BA A5 E0 00 00 00 29      bt qword ptr [r13 + 0xe0], 0x29
00571902  73 2B                           jae 0x14057192f
00571904  49 8B C0                        mov rax, r8
00571907  48 8B CF                        mov rcx, rdi
0057190A  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0057190E  83 E7 0F                        and edi, 0xf
00571911  48 C1 E1 24                     shl rcx, 0x24
00571915  49 B8 FF 0F FF FF FF FF 0F 00   movabs r8, 0xfffffffff0fff
0057191F  48 0B CF                        or rcx, rdi
00571922  49 23 C0                        and rax, r8
00571925  48 C1 E1 0C                     shl rcx, 0xc
00571929  4C 8B C1                        mov r8, rcx
0057192C  4C 0B C0                        or r8, rax
0057192F  41 8B CE                        mov ecx, r14d
00571932  48 C1 E1 04                     shl rcx, 4
00571936  48 8B C1                        mov rax, rcx
00571939  49 33 C0                        xor rax, r8
0057193C  48 25 0F FE FF FF               and rax, 0xfffffffffffffe0f
00571942  48 33 C1                        xor rax, rcx
00571945  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00571949  44 39 5D 77                     cmp dword ptr [rbp + 0x77], r11d
0057194D  75 18                           jne 0x140571967
0057194F  81 E2 FF 07 00 00               and edx, 0x7ff
00571955  48 B8 00 F8 FF FF FF FF FF 7F   movabs rax, 0x7ffffffffffff800
0057195F  48 0B D0                        or rdx, rax
00571962  E9 E4 00 00 00                  jmp 0x140571a4b
00571967  45 85 C9                        test r9d, r9d
0057196A  75 0F                           jne 0x14057197b
0057196C  81 E2 FF 0F 00 00               and edx, 0xfff
00571972  49 8B C4                        mov rax, r12
00571975  48 C1 E0 0C                     shl rax, 0xc
00571979  EB E4                           jmp 0x14057195f
0057197B  81 E2 FE 0F 00 00               and edx, 0xffe
00571981  8B CB                           mov ecx, ebx
00571983  B8 01 00 00 00                  mov eax, 1
00571988  48 D3 E0                        shl rax, cl
0057198B  48 FF C8                        dec rax
0057198E  49 0B C4                        or rax, r12
00571991  48 C1 E0 0C                     shl rax, 0xc
00571995  48 0B C2                        or rax, rdx
00571998  48 83 C8 01                     or rax, 1
0057199C  EB 64                           jmp 0x140571a02
0057199E  0F B7 D7                        movzx edx, di
005719A1  48 C1 E2 20                     shl rdx, 0x20
005719A5  48 83 CA 03                     or rdx, 3
005719A9  49 0F BA A5 E0 00 00 00 29      bt qword ptr [r13 + 0xe0], 0x29
005719B2  73 18                           jae 0x1405719cc
005719B4  48 8B C7                        mov rax, rdi
005719B7  83 E7 0F                        and edi, 0xf
005719BA  48 83 E0 F0                     and rax, 0xfffffffffffffff0
005719BE  48 C1 E0 24                     shl rax, 0x24
005719C2  48 0B C7                        or rax, rdi
005719C5  48 C1 E0 0C                     shl rax, 0xc
005719C9  48 0B D0                        or rdx, rax
005719CC  41 8B CE                        mov ecx, r14d
005719CF  48 C1 E1 10                     shl rcx, 0x10
005719D3  48 8B C1                        mov rax, rcx
005719D6  48 33 C2                        xor rax, rdx
005719D9  48 25 FF FF E0 FF               and rax, 0xffffffffffe0ffff
005719DF  48 33 C1                        xor rax, rcx
005719E2  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
005719E6  44 39 5D 77                     cmp dword ptr [rbp + 0x77], r11d
005719EA  75 1C                           jne 0x140571a08
005719EC  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
005719F0  48 B9 01 F0 FF FF FF FF FF 7F   movabs rcx, 0x7ffffffffffff001
005719FA  25 FE 0F 00 00                  and eax, 0xffe
005719FF  48 0B C1                        or rax, rcx
00571A02  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
00571A06  EB 47                           jmp 0x140571a4f
00571A08  45 85 C9                        test r9d, r9d
00571A0B  75 1A                           jne 0x140571a27
00571A0D  48 8B 4D EF                     mov rcx, qword ptr [rbp - 0x11]
00571A11  49 8B C4                        mov rax, r12
00571A14  81 E1 FF 0F 00 00               and ecx, 0xfff
00571A1A  48 C1 E0 0C                     shl rax, 0xc
00571A1E  48 0B C8                        or rcx, rax
00571A21  48 89 4D EF                     mov qword ptr [rbp - 0x11], rcx
00571A25  EB 28                           jmp 0x140571a4f
00571A27  48 8B 45 EF                     mov rax, qword ptr [rbp - 0x11]
00571A2B  8B CB                           mov ecx, ebx
00571A2D  25 FE 0F 00 00                  and eax, 0xffe
00571A32  BA 01 00 00 00                  mov edx, 1
00571A37  48 D3 E2                        shl rdx, cl
00571A3A  48 FF CA                        dec rdx
00571A3D  49 0B D4                        or rdx, r12
00571A40  48 C1 E2 0C                     shl rdx, 0xc
00571A44  48 0B D0                        or rdx, rax
00571A47  48 83 CA 01                     or rdx, 1
00571A4B  48 89 55 EF                     mov qword ptr [rbp - 0x11], rdx
00571A4F  45 33 C0                        xor r8d, r8d
00571A52  48 8D 55 E7                     lea rdx, [rbp - 0x19]
00571A56  49 8B CD                        mov rcx, r13
00571A59  E8 86 8C EF FF                  call 0x14046a6e4
00571A5E  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
00571A62  45 33 DB                        xor r11d, r11d
00571A65  4D 85 FF                        test r15, r15
00571A68  0F 84 95 00 00 00               je 0x140571b03
00571A6E  45 84 D2                        test r10b, r10b
00571A71  75 4F                           jne 0x140571ac2
00571A73  48 8D 45 A7                     lea rax, [rbp - 0x59]
00571A77  49 8B CF                        mov rcx, r15
00571A7A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00571A7F  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00571A83  48 8D 45 9F                     lea rax, [rbp - 0x61]
00571A87  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00571A8C  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00571A90  48 8D 45 89                     lea rax, [rbp - 0x77]
00571A94  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00571A98  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00571A9D  E8 46 9E F8 FF                  call 0x1404fb8e8
00571AA2  45 33 DB                        xor r11d, r11d
00571AA5  84 C0                           test al, al
00571AA7  74 5A                           je 0x140571b03
00571AA9  48 8B 75 A7                     mov rsi, qword ptr [rbp - 0x59]
00571AAD  44 8B 75 8F                     mov r14d, dword ptr [rbp - 0x71]
00571AB1  48 8B 7D AF                     mov rdi, qword ptr [rbp - 0x51]
00571AB5  44 8B 4D 93                     mov r9d, dword ptr [rbp - 0x6d]
00571AB9  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
00571ABD  E9 6A FD FF FF                  jmp 0x14057182c
00571AC2  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00571AC6  48 8B 30                        mov rsi, qword ptr [rax]
00571AC9  48 89 75 B7                     mov qword ptr [rbp - 0x49], rsi
00571ACD  49 3B F7                        cmp rsi, r15
00571AD0  74 31                           je 0x140571b03
00571AD2  48 8B 46 D8                     mov rax, qword ptr [rsi - 0x28]
00571AD6  44 8B 4D 93                     mov r9d, dword ptr [rbp - 0x6d]
00571ADA  44 88 5D 89                     mov byte ptr [rbp - 0x77], r11b
00571ADE  48 8B 78 30                     mov rdi, qword ptr [rax + 0x30]
00571AE2  44 8B 70 3C                     mov r14d, dword ptr [rax + 0x3c]
00571AE6  48 83 C0 40                     add rax, 0x40
00571AEA  48 83 C6 2C                     add rsi, 0x2c
00571AEE  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
00571AF2  48 89 75 A7                     mov qword ptr [rbp - 0x59], rsi
00571AF6  44 89 75 8F                     mov dword ptr [rbp - 0x71], r14d
00571AFA  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00571AFE  E9 29 FD FF FF                  jmp 0x14057182c
00571B03  48 8B 5D BF                     mov rbx, qword ptr [rbp - 0x41]
00571B07  44 8A 65 88                     mov r12b, byte ptr [rbp - 0x78]
00571B0B  48 8B 75 DF                     mov rsi, qword ptr [rbp - 0x21]
00571B0F  40 8A 7D 8A                     mov dil, byte ptr [rbp - 0x76]
00571B13  44 8B 4D 97                     mov r9d, dword ptr [rbp - 0x69]
00571B17  44 8A 55 87                     mov r10b, byte ptr [rbp - 0x79]
00571B1B  41 FF C1                        inc r9d
00571B1E  8A 45 8B                        mov al, byte ptr [rbp - 0x75]
00571B21  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00571B25  44 89 4D 97                     mov dword ptr [rbp - 0x69], r9d
00571B29  44 3B 4D 77                     cmp r9d, dword ptr [rbp + 0x77]
00571B2D  0F 82 2F FB FF FF               jb 0x140571662
00571B33  45 33 C0                        xor r8d, r8d
00571B36  33 D2                           xor edx, edx
00571B38  49 8B CD                        mov rcx, r13
00571B3B  E8 54 8A EF FF                  call 0x14046a594
00571B40  45 33 F6                        xor r14d, r14d
00571B43  44 38 75 8C                     cmp byte ptr [rbp - 0x74], r14b
00571B47  74 0D                           je 0x140571b56
00571B49  48 8D 4E 40                     lea rcx, [rsi + 0x40]
00571B4D  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
00571B51  E8 2A 83 DD FF                  call 0x140349e80
00571B56  4D 85 FF                        test r15, r15
00571B59  0F 84 80 00 00 00               je 0x140571bdf
00571B5F  40 8A 7D 87                     mov dil, byte ptr [rbp - 0x79]
00571B63  49 8B DF                        mov rbx, r15
00571B66  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
00571B6A  40 84 FF                        test dil, dil
00571B6D  75 41                           jne 0x140571bb0
00571B6F  48 8D 45 A7                     lea rax, [rbp - 0x59]
00571B73  49 8B CF                        mov rcx, r15
00571B76  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00571B7B  4C 8D 4D 8F                     lea r9, [rbp - 0x71]
00571B7F  48 8D 45 9F                     lea rax, [rbp - 0x61]
00571B83  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00571B88  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00571B8C  48 8D 45 89                     lea rax, [rbp - 0x77]
00571B90  48 8D 55 B7                     lea rdx, [rbp - 0x49]
00571B94  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00571B99  E8 4A 9D F8 FF                  call 0x1404fb8e8
00571B9E  84 C0                           test al, al
00571BA0  74 3D                           je 0x140571bdf
00571BA2  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00571BA6  48 8B 45 A7                     mov rax, qword ptr [rbp - 0x59]
00571BAA  48 8B 5D B7                     mov rbx, qword ptr [rbp - 0x49]
00571BAE  EB 20                           jmp 0x140571bd0
00571BB0  48 8B 1B                        mov rbx, qword ptr [rbx]
00571BB3  48 89 5D B7                     mov qword ptr [rbp - 0x49], rbx
00571BB7  49 3B DF                        cmp rbx, r15
00571BBA  74 23                           je 0x140571bdf
00571BBC  48 8B 4B D8                     mov rcx, qword ptr [rbx - 0x28]
00571BC0  48 8D 43 2C                     lea rax, [rbx + 0x2c]
00571BC4  48 83 C1 40                     add rcx, 0x40
00571BC8  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
00571BCC  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
00571BD0  44 38 30                        cmp byte ptr [rax], r14b
00571BD3  74 95                           je 0x140571b6a
00571BD5  44 88 30                        mov byte ptr [rax], r14b
00571BD8  E8 A3 82 DD FF                  call 0x140349e80
00571BDD  EB 8B                           jmp 0x140571b6a
00571BDF  48 8B 4D 07                     mov rcx, qword ptr [rbp + 7]
00571BE3  48 33 CC                        xor rcx, rsp
00571BE6  E8 55 AA 13 00                  call 0x1406ac640
00571BEB  4C 8D 9C 24 D0 00 00 00         lea r11, [rsp + 0xd0]
00571BF3  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00571BF7  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00571BFB  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00571BFF  49 8B E3                        mov rsp, r11
00571C02  41 5F                           pop r15
00571C04  41 5E                           pop r14
00571C06  41 5D                           pop r13
00571C08  41 5C                           pop r12
00571C0A  5D                              pop rbp
00571C0B  C3                              ret
00571C0C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtLegacyFlushTbInternal(__int64 a1, int a2, __int64 a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 9015854)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 63 + 7) = result;
    v_r11 = 0;
    *(unsigned __int8 *)(v_rsp - 63 - 121) = a4;
    *(unsigned __int64 *)(v_rsp - 63 - 41) = *(unsigned __int64 *)(v_rsp - 63 + 127);
    *(unsigned int *)(v_rsp - 63 - 57) = a2;
    *(unsigned __int64 *)(v_rsp - 63 - 33) = *(unsigned __int64 *)(v_rsp - 63 + 103);
    *(unsigned __int64 *)(v_rsp - 63 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 89) = 0;
    *(unsigned __int8 *)(v_rsp - 63 - 119) = 0;
    *(unsigned int *)(v_rsp - 63 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 81) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 25) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 63 - 9) = v_xmm0;
    if (a4 != 0) goto loc_005715BB;
    if (((unsigned int)((unsigned int)(a2))) != -1) goto loc_00571596;
    *(unsigned __int8 *)(v_rsp - 63 - 120) = 0;
    if (((unsigned int)((unsigned int)(a2))) >= -1) goto loc_00571585;
    goto loc_0057158A;
loc_00571585:
loc_0057158A:
    v_rbx = (34) | (192);
    goto loc_0057161E;
loc_00571596:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (0xFFFFFULL));
    v_rbx = (v_rbx) << (32);
    if ((*(unsigned int *)(v_rsp - 63 + 119)) != 0) goto loc_005715AE;
    v_rbx = (v_rbx) | (38);
    goto loc_00571617;
loc_005715AE:
    v_rbx = (v_rbx) | (54);
    *(unsigned __int8 *)(v_rsp - 63 - 120) = 1;
    goto loc_0057161E;
loc_005715BB:
    if (a3 == 0) goto loc_00571612;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) == 0) goto loc_005715DB;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) >= 0) goto loc_005715DB;
    goto loc_005715E3;
loc_005715DB:
loc_005715E3:
    result = ((unsigned int)(*(unsigned int *)(a3 + 48))) << (16);
    *(unsigned __int8 *)(v_rsp - 63 - 120) = 0;
    v_rbx = (result) ^ (34);
    v_rbx = (v_rbx) & (34);
    v_rbx = (v_rbx) ^ (result);
    v_rbx = (v_rbx) | (192);
    goto loc_0057161E;
loc_00571612:
loc_00571617:
    *(unsigned __int8 *)(v_rsp - 63 - 120) = 0;
loc_0057161E:
    *(unsigned __int64 *)(v_rsp - 63 - 65) = 18;
    *(unsigned __int64 *)(v_rsp - 63 - 9) = 18;
    if (*(unsigned __int64 *)(v_rsp - 63 + 103) != 0) goto loc_00571639;
    if (*(unsigned __int64 *)(v_rsp - 63 + 111) != 0) goto loc_00571639;
    *(unsigned __int8 *)(v_rsp - 63 - 118) = 0;
    goto loc_00571649;
loc_00571639:
    *(unsigned __int8 *)(v_rsp - 63 - 118) = 1;
    result = 1;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) == 0) {
        result = 0;
    }
    *(unsigned __int8 *)(v_rsp - 63 - 117) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_rsp - 63 - 116) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 49) = 0;
    *(unsigned int *)(v_rsp - 63 - 109) = 0;
    *(unsigned int *)(v_rsp - 63 - 105) = 0;
loc_00571662:
    if (0 != 0) goto loc_0057166B;
    if ((unsigned __int8)(result) == 0) goto loc_005716CA;
loc_0057166B:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 41) + 0 * 8)) >> (10);
    result = (unsigned int)((result) & (3));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 41) + 0 * 8)) >> (12);
    *(unsigned __int64 *)(v_rsp - 63 - 49) = a3;
    *(unsigned int *)(v_rsp - 63 - 109) = (unsigned int)(result + result * 8);
    a2 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 41) + 0 * 8)) & (0x3FFULL));
    if (!(condition_is_equal)) {
        result = 1;
        result = (result) << ((unsigned __int8)(result + result * 8));
        result = (result) * (a2);
        result = (result) + (a3);
        result = (result) ^ (a3);
        result = 1;
        a1 = (unsigned int)((result + result * 8) + 1);
        result = (result) << ((unsigned __int8)(a1));
        result = (result) - 1;
        *(unsigned int *)(v_rsp - 63 - 109) = (unsigned int)(a1);
        result = ~(result);
        a3 = (a3) & (result);
        *(unsigned __int64 *)(v_rsp - 63 - 49) = a3;
    }
    if (0 != 0) goto loc_005716D1;
loc_005716CA:
    if (0 != 0) goto loc_00571739;
    goto loc_00571717;
loc_005716D1:
    if (a4 == 0) goto loc_005716FA;
    result = (unsigned int)((*(unsigned __int16 *)(a1 + 222)) & (63));
    if (((unsigned int)(a1)) <= ((unsigned int)(result))) goto loc_005716FA;
    v_rbx = (18) & (-17);
    *(unsigned __int8 *)(v_rsp - 63 - 120) = 0;
    v_rbx = (v_rbx) | (32);
    *(unsigned __int64 *)(v_rsp - 63 - 9) = v_rbx;
    goto loc_00571717;
loc_005716FA:
    a1 = (unsigned int)((a1) & (63));
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 1)) & (0xFC0ULL));
    a1 = (a1) | (result);
    result = (a3) << (12);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(v_rsp - 63 - 1) = a1;
loc_00571717:
    a3 = 0;
    result = IvtIommuSendCommand(a1, v_rsp - 63 - 9, a3, 0);
    v_r11 = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 65) = *(unsigned __int64 *)(v_rsp - 63 - 9);
loc_00571739:
    if (1 == 0) goto loc_00571B17;
    *(unsigned __int64 *)(v_rsp - 63 - 73) = *(unsigned __int64 *)(v_rsp - 63 + 111);
    if (*(unsigned __int64 *)(v_rsp - 63 + 103) == 0) goto loc_00571782;
    *(unsigned __int64 *)(v_rsp - 63 - 81) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 48);
    *(unsigned int *)(v_rsp - 63 - 113) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 60)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 - 121)) != 0) goto loc_0057176F;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 103) + 96) + 48))) >> (11));
    a1 = (unsigned __int8)((a1) & (1));
    goto loc_00571772;
loc_0057176F:
loc_00571772:
    *(unsigned __int8 *)(v_rsp - 63 - 119) = 0;
    goto loc_00571818;
loc_00571782:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 - 121)) != 0) goto loc_005717D3;
    v_stack_mC8 = v_rsp - 63 - 89;
    v_stack_mD0 = v_rsp - 63 - 97;
    v_stack_mD8 = v_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(unsigned __int64 *)(v_rsp - 63 + 111), v_rsp - 63 - 73, v_rsp - 63 - 81, v_rsp - 63 - 113);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00571B13;
    goto loc_00571820;
loc_005717D3:
    *(unsigned __int64 *)(v_rsp - 63 - 73) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 111));
    *(unsigned __int8 *)(v_rsp - 63 - 119) = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 + 111))) != (*(unsigned __int64 *)(v_rsp - 63 + 111))) goto loc_005717FC;
    *(unsigned __int64 *)(v_rsp - 63 - 81) = 0;
    *(unsigned int *)(v_rsp - 63 - 113) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 97) = 0;
    *(unsigned __int64 *)(v_rsp - 63 - 89) = 0;
    goto loc_00571B17;
loc_005717FC:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40)) + (64);
    v_rsi = (*(unsigned __int64 *)(v_rsp - 63 - 33)) + (44);
    *(unsigned __int64 *)(v_rsp - 63 - 81) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 48);
    *(unsigned int *)(v_rsp - 63 - 113) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 60)));
loc_00571818:
    *(unsigned __int64 *)(v_rsp - 63 - 89) = v_rsi;
    *(unsigned __int64 *)(v_rsp - 63 - 97) = result;
loc_00571820:
loc_0057182C:
    if ((*(unsigned __int8 *)(v_rsi)) != 0) goto loc_00571850;
    result = ExAcquireRundownProtection(*(unsigned __int64 *)(v_rsp - 63 - 97), v_rsp - 63 - 73, v_rsp - 63 - 81, (unsigned int)(*(unsigned int *)(v_rsp - 63 - 109)));
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00571A65;
    *(unsigned __int8 *)(v_rsi) = 1;
loc_00571850:
    *(unsigned __int64 *)(v_rsp - 63 - 25) = v_xmm0;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 - 121)) != 0) goto loc_0057199E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 57)))) != -1) goto loc_005718D0;
    if ((*(unsigned __int8 *)(v_rsp - 63 - 119)) != 0) goto loc_005718C5;
    if ((*(unsigned int *)(v_rsp - 63 - 105)) != 0) goto loc_00571A65;
    a2 = ((unsigned __int16)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 48))) << (32);
    a2 = (a2) | (3);
    result = (unsigned int)(*(unsigned int *)(v_rsp - 63 - 57));
    v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 48);
    if (!(condition_is_above_or_equal)) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 48);
        v_rdi = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 48)) & (15));
        result = (result) & (-16);
        result = (result) << (36);
        result = (result) | (v_rdi);
        result = (result) << (12);
        a2 = (a2) | (result);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 60))))) << (16);
    result = (a1) ^ (a2);
    result = (result) & (0xFFFFFFFFFFE0FFFFULL);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 63 - 25) = result;
    goto loc_00571A4F;
loc_005718C5:
    goto loc_005718DD;
loc_005718D0:
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 25)) & (0xFFFFFULL));
    result = (result) << (32);
loc_005718DD:
    a3 = ((unsigned __int16)(v_rdi)) << (16);
    result = (result) & (a1);
    a3 = (a3) | (result);
    a3 = (a3) | (8);
    if (!(condition_is_above_or_equal)) {
        result = a3;
        a1 = v_rdi;
        a1 = (a1) & (-16);
        v_rdi = (unsigned int)((v_rdi) & (15));
        a1 = (a1) << (36);
        a1 = (a1) | (v_rdi);
        result = (result) & (a3);
        a1 = (a1) << (12);
        a3 = a1;
        a3 = (a3) | (result);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 60))))) << (4);
    result = (a1) ^ (a3);
    result = (result) & (-497);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 63 - 25) = result;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) != 0) goto loc_00571967;
    a2 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 17)) & (0x7FFULL));
loc_0057195F:
    a2 = (a2) | (result);
    goto loc_00571A4B;
loc_00571967:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 109))) != 0) goto loc_0057197B;
    a2 = (unsigned int)((a2) & (0xFFFULL));
    result = (*(unsigned __int64 *)(v_rsp - 63 - 49)) << (12);
    goto loc_0057195F;
loc_0057197B:
    a2 = (unsigned int)((a2) & (0xFFEULL));
    result = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 109)) - 1))));
    result = (result) - 1;
    result = (result) | (*(unsigned __int64 *)(v_rsp - 63 - 49));
    result = (result) << (12);
    result = (result) | (a2);
    result = (result) | (1);
    goto loc_00571A02;
loc_0057199E:
    a2 = ((unsigned __int16)(v_rdi)) << (32);
    a2 = (a2) | (3);
    if (!(condition_is_above_or_equal)) {
        result = v_rdi;
        v_rdi = (unsigned int)((v_rdi) & (15));
        result = (result) & (-16);
        result = (result) << (36);
        result = (result) | (v_rdi);
        result = (result) << (12);
        a2 = (a2) | (result);
    }
    a1 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 33) - 40) + 60))))) << (16);
    result = (a1) ^ (a2);
    result = (result) & (0xFFFFFFFFFFE0FFFFULL);
    result = (result) ^ (a1);
    *(unsigned __int64 *)(v_rsp - 63 - 25) = result;
    if ((*(unsigned int *)(v_rsp - 63 + 119)) != 0) goto loc_00571A08;
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 17)) & (0xFFEULL));
    result = (result) | (a1);
loc_00571A02:
    *(unsigned __int64 *)(v_rsp - 63 - 17) = result;
    goto loc_00571A4F;
loc_00571A08:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 109))) != 0) goto loc_00571A27;
    a1 = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 17)) & (0xFFFULL));
    result = (*(unsigned __int64 *)(v_rsp - 63 - 49)) << (12);
    a1 = (a1) | (result);
    *(unsigned __int64 *)(v_rsp - 63 - 17) = a1;
    goto loc_00571A4F;
loc_00571A27:
    result = (unsigned int)((*(unsigned __int64 *)(v_rsp - 63 - 17)) & (0xFFEULL));
    a2 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 63 - 109)) - 1))));
    a2 = (a2) - 1;
    a2 = (a2) | (*(unsigned __int64 *)(v_rsp - 63 - 49));
    a2 = (a2) << (12);
    a2 = (a2) | (result);
    a2 = (a2) | (1);
loc_00571A4B:
    *(unsigned __int64 *)(v_rsp - 63 - 17) = a2;
loc_00571A4F:
    a3 = 0;
    result = IvtIommuSendCommand(a1, v_rsp - 63 - 25, a3, (unsigned int)(*(unsigned int *)(v_rsp - 63 - 109)));
    v_r11 = 0;
loc_00571A65:
    if (*(unsigned __int64 *)(v_rsp - 63 + 111) == 0) goto loc_00571B03;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 - 121)) != 0) goto loc_00571AC2;
    v_stack_mC8 = v_rsp - 63 - 89;
    v_stack_mD0 = v_rsp - 63 - 97;
    v_stack_mD8 = v_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(unsigned __int64 *)(v_rsp - 63 + 111), v_rsp - 63 - 73, v_rsp - 63 - 81, v_rsp - 63 - 113);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00571B03;
    goto loc_0057182C;
loc_00571AC2:
    *(unsigned __int64 *)(v_rsp - 63 - 73) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73))) == (*(unsigned __int64 *)(v_rsp - 63 + 111))) goto loc_00571B03;
    *(unsigned __int8 *)(v_rsp - 63 - 119) = 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) - 40)) + (64);
    v_rsi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73))) + (44);
    *(unsigned __int64 *)(v_rsp - 63 - 81) = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) - 40) + 48);
    *(unsigned __int64 *)(v_rsp - 63 - 89) = v_rsi;
    *(unsigned int *)(v_rsp - 63 - 113) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) - 40) + 60)));
    *(unsigned __int64 *)(v_rsp - 63 - 97) = result;
    goto loc_0057182C;
loc_00571B03:
loc_00571B13:
loc_00571B17:
    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rsp - 63 - 105))) + 1);
    *(unsigned int *)(v_rsp - 63 - 105) = a4;
    if (a4 < (*(unsigned int *)(v_rsp - 63 + 119))) goto loc_00571662;
    a3 = 0;
    a2 = 0;
    result = IvtIommuWaitCommand(a1, a2, a3, a4);
    v_r14 = 0;
    if ((*(unsigned __int8 *)(v_rsp - 63 - 116)) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 63 - 33) + 64;
        *(unsigned __int64 *)(v_rsp - 63 - 97) = a1;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 63 + 111) == 0) goto loc_00571BDF;
    *(unsigned __int64 *)(v_rsp - 63 - 73) = *(unsigned __int64 *)(v_rsp - 63 + 111);
loc_00571B6A:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rsp - 63 - 121)) != 0) goto loc_00571BB0;
    v_stack_mC8 = v_rsp - 63 - 89;
    v_stack_mD0 = v_rsp - 63 - 97;
    v_stack_mD8 = v_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(unsigned __int64 *)(v_rsp - 63 + 111), v_rsp - 63 - 73, v_rsp - 63 - 81, v_rsp - 63 - 113);
    if ((unsigned __int8)(result) == 0) goto loc_00571BDF;
    goto loc_00571BD0;
loc_00571BB0:
    *(unsigned __int64 *)(v_rsp - 63 - 73) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73))) == (*(unsigned __int64 *)(v_rsp - 63 + 111))) goto loc_00571BDF;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) - 40)) + (64);
    *(unsigned __int64 *)(v_rsp - 63 - 89) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) + 44;
    *(unsigned __int64 *)(v_rsp - 63 - 97) = a1;
loc_00571BD0:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) + 44)) == 0) goto loc_00571B6A;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 63 - 73)) + 44) = 0;
    result = ExReleaseRundownProtection(a1, v_rsp - 63 - 73, v_rsp - 63 - 81, v_rsp - 63 - 113);
    goto loc_00571B6A;
loc_00571BDF:
    a1 = (*(unsigned __int64 *)(v_rsp - 63 + 7)) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rsp - 63 - 73, v_rsp - 63 - 81, v_rsp - 63 - 113);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IvtLegacyFlushTbInternal(void *Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x89922E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x3F + 0x7) = result;
    local_r11 = 0;
    *(uint8_t *)(local_rsp - 0x3F - 0x79) = Arg4;
    *(uint64_t *)(local_rsp - 0x3F - 0x29) = *(uint64_t *)(local_rsp - 0x3F + 0x7F);
    *(uint32_t *)(local_rsp - 0x3F - 0x39) = Arg2;
    *(uint64_t *)(local_rsp - 0x3F - 0x21) = *(uint64_t *)(local_rsp - 0x3F + 0x67);
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = 0;
    *(uint8_t *)(local_rsp - 0x3F - 0x77) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = v_xmm0;
    if (Arg4 != 0) goto loc_005715BB;
    if (((uint32_t)((uint32_t)(Arg2))) != -1) goto loc_00571596;
    *(uint8_t *)(local_rsp - 0x3F - 0x78) = 0;
    if (((uint32_t)((uint32_t)(Arg2))) >= -1) goto loc_00571585;
    goto loc_0057158A;
loc_00571585:
loc_0057158A:
    local_rbx = (34) | (192);
    goto loc_0057161E;
loc_00571596:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (0xFFFFFULL));
    local_rbx = (local_rbx) << (32);
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) != 0) goto loc_005715AE;
    local_rbx = (local_rbx) | (38);
    goto loc_00571617;
loc_005715AE:
    local_rbx = (local_rbx) | (54);
    *(uint8_t *)(local_rsp - 0x3F - 0x78) = 1;
    goto loc_0057161E;
loc_005715BB:
    if (Arg3 == 0) goto loc_00571612;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) == 0) goto loc_005715DB;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) >= 0) goto loc_005715DB;
    goto loc_005715E3;
loc_005715DB:
loc_005715E3:
    result = ((uint32_t)(*(uint32_t *)(Arg3 + 0x30))) << (16);
    *(uint8_t *)(local_rsp - 0x3F - 0x78) = 0;
    local_rbx = (result) ^ (34);
    local_rbx = (local_rbx) & (34);
    local_rbx = (local_rbx) ^ (result);
    local_rbx = (local_rbx) | (192);
    goto loc_0057161E;
loc_00571612:
loc_00571617:
    *(uint8_t *)(local_rsp - 0x3F - 0x78) = 0;
loc_0057161E:
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = 18;
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = 18;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x67) != 0) goto loc_00571639;
    if (*(uint64_t *)(local_rsp - 0x3F + 0x6F) != 0) goto loc_00571639;
    *(uint8_t *)(local_rsp - 0x3F - 0x76) = 0;
    goto loc_00571649;
loc_00571639:
    *(uint8_t *)(local_rsp - 0x3F - 0x76) = 1;
    result = 1;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) == 0) {
        result = 0;
    }
    *(uint8_t *)(local_rsp - 0x3F - 0x75) = (uint8_t)(result);
    *(uint8_t *)(local_rsp - 0x3F - 0x74) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x6D) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x69) = 0;
loc_00571662:
    if (0 != 0) goto loc_0057166B;
    if ((uint8_t)(result) == 0) goto loc_005716CA;
loc_0057166B:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x29) + 0x0 * 8)) >> (10);
    result = (uint32_t)((result) & (3));
    Arg3 = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x29) + 0x0 * 8)) >> (12);
    *(uint64_t *)(local_rsp - 0x3F - 0x31) = Arg3;
    *(uint32_t *)(local_rsp - 0x3F - 0x6D) = (uint32_t)(result + result * 8);
    Arg2 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x29) + 0x0 * 8)) & (0x3FFULL));
    if (!(condition_is_equal)) {
        result = 1;
        result = (result) << ((uint8_t)(result + result * 8));
        result = (result) * (Arg2);
        result = (result) + (Arg3);
        result = (result) ^ (Arg3);
        result = 1;
        Arg1 = (uint32_t)((result + result * 8) + 1);
        result = (result) << ((uint8_t)(Arg1));
        result = (result) - 1;
        *(uint32_t *)(local_rsp - 0x3F - 0x6D) = (uint32_t)(Arg1);
        result = ~(result);
        Arg3 = (Arg3) & (result);
        *(uint64_t *)(local_rsp - 0x3F - 0x31) = Arg3;
    }
    if (0 != 0) goto loc_005716D1;
loc_005716CA:
    if (0 != 0) goto loc_00571739;
    goto loc_00571717;
loc_005716D1:
    if (Arg4 == 0) goto loc_005716FA;
    result = (uint32_t)((*(uint16_t *)(arg1 + 0xDE)) & (63));
    if (((uint32_t)(Arg1)) <= ((uint32_t)(result))) goto loc_005716FA;
    local_rbx = (18) & (-17);
    *(uint8_t *)(local_rsp - 0x3F - 0x78) = 0;
    local_rbx = (local_rbx) | (32);
    *(uint64_t *)(local_rsp - 0x3F - 0x9) = local_rbx;
    goto loc_00571717;
loc_005716FA:
    Arg1 = (uint32_t)((Arg1) & (63));
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x1)) & (0xFC0ULL));
    Arg1 = (Arg1) | (result);
    result = (Arg3) << (12);
    Arg1 = (Arg1) | (result);
    *(void **)(local_rsp - 0x3F - 0x1) = Arg1;
loc_00571717:
    Arg3 = 0;
    result = IvtIommuSendCommand(Arg1, local_rsp - 63 - 9, Arg3, 0);
    local_r11 = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x41) = *(uint64_t *)(local_rsp - 0x3F - 0x9);
loc_00571739:
    if (1 == 0) goto loc_00571B17;
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
    if (*(uint64_t *)(local_rsp - 0x3F + 0x67) == 0) goto loc_00571782;
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x30);
    *(uint32_t *)(local_rsp - 0x3F - 0x71) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x3C)));
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F - 0x79)) != 0) goto loc_0057176F;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x67) + 0x60) + 0x30))) >> (11));
    Arg1 = (uint8_t)((Arg1) & (1));
    goto loc_00571772;
loc_0057176F:
loc_00571772:
    *(uint8_t *)(local_rsp - 0x3F - 0x77) = 0;
    goto loc_00571818;
loc_00571782:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F - 0x79)) != 0) goto loc_005717D3;
    v_stack_mC8 = local_rsp - 63 - 89;
    v_stack_mD0 = local_rsp - 63 - 97;
    v_stack_mD8 = local_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(uint64_t *)(local_rsp - 0x3F + 0x6F), local_rsp - 63 - 73, local_rsp - 63 - 81, local_rsp - 63 - 113);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00571B13;
    goto loc_00571820;
loc_005717D3:
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x6F));
    *(uint8_t *)(local_rsp - 0x3F - 0x77) = 0;
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F + 0x6F))) != (*(uint64_t *)(local_rsp - 0x3F + 0x6F))) goto loc_005717FC;
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = 0;
    *(uint32_t *)(local_rsp - 0x3F - 0x71) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = 0;
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = 0;
    goto loc_00571B17;
loc_005717FC:
    result = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28)) + (64);
    local_rsi = (*(uint64_t *)(local_rsp - 0x3F - 0x21)) + (44);
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x30);
    *(uint32_t *)(local_rsp - 0x3F - 0x71) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x3C)));
loc_00571818:
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = local_rsi;
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = result;
loc_00571820:
loc_0057182C:
    if ((*(uint8_t *)(local_rsi)) != 0) goto loc_00571850;
    result = ExAcquireRundownProtection(*(uint64_t *)(local_rsp - 0x3F - 0x61), local_rsp - 63 - 73, local_rsp - 63 - 81, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D)));
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00571A65;
    *(uint8_t *)(local_rsi) = 1;
loc_00571850:
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = v_xmm0;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F - 0x79)) != 0) goto loc_0057199E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x39)))) != -1) goto loc_005718D0;
    if ((*(uint8_t *)(local_rsp - 0x3F - 0x77)) != 0) goto loc_005718C5;
    if ((*(uint32_t *)(local_rsp - 0x3F - 0x69)) != 0) goto loc_00571A65;
    Arg2 = ((uint16_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x30))) << (32);
    Arg2 = (Arg2) | (3);
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x39));
    local_rdi = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x30);
    if (!(condition_is_above_or_equal)) {
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x30);
        local_rdi = (uint32_t)((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x30)) & (15));
        result = (result) & (-16);
        result = (result) << (36);
        result = (result) | (local_rdi);
        result = (result) << (12);
        Arg2 = (Arg2) | (result);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x3C))))) << (16);
    result = (Arg1) ^ (Arg2);
    result = (result) & (0xFFFFFFFFFFE0FFFFULL);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = result;
    goto loc_00571A4F;
loc_005718C5:
    goto loc_005718DD;
loc_005718D0:
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x19)) & (0xFFFFFULL));
    result = (result) << (32);
loc_005718DD:
    Arg3 = ((uint16_t)(local_rdi)) << (16);
    result = (result) & (Arg1);
    Arg3 = (Arg3) | (result);
    Arg3 = (Arg3) | (8);
    if (!(condition_is_above_or_equal)) {
        result = Arg3;
        Arg1 = local_rdi;
        Arg1 = (Arg1) & (-16);
        local_rdi = (uint32_t)((local_rdi) & (15));
        Arg1 = (Arg1) << (36);
        Arg1 = (Arg1) | (local_rdi);
        result = (result) & (Arg3);
        Arg1 = (Arg1) << (12);
        Arg3 = Arg1;
        Arg3 = (Arg3) | (result);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x3C))))) << (4);
    result = (Arg1) ^ (Arg3);
    result = (result) & (-497);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = result;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) != 0) goto loc_00571967;
    Arg2 = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x11)) & (0x7FFULL));
loc_0057195F:
    Arg2 = (Arg2) | (result);
    goto loc_00571A4B;
loc_00571967:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D))) != 0) goto loc_0057197B;
    Arg2 = (uint32_t)((Arg2) & (0xFFFULL));
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x31)) << (12);
    goto loc_0057195F;
loc_0057197B:
    Arg2 = (uint32_t)((Arg2) & (0xFFEULL));
    result = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D)) - 1))));
    result = (result) - 1;
    result = (result) | (*(uint64_t *)(local_rsp - 0x3F - 0x31));
    result = (result) << (12);
    result = (result) | (Arg2);
    result = (result) | (1);
    goto loc_00571A02;
loc_0057199E:
    Arg2 = ((uint16_t)(local_rdi)) << (32);
    Arg2 = (Arg2) | (3);
    if (!(condition_is_above_or_equal)) {
        result = local_rdi;
        local_rdi = (uint32_t)((local_rdi) & (15));
        result = (result) & (-16);
        result = (result) << (36);
        result = (result) | (local_rdi);
        result = (result) << (12);
        Arg2 = (Arg2) | (result);
    }
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x21) - 0x28) + 0x3C))))) << (16);
    result = (Arg1) ^ (Arg2);
    result = (result) & (0xFFFFFFFFFFE0FFFFULL);
    result = (result) ^ (Arg1);
    *(uint64_t *)(local_rsp - 0x3F - 0x19) = result;
    if ((*(uint32_t *)(local_rsp - 0x3F + 0x77)) != 0) goto loc_00571A08;
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x11)) & (0xFFEULL));
    result = (result) | (Arg1);
loc_00571A02:
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = result;
    goto loc_00571A4F;
loc_00571A08:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D))) != 0) goto loc_00571A27;
    Arg1 = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x11)) & (0xFFFULL));
    result = (*(uint64_t *)(local_rsp - 0x3F - 0x31)) << (12);
    Arg1 = (Arg1) | (result);
    *(void **)(local_rsp - 0x3F - 0x11) = Arg1;
    goto loc_00571A4F;
loc_00571A27:
    result = (uint32_t)((*(uint64_t *)(local_rsp - 0x3F - 0x11)) & (0xFFEULL));
    Arg2 = (1) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D)) - 1))));
    Arg2 = (Arg2) - 1;
    Arg2 = (Arg2) | (*(uint64_t *)(local_rsp - 0x3F - 0x31));
    Arg2 = (Arg2) << (12);
    Arg2 = (Arg2) | (result);
    Arg2 = (Arg2) | (1);
loc_00571A4B:
    *(uint64_t *)(local_rsp - 0x3F - 0x11) = Arg2;
loc_00571A4F:
    Arg3 = 0;
    result = IvtIommuSendCommand(Arg1, local_rsp - 63 - 25, Arg3, (uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x6D)));
    local_r11 = 0;
loc_00571A65:
    if (*(uint64_t *)(local_rsp - 0x3F + 0x6F) == 0) goto loc_00571B03;
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F - 0x79)) != 0) goto loc_00571AC2;
    v_stack_mC8 = local_rsp - 63 - 89;
    v_stack_mD0 = local_rsp - 63 - 97;
    v_stack_mD8 = local_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(uint64_t *)(local_rsp - 0x3F + 0x6F), local_rsp - 63 - 73, local_rsp - 63 - 81, local_rsp - 63 - 113);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_00571B03;
    goto loc_0057182C;
loc_00571AC2:
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49));
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49))) == (*(uint64_t *)(local_rsp - 0x3F + 0x6F))) goto loc_00571B03;
    *(uint8_t *)(local_rsp - 0x3F - 0x77) = 0;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) - 0x28)) + (64);
    local_rsi = (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49))) + (44);
    *(uint64_t *)(local_rsp - 0x3F - 0x51) = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) - 0x28) + 0x30);
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = local_rsi;
    *(uint32_t *)(local_rsp - 0x3F - 0x71) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) - 0x28) + 0x3C)));
    *(uint64_t *)(local_rsp - 0x3F - 0x61) = result;
    goto loc_0057182C;
loc_00571B03:
loc_00571B13:
loc_00571B17:
    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rsp - 0x3F - 0x69))) + 1);
    *(uint32_t *)(local_rsp - 0x3F - 0x69) = Arg4;
    if (Arg4 < (*(uint32_t *)(local_rsp - 0x3F + 0x77))) goto loc_00571662;
    Arg3 = 0;
    Arg2 = 0;
    result = IvtIommuWaitCommand(Arg1, Arg2, Arg3, Arg4);
    local_r14 = 0;
    if ((*(uint8_t *)(local_rsp - 0x3F - 0x74)) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x3F - 0x21) + 64;
        *(void **)(local_rsp - 0x3F - 0x61) = Arg1;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x3F + 0x6F) == 0) goto loc_00571BDF;
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = *(uint64_t *)(local_rsp - 0x3F + 0x6F);
loc_00571B6A:
    if ((uint8_t)(*(uint8_t *)(local_rsp - 0x3F - 0x79)) != 0) goto loc_00571BB0;
    v_stack_mC8 = local_rsp - 63 - 89;
    v_stack_mD0 = local_rsp - 63 - 97;
    v_stack_mD8 = local_rsp - 63 - 119;
    result = HalpIommuGetNextFlushDevice(*(uint64_t *)(local_rsp - 0x3F + 0x6F), local_rsp - 63 - 73, local_rsp - 63 - 81, local_rsp - 63 - 113);
    if ((uint8_t)(result) == 0) goto loc_00571BDF;
    goto loc_00571BD0;
loc_00571BB0:
    *(uint64_t *)(local_rsp - 0x3F - 0x49) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49));
    if ((*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49))) == (*(uint64_t *)(local_rsp - 0x3F + 0x6F))) goto loc_00571BDF;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) - 0x28)) + (64);
    *(uint64_t *)(local_rsp - 0x3F - 0x59) = *(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) + 44;
    *(void **)(local_rsp - 0x3F - 0x61) = Arg1;
loc_00571BD0:
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) + 0x2C)) == 0) goto loc_00571B6A;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(local_rsp - 0x3F - 0x49)) + 0x2C) = 0;
    result = ExReleaseRundownProtection(Arg1, local_rsp - 63 - 73, local_rsp - 63 - 81, local_rsp - 63 - 113);
    goto loc_00571B6A;
loc_00571BDF:
    Arg1 = (*(uint64_t *)(local_rsp - 0x3F + 0x7)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, local_rsp - 63 - 73, local_rsp - 63 - 81, local_rsp - 63 - 113);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xDE` | `16` | `R` |
| `Arg1` | `+ 0xE0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005714E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
