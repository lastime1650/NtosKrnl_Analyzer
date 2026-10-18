# DifRtlOemStringToCountedUnicodeStringWrapper

- RVA: `0x0063BDC0`–`0x0063BF37` (길이 `375` bytes)
- VA: `0x000000014063BDC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063BDFE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063BE24` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063BE58` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063BE7E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BE97` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063BEA5` → [RtlOemStringToCountedUnicodeString](../../page/90/RtlOemStringToCountedUnicodeString_function_0090F3D0.md) (function, `0x0090F3D0`)
- `0x0063BED1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063BEF7` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063BF10` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063BE34` → RVA `0x00F048B8` (`.data`; read)
- `0x0063BE45` → RVA `0x00F04980` (`.data`; read)
- `0x0063BE51` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063BEA5` → [RtlOemStringToCountedUnicodeString](../../page/90/RtlOemStringToCountedUnicodeString_function_0090F3D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063BDC0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063BDC5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063BDCA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063BDCF  55                              push rbp
0063BDD0  41 54                           push r12
0063BDD2  41 55                           push r13
0063BDD4  41 56                           push r14
0063BDD6  41 57                           push r15
0063BDD8  48 8B EC                        mov rbp, rsp
0063BDDB  48 83 EC 50                     sub rsp, 0x50
0063BDDF  0F 57 C0                        xorps xmm0, xmm0
0063BDE2  33 C0                           xor eax, eax
0063BDE4  4C 8B E9                        mov r13, rcx
0063BDE7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063BDEB  B9 A1 00 00 00                  mov ecx, 0xa1
0063BDF0  45 8A F8                        mov r15b, r8b
0063BDF3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063BDF7  4C 8B E2                        mov r12, rdx
0063BDFA  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063BDFE  E8 31 9C E5 FF                  call 0x140495a34
0063BE03  48 8B F0                        mov rsi, rax
0063BE06  48 85 C0                        test rax, rax
0063BE09  0F 84 8D 00 00 00               je 0x14063be9c
0063BE0F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063BE12  A8 18                           test al, 0x18
0063BE14  74 0A                           je 0x14063be20
0063BE16  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063BE1A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063BE1E  EB 0D                           jmp 0x14063be2d
0063BE20  A8 04                           test al, 4
0063BE22  74 09                           je 0x14063be2d
0063BE24  E8 DF 7D E9 FF                  call 0x1404d3c08
0063BE29  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063BE2D  45 32 F6                        xor r14b, r14b
0063BE30  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063BE34  44 38 35 7D 8A 8C 00            cmp byte ptr [rip + 0x8c8a7d], r14b
0063BE3B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063BE3F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063BE43  75 0C                           jne 0x14063be51
0063BE45  F7 05 31 8B 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8b31], 0x800
0063BE4F  74 13                           je 0x14063be64
0063BE51  48 8D 0D 28 80 8C 00            lea rcx, [rip + 0x8c8028]
0063BE58  E8 C3 A7 BD FF                  call 0x140216620
0063BE5D  44 8A F0                        mov r14b, al
0063BE60  84 C0                           test al, al
0063BE62  74 38                           je 0x14063be9c
0063BE64  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063BE68  48 8B 1F                        mov rbx, qword ptr [rdi]
0063BE6B  EB 19                           jmp 0x14063be86
0063BE6D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063BE71  48 85 C0                        test rax, rax
0063BE74  74 0D                           je 0x14063be83
0063BE76  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063BE7A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063BE7E  E8 4D EC 07 00                  call 0x1406baad0
0063BE83  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BE86  48 3B DF                        cmp rbx, rdi
0063BE89  75 E2                           jne 0x14063be6d
0063BE8B  45 84 F6                        test r14b, r14b
0063BE8E  74 0C                           je 0x14063be9c
0063BE90  48 8D 0D E9 7F 8C 00            lea rcx, [rip + 0x8c7fe9]
0063BE97  E8 E4 DF D0 FF                  call 0x140349e80
0063BE9C  45 8A C7                        mov r8b, r15b
0063BE9F  49 8B D4                        mov rdx, r12
0063BEA2  49 8B CD                        mov rcx, r13
0063BEA5  E8 26 35 2D 00                  call 0x14090f3d0
0063BEAA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063BEAD  48 85 F6                        test rsi, rsi
0063BEB0  74 63                           je 0x14063bf15
0063BEB2  40 32 FF                        xor dil, dil
0063BEB5  40 38 3D FC 89 8C 00            cmp byte ptr [rip + 0x8c89fc], dil
0063BEBC  75 0C                           jne 0x14063beca
0063BEBE  F7 05 B8 8A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c8ab8], 0x800
0063BEC8  74 13                           je 0x14063bedd
0063BECA  48 8D 0D AF 7F 8C 00            lea rcx, [rip + 0x8c7faf]
0063BED1  E8 4A A7 BD FF                  call 0x140216620
0063BED6  40 8A F8                        mov dil, al
0063BED9  84 C0                           test al, al
0063BEDB  74 38                           je 0x14063bf15
0063BEDD  48 83 C6 30                     add rsi, 0x30
0063BEE1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063BEE4  EB 19                           jmp 0x14063beff
0063BEE6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063BEEA  48 85 C0                        test rax, rax
0063BEED  74 0D                           je 0x14063befc
0063BEEF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063BEF3  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063BEF7  E8 D4 EB 07 00                  call 0x1406baad0
0063BEFC  48 8B 1B                        mov rbx, qword ptr [rbx]
0063BEFF  48 3B DE                        cmp rbx, rsi
0063BF02  75 E2                           jne 0x14063bee6
0063BF04  40 84 FF                        test dil, dil
0063BF07  74 0C                           je 0x14063bf15
0063BF09  48 8D 0D 70 7F 8C 00            lea rcx, [rip + 0x8c7f70]
0063BF10  E8 6B DF D0 FF                  call 0x140349e80
0063BF15  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063BF18  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063BF1D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063BF21  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063BF25  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063BF29  49 8B E3                        mov rsp, r11
0063BF2C  41 5F                           pop r15
0063BF2E  41 5E                           pop r14
0063BF30  41 5D                           pop r13
0063BF32  41 5C                           pop r12
0063BF34  5D                              pop rbp
0063BF35  C3                              ret
0063BF36  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlOemStringToCountedUnicodeStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(161, a2, a3, a4);
    if (result == 0) goto loc_0063BE9C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063BE20;
    v_stack_m58 = v_stack_p0;
    goto loc_0063BE2D;
loc_0063BE20:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9210493)) != 0) goto loc_0063BE51;
    if (((*(unsigned int *)(v_rip + 9210673)) & (0x800ULL)) == 0) goto loc_0063BE64;
loc_0063BE51:
    result = ExAcquireRundownProtection(v_rip + 9207848, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BE9C;
loc_0063BE64:
    goto loc_0063BE86;
loc_0063BE6D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BE86:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063BE6D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9207785;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlOemStringToCountedUnicodeString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063BF15;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9210364)) != 0) goto loc_0063BECA;
    if (((*(unsigned int *)(v_rip + 9210552)) & (0x800ULL)) == 0) goto loc_0063BEDD;
loc_0063BECA:
    result = ExAcquireRundownProtection(v_rip + 9207727, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063BF15;
loc_0063BEDD:
    v_rsi = (result) + (48);
    goto loc_0063BEFF;
loc_0063BEE6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063BEFF:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063BEE6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9207664;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlOemStringToCountedUnicodeStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(161, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063BE9C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063BE20;
    v_stack_m58 = v_stack_p0;
    goto loc_0063BE2D;
loc_0063BE20:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C8A7D)) != 0) goto loc_0063BE51;
    if (((*(uint32_t *)(v_rip + 0x8C8B31)) & (0x800ULL)) == 0) goto loc_0063BE64;
loc_0063BE51:
    result = ExAcquireRundownProtection(v_rip + 9207848, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BE9C;
loc_0063BE64:
    goto loc_0063BE86;
loc_0063BE6D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BE86:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063BE6D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9207785;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlOemStringToCountedUnicodeString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063BF15;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C89FC)) != 0) goto loc_0063BECA;
    if (((*(uint32_t *)(v_rip + 0x8C8AB8)) & (0x800ULL)) == 0) goto loc_0063BEDD;
loc_0063BECA:
    result = ExAcquireRundownProtection(v_rip + 9207727, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063BF15;
loc_0063BEDD:
    local_rsi = (result) + (48);
    goto loc_0063BEFF;
loc_0063BEE6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063BEFF:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063BEE6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9207664;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063BDC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063BDC0[BB_0063BDC0]
  bb_0063BE0F[BB_0063BE0F]
  bb_0063BE16[BB_0063BE16]
  bb_0063BE20[BB_0063BE20]
  bb_0063BE24[BB_0063BE24]
  bb_0063BE2D[BB_0063BE2D]
  bb_0063BE45[BB_0063BE45]
  bb_0063BE51[BB_0063BE51]
  bb_0063BE64[BB_0063BE64]
  bb_0063BE6D[BB_0063BE6D]
  bb_0063BE76[BB_0063BE76]
  bb_0063BE83[BB_0063BE83]
  bb_0063BE86[BB_0063BE86]
  bb_0063BE8B[BB_0063BE8B]
  bb_0063BE90[BB_0063BE90]
  bb_0063BE9C[BB_0063BE9C]
  bb_0063BEB2[BB_0063BEB2]
  bb_0063BEBE[BB_0063BEBE]
  bb_0063BECA[BB_0063BECA]
  bb_0063BEDD[BB_0063BEDD]
  bb_0063BEE6[BB_0063BEE6]
  bb_0063BEEF[BB_0063BEEF]
  bb_0063BEFC[BB_0063BEFC]
  bb_0063BEFF[BB_0063BEFF]
  bb_0063BF04[BB_0063BF04]
  bb_0063BF09[BB_0063BF09]
  bb_0063BF15[BB_0063BF15]
  bb_0063BF36[BB_0063BF36]
  bb_0063BDC0 -->|branch| bb_0063BE9C
  bb_0063BDC0 -->|fallthrough| bb_0063BE0F
  bb_0063BE0F -->|branch| bb_0063BE20
  bb_0063BE0F -->|fallthrough| bb_0063BE16
  bb_0063BE16 -->|branch| bb_0063BE2D
  bb_0063BE20 -->|branch| bb_0063BE2D
  bb_0063BE20 -->|fallthrough| bb_0063BE24
  bb_0063BE24 -->|flow| bb_0063BE2D
  bb_0063BE2D -->|branch| bb_0063BE51
  bb_0063BE2D -->|fallthrough| bb_0063BE45
  bb_0063BE45 -->|branch| bb_0063BE64
  bb_0063BE45 -->|fallthrough| bb_0063BE51
  bb_0063BE51 -->|branch| bb_0063BE9C
  bb_0063BE51 -->|fallthrough| bb_0063BE64
  bb_0063BE64 -->|branch| bb_0063BE86
  bb_0063BE6D -->|branch| bb_0063BE83
  bb_0063BE6D -->|fallthrough| bb_0063BE76
  bb_0063BE76 -->|flow| bb_0063BE83
  bb_0063BE83 -->|flow| bb_0063BE86
  bb_0063BE86 -->|branch| bb_0063BE6D
  bb_0063BE86 -->|fallthrough| bb_0063BE8B
  bb_0063BE8B -->|branch| bb_0063BE9C
  bb_0063BE8B -->|fallthrough| bb_0063BE90
  bb_0063BE90 -->|flow| bb_0063BE9C
  bb_0063BE9C -->|branch| bb_0063BF15
  bb_0063BE9C -->|fallthrough| bb_0063BEB2
  bb_0063BEB2 -->|branch| bb_0063BECA
  bb_0063BEB2 -->|fallthrough| bb_0063BEBE
  bb_0063BEBE -->|branch| bb_0063BEDD
  bb_0063BEBE -->|fallthrough| bb_0063BECA
  bb_0063BECA -->|branch| bb_0063BF15
  bb_0063BECA -->|fallthrough| bb_0063BEDD
  bb_0063BEDD -->|branch| bb_0063BEFF
  bb_0063BEE6 -->|branch| bb_0063BEFC
  bb_0063BEE6 -->|fallthrough| bb_0063BEEF
  bb_0063BEEF -->|flow| bb_0063BEFC
  bb_0063BEFC -->|flow| bb_0063BEFF
  bb_0063BEFF -->|branch| bb_0063BEE6
  bb_0063BEFF -->|fallthrough| bb_0063BF04
  bb_0063BF04 -->|branch| bb_0063BF15
  bb_0063BF04 -->|fallthrough| bb_0063BF09
  bb_0063BF09 -->|flow| bb_0063BF15
```
