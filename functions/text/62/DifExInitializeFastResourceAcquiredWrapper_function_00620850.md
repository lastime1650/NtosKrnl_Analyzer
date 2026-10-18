# DifExInitializeFastResourceAcquiredWrapper

- RVA: `0x00620850`–`0x006209C2` (길이 `370` bytes)
- VA: `0x0000000140620850`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `101`개 명령, `370/370` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00620886` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x006208AE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x006208E6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062090D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00620926` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00620934` → [ExInitializeFastResourceAcquired](../49/ExInitializeFastResourceAcquired_function_0049ADE0.md) (function, `0x0049ADE0`)
- `0x0062095D` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00620984` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062099D` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006208C0` → RVA `0x00F048B8` (`.data`; read)
- `0x006208D3` → RVA `0x00F04980` (`.data`; read)
- `0x006208DF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00620850  48 8B C4                        mov rax, rsp
00620853  48 89 58 08                     mov qword ptr [rax + 8], rbx
00620857  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062085B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062085F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00620863  41 54                           push r12
00620865  41 56                           push r14
00620867  41 57                           push r15
00620869  48 83 EC 40                     sub rsp, 0x40
0062086D  0F 57 C0                        xorps xmm0, xmm0
00620870  4C 8B E1                        mov r12, rcx
00620873  B9 BF 01 00 00                  mov ecx, 0x1bf
00620878  4D 8B F0                        mov r14, r8
0062087B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062087F  44 8B FA                        mov r15d, edx
00620882  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
00620886  E8 A9 51 E7 FF                  call 0x140495a34
0062088B  48 8B F0                        mov rsi, rax
0062088E  48 85 C0                        test rax, rax
00620891  0F 84 94 00 00 00               je 0x14062092b
00620897  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062089A  A8 18                           test al, 0x18
0062089C  74 0C                           je 0x1406208aa
0062089E  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
006208A3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
006208A8  EB 0E                           jmp 0x1406208b8
006208AA  A8 04                           test al, 4
006208AC  74 0A                           je 0x1406208b8
006208AE  E8 55 33 EB FF                  call 0x1404d3c08
006208B3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006208B8  40 32 ED                        xor bpl, bpl
006208BB  4C 89 64 24 38                  mov qword ptr [rsp + 0x38], r12
006208C0  40 38 2D F1 3F 8E 00            cmp byte ptr [rip + 0x8e3ff1], bpl
006208C7  44 89 7C 24 30                  mov dword ptr [rsp + 0x30], r15d
006208CC  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
006208D1  75 0C                           jne 0x1406208df
006208D3  F7 05 A3 40 8E 00 00 08 00 00   test dword ptr [rip + 0x8e40a3], 0x800
006208DD  74 13                           je 0x1406208f2
006208DF  48 8D 0D 9A 35 8E 00            lea rcx, [rip + 0x8e359a]
006208E6  E8 35 5D BF FF                  call 0x140216620
006208EB  40 8A E8                        mov bpl, al
006208EE  84 C0                           test al, al
006208F0  74 39                           je 0x14062092b
006208F2  48 8D 7E 20                     lea rdi, [rsi + 0x20]
006208F6  48 8B 1F                        mov rbx, qword ptr [rdi]
006208F9  EB 1A                           jmp 0x140620915
006208FB  48 8D 43 F0                     lea rax, [rbx - 0x10]
006208FF  48 85 C0                        test rax, rax
00620902  74 0E                           je 0x140620912
00620904  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00620908  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062090D  E8 BE A1 09 00                  call 0x1406baad0
00620912  48 8B 1B                        mov rbx, qword ptr [rbx]
00620915  48 3B DF                        cmp rbx, rdi
00620918  75 E1                           jne 0x1406208fb
0062091A  40 84 ED                        test bpl, bpl
0062091D  74 0C                           je 0x14062092b
0062091F  48 8D 0D 5A 35 8E 00            lea rcx, [rip + 0x8e355a]
00620926  E8 55 95 D2 FF                  call 0x140349e80
0062092B  4D 8B C6                        mov r8, r14
0062092E  41 8B D7                        mov edx, r15d
00620931  49 8B CC                        mov rcx, r12
00620934  E8 A7 A4 E7 FF                  call 0x14049ade0
00620939  48 85 F6                        test rsi, rsi
0062093C  74 64                           je 0x1406209a2
0062093E  40 32 FF                        xor dil, dil
00620941  40 38 3D 70 3F 8E 00            cmp byte ptr [rip + 0x8e3f70], dil
00620948  75 0C                           jne 0x140620956
0062094A  F7 05 2C 40 8E 00 00 08 00 00   test dword ptr [rip + 0x8e402c], 0x800
00620954  74 13                           je 0x140620969
00620956  48 8D 0D 23 35 8E 00            lea rcx, [rip + 0x8e3523]
0062095D  E8 BE 5C BF FF                  call 0x140216620
00620962  40 8A F8                        mov dil, al
00620965  84 C0                           test al, al
00620967  74 39                           je 0x1406209a2
00620969  48 83 C6 30                     add rsi, 0x30
0062096D  48 8B 1E                        mov rbx, qword ptr [rsi]
00620970  EB 1A                           jmp 0x14062098c
00620972  48 8D 43 F0                     lea rax, [rbx - 0x10]
00620976  48 85 C0                        test rax, rax
00620979  74 0E                           je 0x140620989
0062097B  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062097F  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00620984  E8 47 A1 09 00                  call 0x1406baad0
00620989  48 8B 1B                        mov rbx, qword ptr [rbx]
0062098C  48 3B DE                        cmp rbx, rsi
0062098F  75 E1                           jne 0x140620972
00620991  40 84 FF                        test dil, dil
00620994  74 0C                           je 0x1406209a2
00620996  48 8D 0D E3 34 8E 00            lea rcx, [rip + 0x8e34e3]
0062099D  E8 DE 94 D2 FF                  call 0x140349e80
006209A2  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
006209A7  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
006209AC  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
006209B1  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
006209B6  48 83 C4 40                     add rsp, 0x40
006209BA  41 5F                           pop r15
006209BC  41 5E                           pop r14
006209BE  41 5C                           pop r12
006209C0  C3                              ret
006209C1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifExInitializeFastResourceAcquiredWrapper(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
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
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(447, a2, a3, a4);
    if (result == 0) goto loc_0062092B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_006208AA;
    v_stack_m38 = v_stack_p0;
    goto loc_006208B8;
loc_006208AA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    v_stack_m28 = (unsigned int)((unsigned int)(a2));
    v_stack_m30 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9322481)) != 0) goto loc_006208DF;
    if (((*(unsigned int *)(v_rip + 9322659)) & (0x800ULL)) == 0) goto loc_006208F2;
loc_006208DF:
    result = ExAcquireRundownProtection(v_rip + 9319834, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062092B;
loc_006208F2:
    goto loc_00620915;
loc_006208FB:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00620915:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_006208FB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9319770;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ExInitializeFastResourceAcquired(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if (result == 0) goto loc_006209A2;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9322352)) != 0) goto loc_00620956;
    if (((*(unsigned int *)(v_rip + 9322540)) & (0x800ULL)) == 0) goto loc_00620969;
loc_00620956:
    result = ExAcquireRundownProtection(v_rip + 9319715, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_006209A2;
loc_00620969:
    v_rsi = (result) + (48);
    goto loc_0062098C;
loc_00620972:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_0062098C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00620972;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9319651;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifExInitializeFastResourceAcquiredWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
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
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(447, Arg2, Arg3, a4);
    if (result == 0) goto loc_0062092B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_006208AA;
    v_stack_m38 = v_stack_p0;
    goto loc_006208B8;
loc_006208AA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m30 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8E3FF1)) != 0) goto loc_006208DF;
    if (((*(uint32_t *)(v_rip + 0x8E40A3)) & (0x800ULL)) == 0) goto loc_006208F2;
loc_006208DF:
    result = ExAcquireRundownProtection(v_rip + 9319834, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062092B;
loc_006208F2:
    goto loc_00620915;
loc_006208FB:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_00620915:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_006208FB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9319770;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ExInitializeFastResourceAcquired(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if (result == 0) goto loc_006209A2;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E3F70)) != 0) goto loc_00620956;
    if (((*(uint32_t *)(v_rip + 0x8E402C)) & (0x800ULL)) == 0) goto loc_00620969;
loc_00620956:
    result = ExAcquireRundownProtection(v_rip + 9319715, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_006209A2;
loc_00620969:
    local_rsi = (result) + (48);
    goto loc_0062098C;
loc_00620972:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
loc_0062098C:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00620972;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9319651;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00620850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00620850[BB_00620850]
  bb_00620897[BB_00620897]
  bb_0062089E[BB_0062089E]
  bb_006208AA[BB_006208AA]
  bb_006208AE[BB_006208AE]
  bb_006208B8[BB_006208B8]
  bb_006208D3[BB_006208D3]
  bb_006208DF[BB_006208DF]
  bb_006208F2[BB_006208F2]
  bb_006208FB[BB_006208FB]
  bb_00620904[BB_00620904]
  bb_00620912[BB_00620912]
  bb_00620915[BB_00620915]
  bb_0062091A[BB_0062091A]
  bb_0062091F[BB_0062091F]
  bb_0062092B[BB_0062092B]
  bb_0062093E[BB_0062093E]
  bb_0062094A[BB_0062094A]
  bb_00620956[BB_00620956]
  bb_00620969[BB_00620969]
  bb_00620972[BB_00620972]
  bb_0062097B[BB_0062097B]
  bb_00620989[BB_00620989]
  bb_0062098C[BB_0062098C]
  bb_00620991[BB_00620991]
  bb_00620996[BB_00620996]
  bb_006209A2[BB_006209A2]
  bb_006209C1[BB_006209C1]
  bb_00620850 -->|branch| bb_0062092B
  bb_00620850 -->|fallthrough| bb_00620897
  bb_00620897 -->|branch| bb_006208AA
  bb_00620897 -->|fallthrough| bb_0062089E
  bb_0062089E -->|branch| bb_006208B8
  bb_006208AA -->|branch| bb_006208B8
  bb_006208AA -->|fallthrough| bb_006208AE
  bb_006208AE -->|flow| bb_006208B8
  bb_006208B8 -->|branch| bb_006208DF
  bb_006208B8 -->|fallthrough| bb_006208D3
  bb_006208D3 -->|branch| bb_006208F2
  bb_006208D3 -->|fallthrough| bb_006208DF
  bb_006208DF -->|branch| bb_0062092B
  bb_006208DF -->|fallthrough| bb_006208F2
  bb_006208F2 -->|branch| bb_00620915
  bb_006208FB -->|branch| bb_00620912
  bb_006208FB -->|fallthrough| bb_00620904
  bb_00620904 -->|flow| bb_00620912
  bb_00620912 -->|flow| bb_00620915
  bb_00620915 -->|branch| bb_006208FB
  bb_00620915 -->|fallthrough| bb_0062091A
  bb_0062091A -->|branch| bb_0062092B
  bb_0062091A -->|fallthrough| bb_0062091F
  bb_0062091F -->|flow| bb_0062092B
  bb_0062092B -->|branch| bb_006209A2
  bb_0062092B -->|fallthrough| bb_0062093E
  bb_0062093E -->|branch| bb_00620956
  bb_0062093E -->|fallthrough| bb_0062094A
  bb_0062094A -->|branch| bb_00620969
  bb_0062094A -->|fallthrough| bb_00620956
  bb_00620956 -->|branch| bb_006209A2
  bb_00620956 -->|fallthrough| bb_00620969
  bb_00620969 -->|branch| bb_0062098C
  bb_00620972 -->|branch| bb_00620989
  bb_00620972 -->|fallthrough| bb_0062097B
  bb_0062097B -->|flow| bb_00620989
  bb_00620989 -->|flow| bb_0062098C
  bb_0062098C -->|branch| bb_00620972
  bb_0062098C -->|fallthrough| bb_00620991
  bb_00620991 -->|branch| bb_006209A2
  bb_00620991 -->|fallthrough| bb_00620996
  bb_00620996 -->|flow| bb_006209A2
```
