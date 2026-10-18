# DifExIsResourceAcquiredSharedLiteWrapper

- RVA: `0x00621950`–`0x00621AAF` (길이 `351` bytes)
- VA: `0x0000000140621950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062197F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006219A7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006219D5` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006219FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621A15` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00621A1D` → [ExIsResourceAcquiredSharedLite](../34/ExIsResourceAcquiredSharedLite_function_00341B10.md) (function, `0x00341B10`)
- `0x00621A4A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621A71` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00621A8A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006219B9` → RVA `0x00F048B8` (`.data`; read)
- `0x006219C2` → RVA `0x00F04980` (`.data`; read)
- `0x006219CE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00621950  4C 8B DC                        mov r11, rsp
00621953  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00621957  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062195B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062195F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00621963  41 56                           push r14
00621965  48 83 EC 40                     sub rsp, 0x40
00621969  33 C0                           xor eax, eax
0062196B  0F 57 C0                        xorps xmm0, xmm0
0062196E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00621973  48 8B E9                        mov rbp, rcx
00621976  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062197A  B9 D0 01 00 00                  mov ecx, 0x1d0
0062197F  E8 B0 40 E7 FF                  call 0x140495a34
00621984  48 8B F0                        mov rsi, rax
00621987  48 85 C0                        test rax, rax
0062198A  0F 84 8A 00 00 00               je 0x140621a1a
00621990  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621993  A8 18                           test al, 0x18
00621995  74 0C                           je 0x1406219a3
00621997  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062199C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006219A1  EB 0E                           jmp 0x1406219b1
006219A3  A8 04                           test al, 4
006219A5  74 0A                           je 0x1406219b1
006219A7  E8 5C 22 EB FF                  call 0x1404d3c08
006219AC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006219B1  40 32 FF                        xor dil, dil
006219B4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
006219B9  40 38 3D F8 2E 8E 00            cmp byte ptr [rip + 0x8e2ef8], dil
006219C0  75 0C                           jne 0x1406219ce
006219C2  F7 05 B4 2F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2fb4], 0x800
006219CC  74 13                           je 0x1406219e1
006219CE  48 8D 0D AB 24 8E 00            lea rcx, [rip + 0x8e24ab]
006219D5  E8 46 4C BF FF                  call 0x140216620
006219DA  40 8A F8                        mov dil, al
006219DD  84 C0                           test al, al
006219DF  74 39                           je 0x140621a1a
006219E1  4C 8D 76 20                     lea r14, [rsi + 0x20]
006219E5  49 8B 1E                        mov rbx, qword ptr [r14]
006219E8  EB 1A                           jmp 0x140621a04
006219EA  48 8D 43 F0                     lea rax, [rbx - 0x10]
006219EE  48 85 C0                        test rax, rax
006219F1  74 0E                           je 0x140621a01
006219F3  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006219F7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006219FC  E8 CF 90 09 00                  call 0x1406baad0
00621A01  48 8B 1B                        mov rbx, qword ptr [rbx]
00621A04  49 3B DE                        cmp rbx, r14
00621A07  75 E1                           jne 0x1406219ea
00621A09  40 84 FF                        test dil, dil
00621A0C  74 0C                           je 0x140621a1a
00621A0E  48 8D 0D 6B 24 8E 00            lea rcx, [rip + 0x8e246b]
00621A15  E8 66 84 D2 FF                  call 0x140349e80
00621A1A  48 8B CD                        mov rcx, rbp
00621A1D  E8 EE 00 D2 FF                  call 0x140341b10
00621A22  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00621A26  48 85 F6                        test rsi, rsi
00621A29  74 64                           je 0x140621a8f
00621A2B  40 32 FF                        xor dil, dil
00621A2E  40 38 3D 83 2E 8E 00            cmp byte ptr [rip + 0x8e2e83], dil
00621A35  75 0C                           jne 0x140621a43
00621A37  F7 05 3F 2F 8E 00 00 08 00 00   test dword ptr [rip + 0x8e2f3f], 0x800
00621A41  74 13                           je 0x140621a56
00621A43  48 8D 0D 36 24 8E 00            lea rcx, [rip + 0x8e2436]
00621A4A  E8 D1 4B BF FF                  call 0x140216620
00621A4F  40 8A F8                        mov dil, al
00621A52  84 C0                           test al, al
00621A54  74 39                           je 0x140621a8f
00621A56  48 83 C6 30                     add rsi, 0x30
00621A5A  48 8B 1E                        mov rbx, qword ptr [rsi]
00621A5D  EB 1A                           jmp 0x140621a79
00621A5F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00621A63  48 85 C0                        test rax, rax
00621A66  74 0E                           je 0x140621a76
00621A68  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621A6C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621A71  E8 5A 90 09 00                  call 0x1406baad0
00621A76  48 8B 1B                        mov rbx, qword ptr [rbx]
00621A79  48 3B DE                        cmp rbx, rsi
00621A7C  75 E1                           jne 0x140621a5f
00621A7E  40 84 FF                        test dil, dil
00621A81  74 0C                           je 0x140621a8f
00621A83  48 8D 0D F6 23 8E 00            lea rcx, [rip + 0x8e23f6]
00621A8A  E8 F1 83 D2 FF                  call 0x140349e80
00621A8F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00621A93  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00621A98  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00621A9D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00621AA2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00621AA7  48 83 C4 40                     add rsp, 0x40
00621AAB  41 5E                           pop r14
00621AAD  C3                              ret
00621AAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsResourceAcquiredSharedLiteWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
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
    result = DifGetAPIThunkContextById(464, a2, a3, a4);
    if (result == 0) goto loc_00621A1A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006219A3;
    v_stack_m28 = v_stack_p0;
    goto loc_006219B1;
loc_006219A3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9318136)) != 0) goto loc_006219CE;
    if (((*(unsigned int *)(v_rip + 9318324)) & (0x800ULL)) == 0) goto loc_006219E1;
loc_006219CE:
    result = ExAcquireRundownProtection(v_rip + 9315499, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621A1A;
loc_006219E1:
    goto loc_00621A04;
loc_006219EA:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621A04:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006219EA;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9315435;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExIsResourceAcquiredSharedLite(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_00621A8F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9318019)) != 0) goto loc_00621A43;
    if (((*(unsigned int *)(v_rip + 9318207)) & (0x800ULL)) == 0) goto loc_00621A56;
loc_00621A43:
    result = ExAcquireRundownProtection(v_rip + 9315382, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00621A8F;
loc_00621A56:
    v_rsi = (result) + (48);
    goto loc_00621A79;
loc_00621A5F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621A79:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00621A5F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9315318;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsResourceAcquiredSharedLiteWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(464, a2, a3, a4);
    if (result == 0) goto loc_00621A1A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006219A3;
    v_stack_m28 = v_stack_p0;
    goto loc_006219B1;
loc_006219A3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E2EF8)) != 0) goto loc_006219CE;
    if (((*(uint32_t *)(v_rip + 0x8E2FB4)) & (0x800ULL)) == 0) goto loc_006219E1;
loc_006219CE:
    result = ExAcquireRundownProtection(v_rip + 9315499, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621A1A;
loc_006219E1:
    goto loc_00621A04;
loc_006219EA:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621A04:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006219EA;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9315435;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExIsResourceAcquiredSharedLite(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_00621A8F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E2E83)) != 0) goto loc_00621A43;
    if (((*(uint32_t *)(v_rip + 0x8E2F3F)) & (0x800ULL)) == 0) goto loc_00621A56;
loc_00621A43:
    result = ExAcquireRundownProtection(v_rip + 9315382, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00621A8F;
loc_00621A56:
    local_rsi = (result) + (48);
    goto loc_00621A79;
loc_00621A5F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621A79:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00621A5F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9315318;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00621950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00621950[BB_00621950]
  bb_00621990[BB_00621990]
  bb_00621997[BB_00621997]
  bb_006219A3[BB_006219A3]
  bb_006219A7[BB_006219A7]
  bb_006219B1[BB_006219B1]
  bb_006219C2[BB_006219C2]
  bb_006219CE[BB_006219CE]
  bb_006219E1[BB_006219E1]
  bb_006219EA[BB_006219EA]
  bb_006219F3[BB_006219F3]
  bb_00621A01[BB_00621A01]
  bb_00621A04[BB_00621A04]
  bb_00621A09[BB_00621A09]
  bb_00621A0E[BB_00621A0E]
  bb_00621A1A[BB_00621A1A]
  bb_00621A2B[BB_00621A2B]
  bb_00621A37[BB_00621A37]
  bb_00621A43[BB_00621A43]
  bb_00621A56[BB_00621A56]
  bb_00621A5F[BB_00621A5F]
  bb_00621A68[BB_00621A68]
  bb_00621A76[BB_00621A76]
  bb_00621A79[BB_00621A79]
  bb_00621A7E[BB_00621A7E]
  bb_00621A83[BB_00621A83]
  bb_00621A8F[BB_00621A8F]
  bb_00621AAE[BB_00621AAE]
  bb_00621950 -->|branch| bb_00621A1A
  bb_00621950 -->|fallthrough| bb_00621990
  bb_00621990 -->|branch| bb_006219A3
  bb_00621990 -->|fallthrough| bb_00621997
  bb_00621997 -->|branch| bb_006219B1
  bb_006219A3 -->|branch| bb_006219B1
  bb_006219A3 -->|fallthrough| bb_006219A7
  bb_006219A7 -->|flow| bb_006219B1
  bb_006219B1 -->|branch| bb_006219CE
  bb_006219B1 -->|fallthrough| bb_006219C2
  bb_006219C2 -->|branch| bb_006219E1
  bb_006219C2 -->|fallthrough| bb_006219CE
  bb_006219CE -->|branch| bb_00621A1A
  bb_006219CE -->|fallthrough| bb_006219E1
  bb_006219E1 -->|branch| bb_00621A04
  bb_006219EA -->|branch| bb_00621A01
  bb_006219EA -->|fallthrough| bb_006219F3
  bb_006219F3 -->|flow| bb_00621A01
  bb_00621A01 -->|flow| bb_00621A04
  bb_00621A04 -->|branch| bb_006219EA
  bb_00621A04 -->|fallthrough| bb_00621A09
  bb_00621A09 -->|branch| bb_00621A1A
  bb_00621A09 -->|fallthrough| bb_00621A0E
  bb_00621A0E -->|flow| bb_00621A1A
  bb_00621A1A -->|branch| bb_00621A8F
  bb_00621A1A -->|fallthrough| bb_00621A2B
  bb_00621A2B -->|branch| bb_00621A43
  bb_00621A2B -->|fallthrough| bb_00621A37
  bb_00621A37 -->|branch| bb_00621A56
  bb_00621A37 -->|fallthrough| bb_00621A43
  bb_00621A43 -->|branch| bb_00621A8F
  bb_00621A43 -->|fallthrough| bb_00621A56
  bb_00621A56 -->|branch| bb_00621A79
  bb_00621A5F -->|branch| bb_00621A76
  bb_00621A5F -->|fallthrough| bb_00621A68
  bb_00621A68 -->|flow| bb_00621A76
  bb_00621A76 -->|flow| bb_00621A79
  bb_00621A79 -->|branch| bb_00621A5F
  bb_00621A79 -->|fallthrough| bb_00621A7E
  bb_00621A7E -->|branch| bb_00621A8F
  bb_00621A7E -->|fallthrough| bb_00621A83
  bb_00621A83 -->|flow| bb_00621A8F
```
