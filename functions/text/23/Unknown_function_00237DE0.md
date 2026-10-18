# sub_00237DE0

- RVA: `0x00237DE0`–`0x00238582` (길이 `1,954` bytes)
- VA: `0x0000000140237DE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A20`
- 디코드: `495`개 명령, `1,954/1,954` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00237ECD` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00237F32` → [MiReturnSystemVa](MiReturnSystemVa_function_002394C4.md) (function, `0x002394C4`)
- `0x00237FDB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0023826C` → [RtlInterlockedSetClearRunEx](RtlInterlockedSetClearRunEx_function_00238660.md) (function, `0x00238660`)
- `0x0023829D` → [MiReturnSystemPtes](MiReturnSystemPtes_function_002385C0.md) (function, `0x002385C0`)
- `0x00238357` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x002383D4` → [MiVaToFlushVm](../31/MiVaToFlushVm_function_0031AD84.md) (function, `0x0031AD84`)
- `0x00238471` → [MiInsertTbFlushEntry](../29/MiInsertTbFlushEntry_function_00293670.md) (function, `0x00293670`)
- `0x00238482` → [MiTbFlushListPromoteThreshold](../41/MiTbFlushListPromoteThreshold_function_004195D0.md) (function, `0x004195D0`)
- `0x002384A7` → [MiTbFlushListPromoteThreshold](../41/MiTbFlushListPromoteThreshold_function_004195D0.md) (function, `0x004195D0`)
- `0x002384BC` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x002384D6` → [MiTbFlushTimeStampMayNeedFlush](../45/MiTbFlushTimeStampMayNeedFlush_function_004584B8.md) (function, `0x004584B8`)
- `0x002384F4` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00237E1D` → RVA `0x00E2DC80` (`.data`; read)
- `0x00238100` → RVA `0x00010880` (`.rdata`; read)
- `0x002384C6` → RVA `0x00FCF080` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00237F83` → [sub_00237D2C + 0x70](Unknown_function_00237D2C.md) (`tail-transfer`)
  - `0x0023842C` → [sub_00238595](Unknown_function_00238595.md) (`tail-transfer`)
  - `0x0023843D` → [sub_00238595 + 0x5](Unknown_function_00238595.md) (`tail-transfer`)
  - `0x002384B2` → [sub_00238595 + 0x1B](Unknown_function_00238595.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00237DE0  4C 8B C0                        mov r8, rax
00237DE3  0F 1F 40 00                     nop dword ptr [rax]
00237DE7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00237DF0  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00237DF4  49 8B CC                        mov rcx, r12
00237DF7  49 0F AF C8                     imul rcx, r8
00237DFB  48 8B 3C C8                     mov rdi, qword ptr [rax + rcx*8]
00237DFF  48 8D 1C C8                     lea rbx, [rax + rcx*8]
00237E03  40 F6 C7 02                     test dil, 2
00237E07  0F 84 D4 01 00 00               je 0x140237fe1
00237E0D  49 8B C1                        mov rax, r9
00237E10  4C 03 F0                        add r14, rax
00237E13  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
00237E18  48 85 FF                        test rdi, rdi
00237E1B  74 53                           je 0x140237e70
00237E1D  48 8B 05 5C 5E BF 00            mov rax, qword ptr [rip + 0xbf5e5c]
00237E24  48 85 C0                        test rax, rax
00237E27  74 10                           je 0x140237e39
00237E29  40 F6 C7 10                     test dil, 0x10
00237E2D  0F 85 55 01 00 00               jne 0x140237f88
00237E33  48 F7 D0                        not rax
00237E36  48 23 F8                        and rdi, rax
00237E39  48 C1 EF 19                     shr rdi, 0x19
00237E3D  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00237E42  48 85 FF                        test rdi, rdi
00237E45  74 2E                           je 0x140237e75
00237E47  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00237E4B  48 8D 0C F8                     lea rcx, [rax + rdi*8]
00237E4F  48 8B 04 F8                     mov rax, qword ptr [rax + rdi*8]
00237E53  A8 02                           test al, 2
00237E55  0F 84 AD 01 00 00               je 0x140238008
00237E5B  49 8B C1                        mov rax, r9
00237E5E  48 03 C7                        add rax, rdi
00237E61  33 D2                           xor edx, edx
00237E63  49 F7 F4                        div r12
00237E66  49 3B C0                        cmp rax, r8
00237E69  75 0A                           jne 0x140237e75
00237E6B  E9 DE 00 00 00                  jmp 0x140237f4e
00237E70  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00237E75  33 D2                           xor edx, edx
00237E77  49 8B C6                        mov rax, r14
00237E7A  49 F7 F4                        div r12
00237E7D  48 8B F0                        mov rsi, rax
00237E80  45 85 D2                        test r10d, r10d
00237E83  0F 84 08 01 00 00               je 0x140237f91
00237E89  45 85 ED                        test r13d, r13d
00237E8C  0F 84 19 05 00 00               je 0x1402383ab
00237E92  48 85 FF                        test rdi, rdi
00237E95  0F 84 5E 02 00 00               je 0x1402380f9
00237E9B  45 85 D2                        test r10d, r10d
00237E9E  0F 85 55 02 00 00               jne 0x1402380f9
00237EA4  4D 8B 0F                        mov r9, qword ptr [r15]
00237EA7  33 D2                           xor edx, edx
00237EA9  48 8B C7                        mov rax, rdi
00237EAC  49 F7 F4                        div r12
00237EAF  49 3B C1                        cmp rax, r9
00237EB2  0F 82 E1 01 00 00               jb 0x140238099
00237EB8  4C 8B 0B                        mov r9, qword ptr [rbx]
00237EBB  4C 8B C3                        mov r8, rbx
00237EBE  BA 05 05 00 00                  mov edx, 0x505
00237EC3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00237EC8  B9 DA 00 00 00                  mov ecx, 0xda
00237ECD  E8 8E 57 2C 00                  call 0x1404fd660
00237ED2  CC                              int3
00237ED3  49 C1 E0 04                     shl r8, 4
00237ED7  48 8B D0                        mov rdx, rax
00237EDA  48 C1 E2 04                     shl rdx, 4
00237EDE  85 C9                           test ecx, ecx
00237EE0  48 0F 44 D0                     cmove rdx, rax
00237EE4  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
00237EE8  4A 8D 0C C0                     lea rcx, [rax + r8*8]
00237EEC  48 8B C2                        mov rax, rdx
00237EEF  48 F7 D8                        neg rax
00237EF2  F0 49 01 47 38                  lock add qword ptr [r15 + 0x38], rax
00237EF7  48 C1 E1 19                     shl rcx, 0x19
00237EFB  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00237F05  48 8B C0                        mov rax, rax
00237F08  45 8B 47 2C                     mov r8d, dword ptr [r15 + 0x2c]
00237F0C  48 C1 E2 1C                     shl rdx, 0x1c
00237F10  48 C1 E0 19                     shl rax, 0x19
00237F14  48 2B C8                        sub rcx, rax
00237F17  48 03 D1                        add rdx, rcx
00237F1A  4C 8B C9                        mov r9, rcx
00237F1D  49 C1 F9 10                     sar r9, 0x10
00237F21  48 C1 FA 10                     sar rdx, 0x10
00237F25  41 83 FA 01                     cmp r10d, 1
00237F29  0F 84 CF 05 00 00               je 0x1402384fe
00237F2F  49 8B C9                        mov rcx, r9
00237F32  E8 8D 15 00 00                  call 0x1402394c4
00237F37  4C 01 74 24 40                  add qword ptr [rsp + 0x40], r14
00237F3C  44 8B 54 24 34                  mov r10d, dword ptr [rsp + 0x34]
00237F41  45 33 F6                        xor r14d, r14d
00237F44  41 BB 00 FE FF FF               mov r11d, 0xfffffe00
00237F4A  45 8D 4E 01                     lea r9d, [r14 + 1]
00237F4E  33 D2                           xor edx, edx
00237F50  48 8B C7                        mov rax, rdi
00237F53  49 F7 F4                        div r12
00237F56  4C 8B C0                        mov r8, rax
00237F59  48 85 C0                        test rax, rax
00237F5C  0F 85 8E FE FF FF               jne 0x140237df0
00237F62  45 85 ED                        test r13d, r13d
00237F65  0F 84 7B 05 00 00               je 0x1402384e6
00237F6B  44 8B 54 24 34                  mov r10d, dword ptr [rsp + 0x34]
00237F70  41 FF C5                        inc r13d
00237F73  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00237F78  41 B9 01 00 00 00               mov r9d, 1
00237F7E  44 89 6C 24 30                  mov dword ptr [rsp + 0x30], r13d
00237F83  E9 14 FE FF FF                  jmp 0x140237d9c
00237F88  48 83 E7 EF                     and rdi, 0xffffffffffffffef
00237F8C  E9 A8 FE FF FF                  jmp 0x140237e39
00237F91  49 8B 0F                        mov rcx, qword ptr [r15]
00237F94  4C 3B C1                        cmp r8, rcx
00237F97  73 2D                           jae 0x140237fc6
00237F99  48 83 FE 01                     cmp rsi, 1
00237F9D  0F 87 8C 00 00 00               ja 0x14023802f
00237FA3  75 21                           jne 0x140237fc6
00237FA5  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
00237FA9  49 8B D0                        mov rdx, r8
00237FAC  83 E2 3F                        and edx, 0x3f
00237FAF  49 8B C8                        mov rcx, r8
00237FB2  48 C1 E9 06                     shr rcx, 6
00237FB6  48 0F A3 14 C8                  bt qword ptr [rax + rcx*8], rdx
00237FBB  0F 92 C0                        setb al
00237FBE  84 C0                           test al, al
00237FC0  0F 85 C3 FE FF FF               jne 0x140237e89
00237FC6  4C 89 44 24 20                  mov qword ptr [rsp + 0x20], r8
00237FCB  4D 8B CE                        mov r9, r14
00237FCE  4C 8B C3                        mov r8, rbx
00237FD1  BA 04 05 00 00                  mov edx, 0x504
00237FD6  B9 DA 00 00 00                  mov ecx, 0xda
00237FDB  E8 80 56 2C 00                  call 0x1404fd660
00237FE0  CC                              int3
00237FE1  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00237FE5  48 8B 0D 94 5C BF 00            mov rcx, qword ptr [rip + 0xbf5c94]
00237FEC  48 85 C9                        test rcx, rcx
00237FEF  74 0E                           je 0x140237fff
00237FF1  A8 10                           test al, 0x10
00237FF3  0F 85 37 03 00 00               jne 0x140238330
00237FF9  48 F7 D1                        not rcx
00237FFC  48 23 C1                        and rax, rcx
00237FFF  48 C1 E8 20                     shr rax, 0x20
00238003  E9 08 FE FF FF                  jmp 0x140237e10
00238008  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0023800C  48 8B 0D 6D 5C BF 00            mov rcx, qword ptr [rip + 0xbf5c6d]
00238013  48 85 C9                        test rcx, rcx
00238016  74 0E                           je 0x140238026
00238018  A8 10                           test al, 0x10
0023801A  0F 85 19 03 00 00               jne 0x140238339
00238020  48 F7 D1                        not rcx
00238023  48 23 C1                        and rax, rcx
00238026  48 C1 E8 20                     shr rax, 0x20
0023802A  E9 2F FE FF FF                  jmp 0x140237e5e
0023802F  49 2B C8                        sub rcx, r8
00238032  48 3B CE                        cmp rcx, rsi
00238035  72 8F                           jb 0x140237fc6
00238037  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
0023803B  4D 8D 50 FF                     lea r10, [r8 - 1]
0023803F  4C 03 D6                        add r10, rsi
00238042  49 8B C0                        mov rax, r8
00238045  48 C1 E8 06                     shr rax, 6
00238049  4C 8B 1C C1                     mov r11, qword ptr [rcx + rax*8]
0023804D  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00238051  49 8B C2                        mov rax, r10
00238054  48 C1 E8 06                     shr rax, 6
00238058  4C 8D 0C C1                     lea r9, [rcx + rax*8]
0023805C  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00238063  49 3B D1                        cmp rdx, r9
00238066  0F 85 F1 02 00 00               jne 0x14023835d
0023806C  B9 40 00 00 00                  mov ecx, 0x40
00238071  40 2A CE                        sub cl, sil
00238074  48 D3 E8                        shr rax, cl
00238077  49 8B C8                        mov rcx, r8
0023807A  48 D3 E0                        shl rax, cl
0023807D  4C 23 D8                        and r11, rax
00238080  4C 3B D8                        cmp r11, rax
00238083  0F 85 3D FF FF FF               jne 0x140237fc6
00238089  44 8B 54 24 34                  mov r10d, dword ptr [rsp + 0x34]
0023808E  41 BB 00 FE FF FF               mov r11d, 0xfffffe00
00238094  E9 F0 FD FF FF                  jmp 0x140237e89
00238099  49 8B 47 20                     mov rax, qword ptr [r15 + 0x20]
0023809D  48 8B 0C F8                     mov rcx, qword ptr [rax + rdi*8]
002380A1  48 F7 C1 01 0C 00 00            test rcx, 0xc01
002380A8  0F 94 C2                        sete dl
002380AB  48 F7 C1 E0 03 00 00            test rcx, 0x3e0
002380B2  0F 94 C0                        sete al
002380B5  84 D0                           test al, dl
002380B7  0F 84 85 02 00 00               je 0x140238342
002380BD  48 85 C9                        test rcx, rcx
002380C0  0F 84 51 04 00 00               je 0x140238517
002380C6  48 8B 15 B3 5B BF 00            mov rdx, qword ptr [rip + 0xbf5bb3]
002380CD  48 8B C1                        mov rax, rcx
002380D0  48 85 D2                        test rdx, rdx
002380D3  74 12                           je 0x1402380e7
002380D5  F6 C1 10                        test cl, 0x10
002380D8  0F 85 0B 02 00 00               jne 0x1402382e9
002380DE  48 8B C2                        mov rax, rdx
002380E1  48 F7 D0                        not rax
002380E4  48 23 C1                        and rax, rcx
002380E7  48 C1 E8 19                     shr rax, 0x19
002380EB  33 D2                           xor edx, edx
002380ED  49 F7 F4                        div r12
002380F0  49 3B C1                        cmp rax, r9
002380F3  0F 83 49 02 00 00               jae 0x140238342
002380F9  33 C9                           xor ecx, ecx
002380FB  4D 85 F6                        test r14, r14
002380FE  74 1C                           je 0x14023811c
00238100  48 8B 05 79 87 DD FF            mov rax, qword ptr [rip - 0x227887]
00238107  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00238110  48 89 04 CB                     mov qword ptr [rbx + rcx*8], rax
00238114  48 FF C1                        inc rcx
00238117  49 3B CE                        cmp rcx, r14
0023811A  72 F4                           jb 0x140238110
0023811C  45 85 D2                        test r10d, r10d
0023811F  74 21                           je 0x140238142
00238121  41 8B 4F 28                     mov ecx, dword ptr [r15 + 0x28]
00238125  41 8D 86 FF 01 00 00            lea eax, [r14 + 0x1ff]
0023812C  49 23 C3                        and rax, r11
0023812F  33 D2                           xor edx, edx
00238131  49 F7 F4                        div r12
00238134  83 E1 01                        and ecx, 1
00238137  0F 85 96 FD FF FF               jne 0x140237ed3
0023813D  E9 95 FD FF FF                  jmp 0x140237ed7
00238142  4D 8B CE                        mov r9, r14
00238145  F0 4D 0F C1 4F 58               lock xadd qword ptr [r15 + 0x58], r9
0023814B  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
0023814F  4D 8B D0                        mov r10, r8
00238152  41 83 E2 1F                     and r10d, 0x1f
00238156  49 8B C8                        mov rcx, r8
00238159  48 C1 E9 05                     shr rcx, 5
0023815D  4D 03 CE                        add r9, r14
00238160  48 8B D6                        mov rdx, rsi
00238163  4C 8D 1C 88                     lea r11, [rax + rcx*4]
00238167  49 8D 04 32                     lea rax, [r10 + rsi]
0023816B  48 83 F8 20                     cmp rax, 0x20
0023816F  0F 87 92 01 00 00               ja 0x140238307
00238175  48 83 FE 20                     cmp rsi, 0x20
00238179  0F 84 F7 03 00 00               je 0x140238576
0023817F  48 8B CE                        mov rcx, rsi
00238182  B8 01 00 00 00                  mov eax, 1
00238187  D3 E0                           shl eax, cl
00238189  41 8B CA                        mov ecx, r10d
0023818C  FF C8                           dec eax
0023818E  D3 E0                           shl eax, cl
00238190  F7 D0                           not eax
00238192  F0 41 21 03                     lock and dword ptr [r11], eax
00238196  49 81 F9 00 00 20 00            cmp r9, 0x200000
0023819D  0F 86 94 FD FF FF               jbe 0x140237f37
002381A3  41 8B 47 28                     mov eax, dword ptr [r15 + 0x28]
002381A7  41 BE 20 00 00 00               mov r14d, 0x20
002381AD  83 E0 01                        and eax, 1
002381B0  BB 00 00 00 00                  mov ebx, 0
002381B5  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
002381B9  B8 00 02 00 00                  mov eax, 0x200
002381BE  44 0F 44 F0                     cmove r14d, eax
002381C2  49 8D 4E FF                     lea rcx, [r14 - 1]
002381C6  48 F7 D1                        not rcx
002381C9  4D 8D 66 FF                     lea r12, [r14 - 1]
002381CD  4C 03 E6                        add r12, rsi
002381D0  4C 8B E9                        mov r13, rcx
002381D3  4D 03 E0                        add r12, r8
002381D6  4D 23 E8                        and r13, r8
002381D9  4C 23 E1                        and r12, rcx
002381DC  4D 2B E5                        sub r12, r13
002381DF  0F 84 D3 00 00 00               je 0x1402382b8
002381E5  8B 7C 24 3C                     mov edi, dword ptr [rsp + 0x3c]
002381E9  41 BB 40 00 00 00               mov r11d, 0x40
002381EF  4D 2B DE                        sub r11, r14
002381F2  4C 89 5C 24 48                  mov qword ptr [rsp + 0x48], r11
002381F7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00238200  49 8B 07                        mov rax, qword ptr [r15]
00238203  4A 8D 34 2B                     lea rsi, [rbx + r13]
00238207  48 3B F0                        cmp rsi, rax
0023820A  0F 83 97 00 00 00               jae 0x1402382a7
00238210  48 2B C6                        sub rax, rsi
00238213  49 3B C6                        cmp rax, r14
00238216  0F 82 8B 00 00 00               jb 0x1402382a7
0023821C  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
00238220  4D 8D 56 FF                     lea r10, [r14 - 1]
00238224  4C 03 D6                        add r10, rsi
00238227  48 8B C6                        mov rax, rsi
0023822A  48 C1 E8 06                     shr rax, 6
0023822E  4C 8B 04 C1                     mov r8, qword ptr [rcx + rax*8]
00238232  48 8D 14 C1                     lea rdx, [rcx + rax*8]
00238236  49 8B C2                        mov rax, r10
00238239  48 C1 E8 06                     shr rax, 6
0023823D  4C 8D 0C C1                     lea r9, [rcx + rax*8]
00238241  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00238248  49 3B D1                        cmp rdx, r9
0023824B  75 7F                           jne 0x1402382cc
0023824D  49 8B CB                        mov rcx, r11
00238250  48 D3 E8                        shr rax, cl
00238253  48 8B CE                        mov rcx, rsi
00238256  48 D3 E0                        shl rax, cl
00238259  49 85 C0                        test r8, rax
0023825C  0F 94 C0                        sete al
0023825F  84 C0                           test al, al
00238261  74 44                           je 0x1402382a7
00238263  4D 8B C6                        mov r8, r14
00238266  48 8B D6                        mov rdx, rsi
00238269  49 8B CF                        mov rcx, r15
0023826C  E8 EF 03 00 00                  call 0x140238660
00238271  85 C0                           test eax, eax
00238273  74 2D                           je 0x1402382a2
00238275  85 FF                           test edi, edi
00238277  48 C7 C0 F0 FF FF FF            mov rax, 0xfffffffffffffff0
0023827E  48 C7 C1 FF FF FF FF            mov rcx, 0xffffffffffffffff
00238285  48 0F 44 C1                     cmove rax, rcx
00238289  49 0F AF C6                     imul rax, r14
0023828D  F0 49 01 47 58                  lock add qword ptr [r15 + 0x58], rax
00238292  4D 8B CE                        mov r9, r14
00238295  4C 8B C6                        mov r8, rsi
00238298  33 D2                           xor edx, edx
0023829A  49 8B CF                        mov rcx, r15
0023829D  E8 1E 03 00 00                  call 0x1402385c0
002382A2  4C 8B 5C 24 48                  mov r11, qword ptr [rsp + 0x48]
002382A7  49 03 DE                        add rbx, r14
002382AA  49 3B DC                        cmp rbx, r12
002382AD  0F 82 4D FF FF FF               jb 0x140238200
002382B3  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
002382B8  44 8B 6C 24 30                  mov r13d, dword ptr [rsp + 0x30]
002382BD  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
002382C2  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
002382C7  E9 6B FC FF FF                  jmp 0x140237f37
002382CC  48 8B CE                        mov rcx, rsi
002382CF  48 D3 E0                        shl rax, cl
002382D2  49 85 C0                        test r8, rax
002382D5  75 D0                           jne 0x1402382a7
002382D7  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
002382DB  48 83 C2 08                     add rdx, 8
002382DF  49 3B D1                        cmp rdx, r9
002382E2  74 0E                           je 0x1402382f2
002382E4  4D 85 C0                        test r8, r8
002382E7  EB EC                           jmp 0x1402382d5
002382E9  48 83 E0 EF                     and rax, 0xffffffffffffffef
002382ED  E9 F5 FD FF FF                  jmp 0x1402380e7
002382F2  41 0F B6 CA                     movzx ecx, r10b
002382F6  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
002382FD  F6 D1                           not cl
002382FF  48 D3 E8                        shr rax, cl
00238302  E9 52 FF FF FF                  jmp 0x140238259
00238307  4D 85 D2                        test r10, r10
0023830A  0F 85 0E 02 00 00               jne 0x14023851e
00238310  48 83 FA 20                     cmp rdx, 0x20
00238314  73 70                           jae 0x140238386
00238316  48 85 D2                        test rdx, rdx
00238319  0F 84 77 FE FF FF               je 0x140238196
0023831F  48 8B CA                        mov rcx, rdx
00238322  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00238329  D3 E0                           shl eax, cl
0023832B  E9 62 FE FF FF                  jmp 0x140238192
00238330  48 83 E0 EF                     and rax, 0xffffffffffffffef
00238334  E9 C6 FC FF FF                  jmp 0x140237fff
00238339  48 83 E0 EF                     and rax, 0xffffffffffffffef
0023833D  E9 E4 FC FF FF                  jmp 0x140238026
00238342  4C 8B 0B                        mov r9, qword ptr [rbx]
00238345  4C 8B C3                        mov r8, rbx
00238348  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0023834D  BA 06 05 00 00                  mov edx, 0x506
00238352  B9 DA 00 00 00                  mov ecx, 0xda
00238357  E8 04 53 2C 00                  call 0x1404fd660
0023835C  CC                              int3
0023835D  49 8B C8                        mov rcx, r8
00238360  48 D3 E0                        shl rax, cl
00238363  4C 23 D8                        and r11, rax
00238366  4C 3B D8                        cmp r11, rax
00238369  0F 85 57 FC FF FF               jne 0x140237fc6
0023836F  4C 8B 5A 08                     mov r11, qword ptr [rdx + 8]
00238373  48 83 C2 08                     add rdx, 8
00238377  49 3B D1                        cmp rdx, r9
0023837A  0F 84 D2 01 00 00               je 0x140238552
00238380  49 83 FB FF                     cmp r11, -1
00238384  EB E3                           jmp 0x140238369
00238386  48 8B CA                        mov rcx, rdx
00238389  48 C1 E9 05                     shr rcx, 5
0023838D  48 6B C1 E0                     imul rax, rcx, -0x20
00238391  48 03 D0                        add rdx, rax
00238394  41 C7 03 00 00 00 00            mov dword ptr [r11], 0
0023839B  49 83 C3 04                     add r11, 4
0023839F  48 83 E9 01                     sub rcx, 1
002383A3  0F 84 6D FF FF FF               je 0x140238316
002383A9  EB E9                           jmp 0x140238394
002383AB  48 C1 E3 19                     shl rbx, 0x19
002383AF  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
002383B9  48 8B C0                        mov rax, rax
002383BC  48 C1 E0 19                     shl rax, 0x19
002383C0  48 2B D8                        sub rbx, rax
002383C3  48 C1 FB 10                     sar rbx, 0x10
002383C7  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
002383CB  0F 85 93 00 00 00               jne 0x140238464
002383D1  48 8B CB                        mov rcx, rbx
002383D4  E8 AB 29 0E 00                  call 0x14031ad84
002383D9  C7 45 8C 14 00 00 00            mov dword ptr [rbp - 0x74], 0x14
002383E0  48 8B D0                        mov rdx, rax
002383E3  C7 45 90 08 00 00 00            mov dword ptr [rbp - 0x70], 8
002383EA  C7 45 94 01 00 00 00            mov dword ptr [rbp - 0x6c], 1
002383F1  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
002383F5  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
002383FB  C1 E9 08                        shr ecx, 8
002383FE  C0 E9 03                        shr cl, 3
00238401  80 E1 01                        and cl, 1
00238404  88 4D 98                        mov byte ptr [rbp - 0x68], cl
00238407  8B 88 B8 00 00 00               mov ecx, dword ptr [rax + 0xb8]
0023840D  F6 C1 0F                        test cl, 0xf
00238410  75 20                           jne 0x140238432
00238412  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0023841B  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00238422  48 81 C1 00 04 00 00            add rcx, 0x400
00238429  48 3B D1                        cmp rdx, rcx
0023842C  0F 85 63 01 00 00               jne 0x140238595
00238432  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00238438  A8 0F                           test al, 0xf
0023843A  8B 45 90                        mov eax, dword ptr [rbp - 0x70]
0023843D  0F 85 57 01 00 00               jne 0x14023859a
00238443  B9 01 00 00 00                  mov ecx, 1
00238448  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
0023844B  33 C9                           xor ecx, ecx
0023844D  83 E0 DB                        and eax, 0xffffffdb
00238450  66 C7 45 99 00 00               mov word ptr [rbp - 0x67], 0
00238456  89 45 90                        mov dword ptr [rbp - 0x70], eax
00238459  89 4D 9C                        mov dword ptr [rbp - 0x64], ecx
0023845C  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00238460  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00238464  45 33 C9                        xor r9d, r9d
00238467  48 8D 4D 80                     lea rcx, [rbp - 0x80]
0023846B  4D 8B C6                        mov r8, r14
0023846E  48 8B D3                        mov rdx, rbx
00238471  E8 FA B1 05 00                  call 0x140293670
00238476  8B 45 8C                        mov eax, dword ptr [rbp - 0x74]
00238479  39 45 9C                        cmp dword ptr [rbp - 0x64], eax
0023847C  74 19                           je 0x140238497
0023847E  48 8D 4D 80                     lea rcx, [rbp - 0x80]
00238482  E8 49 11 1E 00                  call 0x1404195d0
00238487  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0023848B  48 FF C1                        inc rcx
0023848E  48 3B C8                        cmp rcx, rax
00238491  0F 82 A5 FA FF FF               jb 0x140237f3c
00238497  80 7D 99 00                     cmp byte ptr [rbp - 0x67], 0
0023849B  75 1B                           jne 0x1402384b8
0023849D  80 7D 9A 00                     cmp byte ptr [rbp - 0x66], 0
002384A1  75 15                           jne 0x1402384b8
002384A3  48 8D 4D 80                     lea rcx, [rbp - 0x80]
002384A7  E8 24 11 1E 00                  call 0x1404195d0
002384AC  48 3D 00 04 00 00               cmp rax, 0x400
002384B2  0F 82 F8 00 00 00               jb 0x1402385b0
002384B8  48 8D 4D 80                     lea rcx, [rbp - 0x80]
002384BC  E8 FF 9A 0D 00                  call 0x140311fc0
002384C1  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
002384C6  8B 15 B4 6B D9 00               mov edx, dword ptr [rip + 0xd96bb4]
002384CC  41 B8 FF FF FF FF               mov r8d, 0xffffffff
002384D2  8B 4C 24 38                     mov ecx, dword ptr [rsp + 0x38]
002384D6  E8 DD FF 21 00                  call 0x1404584b8
002384DB  84 C0                           test al, al
002384DD  0F 85 59 FA FF FF               jne 0x140237f3c
002384E3  45 33 F6                        xor r14d, r14d
002384E6  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
002384EA  0F 84 7B FA FF FF               je 0x140237f6b
002384F0  48 8D 4D 80                     lea rcx, [rbp - 0x80]
002384F4  E8 C7 9A 0D 00                  call 0x140311fc0
002384F9  E9 6D FA FF FF                  jmp 0x140237f6b
002384FE  41 83 F8 08                     cmp r8d, 8
00238502  B8 0A 00 00 00                  mov eax, 0xa
00238507  B9 0C 00 00 00                  mov ecx, 0xc
0023850C  0F 44 C1                        cmove eax, ecx
0023850F  44 8B C0                        mov r8d, eax
00238512  E9 18 FA FF FF                  jmp 0x140237f2f
00238517  33 C0                           xor eax, eax
00238519  E9 CD FB FF FF                  jmp 0x1402380eb
0023851E  41 8B C0                        mov eax, r8d
00238521  BA 20 00 00 00                  mov edx, 0x20
00238526  83 E0 1F                        and eax, 0x1f
00238529  2B D0                           sub edx, eax
0023852B  B8 01 00 00 00                  mov eax, 1
00238530  8B CA                           mov ecx, edx
00238532  D3 E0                           shl eax, cl
00238534  49 8B CA                        mov rcx, r10
00238537  FF C8                           dec eax
00238539  D3 E0                           shl eax, cl
0023853B  F7 D0                           not eax
0023853D  F0 41 21 03                     lock and dword ptr [r11], eax
00238541  8B C2                           mov eax, edx
00238543  48 8B D6                        mov rdx, rsi
00238546  48 2B D0                        sub rdx, rax
00238549  49 83 C3 04                     add r11, 4
0023854D  E9 BE FD FF FF                  jmp 0x140238310
00238552  41 0F B6 CA                     movzx ecx, r10b
00238556  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0023855D  F6 D1                           not cl
0023855F  48 D3 EA                        shr rdx, cl
00238562  48 8B C2                        mov rax, rdx
00238565  49 23 C3                        and rax, r11
00238568  48 3B C2                        cmp rax, rdx
0023856B  0F 85 55 FA FF FF               jne 0x140237fc6
00238571  E9 13 FB FF FF                  jmp 0x140238089
00238576  41 C7 03 00 00 00 00            mov dword ptr [r11], 0
0023857D  E9 14 FC FF FF                  jmp 0x140238196
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00237DE0(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p3C;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;

loc_00237DF0:
    a1 = (v_r12) * (result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8))) & (2)) == 0) goto loc_00237FE1;
loc_00237E10:
    v_r14 = (v_r14) + (a4);
    v_stack_p58 = v_r14;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8) == 0) goto loc_00237E70;
    if (*(unsigned __int64 *)(v_rip + 12541532) == 0) goto loc_00237E39;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8))) & (16)) != 0) goto loc_00237F88;
    result = ~(*(unsigned __int64 *)(v_rip + 12541532));
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8)) & (result);
loc_00237E39:
    v_rdi = (v_rdi) >> (25);
    v_stack_p50 = v_rdi;
    if (v_rdi == 0) goto loc_00237E75;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8))) & (2)) == 0) goto loc_00238008;
loc_00237E5E:
    result = (a4) + (v_rdi);
    a2 = 0;
    if (result != result) goto loc_00237E75;
    goto loc_00237F4E;
loc_00237E70:
    v_stack_p50 = v_rdi;
loc_00237E75:
    a2 = 0;
    if ((unsigned int)(v_r10) == 0) goto loc_00237F91;
loc_00237E89:
    if ((unsigned int)(v_r13) == 0) goto loc_002383AB;
    if (v_rdi == 0) goto loc_002380F9;
    if ((unsigned int)(v_r10) != 0) goto loc_002380F9;
    a2 = 0;
    if (v_rdi < (*(unsigned __int64 *)(v_r15))) goto loc_00238099;
    v_stack_p20 = v_rdi;
    result = KeBugCheckEx(218, (unsigned int)(0x505ULL), *(unsigned __int64 *)(v_r15 + 32) + a1 * 8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8));
loc_00237ED3:
    a3 = (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8) << (4);
loc_00237ED7:
    a2 = (result) << (4);
    if (218 == 0) { a2 = result; }
    result = -(a2);
    a1 = (*(unsigned __int64 *)(v_r15 + 32) + a3 * 8) << (25);
    a2 = (a2) << (28);
    result = (result) << (25);
    a1 = (a1) - (result);
    a2 = (a2) + (a1);
    a4 = (a1) >> (16);
    a2 = (a2) >> (16);
    if (((unsigned int)(v_r10)) == 1) goto loc_002384FE;
loc_00237F2F:
    result = MiReturnSystemVa(a4, a2, (unsigned int)(*(unsigned int *)(v_r15 + 44)), a4);
loc_00237F37:
loc_00237F3C:
    v_r14 = 0;
loc_00237F4E:
    a2 = 0;
    if (v_rdi != 0) goto loc_00237DF0;
    if ((unsigned int)(v_r13) == 0) goto loc_002384E6;
loc_00237F6B:
    v_r13 = (unsigned int)((v_r13) + 1);
    v_stack_p30 = (unsigned int)(v_r13);
loc_00237F88:
    v_rdi = (v_rdi) & (-17);
    goto loc_00237E39;
loc_00237F91:
    if (v_rdi >= (*(unsigned __int64 *)(v_r15))) goto loc_00237FC6;
    if (0 > 1) goto loc_0023802F;
    if (0 != 1) goto loc_00237FC6;
    a2 = (unsigned int)((v_rdi) & (63));
    a1 = (v_rdi) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((unsigned __int8)(result) != 0) goto loc_00237E89;
loc_00237FC6:
    v_stack_p20 = v_rdi;
    result = KeBugCheckEx(218, (unsigned int)(0x504ULL), *(unsigned __int64 *)(v_r15 + 32) + a1 * 8, 0);
loc_00237FE1:
    if (*(unsigned __int64 *)(v_rip + 12541076) == 0) goto loc_00237FFF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8 + 8))) & (16)) != 0) goto loc_00238330;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12541076));
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8 + 8)) & (a1);
loc_00237FFF:
    result = (result) >> (32);
    goto loc_00237E10;
loc_00238008:
    if (*(unsigned __int64 *)(v_rip + 12541037) == 0) goto loc_00238026;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 8))) & (16)) != 0) goto loc_00238339;
    a1 = ~(*(unsigned __int64 *)(v_rip + 12541037));
    result = (*(unsigned __int64 *)(a1 + 8)) & (a1);
loc_00238026:
    result = (result) >> (32);
    goto loc_00237E5E;
loc_0023802F:
    a1 = (a1) - (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8);
    if (a1 < 0) goto loc_00237FC6;
    v_r10 = (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8 - 1) + (0);
    result = (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8) >> (6);
    result = (v_r10) >> (6);
    if ((*(unsigned __int64 *)(v_r15 + 8) + result * 8) != (*(unsigned __int64 *)(v_r15 + 8) + result * 8)) goto loc_0023835D;
    a1 = (unsigned __int8)((64) - (0));
    result = (-1) >> ((unsigned __int8)(a1));
    result = (result) << ((unsigned __int8)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8));
    v_r11 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + result * 8)) & (result);
    if (v_r11 != result) goto loc_00237FC6;
loc_00238089:
    goto loc_00237E89;
loc_00238099:
    a2 = (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8)) & (992)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a2))) == 0) goto loc_00238342;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8) == 0) goto loc_00238517;
    if (*(unsigned __int64 *)(v_rip + 12540851) == 0) goto loc_002380E7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8))) & (16)) != 0) goto loc_002382E9;
    result = ~(*(unsigned __int64 *)(v_rip + 12540851));
    result = (result) & (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + v_rdi * 8));
loc_002380E7:
    result = (result) >> (25);
loc_002380EB:
    a2 = 0;
    if (result >= (*(unsigned __int64 *)(v_r15 + 8) + result * 8)) goto loc_00238342;
loc_002380F9:
    a1 = 0;
    if (0 == 0) goto loc_0023811C;
loc_00238110:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 32) + a1 * 8 + a1 * 8) = *(unsigned __int64 *)(v_rip - 2259079);
    a1 = (a1) + 1;
    if (a1 < 0) goto loc_00238110;
loc_0023811C:
    if ((unsigned int)((unsigned int)(v_stack_p34)) == 0) goto loc_00238142;
    result = (v_r14 + 511) & ((unsigned int)(0xFFFFFE00ULL));
    a2 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 40))) & (1));
    if (condition_is_not_equal) goto loc_00237ED3;
    goto loc_00237ED7;
loc_00238142:
    v_r10 = (unsigned int)((*(unsigned __int64 *)(v_r15 + 32) + a1 * 8) & (31));
    a1 = (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8) >> (5);
    a4 = (0) + (0);
    if ((v_r10 + v_r14 * 1) > 32) goto loc_00238307;
    if (0 == 32) goto loc_00238576;
    result = (unsigned int)((1) << (0));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned int)((unsigned int)(v_r10)))));
    result = (unsigned int)(~(result));
loc_00238192:
loc_00238196:
    if (a4 <= 0x200000ULL) goto loc_00237F37;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r15 + 40))) & (1));
    v_stack_p3C = (unsigned int)(result);
    v_r14 = 32;
    if (condition_is_equal) { v_r14 = 512; }
    a1 = ~(v_r14 - 1);
    v_r12 = (v_r14 - 1) + (v_r14);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8);
    v_r13 = (a1) & (*(unsigned __int64 *)(v_r15 + 32) + a1 * 8);
    v_r12 = (v_r12) & (a1);
    v_r12 = (v_r12) - (v_r13);
    if (condition_is_equal) goto loc_002382B8;
    v_r11 = (64) - (v_r14);
    v_stack_p48 = v_r11;
loc_00238200:
    if ((0 + v_r13 * 1) >= (*(unsigned __int64 *)(v_r15))) goto loc_002382A7;
    result = (*(unsigned __int64 *)(v_r15)) - (0 + v_r13 * 1);
    if (result < v_r14) goto loc_002382A7;
    v_r10 = (v_r14 - 1) + (0 + v_r13 * 1);
    result = (0 + v_r13 * 1) >> (6);
    result = (v_r10) >> (6);
    if ((*(unsigned __int64 *)(v_r15 + 8) + result * 8) != (*(unsigned __int64 *)(v_r15 + 8) + result * 8)) goto loc_002382CC;
    result = (-1) >> ((unsigned __int8)(v_r11));
    result = (result) << ((unsigned __int8)(0 + v_r13 * 1));
loc_00238259:
    result = (((*(unsigned __int64 *)(*(unsigned __int64 *)(v_r15 + 8) + result * 8)) & (result)) == 0) ? 1 : 0;
    if ((unsigned __int8)(result) == 0) goto loc_002382A7;
    result = RtlInterlockedSetClearRunEx(v_r15, 0 + v_r13 * 1, v_r14, *(unsigned __int64 *)(v_r15 + 8) + result * 8);
    if ((unsigned int)(result) != 0) {
        result = -16;
        a1 = -1;
        if ((unsigned int)((unsigned int)(v_stack_p3C)) == 0) { result = a1; }
        result = (result) * (v_r14);
        a4 = v_r14;
        a3 = 0 + v_r13 * 1;
        a2 = 0;
        a1 = v_r15;
        result = MiReturnSystemPtes(a1, a2, a3, a4);
    }
loc_002382A7:
    v_rbx = (0) + (v_r14);
    if (v_rbx < v_r12) goto loc_00238200;
loc_002382B8:
    goto loc_00237F37;
loc_002382CC:
    result = (result) << ((unsigned __int8)(0 + v_r13 * 1));
loc_002382D5:
    if (((a3) & (result)) != 0) goto loc_002382A7;
    a2 = (a2) + (8);
    if (a2 == a4) goto loc_002382F2;
    goto loc_002382D5;
loc_002382E9:
    result = (result) & (-17);
    goto loc_002380E7;
loc_002382F2:
    a1 = (unsigned __int8)(~((unsigned __int8)(v_r10)));
    result = (-1) >> ((unsigned __int8)(a1));
    goto loc_00238259;
loc_00238307:
    if (v_r10 != 0) goto loc_0023851E;
loc_00238310:
    if (a2 >= 32) goto loc_00238386;
loc_00238316:
    if (a2 == 0) goto loc_00238196;
    result = (unsigned int)((-1) << ((unsigned __int8)(a2)));
    goto loc_00238192;
loc_00238330:
    result = (result) & (-17);
    goto loc_00237FFF;
loc_00238339:
    result = (result) & (-17);
    goto loc_00238026;
loc_00238342:
    v_stack_p20 = a2;
    result = KeBugCheckEx(218, (unsigned int)(0x506ULL), v_rbx, *(unsigned __int64 *)(v_rbx));
loc_0023835D:
    result = (result) << ((unsigned __int8)(v_rbx));
    v_r11 = (a9) & (result);
loc_00238369:
    if (v_r11 != result) goto loc_00237FC6;
    a2 = ((unsigned int)(0x506ULL)) + (8);
    if (a2 == (*(unsigned __int64 *)(v_rbx))) goto loc_00238552;
    goto loc_00238369;
loc_00238386:
    a1 = (a2) >> (5);
    result = (result) * (a1);
    a2 = (a2) + (result);
loc_00238394:
    *(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0x506ULL) + 8)) = 0;
    v_r11 = (*(unsigned __int64 *)((unsigned int)(0x506ULL) + 8)) + (4);
    a1 = (a1) - (1);
    if (condition_is_equal) goto loc_00238316;
    goto loc_00238394;
loc_002383AB:
    v_rbx = (v_rbx) << (25);
    result = (result) << (25);
    v_rbx = (v_rbx) - (result);
    v_rbx = (v_rbx) >> (16);
    if ((*(unsigned int *)(v_rbp - 100)) != 0) goto loc_00238464;
    result = MiVaToFlushVm(v_rbx, a2, v_rbx, *(unsigned __int64 *)(v_rbx));
    *(unsigned int *)(v_rbp - 116) = 20;
    *(unsigned int *)(v_rbp - 112) = 8;
    *(unsigned int *)(v_rbp - 108) = 1;
    *(unsigned __int64 *)(v_rbp - 128) = result;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 184))) >> (8));
    a1 = (unsigned __int8)((a1) >> (3));
    a1 = (unsigned __int8)((a1) & (1));
    *(unsigned __int8 *)(v_rbp - 104) = (unsigned __int8)(a1);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 184)))) & (15)) != 0) goto loc_00238432;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) + (0x400ULL);
loc_00238432:
    *(unsigned int *)(v_rbp - 120) = 1;
    a1 = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp - 112))) & (0xFFFFFFDBULL));
    *(unsigned __int16 *)(v_rbp - 103) = 0;
    *(unsigned int *)(v_rbp - 112) = (unsigned int)(result);
    *(unsigned int *)(v_rbp - 100) = 0;
    *(unsigned __int64 *)(v_rbp - 96) = 0;
    *(unsigned __int64 *)(v_rbp - 88) = 0;
loc_00238464:
    a4 = 0;
    result = MiInsertTbFlushEntry(v_rbp - 128, v_rbx, a11, a4);
    if ((*(unsigned int *)(v_rbp - 100)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 116))))) goto loc_00238497;
    result = MiTbFlushListPromoteThreshold(v_rbp - 128, v_rbx, a11, a4);
    a1 = (*(unsigned __int64 *)(v_rbp - 96)) + 1;
    if (a1 < result) goto loc_00237F3C;
loc_00238497:
    if ((*(unsigned __int8 *)(v_rbp - 103)) != 0) goto loc_002384B8;
    if ((*(unsigned __int8 *)(v_rbp - 102)) != 0) goto loc_002384B8;
    result = MiTbFlushListPromoteThreshold(v_rbp - 128, v_rbx, a11, a4);
loc_002384B8:
    result = MiFlushTbList(v_rbp - 128, v_rbx, a11, a4);
    result = MiTbFlushTimeStampMayNeedFlush((unsigned int)(a7), (unsigned int)(*(unsigned int *)(v_rip + 14248884)), (unsigned int)(0xFFFFFFFFULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00237F3C;
    v_r14 = 0;
loc_002384E6:
    if ((*(unsigned int *)(v_rbp - 100)) == 0) goto loc_00237F6B;
    result = MiFlushTbList(v_rbp - 128, (unsigned int)(*(unsigned int *)(v_rip + 14248884)), (unsigned int)(0xFFFFFFFFULL), a4);
    goto loc_00237F6B;
loc_002384FE:
    result = 10;
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == 8) { result = 12; }
    goto loc_00237F2F;
loc_00238517:
    result = 0;
    goto loc_002380EB;
loc_0023851E:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)(v_r10)));
    result = (unsigned int)(~(result));
    a2 = (0 + v_r13 * 1) - ((unsigned int)(a2));
    v_r11 = (v_r11) + (4);
    goto loc_00238310;
loc_00238552:
    a1 = (unsigned __int8)(~((unsigned __int8)(v_r10)));
    a2 = (-1) >> ((unsigned __int8)(a1));
    result = (a2) & (v_r11);
    if (result != a2) goto loc_00237FC6;
    goto loc_00238089;
loc_00238576:
    *(unsigned int *)(v_r11) = 0;
    goto loc_00238196;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00237DE0(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11, int64_t Arg12, int64_t Arg13)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p3C;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;

loc_00237DF0:
    Arg1 = (local_r12) * (result);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8))) & (2)) == 0) goto loc_00237FE1;
loc_00237E10:
    local_r14 = (local_r14) + (Arg4);
    v_stack_p58 = local_r14;
    if (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8) == 0) goto loc_00237E70;
    if (*(uint64_t *)(v_rip + 0xBF5E5C) == 0) goto loc_00237E39;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8))) & (16)) != 0) goto loc_00237F88;
    result = ~(*(uint64_t *)(v_rip + 0xBF5E5C));
    local_rdi = (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8)) & (result);
loc_00237E39:
    local_rdi = (local_rdi) >> (25);
    v_stack_p50 = local_rdi;
    if (local_rdi == 0) goto loc_00237E75;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8))) & (2)) == 0) goto loc_00238008;
loc_00237E5E:
    result = (Arg4) + (local_rdi);
    Arg2 = 0;
    if (result != result) goto loc_00237E75;
    goto loc_00237F4E;
loc_00237E70:
    v_stack_p50 = local_rdi;
loc_00237E75:
    Arg2 = 0;
    if ((uint32_t)(local_r10) == 0) goto loc_00237F91;
loc_00237E89:
    if ((uint32_t)(local_r13) == 0) goto loc_002383AB;
    if (local_rdi == 0) goto loc_002380F9;
    if ((uint32_t)(local_r10) != 0) goto loc_002380F9;
    Arg2 = 0;
    if (local_rdi < (*(uint64_t *)(local_r15))) goto loc_00238099;
    v_stack_p20 = local_rdi;
    result = KeBugCheckEx(218, (uint32_t)(0x505ULL), *(uint64_t *)(local_r15 + 0x20) + Arg1 * 8, *(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8));
loc_00237ED3:
    Arg3 = (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8) << (4);
loc_00237ED7:
    Arg2 = (result) << (4);
    if (218 == 0) { Arg2 = result; }
    result = -(Arg2);
    Arg1 = (*(uint64_t *)(local_r15 + 0x20) + Arg3 * 8) << (25);
    Arg2 = (Arg2) << (28);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    Arg2 = (Arg2) + (Arg1);
    Arg4 = (Arg1) >> (16);
    Arg2 = (Arg2) >> (16);
    if (((uint32_t)(local_r10)) == 1) goto loc_002384FE;
loc_00237F2F:
    result = MiReturnSystemVa(Arg4, Arg2, (uint32_t)(*(uint32_t *)(local_r15 + 0x2C)), Arg4);
loc_00237F37:
loc_00237F3C:
    local_r14 = 0;
loc_00237F4E:
    Arg2 = 0;
    if (local_rdi != 0) goto loc_00237DF0;
    if ((uint32_t)(local_r13) == 0) goto loc_002384E6;
loc_00237F6B:
    local_r13 = (uint32_t)((local_r13) + 1);
    v_stack_p30 = (uint32_t)(local_r13);
loc_00237F88:
    local_rdi = (local_rdi) & (-17);
    goto loc_00237E39;
loc_00237F91:
    if (local_rdi >= (*(uint64_t *)(local_r15))) goto loc_00237FC6;
    if (0 > 1) goto loc_0023802F;
    if (0 != 1) goto loc_00237FC6;
    Arg2 = (uint32_t)((local_rdi) & (63));
    Arg1 = (local_rdi) >> (6);
    result = (condition_is_below) ? 1 : 0;
    if ((uint8_t)(result) != 0) goto loc_00237E89;
loc_00237FC6:
    v_stack_p20 = local_rdi;
    result = KeBugCheckEx(218, (uint32_t)(0x504ULL), *(uint64_t *)(local_r15 + 0x20) + Arg1 * 8, 0);
loc_00237FE1:
    if (*(uint64_t *)(v_rip + 0xBF5C94) == 0) goto loc_00237FFF;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8 + 0x8))) & (16)) != 0) goto loc_00238330;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBF5C94));
    result = (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8 + 0x8)) & (Arg1);
loc_00237FFF:
    result = (result) >> (32);
    goto loc_00237E10;
loc_00238008:
    if (*(uint64_t *)(v_rip + 0xBF5C6D) == 0) goto loc_00238026;
    if ((((uint8_t)(*(uint64_t *)(Arg1 + 0x8))) & (16)) != 0) goto loc_00238339;
    Arg1 = ~(*(uint64_t *)(v_rip + 0xBF5C6D));
    result = (*(uint64_t *)(Arg1 + 0x8)) & (Arg1);
loc_00238026:
    result = (result) >> (32);
    goto loc_00237E5E;
loc_0023802F:
    Arg1 = (Arg1) - (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8);
    if (Arg1 < 0) goto loc_00237FC6;
    local_r10 = (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8 - 1) + (0);
    result = (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8) >> (6);
    result = (local_r10) >> (6);
    if ((*(uint64_t *)(local_r15 + 0x8) + result * 8) != (*(uint64_t *)(local_r15 + 0x8) + result * 8)) goto loc_0023835D;
    Arg1 = (uint8_t)((64) - (0));
    result = (-1) >> ((uint8_t)(Arg1));
    result = (result) << ((uint8_t)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8));
    local_r11 = (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + result * 8)) & (result);
    if (local_r11 != result) goto loc_00237FC6;
loc_00238089:
    goto loc_00237E89;
loc_00238099:
    Arg2 = (((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8)) & (0xC01ULL)) == 0) ? 1 : 0;
    result = (((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8)) & (992)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg2))) == 0) goto loc_00238342;
    if (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8) == 0) goto loc_00238517;
    if (*(uint64_t *)(v_rip + 0xBF5BB3) == 0) goto loc_002380E7;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8))) & (16)) != 0) goto loc_002382E9;
    result = ~(*(uint64_t *)(v_rip + 0xBF5BB3));
    result = (result) & (*(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + local_rdi * 8));
loc_002380E7:
    result = (result) >> (25);
loc_002380EB:
    Arg2 = 0;
    if (result >= (*(uint64_t *)(local_r15 + 0x8) + result * 8)) goto loc_00238342;
loc_002380F9:
    Arg1 = 0;
    if (0 == 0) goto loc_0023811C;
loc_00238110:
    *(uint64_t *)(*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8 + Arg1 * 8) = *(uint64_t *)(v_rip - 0x227887);
    Arg1 = (Arg1) + 1;
    if (Arg1 < 0) goto loc_00238110;
loc_0023811C:
    if ((uint32_t)((uint32_t)(v_stack_p34)) == 0) goto loc_00238142;
    result = (local_r14 + 511) & ((uint32_t)(0xFFFFFE00ULL));
    Arg2 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x28))) & (1));
    if (condition_is_not_equal) goto loc_00237ED3;
    goto loc_00237ED7;
loc_00238142:
    local_r10 = (uint32_t)((*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8) & (31));
    Arg1 = (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8) >> (5);
    Arg4 = (0) + (0);
    if ((local_r10 + local_r14 * 1) > 32) goto loc_00238307;
    if (0 == 32) goto loc_00238576;
    result = (uint32_t)((1) << (0));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)((uint32_t)((uint32_t)(local_r10)))));
    result = (uint32_t)(~(result));
loc_00238192:
loc_00238196:
    if (Arg4 <= 0x200000ULL) goto loc_00237F37;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r15 + 0x28))) & (1));
    v_stack_p3C = (uint32_t)(result);
    local_r14 = 32;
    if (condition_is_equal) { local_r14 = 512; }
    Arg1 = ~(local_r14 - 1);
    local_r12 = (local_r14 - 1) + (local_r14);
    local_r12 = (local_r12) + (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8);
    local_r13 = (Arg1) & (*(uint64_t *)(local_r15 + 0x20) + Arg1 * 8);
    local_r12 = (local_r12) & (Arg1);
    local_r12 = (local_r12) - (local_r13);
    if (condition_is_equal) goto loc_002382B8;
    local_r11 = (64) - (local_r14);
    v_stack_p48 = local_r11;
loc_00238200:
    if ((0 + local_r13 * 1) >= (*(uint64_t *)(local_r15))) goto loc_002382A7;
    result = (*(uint64_t *)(local_r15)) - (0 + local_r13 * 1);
    if (result < local_r14) goto loc_002382A7;
    local_r10 = (local_r14 - 1) + (0 + local_r13 * 1);
    result = (0 + local_r13 * 1) >> (6);
    result = (local_r10) >> (6);
    if ((*(uint64_t *)(local_r15 + 0x8) + result * 8) != (*(uint64_t *)(local_r15 + 0x8) + result * 8)) goto loc_002382CC;
    result = (-1) >> ((uint8_t)(local_r11));
    result = (result) << ((uint8_t)(0 + local_r13 * 1));
loc_00238259:
    result = (((*(uint64_t *)(*(uint64_t *)(local_r15 + 0x8) + result * 8)) & (result)) == 0) ? 1 : 0;
    if ((uint8_t)(result) == 0) goto loc_002382A7;
    result = RtlInterlockedSetClearRunEx(local_r15, 0 + local_r13 * 1, local_r14, *(uint64_t *)(local_r15 + 0x8) + result * 8);
    if ((uint32_t)(result) != 0) {
        result = -16;
        Arg1 = -1;
        if ((uint32_t)((uint32_t)(v_stack_p3C)) == 0) { result = Arg1; }
        result = (result) * (local_r14);
        Arg4 = local_r14;
        Arg3 = 0 + local_r13 * 1;
        Arg2 = 0;
        Arg1 = local_r15;
        result = MiReturnSystemPtes(Arg1, Arg2, Arg3, Arg4);
    }
loc_002382A7:
    local_rbx = (0) + (local_r14);
    if (local_rbx < local_r12) goto loc_00238200;
loc_002382B8:
    goto loc_00237F37;
loc_002382CC:
    result = (result) << ((uint8_t)(0 + local_r13 * 1));
loc_002382D5:
    if (((Arg3) & (result)) != 0) goto loc_002382A7;
    Arg2 = (Arg2) + (8);
    if (Arg2 == Arg4) goto loc_002382F2;
    goto loc_002382D5;
loc_002382E9:
    result = (result) & (-17);
    goto loc_002380E7;
loc_002382F2:
    Arg1 = (uint8_t)(~((uint8_t)(local_r10)));
    result = (-1) >> ((uint8_t)(Arg1));
    goto loc_00238259;
loc_00238307:
    if (local_r10 != 0) goto loc_0023851E;
loc_00238310:
    if (Arg2 >= 32) goto loc_00238386;
loc_00238316:
    if (Arg2 == 0) goto loc_00238196;
    result = (uint32_t)((-1) << ((uint8_t)(Arg2)));
    goto loc_00238192;
loc_00238330:
    result = (result) & (-17);
    goto loc_00237FFF;
loc_00238339:
    result = (result) & (-17);
    goto loc_00238026;
loc_00238342:
    v_stack_p20 = Arg2;
    result = KeBugCheckEx(218, (uint32_t)(0x506ULL), local_rbx, *(uint64_t *)(local_rbx));
loc_0023835D:
    result = (result) << ((uint8_t)(local_rbx));
    local_r11 = (Arg9) & (result);
loc_00238369:
    if (local_r11 != result) goto loc_00237FC6;
    Arg2 = ((uint32_t)(0x506ULL)) + (8);
    if (Arg2 == (*(uint64_t *)(local_rbx))) goto loc_00238552;
    goto loc_00238369;
loc_00238386:
    Arg1 = (Arg2) >> (5);
    result = (result) * (Arg1);
    Arg2 = (Arg2) + (result);
loc_00238394:
    *(uint32_t *)(*(uint64_t *)((uint32_t)(0x506ULL) + 0x8)) = 0;
    local_r11 = (*(uint64_t *)((uint32_t)(0x506ULL) + 0x8)) + (4);
    Arg1 = (Arg1) - (1);
    if (condition_is_equal) goto loc_00238316;
    goto loc_00238394;
loc_002383AB:
    local_rbx = (local_rbx) << (25);
    result = (result) << (25);
    local_rbx = (local_rbx) - (result);
    local_rbx = (local_rbx) >> (16);
    if ((*(uint32_t *)(local_rbp - 0x64)) != 0) goto loc_00238464;
    result = MiVaToFlushVm(local_rbx, Arg2, local_rbx, *(uint64_t *)(local_rbx));
    *(uint32_t *)(local_rbp - 0x74) = 20;
    *(uint32_t *)(local_rbp - 0x70) = 8;
    *(uint32_t *)(local_rbp - 0x6C) = 1;
    *(uint64_t *)(local_rbp - 0x80) = result;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0xB8))) >> (8));
    Arg1 = (uint8_t)((Arg1) >> (3));
    Arg1 = (uint8_t)((Arg1) & (1));
    *(uint8_t *)(local_rbp - 0x68) = (uint8_t)(Arg1);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xB8)))) & (15)) != 0) goto loc_00238432;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) + (0x400ULL);
loc_00238432:
    *(uint32_t *)(local_rbp - 0x78) = 1;
    Arg1 = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp - 0x70))) & (0xFFFFFFDBULL));
    *(uint16_t *)(local_rbp - 0x67) = 0;
    *(uint32_t *)(local_rbp - 0x70) = (uint32_t)(result);
    *(uint32_t *)(local_rbp - 0x64) = 0;
    *(uint64_t *)(local_rbp - 0x60) = 0;
    *(uint64_t *)(local_rbp - 0x58) = 0;
loc_00238464:
    Arg4 = 0;
    result = MiInsertTbFlushEntry(local_rbp - 128, local_rbx, Arg11, Arg4);
    if ((*(uint32_t *)(local_rbp - 0x64)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x74))))) goto loc_00238497;
    result = MiTbFlushListPromoteThreshold(local_rbp - 128, local_rbx, Arg11, Arg4);
    Arg1 = (*(uint64_t *)(local_rbp - 0x60)) + 1;
    if (Arg1 < result) goto loc_00237F3C;
loc_00238497:
    if ((*(uint8_t *)(local_rbp - 0x67)) != 0) goto loc_002384B8;
    if ((*(uint8_t *)(local_rbp - 0x66)) != 0) goto loc_002384B8;
    result = MiTbFlushListPromoteThreshold(local_rbp - 128, local_rbx, Arg11, Arg4);
loc_002384B8:
    result = MiFlushTbList(local_rbp - 128, local_rbx, Arg11, Arg4);
    result = MiTbFlushTimeStampMayNeedFlush((uint32_t)(Arg7), (uint32_t)(*(uint32_t *)(v_rip + 0xD96BB4)), (uint32_t)(0xFFFFFFFFULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00237F3C;
    local_r14 = 0;
loc_002384E6:
    if ((*(uint32_t *)(local_rbp - 0x64)) == 0) goto loc_00237F6B;
    result = MiFlushTbList(local_rbp - 128, (uint32_t)(*(uint32_t *)(v_rip + 0xD96BB4)), (uint32_t)(0xFFFFFFFFULL), Arg4);
    goto loc_00237F6B;
loc_002384FE:
    result = 10;
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == 8) { result = 12; }
    goto loc_00237F2F;
loc_00238517:
    result = 0;
    goto loc_002380EB;
loc_0023851E:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)(local_r10)));
    result = (uint32_t)(~(result));
    Arg2 = (0 + local_r13 * 1) - ((uint32_t)(Arg2));
    local_r11 = (local_r11) + (4);
    goto loc_00238310;
loc_00238552:
    Arg1 = (uint8_t)(~((uint8_t)(local_r10)));
    Arg2 = (-1) >> ((uint8_t)(Arg1));
    result = (Arg2) & (local_r11);
    if (result != Arg2) goto loc_00237FC6;
    goto loc_00238089;
loc_00238576:
    *(uint32_t *)(local_r11) = 0;
    goto loc_00238196;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00237DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
