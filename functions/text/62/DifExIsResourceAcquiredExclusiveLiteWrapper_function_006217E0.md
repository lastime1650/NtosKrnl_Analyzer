# DifExIsResourceAcquiredExclusiveLiteWrapper

- RVA: `0x006217E0`–`0x0062193F` (길이 `351` bytes)
- VA: `0x00000001406217E0`
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
- `0x0062180F` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00621837` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00621865` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062188C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006218A5` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x006218AD` → [ExIsResourceAcquiredExclusiveLite](../40/ExIsResourceAcquiredExclusiveLite_function_0040B750.md) (function, `0x0040B750`)
- `0x006218DA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00621901` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062191A` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00621849` → RVA `0x00F048B8` (`.data`; read)
- `0x00621852` → RVA `0x00F04980` (`.data`; read)
- `0x0062185E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006217E0  4C 8B DC                        mov r11, rsp
006217E3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
006217E7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
006217EB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
006217EF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
006217F3  41 56                           push r14
006217F5  48 83 EC 40                     sub rsp, 0x40
006217F9  33 C0                           xor eax, eax
006217FB  0F 57 C0                        xorps xmm0, xmm0
006217FE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00621803  48 8B E9                        mov rbp, rcx
00621806  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062180A  B9 CF 01 00 00                  mov ecx, 0x1cf
0062180F  E8 20 42 E7 FF                  call 0x140495a34
00621814  48 8B F0                        mov rsi, rax
00621817  48 85 C0                        test rax, rax
0062181A  0F 84 8A 00 00 00               je 0x1406218aa
00621820  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00621823  A8 18                           test al, 0x18
00621825  74 0C                           je 0x140621833
00621827  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062182C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00621831  EB 0E                           jmp 0x140621841
00621833  A8 04                           test al, 4
00621835  74 0A                           je 0x140621841
00621837  E8 CC 23 EB FF                  call 0x1404d3c08
0062183C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00621841  40 32 FF                        xor dil, dil
00621844  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00621849  40 38 3D 68 30 8E 00            cmp byte ptr [rip + 0x8e3068], dil
00621850  75 0C                           jne 0x14062185e
00621852  F7 05 24 31 8E 00 00 08 00 00   test dword ptr [rip + 0x8e3124], 0x800
0062185C  74 13                           je 0x140621871
0062185E  48 8D 0D 1B 26 8E 00            lea rcx, [rip + 0x8e261b]
00621865  E8 B6 4D BF FF                  call 0x140216620
0062186A  40 8A F8                        mov dil, al
0062186D  84 C0                           test al, al
0062186F  74 39                           je 0x1406218aa
00621871  4C 8D 76 20                     lea r14, [rsi + 0x20]
00621875  49 8B 1E                        mov rbx, qword ptr [r14]
00621878  EB 1A                           jmp 0x140621894
0062187A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062187E  48 85 C0                        test rax, rax
00621881  74 0E                           je 0x140621891
00621883  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00621887  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062188C  E8 3F 92 09 00                  call 0x1406baad0
00621891  48 8B 1B                        mov rbx, qword ptr [rbx]
00621894  49 3B DE                        cmp rbx, r14
00621897  75 E1                           jne 0x14062187a
00621899  40 84 FF                        test dil, dil
0062189C  74 0C                           je 0x1406218aa
0062189E  48 8D 0D DB 25 8E 00            lea rcx, [rip + 0x8e25db]
006218A5  E8 D6 85 D2 FF                  call 0x140349e80
006218AA  48 8B CD                        mov rcx, rbp
006218AD  E8 9E 9E DE FF                  call 0x14040b750
006218B2  88 44 24 30                     mov byte ptr [rsp + 0x30], al
006218B6  48 85 F6                        test rsi, rsi
006218B9  74 64                           je 0x14062191f
006218BB  40 32 FF                        xor dil, dil
006218BE  40 38 3D F3 2F 8E 00            cmp byte ptr [rip + 0x8e2ff3], dil
006218C5  75 0C                           jne 0x1406218d3
006218C7  F7 05 AF 30 8E 00 00 08 00 00   test dword ptr [rip + 0x8e30af], 0x800
006218D1  74 13                           je 0x1406218e6
006218D3  48 8D 0D A6 25 8E 00            lea rcx, [rip + 0x8e25a6]
006218DA  E8 41 4D BF FF                  call 0x140216620
006218DF  40 8A F8                        mov dil, al
006218E2  84 C0                           test al, al
006218E4  74 39                           je 0x14062191f
006218E6  48 83 C6 30                     add rsi, 0x30
006218EA  48 8B 1E                        mov rbx, qword ptr [rsi]
006218ED  EB 1A                           jmp 0x140621909
006218EF  48 8D 43 F0                     lea rax, [rbx - 0x10]
006218F3  48 85 C0                        test rax, rax
006218F6  74 0E                           je 0x140621906
006218F8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006218FC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00621901  E8 CA 91 09 00                  call 0x1406baad0
00621906  48 8B 1B                        mov rbx, qword ptr [rbx]
00621909  48 3B DE                        cmp rbx, rsi
0062190C  75 E1                           jne 0x1406218ef
0062190E  40 84 FF                        test dil, dil
00621911  74 0C                           je 0x14062191f
00621913  48 8D 0D 66 25 8E 00            lea rcx, [rip + 0x8e2566]
0062191A  E8 61 85 D2 FF                  call 0x140349e80
0062191F  8A 44 24 30                     mov al, byte ptr [rsp + 0x30]
00621923  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00621928  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062192D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00621932  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00621937  48 83 C4 40                     add rsp, 0x40
0062193B  41 5E                           pop r14
0062193D  C3                              ret
0062193E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExIsResourceAcquiredExclusiveLiteWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
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
    result = DifGetAPIThunkContextById(463, a2, a3, a4);
    if (result == 0) goto loc_006218AA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00621833;
    v_stack_m28 = v_stack_p0;
    goto loc_00621841;
loc_00621833:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9318504)) != 0) goto loc_0062185E;
    if (((*(unsigned int *)(v_rip + 9318692)) & (0x800ULL)) == 0) goto loc_00621871;
loc_0062185E:
    result = ExAcquireRundownProtection(v_rip + 9315867, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006218AA;
loc_00621871:
    goto loc_00621894;
loc_0062187A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621894:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062187A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9315803;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExIsResourceAcquiredExclusiveLite(a1, a2, a3, a4);
    v_stack_m18 = (unsigned __int8)(result);
    if (result == 0) goto loc_0062191F;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9318387)) != 0) goto loc_006218D3;
    if (((*(unsigned int *)(v_rip + 9318575)) & (0x800ULL)) == 0) goto loc_006218E6;
loc_006218D3:
    result = ExAcquireRundownProtection(v_rip + 9315750, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062191F;
loc_006218E6:
    v_rsi = (result) + (48);
    goto loc_00621909;
loc_006218EF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00621909:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006218EF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9315686;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifExIsResourceAcquiredExclusiveLiteWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(463, a2, a3, a4);
    if (result == 0) goto loc_006218AA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00621833;
    v_stack_m28 = v_stack_p0;
    goto loc_00621841;
loc_00621833:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E3068)) != 0) goto loc_0062185E;
    if (((*(uint32_t *)(v_rip + 0x8E3124)) & (0x800ULL)) == 0) goto loc_00621871;
loc_0062185E:
    result = ExAcquireRundownProtection(v_rip + 9315867, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_006218AA;
loc_00621871:
    goto loc_00621894;
loc_0062187A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621894:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062187A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9315803;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = ExIsResourceAcquiredExclusiveLite(Arg1, a2, a3, a4);
    v_stack_m18 = (uint8_t)(result);
    if (result == 0) goto loc_0062191F;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E2FF3)) != 0) goto loc_006218D3;
    if (((*(uint32_t *)(v_rip + 0x8E30AF)) & (0x800ULL)) == 0) goto loc_006218E6;
loc_006218D3:
    result = ExAcquireRundownProtection(v_rip + 9315750, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062191F;
loc_006218E6:
    local_rsi = (result) + (48);
    goto loc_00621909;
loc_006218EF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00621909:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006218EF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9315686;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006217E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006217E0[BB_006217E0]
  bb_00621820[BB_00621820]
  bb_00621827[BB_00621827]
  bb_00621833[BB_00621833]
  bb_00621837[BB_00621837]
  bb_00621841[BB_00621841]
  bb_00621852[BB_00621852]
  bb_0062185E[BB_0062185E]
  bb_00621871[BB_00621871]
  bb_0062187A[BB_0062187A]
  bb_00621883[BB_00621883]
  bb_00621891[BB_00621891]
  bb_00621894[BB_00621894]
  bb_00621899[BB_00621899]
  bb_0062189E[BB_0062189E]
  bb_006218AA[BB_006218AA]
  bb_006218BB[BB_006218BB]
  bb_006218C7[BB_006218C7]
  bb_006218D3[BB_006218D3]
  bb_006218E6[BB_006218E6]
  bb_006218EF[BB_006218EF]
  bb_006218F8[BB_006218F8]
  bb_00621906[BB_00621906]
  bb_00621909[BB_00621909]
  bb_0062190E[BB_0062190E]
  bb_00621913[BB_00621913]
  bb_0062191F[BB_0062191F]
  bb_0062193E[BB_0062193E]
  bb_006217E0 -->|branch| bb_006218AA
  bb_006217E0 -->|fallthrough| bb_00621820
  bb_00621820 -->|branch| bb_00621833
  bb_00621820 -->|fallthrough| bb_00621827
  bb_00621827 -->|branch| bb_00621841
  bb_00621833 -->|branch| bb_00621841
  bb_00621833 -->|fallthrough| bb_00621837
  bb_00621837 -->|flow| bb_00621841
  bb_00621841 -->|branch| bb_0062185E
  bb_00621841 -->|fallthrough| bb_00621852
  bb_00621852 -->|branch| bb_00621871
  bb_00621852 -->|fallthrough| bb_0062185E
  bb_0062185E -->|branch| bb_006218AA
  bb_0062185E -->|fallthrough| bb_00621871
  bb_00621871 -->|branch| bb_00621894
  bb_0062187A -->|branch| bb_00621891
  bb_0062187A -->|fallthrough| bb_00621883
  bb_00621883 -->|flow| bb_00621891
  bb_00621891 -->|flow| bb_00621894
  bb_00621894 -->|branch| bb_0062187A
  bb_00621894 -->|fallthrough| bb_00621899
  bb_00621899 -->|branch| bb_006218AA
  bb_00621899 -->|fallthrough| bb_0062189E
  bb_0062189E -->|flow| bb_006218AA
  bb_006218AA -->|branch| bb_0062191F
  bb_006218AA -->|fallthrough| bb_006218BB
  bb_006218BB -->|branch| bb_006218D3
  bb_006218BB -->|fallthrough| bb_006218C7
  bb_006218C7 -->|branch| bb_006218E6
  bb_006218C7 -->|fallthrough| bb_006218D3
  bb_006218D3 -->|branch| bb_0062191F
  bb_006218D3 -->|fallthrough| bb_006218E6
  bb_006218E6 -->|branch| bb_00621909
  bb_006218EF -->|branch| bb_00621906
  bb_006218EF -->|fallthrough| bb_006218F8
  bb_006218F8 -->|flow| bb_00621906
  bb_00621906 -->|flow| bb_00621909
  bb_00621909 -->|branch| bb_006218EF
  bb_00621909 -->|fallthrough| bb_0062190E
  bb_0062190E -->|branch| bb_0062191F
  bb_0062190E -->|fallthrough| bb_00621913
  bb_00621913 -->|flow| bb_0062191F
```
