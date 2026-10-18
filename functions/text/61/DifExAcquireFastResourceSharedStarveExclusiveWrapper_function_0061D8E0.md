# DifExAcquireFastResourceSharedStarveExclusiveWrapper

- RVA: `0x0061D8E0`–`0x0061DA57` (길이 `375` bytes)
- VA: `0x000000014061D8E0`
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
- `0x0061D91E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061D944` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061D978` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061D99E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061D9B7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061D9C5` → [ExAcquireFastResourceSharedStarveExclusive](../3B/ExAcquireFastResourceSharedStarveExclusive_function_003BDC80.md) (function, `0x003BDC80`)
- `0x0061D9F1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061DA17` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061DA30` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061D954` → RVA `0x00F048B8` (`.data`; read)
- `0x0061D965` → RVA `0x00F04980` (`.data`; read)
- `0x0061D971` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061D8E0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0061D8E5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0061D8EA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0061D8EF  55                              push rbp
0061D8F0  41 54                           push r12
0061D8F2  41 55                           push r13
0061D8F4  41 56                           push r14
0061D8F6  41 57                           push r15
0061D8F8  48 8B EC                        mov rbp, rsp
0061D8FB  48 83 EC 50                     sub rsp, 0x50
0061D8FF  0F 57 C0                        xorps xmm0, xmm0
0061D902  33 C0                           xor eax, eax
0061D904  4C 8B E9                        mov r13, rcx
0061D907  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061D90B  B9 BC 01 00 00                  mov ecx, 0x1bc
0061D910  45 8A F8                        mov r15b, r8b
0061D913  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061D917  4C 8B E2                        mov r12, rdx
0061D91A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061D91E  E8 11 81 E7 FF                  call 0x140495a34
0061D923  48 8B F0                        mov rsi, rax
0061D926  48 85 C0                        test rax, rax
0061D929  0F 84 8D 00 00 00               je 0x14061d9bc
0061D92F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061D932  A8 18                           test al, 0x18
0061D934  74 0A                           je 0x14061d940
0061D936  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061D93A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0061D93E  EB 0D                           jmp 0x14061d94d
0061D940  A8 04                           test al, 4
0061D942  74 09                           je 0x14061d94d
0061D944  E8 BF 62 EB FF                  call 0x1404d3c08
0061D949  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061D94D  45 32 F6                        xor r14b, r14b
0061D950  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061D954  44 38 35 5D 6F 8E 00            cmp byte ptr [rip + 0x8e6f5d], r14b
0061D95B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0061D95F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0061D963  75 0C                           jne 0x14061d971
0061D965  F7 05 11 70 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7011], 0x800
0061D96F  74 13                           je 0x14061d984
0061D971  48 8D 0D 08 65 8E 00            lea rcx, [rip + 0x8e6508]
0061D978  E8 A3 8C BF FF                  call 0x140216620
0061D97D  44 8A F0                        mov r14b, al
0061D980  84 C0                           test al, al
0061D982  74 38                           je 0x14061d9bc
0061D984  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061D988  48 8B 1F                        mov rbx, qword ptr [rdi]
0061D98B  EB 19                           jmp 0x14061d9a6
0061D98D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061D991  48 85 C0                        test rax, rax
0061D994  74 0D                           je 0x14061d9a3
0061D996  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061D99A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061D99E  E8 2D D1 09 00                  call 0x1406baad0
0061D9A3  48 8B 1B                        mov rbx, qword ptr [rbx]
0061D9A6  48 3B DF                        cmp rbx, rdi
0061D9A9  75 E2                           jne 0x14061d98d
0061D9AB  45 84 F6                        test r14b, r14b
0061D9AE  74 0C                           je 0x14061d9bc
0061D9B0  48 8D 0D C9 64 8E 00            lea rcx, [rip + 0x8e64c9]
0061D9B7  E8 C4 C4 D2 FF                  call 0x140349e80
0061D9BC  45 8A C7                        mov r8b, r15b
0061D9BF  49 8B D4                        mov rdx, r12
0061D9C2  49 8B CD                        mov rcx, r13
0061D9C5  E8 B6 02 DA FF                  call 0x1403bdc80
0061D9CA  88 45 F0                        mov byte ptr [rbp - 0x10], al
0061D9CD  48 85 F6                        test rsi, rsi
0061D9D0  74 63                           je 0x14061da35
0061D9D2  40 32 FF                        xor dil, dil
0061D9D5  40 38 3D DC 6E 8E 00            cmp byte ptr [rip + 0x8e6edc], dil
0061D9DC  75 0C                           jne 0x14061d9ea
0061D9DE  F7 05 98 6F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e6f98], 0x800
0061D9E8  74 13                           je 0x14061d9fd
0061D9EA  48 8D 0D 8F 64 8E 00            lea rcx, [rip + 0x8e648f]
0061D9F1  E8 2A 8C BF FF                  call 0x140216620
0061D9F6  40 8A F8                        mov dil, al
0061D9F9  84 C0                           test al, al
0061D9FB  74 38                           je 0x14061da35
0061D9FD  48 83 C6 30                     add rsi, 0x30
0061DA01  48 8B 1E                        mov rbx, qword ptr [rsi]
0061DA04  EB 19                           jmp 0x14061da1f
0061DA06  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061DA0A  48 85 C0                        test rax, rax
0061DA0D  74 0D                           je 0x14061da1c
0061DA0F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061DA13  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061DA17  E8 B4 D0 09 00                  call 0x1406baad0
0061DA1C  48 8B 1B                        mov rbx, qword ptr [rbx]
0061DA1F  48 3B DE                        cmp rbx, rsi
0061DA22  75 E2                           jne 0x14061da06
0061DA24  40 84 FF                        test dil, dil
0061DA27  74 0C                           je 0x14061da35
0061DA29  48 8D 0D 50 64 8E 00            lea rcx, [rip + 0x8e6450]
0061DA30  E8 4B C4 D2 FF                  call 0x140349e80
0061DA35  8A 45 F0                        mov al, byte ptr [rbp - 0x10]
0061DA38  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0061DA3D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0061DA41  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0061DA45  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0061DA49  49 8B E3                        mov rsp, r11
0061DA4C  41 5F                           pop r15
0061DA4E  41 5E                           pop r14
0061DA50  41 5D                           pop r13
0061DA52  41 5C                           pop r12
0061DA54  5D                              pop rbp
0061DA55  C3                              ret
0061DA56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExAcquireFastResourceSharedStarveExclusiveWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
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
    result = DifGetAPIThunkContextById(444, a2, a3, a4);
    if (result == 0) goto loc_0061D9BC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061D940;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D94D;
loc_0061D940:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9334621)) != 0) goto loc_0061D971;
    if (((*(unsigned int *)(v_rip + 9334801)) & (0x800ULL)) == 0) goto loc_0061D984;
loc_0061D971:
    result = ExAcquireRundownProtection(v_rip + 9331976, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061D9BC;
loc_0061D984:
    goto loc_0061D9A6;
loc_0061D98D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061D9A6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061D98D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9331913;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExAcquireFastResourceSharedStarveExclusive(a1, a2, a3, a4);
    v_stack_m38 = (unsigned __int8)(result);
    if (result == 0) goto loc_0061DA35;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9334492)) != 0) goto loc_0061D9EA;
    if (((*(unsigned int *)(v_rip + 9334680)) & (0x800ULL)) == 0) goto loc_0061D9FD;
loc_0061D9EA:
    result = ExAcquireRundownProtection(v_rip + 9331855, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061DA35;
loc_0061D9FD:
    v_rsi = (result) + (48);
    goto loc_0061DA1F;
loc_0061DA06:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061DA1F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061DA06;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9331792;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return v_stack_m38;
}
```

## 5. (Beta) C Style

```c
int64_t DifExAcquireFastResourceSharedStarveExclusiveWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
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
    result = DifGetAPIThunkContextById(444, Arg2, Arg3, a4);
    if (result == 0) goto loc_0061D9BC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061D940;
    v_stack_m58 = v_stack_p0;
    goto loc_0061D94D;
loc_0061D940:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8E6F5D)) != 0) goto loc_0061D971;
    if (((*(uint32_t *)(v_rip + 0x8E7011)) & (0x800ULL)) == 0) goto loc_0061D984;
loc_0061D971:
    result = ExAcquireRundownProtection(v_rip + 9331976, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061D9BC;
loc_0061D984:
    goto loc_0061D9A6;
loc_0061D98D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061D9A6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061D98D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9331913;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ExAcquireFastResourceSharedStarveExclusive(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint8_t)(result);
    if (result == 0) goto loc_0061DA35;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E6EDC)) != 0) goto loc_0061D9EA;
    if (((*(uint32_t *)(v_rip + 0x8E6F98)) & (0x800ULL)) == 0) goto loc_0061D9FD;
loc_0061D9EA:
    result = ExAcquireRundownProtection(v_rip + 9331855, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061DA35;
loc_0061D9FD:
    local_rsi = (result) + (48);
    goto loc_0061DA1F;
loc_0061DA06:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0061DA1F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061DA06;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9331792;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return v_stack_m38;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061D8E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061D8E0[BB_0061D8E0]
  bb_0061D92F[BB_0061D92F]
  bb_0061D936[BB_0061D936]
  bb_0061D940[BB_0061D940]
  bb_0061D944[BB_0061D944]
  bb_0061D94D[BB_0061D94D]
  bb_0061D965[BB_0061D965]
  bb_0061D971[BB_0061D971]
  bb_0061D984[BB_0061D984]
  bb_0061D98D[BB_0061D98D]
  bb_0061D996[BB_0061D996]
  bb_0061D9A3[BB_0061D9A3]
  bb_0061D9A6[BB_0061D9A6]
  bb_0061D9AB[BB_0061D9AB]
  bb_0061D9B0[BB_0061D9B0]
  bb_0061D9BC[BB_0061D9BC]
  bb_0061D9D2[BB_0061D9D2]
  bb_0061D9DE[BB_0061D9DE]
  bb_0061D9EA[BB_0061D9EA]
  bb_0061D9FD[BB_0061D9FD]
  bb_0061DA06[BB_0061DA06]
  bb_0061DA0F[BB_0061DA0F]
  bb_0061DA1C[BB_0061DA1C]
  bb_0061DA1F[BB_0061DA1F]
  bb_0061DA24[BB_0061DA24]
  bb_0061DA29[BB_0061DA29]
  bb_0061DA35[BB_0061DA35]
  bb_0061DA56[BB_0061DA56]
  bb_0061D8E0 -->|branch| bb_0061D9BC
  bb_0061D8E0 -->|fallthrough| bb_0061D92F
  bb_0061D92F -->|branch| bb_0061D940
  bb_0061D92F -->|fallthrough| bb_0061D936
  bb_0061D936 -->|branch| bb_0061D94D
  bb_0061D940 -->|branch| bb_0061D94D
  bb_0061D940 -->|fallthrough| bb_0061D944
  bb_0061D944 -->|flow| bb_0061D94D
  bb_0061D94D -->|branch| bb_0061D971
  bb_0061D94D -->|fallthrough| bb_0061D965
  bb_0061D965 -->|branch| bb_0061D984
  bb_0061D965 -->|fallthrough| bb_0061D971
  bb_0061D971 -->|branch| bb_0061D9BC
  bb_0061D971 -->|fallthrough| bb_0061D984
  bb_0061D984 -->|branch| bb_0061D9A6
  bb_0061D98D -->|branch| bb_0061D9A3
  bb_0061D98D -->|fallthrough| bb_0061D996
  bb_0061D996 -->|flow| bb_0061D9A3
  bb_0061D9A3 -->|flow| bb_0061D9A6
  bb_0061D9A6 -->|branch| bb_0061D98D
  bb_0061D9A6 -->|fallthrough| bb_0061D9AB
  bb_0061D9AB -->|branch| bb_0061D9BC
  bb_0061D9AB -->|fallthrough| bb_0061D9B0
  bb_0061D9B0 -->|flow| bb_0061D9BC
  bb_0061D9BC -->|branch| bb_0061DA35
  bb_0061D9BC -->|fallthrough| bb_0061D9D2
  bb_0061D9D2 -->|branch| bb_0061D9EA
  bb_0061D9D2 -->|fallthrough| bb_0061D9DE
  bb_0061D9DE -->|branch| bb_0061D9FD
  bb_0061D9DE -->|fallthrough| bb_0061D9EA
  bb_0061D9EA -->|branch| bb_0061DA35
  bb_0061D9EA -->|fallthrough| bb_0061D9FD
  bb_0061D9FD -->|branch| bb_0061DA1F
  bb_0061DA06 -->|branch| bb_0061DA1C
  bb_0061DA06 -->|fallthrough| bb_0061DA0F
  bb_0061DA0F -->|flow| bb_0061DA1C
  bb_0061DA1C -->|flow| bb_0061DA1F
  bb_0061DA1F -->|branch| bb_0061DA06
  bb_0061DA1F -->|fallthrough| bb_0061DA24
  bb_0061DA24 -->|branch| bb_0061DA35
  bb_0061DA24 -->|fallthrough| bb_0061DA29
  bb_0061DA29 -->|flow| bb_0061DA35
```
