# DifZwSetSystemInformationWrapper

- RVA: `0x0064AF70`–`0x0064B0EA` (길이 `378` bytes)
- VA: `0x000000014064AF70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A668`
- 디코드: `103`개 명령, `378/378` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064AFA6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064AFCE` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064B006` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064B02D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064B046` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064B054` → [ZwSetSystemInformation](../6B/ZwSetSystemInformation_function_006B0870.md) (function, `0x006B0870`)
- `0x0064B081` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064B0A8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064B0C1` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064AFE0` → RVA `0x00F048B8` (`.data`; read)
- `0x0064AFF3` → RVA `0x00F04980` (`.data`; read)
- `0x0064AFFF` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064AF70  48 8B C4                        mov rax, rsp
0064AF73  48 89 58 08                     mov qword ptr [rax + 8], rbx
0064AF77  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0064AF7B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064AF7F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064AF83  41 54                           push r12
0064AF85  41 56                           push r14
0064AF87  41 57                           push r15
0064AF89  48 83 EC 40                     sub rsp, 0x40
0064AF8D  0F 57 C0                        xorps xmm0, xmm0
0064AF90  44 8B E1                        mov r12d, ecx
0064AF93  B9 0A 00 00 00                  mov ecx, 0xa
0064AF98  45 8B F0                        mov r14d, r8d
0064AF9B  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0064AF9F  4C 8B FA                        mov r15, rdx
0064AFA2  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0064AFA6  E8 89 AA E4 FF                  call 0x140495a34
0064AFAB  48 8B F0                        mov rsi, rax
0064AFAE  48 85 C0                        test rax, rax
0064AFB1  0F 84 94 00 00 00               je 0x14064b04b
0064AFB7  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064AFBA  A8 18                           test al, 0x18
0064AFBC  74 0C                           je 0x14064afca
0064AFBE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0064AFC3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0064AFC8  EB 0E                           jmp 0x14064afd8
0064AFCA  A8 04                           test al, 4
0064AFCC  74 0A                           je 0x14064afd8
0064AFCE  E8 35 8C E8 FF                  call 0x1404d3c08
0064AFD3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0064AFD8  40 32 ED                        xor bpl, bpl
0064AFDB  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
0064AFE0  40 38 2D D1 98 8B 00            cmp byte ptr [rip + 0x8b98d1], bpl
0064AFE7  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0064AFEC  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0064AFF1  75 0C                           jne 0x14064afff
0064AFF3  F7 05 83 99 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9983], 0x800
0064AFFD  74 13                           je 0x14064b012
0064AFFF  48 8D 0D 7A 8E 8B 00            lea rcx, [rip + 0x8b8e7a]
0064B006  E8 15 B6 BC FF                  call 0x140216620
0064B00B  40 8A E8                        mov bpl, al
0064B00E  84 C0                           test al, al
0064B010  74 39                           je 0x14064b04b
0064B012  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0064B016  48 8B 1F                        mov rbx, qword ptr [rdi]
0064B019  EB 1A                           jmp 0x14064b035
0064B01B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064B01F  48 85 C0                        test rax, rax
0064B022  74 0E                           je 0x14064b032
0064B024  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064B028  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064B02D  E8 9E FA 06 00                  call 0x1406baad0
0064B032  48 8B 1B                        mov rbx, qword ptr [rbx]
0064B035  48 3B DF                        cmp rbx, rdi
0064B038  75 E1                           jne 0x14064b01b
0064B03A  40 84 ED                        test bpl, bpl
0064B03D  74 0C                           je 0x14064b04b
0064B03F  48 8D 0D 3A 8E 8B 00            lea rcx, [rip + 0x8b8e3a]
0064B046  E8 35 EE CF FF                  call 0x140349e80
0064B04B  45 8B C6                        mov r8d, r14d
0064B04E  49 8B D7                        mov rdx, r15
0064B051  41 8B CC                        mov ecx, r12d
0064B054  E8 17 58 06 00                  call 0x1406b0870
0064B059  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0064B05D  48 85 F6                        test rsi, rsi
0064B060  74 64                           je 0x14064b0c6
0064B062  40 32 FF                        xor dil, dil
0064B065  40 38 3D 4C 98 8B 00            cmp byte ptr [rip + 0x8b984c], dil
0064B06C  75 0C                           jne 0x14064b07a
0064B06E  F7 05 08 99 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9908], 0x800
0064B078  74 13                           je 0x14064b08d
0064B07A  48 8D 0D FF 8D 8B 00            lea rcx, [rip + 0x8b8dff]
0064B081  E8 9A B5 BC FF                  call 0x140216620
0064B086  40 8A F8                        mov dil, al
0064B089  84 C0                           test al, al
0064B08B  74 39                           je 0x14064b0c6
0064B08D  48 83 C6 30                     add rsi, 0x30
0064B091  48 8B 1E                        mov rbx, qword ptr [rsi]
0064B094  EB 1A                           jmp 0x14064b0b0
0064B096  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064B09A  48 85 C0                        test rax, rax
0064B09D  74 0E                           je 0x14064b0ad
0064B09F  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064B0A3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0064B0A8  E8 23 FA 06 00                  call 0x1406baad0
0064B0AD  48 8B 1B                        mov rbx, qword ptr [rbx]
0064B0B0  48 3B DE                        cmp rbx, rsi
0064B0B3  75 E1                           jne 0x14064b096
0064B0B5  40 84 FF                        test dil, dil
0064B0B8  74 0C                           je 0x14064b0c6
0064B0BA  48 8D 0D BF 8D 8B 00            lea rcx, [rip + 0x8b8dbf]
0064B0C1  E8 BA ED CF FF                  call 0x140349e80
0064B0C6  8B 44 24 3C                     mov eax, dword ptr [rsp + 0x3c]
0064B0CA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0064B0CF  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0064B0D4  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0064B0D9  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0064B0DE  48 83 C4 40                     add rsp, 0x40
0064B0E2  41 5F                           pop r15
0064B0E4  41 5E                           pop r14
0064B0E6  41 5C                           pop r12
0064B0E8  C3                              ret
0064B0E9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetSystemInformationWrapper(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
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
    result = DifGetAPIThunkContextById(10, a2, a3, a4);
    if (result == 0) goto loc_0064B04B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064AFCA;
    v_stack_m38 = v_stack_p0;
    goto loc_0064AFD8;
loc_0064AFCA:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m20 = (unsigned int)((unsigned int)(a1));
    v_stack_m28 = a2;
    v_stack_m30 = (unsigned int)((unsigned int)(a3));
    if ((*(unsigned __int8 *)(v_rip + 9148625)) != 0) goto loc_0064AFFF;
    if (((*(unsigned int *)(v_rip + 9148803)) & (0x800ULL)) == 0) goto loc_0064B012;
loc_0064AFFF:
    result = ExAcquireRundownProtection(v_rip + 9145978, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064B04B;
loc_0064B012:
    goto loc_0064B035;
loc_0064B01B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064B035:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064B01B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9145914;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetSystemInformation((unsigned int)((unsigned int)((unsigned int)(a1))), a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m1C = (unsigned int)(result);
    if (result == 0) goto loc_0064B0C6;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9148492)) != 0) goto loc_0064B07A;
    if (((*(unsigned int *)(v_rip + 9148680)) & (0x800ULL)) == 0) goto loc_0064B08D;
loc_0064B07A:
    result = ExAcquireRundownProtection(v_rip + 9145855, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064B0C6;
loc_0064B08D:
    v_rsi = (result) + (48);
    goto loc_0064B0B0;
loc_0064B096:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0064B0B0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064B096;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9145791;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m1C);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetSystemInformationWrapper(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
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
    result = DifGetAPIThunkContextById(10, Arg2, Arg3, a4);
    if (result == 0) goto loc_0064B04B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064AFCA;
    v_stack_m38 = v_stack_p0;
    goto loc_0064AFD8;
loc_0064AFCA:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg1));
    v_stack_m28 = Arg2;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg3));
    if ((*(uint8_t *)(v_rip + 0x8B98D1)) != 0) goto loc_0064AFFF;
    if (((*(uint32_t *)(v_rip + 0x8B9983)) & (0x800ULL)) == 0) goto loc_0064B012;
loc_0064AFFF:
    result = ExAcquireRundownProtection(v_rip + 9145978, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0064B04B;
loc_0064B012:
    goto loc_0064B035;
loc_0064B01B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0064B035:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064B01B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9145914;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = ZwSetSystemInformation((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    v_stack_m1C = (uint32_t)(result);
    if (result == 0) goto loc_0064B0C6;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8B984C)) != 0) goto loc_0064B07A;
    if (((*(uint32_t *)(v_rip + 0x8B9908)) & (0x800ULL)) == 0) goto loc_0064B08D;
loc_0064B07A:
    result = ExAcquireRundownProtection(v_rip + 9145855, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    if ((uint8_t)(result) == 0) goto loc_0064B0C6;
loc_0064B08D:
    local_rsi = (result) + (48);
    goto loc_0064B0B0;
loc_0064B096:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
loc_0064B0B0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064B096;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9145791;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m1C);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064AF70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064AF70[BB_0064AF70]
  bb_0064AFB7[BB_0064AFB7]
  bb_0064AFBE[BB_0064AFBE]
  bb_0064AFCA[BB_0064AFCA]
  bb_0064AFCE[BB_0064AFCE]
  bb_0064AFD8[BB_0064AFD8]
  bb_0064AFF3[BB_0064AFF3]
  bb_0064AFFF[BB_0064AFFF]
  bb_0064B012[BB_0064B012]
  bb_0064B01B[BB_0064B01B]
  bb_0064B024[BB_0064B024]
  bb_0064B032[BB_0064B032]
  bb_0064B035[BB_0064B035]
  bb_0064B03A[BB_0064B03A]
  bb_0064B03F[BB_0064B03F]
  bb_0064B04B[BB_0064B04B]
  bb_0064B062[BB_0064B062]
  bb_0064B06E[BB_0064B06E]
  bb_0064B07A[BB_0064B07A]
  bb_0064B08D[BB_0064B08D]
  bb_0064B096[BB_0064B096]
  bb_0064B09F[BB_0064B09F]
  bb_0064B0AD[BB_0064B0AD]
  bb_0064B0B0[BB_0064B0B0]
  bb_0064B0B5[BB_0064B0B5]
  bb_0064B0BA[BB_0064B0BA]
  bb_0064B0C6[BB_0064B0C6]
  bb_0064B0E9[BB_0064B0E9]
  bb_0064AF70 -->|branch| bb_0064B04B
  bb_0064AF70 -->|fallthrough| bb_0064AFB7
  bb_0064AFB7 -->|branch| bb_0064AFCA
  bb_0064AFB7 -->|fallthrough| bb_0064AFBE
  bb_0064AFBE -->|branch| bb_0064AFD8
  bb_0064AFCA -->|branch| bb_0064AFD8
  bb_0064AFCA -->|fallthrough| bb_0064AFCE
  bb_0064AFCE -->|flow| bb_0064AFD8
  bb_0064AFD8 -->|branch| bb_0064AFFF
  bb_0064AFD8 -->|fallthrough| bb_0064AFF3
  bb_0064AFF3 -->|branch| bb_0064B012
  bb_0064AFF3 -->|fallthrough| bb_0064AFFF
  bb_0064AFFF -->|branch| bb_0064B04B
  bb_0064AFFF -->|fallthrough| bb_0064B012
  bb_0064B012 -->|branch| bb_0064B035
  bb_0064B01B -->|branch| bb_0064B032
  bb_0064B01B -->|fallthrough| bb_0064B024
  bb_0064B024 -->|flow| bb_0064B032
  bb_0064B032 -->|flow| bb_0064B035
  bb_0064B035 -->|branch| bb_0064B01B
  bb_0064B035 -->|fallthrough| bb_0064B03A
  bb_0064B03A -->|branch| bb_0064B04B
  bb_0064B03A -->|fallthrough| bb_0064B03F
  bb_0064B03F -->|flow| bb_0064B04B
  bb_0064B04B -->|branch| bb_0064B0C6
  bb_0064B04B -->|fallthrough| bb_0064B062
  bb_0064B062 -->|branch| bb_0064B07A
  bb_0064B062 -->|fallthrough| bb_0064B06E
  bb_0064B06E -->|branch| bb_0064B08D
  bb_0064B06E -->|fallthrough| bb_0064B07A
  bb_0064B07A -->|branch| bb_0064B0C6
  bb_0064B07A -->|fallthrough| bb_0064B08D
  bb_0064B08D -->|branch| bb_0064B0B0
  bb_0064B096 -->|branch| bb_0064B0AD
  bb_0064B096 -->|fallthrough| bb_0064B09F
  bb_0064B09F -->|flow| bb_0064B0AD
  bb_0064B0AD -->|flow| bb_0064B0B0
  bb_0064B0B0 -->|branch| bb_0064B096
  bb_0064B0B0 -->|fallthrough| bb_0064B0B5
  bb_0064B0B5 -->|branch| bb_0064B0C6
  bb_0064B0B5 -->|fallthrough| bb_0064B0BA
  bb_0064B0BA -->|flow| bb_0064B0C6
```
