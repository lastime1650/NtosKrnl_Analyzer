# DifObfDereferenceObjectWithTagWrapper

- RVA: `0x006386C0`–`0x00638826` (길이 `358` bytes)
- VA: `0x00000001406386C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `358/358` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x006386EE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00638716` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00638749` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00638770` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638789` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00638794` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x006387C2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x006387E9` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00638802` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00638728` → RVA `0x00F048B8` (`.data`; read)
- `0x00638736` → RVA `0x00F04980` (`.data`; read)
- `0x00638742` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006386C0  48 8B C4                        mov rax, rsp
006386C3  48 89 58 08                     mov qword ptr [rax + 8], rbx
006386C7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
006386CB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
006386CF  57                              push rdi
006386D0  41 56                           push r14
006386D2  41 57                           push r15
006386D4  48 83 EC 40                     sub rsp, 0x40
006386D8  0F 57 C0                        xorps xmm0, xmm0
006386DB  4C 8B F9                        mov r15, rcx
006386DE  B9 C5 00 00 00                  mov ecx, 0xc5
006386E3  44 8B F2                        mov r14d, edx
006386E6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
006386EA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
006386EE  E8 41 D3 E5 FF                  call 0x140495a34
006386F3  48 8B F0                        mov rsi, rax
006386F6  48 85 C0                        test rax, rax
006386F9  0F 84 8F 00 00 00               je 0x14063878e
006386FF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00638702  A8 18                           test al, 0x18
00638704  74 0C                           je 0x140638712
00638706  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0063870B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00638710  EB 0E                           jmp 0x140638720
00638712  A8 04                           test al, 4
00638714  74 0A                           je 0x140638720
00638716  E8 ED B4 E9 FF                  call 0x1404d3c08
0063871B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00638720  40 32 ED                        xor bpl, bpl
00638723  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
00638728  40 38 2D 89 C1 8C 00            cmp byte ptr [rip + 0x8cc189], bpl
0063872F  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
00638734  75 0C                           jne 0x140638742
00638736  F7 05 40 C2 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc240], 0x800
00638740  74 13                           je 0x140638755
00638742  48 8D 0D 37 B7 8C 00            lea rcx, [rip + 0x8cb737]
00638749  E8 D2 DE BD FF                  call 0x140216620
0063874E  40 8A E8                        mov bpl, al
00638751  84 C0                           test al, al
00638753  74 39                           je 0x14063878e
00638755  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00638759  48 8B 1F                        mov rbx, qword ptr [rdi]
0063875C  EB 1A                           jmp 0x140638778
0063875E  48 8D 43 F0                     lea rax, [rbx - 0x10]
00638762  48 85 C0                        test rax, rax
00638765  74 0E                           je 0x140638775
00638767  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063876B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00638770  E8 5B 23 08 00                  call 0x1406baad0
00638775  48 8B 1B                        mov rbx, qword ptr [rbx]
00638778  48 3B DF                        cmp rbx, rdi
0063877B  75 E1                           jne 0x14063875e
0063877D  40 84 ED                        test bpl, bpl
00638780  74 0C                           je 0x14063878e
00638782  48 8D 0D F7 B6 8C 00            lea rcx, [rip + 0x8cb6f7]
00638789  E8 F2 16 D1 FF                  call 0x140349e80
0063878E  41 8B D6                        mov edx, r14d
00638791  49 8B CF                        mov rcx, r15
00638794  E8 47 F1 CB FF                  call 0x1402f78e0
00638799  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0063879E  48 85 F6                        test rsi, rsi
006387A1  74 64                           je 0x140638807
006387A3  40 32 FF                        xor dil, dil
006387A6  40 38 3D 0B C1 8C 00            cmp byte ptr [rip + 0x8cc10b], dil
006387AD  75 0C                           jne 0x1406387bb
006387AF  F7 05 C7 C1 8C 00 00 08 00 00   test dword ptr [rip + 0x8cc1c7], 0x800
006387B9  74 13                           je 0x1406387ce
006387BB  48 8D 0D BE B6 8C 00            lea rcx, [rip + 0x8cb6be]
006387C2  E8 59 DE BD FF                  call 0x140216620
006387C7  40 8A F8                        mov dil, al
006387CA  84 C0                           test al, al
006387CC  74 39                           je 0x140638807
006387CE  48 83 C6 30                     add rsi, 0x30
006387D2  48 8B 1E                        mov rbx, qword ptr [rsi]
006387D5  EB 1A                           jmp 0x1406387f1
006387D7  48 8D 43 F0                     lea rax, [rbx - 0x10]
006387DB  48 85 C0                        test rax, rax
006387DE  74 0E                           je 0x1406387ee
006387E0  48 8B 40 08                     mov rax, qword ptr [rax + 8]
006387E4  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006387E9  E8 E2 22 08 00                  call 0x1406baad0
006387EE  48 8B 1B                        mov rbx, qword ptr [rbx]
006387F1  48 3B DE                        cmp rbx, rsi
006387F4  75 E1                           jne 0x1406387d7
006387F6  40 84 FF                        test dil, dil
006387F9  74 0C                           je 0x140638807
006387FB  48 8D 0D 7E B6 8C 00            lea rcx, [rip + 0x8cb67e]
00638802  E8 79 16 D1 FF                  call 0x140349e80
00638807  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0063880C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00638811  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00638816  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0063881B  48 83 C4 40                     add rsp, 0x40
0063881F  41 5F                           pop r15
00638821  41 5E                           pop r14
00638823  5F                              pop rdi
00638824  C3                              ret
00638825  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifObfDereferenceObjectWithTagWrapper(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(197, a2, a3, a4);
    if (result == 0) goto loc_0063878E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00638712;
    v_stack_m38 = v_stack_p0;
    goto loc_00638720;
loc_00638712:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int8 *)(v_rip + 9224585)) != 0) goto loc_00638742;
    if (((*(unsigned int *)(v_rip + 9224768)) & (0x800ULL)) == 0) goto loc_00638755;
loc_00638742:
    result = ExAcquireRundownProtection(v_rip + 9221943, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063878E;
loc_00638755:
    goto loc_00638778;
loc_0063875E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00638778:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063875E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9221879;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00638807;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9224459)) != 0) goto loc_006387BB;
    if (((*(unsigned int *)(v_rip + 9224647)) & (0x800ULL)) == 0) goto loc_006387CE;
loc_006387BB:
    result = ExAcquireRundownProtection(v_rip + 9221822, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00638807;
loc_006387CE:
    v_rsi = (result) + (48);
    goto loc_006387F1;
loc_006387D7:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
loc_006387F1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_006387D7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9221758;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m20;
}
```

## 5. (Beta) C Style

```c
int64_t DifObfDereferenceObjectWithTagWrapper(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(197, Arg2, a3, a4);
    if (result == 0) goto loc_0063878E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00638712;
    v_stack_m38 = v_stack_p0;
    goto loc_00638720;
loc_00638712:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint8_t *)(v_rip + 0x8CC189)) != 0) goto loc_00638742;
    if (((*(uint32_t *)(v_rip + 0x8CC240)) & (0x800ULL)) == 0) goto loc_00638755;
loc_00638742:
    result = ExAcquireRundownProtection(v_rip + 9221943, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063878E;
loc_00638755:
    goto loc_00638778;
loc_0063875E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_00638778:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063875E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9221879;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    v_stack_m20 = result;
    if (result == 0) goto loc_00638807;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CC10B)) != 0) goto loc_006387BB;
    if (((*(uint32_t *)(v_rip + 0x8CC1C7)) & (0x800ULL)) == 0) goto loc_006387CE;
loc_006387BB:
    result = ExAcquireRundownProtection(v_rip + 9221822, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00638807;
loc_006387CE:
    local_rsi = (result) + (48);
    goto loc_006387F1;
loc_006387D7:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
loc_006387F1:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_006387D7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9221758;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m20;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006386C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006386C0[BB_006386C0]
  bb_006386FF[BB_006386FF]
  bb_00638706[BB_00638706]
  bb_00638712[BB_00638712]
  bb_00638716[BB_00638716]
  bb_00638720[BB_00638720]
  bb_00638736[BB_00638736]
  bb_00638742[BB_00638742]
  bb_00638755[BB_00638755]
  bb_0063875E[BB_0063875E]
  bb_00638767[BB_00638767]
  bb_00638775[BB_00638775]
  bb_00638778[BB_00638778]
  bb_0063877D[BB_0063877D]
  bb_00638782[BB_00638782]
  bb_0063878E[BB_0063878E]
  bb_006387A3[BB_006387A3]
  bb_006387AF[BB_006387AF]
  bb_006387BB[BB_006387BB]
  bb_006387CE[BB_006387CE]
  bb_006387D7[BB_006387D7]
  bb_006387E0[BB_006387E0]
  bb_006387EE[BB_006387EE]
  bb_006387F1[BB_006387F1]
  bb_006387F6[BB_006387F6]
  bb_006387FB[BB_006387FB]
  bb_00638807[BB_00638807]
  bb_00638825[BB_00638825]
  bb_006386C0 -->|branch| bb_0063878E
  bb_006386C0 -->|fallthrough| bb_006386FF
  bb_006386FF -->|branch| bb_00638712
  bb_006386FF -->|fallthrough| bb_00638706
  bb_00638706 -->|branch| bb_00638720
  bb_00638712 -->|branch| bb_00638720
  bb_00638712 -->|fallthrough| bb_00638716
  bb_00638716 -->|flow| bb_00638720
  bb_00638720 -->|branch| bb_00638742
  bb_00638720 -->|fallthrough| bb_00638736
  bb_00638736 -->|branch| bb_00638755
  bb_00638736 -->|fallthrough| bb_00638742
  bb_00638742 -->|branch| bb_0063878E
  bb_00638742 -->|fallthrough| bb_00638755
  bb_00638755 -->|branch| bb_00638778
  bb_0063875E -->|branch| bb_00638775
  bb_0063875E -->|fallthrough| bb_00638767
  bb_00638767 -->|flow| bb_00638775
  bb_00638775 -->|flow| bb_00638778
  bb_00638778 -->|branch| bb_0063875E
  bb_00638778 -->|fallthrough| bb_0063877D
  bb_0063877D -->|branch| bb_0063878E
  bb_0063877D -->|fallthrough| bb_00638782
  bb_00638782 -->|flow| bb_0063878E
  bb_0063878E -->|branch| bb_00638807
  bb_0063878E -->|fallthrough| bb_006387A3
  bb_006387A3 -->|branch| bb_006387BB
  bb_006387A3 -->|fallthrough| bb_006387AF
  bb_006387AF -->|branch| bb_006387CE
  bb_006387AF -->|fallthrough| bb_006387BB
  bb_006387BB -->|branch| bb_00638807
  bb_006387BB -->|fallthrough| bb_006387CE
  bb_006387CE -->|branch| bb_006387F1
  bb_006387D7 -->|branch| bb_006387EE
  bb_006387D7 -->|fallthrough| bb_006387E0
  bb_006387E0 -->|flow| bb_006387EE
  bb_006387EE -->|flow| bb_006387F1
  bb_006387F1 -->|branch| bb_006387D7
  bb_006387F1 -->|fallthrough| bb_006387F6
  bb_006387F6 -->|branch| bb_00638807
  bb_006387F6 -->|fallthrough| bb_006387FB
  bb_006387FB -->|flow| bb_00638807
```
