# DifExEnterPriorityRegionAndAcquireResourceExclusiveWrapper

- RVA: `0x00620140`–`0x006202A1` (길이 `353` bytes)
- VA: `0x0000000140620140`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062016F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00620197` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006201C5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006201EC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620205` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062020D` → [ExEnterPriorityRegionAndAcquireResourceExclusive](../65/ExEnterPriorityRegionAndAcquireResourceExclusive_function_00658D40.md) (function, `0x00658D40`)
- `0x0062023B` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620262` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062027B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006201A9` → RVA `0x00F048B8` (`.data`; read)
- `0x006201B2` → RVA `0x00F04980` (`.data`; read)
- `0x006201BE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00620140  4C 8B DC                        mov r11, rsp
00620143  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00620147  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062014B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062014F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00620153  41 56                           push r14
00620155  48 83 EC 40                     sub rsp, 0x40
00620159  33 C0                           xor eax, eax
0062015B  0F 57 C0                        xorps xmm0, xmm0
0062015E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00620163  48 8B E9                        mov rbp, rcx
00620166  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062016A  B9 93 01 00 00                  mov ecx, 0x193
0062016F  E8 C0 58 E7 FF                  call 0x140495a34
00620174  48 8B F0                        mov rsi, rax
00620177  48 85 C0                        test rax, rax
0062017A  0F 84 8A 00 00 00               je 0x14062020a
00620180  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00620183  A8 18                           test al, 0x18
00620185  74 0C                           je 0x140620193
00620187  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062018C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00620191  EB 0E                           jmp 0x1406201a1
00620193  A8 04                           test al, 4
00620195  74 0A                           je 0x1406201a1
00620197  E8 6C 3A EB FF                  call 0x1404d3c08
0062019C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006201A1  40 32 FF                        xor dil, dil
006201A4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006201A9  40 38 3D 08 47 8E 00            cmp byte ptr [rip + 0x8e4708], dil
006201B0  75 0C                           jne 0x1406201be
006201B2  F7 05 C4 47 8E 00 00 08 00 00   test dword ptr [rip + 0x8e47c4], 0x800
006201BC  74 13                           je 0x1406201d1
006201BE  48 8D 0D BB 3C 8E 00            lea rcx, [rip + 0x8e3cbb]
006201C5  E8 56 64 BF FF                  call 0x140216620
006201CA  40 8A F8                        mov dil, al
006201CD  84 C0                           test al, al
006201CF  74 39                           je 0x14062020a
006201D1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006201D5  49 8B 1E                        mov rbx, qword ptr [r14]
006201D8  EB 1A                           jmp 0x1406201f4
006201DA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006201DE  48 85 C0                        test rax, rax
006201E1  74 0E                           je 0x1406201f1
006201E3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006201E7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006201EC  E8 DF A8 09 00                  call 0x1406baad0
006201F1  48 8B 1B                        mov rbx, qword ptr [rbx]
006201F4  49 3B DE                        cmp rbx, r14
006201F7  75 E1                           jne 0x1406201da
006201F9  40 84 FF                        test dil, dil
006201FC  74 0C                           je 0x14062020a
006201FE  48 8D 0D 7B 3C 8E 00            lea rcx, [rip + 0x8e3c7b]
00620205  E8 76 9C D2 FF                  call 0x140349e80
0062020A  48 8B CD                        mov rcx, rbp
0062020D  E8 2E 8B 03 00                  call 0x140658d40
00620212  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00620217  48 85 F6                        test rsi, rsi
0062021A  74 64                           je 0x140620280
0062021C  40 32 FF                        xor dil, dil
0062021F  40 38 3D 92 46 8E 00            cmp byte ptr [rip + 0x8e4692], dil
00620226  75 0C                           jne 0x140620234
00620228  F7 05 4E 47 8E 00 00 08 00 00   test dword ptr [rip + 0x8e474e], 0x800
00620232  74 13                           je 0x140620247
00620234  48 8D 0D 45 3C 8E 00            lea rcx, [rip + 0x8e3c45]
0062023B  E8 E0 63 BF FF                  call 0x140216620
00620240  40 8A F8                        mov dil, al
00620243  84 C0                           test al, al
00620245  74 39                           je 0x140620280
00620247  48 83 C6 30                     add rsi, 0x30
0062024B  48 8B 1E                        mov rbx, qword ptr [rsi]
0062024E  EB 1A                           jmp 0x14062026a
00620250  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620254  48 85 C0                        test rax, rax
00620257  74 0E                           je 0x140620267
00620259  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062025D  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620262  E8 69 A8 09 00                  call 0x1406baad0
00620267  48 8B 1B                        mov rbx, qword ptr [rbx]
0062026A  48 3B DE                        cmp rbx, rsi
0062026D  75 E1                           jne 0x140620250
0062026F  40 84 FF                        test dil, dil
00620272  74 0C                           je 0x140620280
00620274  48 8D 0D 05 3C 8E 00            lea rcx, [rip + 0x8e3c05]
0062027B  E8 00 9C D2 FF                  call 0x140349e80
00620280  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00620285  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062028A  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062028F  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00620294  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00620299  48 83 C4 40                     add rsp, 0x40
0062029D  41 5E                           pop r14
0062029F  C3                              ret
006202A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExEnterPriorityRegionAndAcquireResourceExclusiveWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(403, a2, a3, a4);
    if (result == 0) goto loc_0062020A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00620193;
    v_stack_m28 = v_stack_p0;
    goto loc_006201A1;
loc_00620193:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9324296)) != 0) goto loc_006201BE;
    if (((*(unsigned int *)(v_rip + 9324484)) & (0x800ULL)) == 0) goto loc_006201D1;
loc_006201BE:
    result = ExAcquireRundownProtection(v_rip + 9321659, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062020A;
loc_006201D1:
    goto loc_006201F4;
loc_006201DA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_006201F4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006201DA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321595;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExEnterPriorityRegionAndAcquireResourceExclusive(a1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00620280;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9324178)) != 0) goto loc_00620234;
    if (((*(unsigned int *)(v_rip + 9324366)) & (0x800ULL)) == 0) goto loc_00620247;
loc_00620234:
    result = ExAcquireRundownProtection(v_rip + 9321541, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00620280;
loc_00620247:
    v_rsi = (result) + (48);
    goto loc_0062026A;
loc_00620250:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062026A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00620250;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9321477;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExEnterPriorityRegionAndAcquireResourceExclusiveWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(403, a2, a3, a4);
    if (result == 0) goto loc_0062020A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00620193;
    v_stack_m28 = v_stack_p0;
    goto loc_006201A1;
loc_00620193:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E4708)) != 0) goto loc_006201BE;
    if (((*(uint32_t *)(v_rip + 0x8E47C4)) & (0x800ULL)) == 0) goto loc_006201D1;
loc_006201BE:
    result = ExAcquireRundownProtection(v_rip + 9321659, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062020A;
loc_006201D1:
    goto loc_006201F4;
loc_006201DA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_006201F4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006201DA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321595;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExEnterPriorityRegionAndAcquireResourceExclusive(Arg1, a2, a3, a4);
    v_stack_m18 = result;
    if (result == 0) goto loc_00620280;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E4692)) != 0) goto loc_00620234;
    if (((*(uint32_t *)(v_rip + 0x8E474E)) & (0x800ULL)) == 0) goto loc_00620247;
loc_00620234:
    result = ExAcquireRundownProtection(v_rip + 9321541, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00620280;
loc_00620247:
    local_rsi = (result) + (48);
    goto loc_0062026A;
loc_00620250:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062026A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00620250;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9321477;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00620140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00620140[BB_00620140]
  bb_00620180[BB_00620180]
  bb_00620187[BB_00620187]
  bb_00620193[BB_00620193]
  bb_00620197[BB_00620197]
  bb_006201A1[BB_006201A1]
  bb_006201B2[BB_006201B2]
  bb_006201BE[BB_006201BE]
  bb_006201D1[BB_006201D1]
  bb_006201DA[BB_006201DA]
  bb_006201E3[BB_006201E3]
  bb_006201F1[BB_006201F1]
  bb_006201F4[BB_006201F4]
  bb_006201F9[BB_006201F9]
  bb_006201FE[BB_006201FE]
  bb_0062020A[BB_0062020A]
  bb_0062021C[BB_0062021C]
  bb_00620228[BB_00620228]
  bb_00620234[BB_00620234]
  bb_00620247[BB_00620247]
  bb_00620250[BB_00620250]
  bb_00620259[BB_00620259]
  bb_00620267[BB_00620267]
  bb_0062026A[BB_0062026A]
  bb_0062026F[BB_0062026F]
  bb_00620274[BB_00620274]
  bb_00620280[BB_00620280]
  bb_006202A0[BB_006202A0]
  bb_00620140 -->|branch| bb_0062020A
  bb_00620140 -->|fallthrough| bb_00620180
  bb_00620180 -->|branch| bb_00620193
  bb_00620180 -->|fallthrough| bb_00620187
  bb_00620187 -->|branch| bb_006201A1
  bb_00620193 -->|branch| bb_006201A1
  bb_00620193 -->|fallthrough| bb_00620197
  bb_00620197 -->|flow| bb_006201A1
  bb_006201A1 -->|branch| bb_006201BE
  bb_006201A1 -->|fallthrough| bb_006201B2
  bb_006201B2 -->|branch| bb_006201D1
  bb_006201B2 -->|fallthrough| bb_006201BE
  bb_006201BE -->|branch| bb_0062020A
  bb_006201BE -->|fallthrough| bb_006201D1
  bb_006201D1 -->|branch| bb_006201F4
  bb_006201DA -->|branch| bb_006201F1
  bb_006201DA -->|fallthrough| bb_006201E3
  bb_006201E3 -->|flow| bb_006201F1
  bb_006201F1 -->|flow| bb_006201F4
  bb_006201F4 -->|branch| bb_006201DA
  bb_006201F4 -->|fallthrough| bb_006201F9
  bb_006201F9 -->|branch| bb_0062020A
  bb_006201F9 -->|fallthrough| bb_006201FE
  bb_006201FE -->|flow| bb_0062020A
  bb_0062020A -->|branch| bb_00620280
  bb_0062020A -->|fallthrough| bb_0062021C
  bb_0062021C -->|branch| bb_00620234
  bb_0062021C -->|fallthrough| bb_00620228
  bb_00620228 -->|branch| bb_00620247
  bb_00620228 -->|fallthrough| bb_00620234
  bb_00620234 -->|branch| bb_00620280
  bb_00620234 -->|fallthrough| bb_00620247
  bb_00620247 -->|branch| bb_0062026A
  bb_00620250 -->|branch| bb_00620267
  bb_00620250 -->|fallthrough| bb_00620259
  bb_00620259 -->|flow| bb_00620267
  bb_00620267 -->|flow| bb_0062026A
  bb_0062026A -->|branch| bb_00620250
  bb_0062026A -->|fallthrough| bb_0062026F
  bb_0062026F -->|branch| bb_00620280
  bb_0062026F -->|fallthrough| bb_00620274
  bb_00620274 -->|flow| bb_00620280
```
